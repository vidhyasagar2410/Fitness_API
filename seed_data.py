#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 10:24:05 2025

@author: saimonica
"""

from datetime import datetime, timedelta
from models import Class
from database import SessionLocal

def seed_classes():
    db = SessionLocal()
    if db.query(Class).count() == 0:
        classes = [
            Class(name="Yoga", date_time=datetime.now() + timedelta(days=1), instructor="Anita", available_slots=5),
            Class(name="Zumba", date_time=datetime.now() + timedelta(days=2), instructor="Vikram", available_slots=10),
            Class(name="HIIT", date_time=datetime.now() + timedelta(days=3), instructor="Riya", available_slots=8)
        ]
        db.add_all(classes)
        db.commit()
    db.close()
