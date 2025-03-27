import pytest
from utils.request_manager import RequestManager

rm = RequestManager()

def test_get_users():
    response = rm.get("users?page=2")
    assert response.status_code == 200
    assert "data" in response.json()

def test_create_user():
    payload = {"name": "John", "job": "QA Engineer"}
    response = rm.post("users", data=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "John"

def test_update_user():
    payload = {"name": "Updated User"}
    response = rm.put("users/2", data=payload)
    assert response.status_code == 200

def test_delete_user():
    response = rm.delete("users/2")
    assert response.status_code == 204
