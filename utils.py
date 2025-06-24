#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 10:24:24 2025

@author: saimonica
"""

import pytz
from models import Class

def to_timezone(fitness_class: Class, timezone: str):
    target = pytz.timezone(timezone)
    fitness_class.date_time = fitness_class.date_time.astimezone(target)
    return fitness_class
