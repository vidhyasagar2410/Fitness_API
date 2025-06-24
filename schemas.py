#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 10:23:10 2025

@author: saimonica
"""

from pydantic import BaseModel, EmailStr
from datetime import datetime

class ClassOut(BaseModel):
    id: int
    name: str
    date_time: datetime
    instructor: str
    available_slots: int

    class Config:
        from_attributes = True  # Replaces `orm_mode = True` in Pydantic v2

class BookingIn(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr

class BookingOut(BookingIn):
    id: int

    class Config:
        from_attributes = True  # Replaces `orm_mode = True` in Pydantic v2
