#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 10:21:01 2025

@author: saimonica
"""

from fastapi import FastAPI, HTTPException, Query
from models import Class, Booking
from schemas import ClassOut, BookingIn, BookingOut
from database import SessionLocal, engine, Base
from seed_data import seed_classes
from utils import to_timezone
from sqlalchemy.orm import Session
from typing import List
import pytz

app = FastAPI()
Base.metadata.create_all(bind=engine)
seed_classes()

@app.get("/classes", response_model=List[ClassOut])
def get_classes(timezone: str = "Asia/Kolkata"):
    db = SessionLocal()
    try:
        classes = db.query(Class).all()
        return [to_timezone(c, timezone) for c in classes]
    finally:
        db.close()

@app.post("/book", response_model=BookingOut)
def book_class(booking: BookingIn):
    db = SessionLocal()
    fitness_class = db.query(Class).filter(Class.id == booking.class_id).first()
    if not fitness_class:
        raise HTTPException(status_code=404, detail="Class not found")
    if fitness_class.available_slots < 1:
        raise HTTPException(status_code=400, detail="No slots available")

    new_booking = Booking(
        class_id=booking.class_id,
        client_name=booking.client_name,
        client_email=booking.client_email
    )
    fitness_class.available_slots -= 1
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    db.refresh(fitness_class)
    db.close()
    return new_booking

@app.get("/bookings", response_model=List[BookingOut])
def get_bookings(client_email: str = Query(...)):
    db = SessionLocal()
    bookings = db.query(Booking).filter(Booking.client_email == client_email).all()
    db.close()
    return bookings
