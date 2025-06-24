#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 10:25:04 2025

@author: saimonica
"""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_classes():
    response = client.get("/classes")
    assert response.status_code == 200

def test_book_class():
    response = client.post("/book", json={
        "class_id": 1,
        "client_name": "John",
        "client_email": "john@example.com"
    })
    assert response.status_code == 200
