from starlette.testclient import TestClient
from fastapi.testclient import TestClient
from app import *
from fastapi import FastAPI
from predict import *


app = FastAPI()

client = TestClient(app)

def test_try():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"hello": "world"} # WORKS

def test_two():
    resp = client.get("/")
    assert resp.status_code == 200
    assert isinstance(resp.json(),str)#GOOD and NEEDED 

def test_predict():
    resp = clientlocal.get("/")
    assert resp.status_code == 200
    assert isinstance(resp.text,dict) #GOOD


from predict import *


def test_try():
    resp = client.post("/")
    assert resp.status_code == 200
    assert resp.() <= 72.2
    assert resp.() <= 73.7 # ?

def test_try():
    resp = client.post("/")
    assert resp.status_code == 200
    assert resp.json() <= 40.5
    assert resp.json() <= 40.9 # ? 


    def test_check_input():
    response = client.get("/", headers={" stuff ": "stuff "})
    assert response.status_code == 200
    assert response.json() == {
        "bourogh": " stuff ",
        "neighborhood": " stuff ",   ## FOR CHECKINFG CUSTOMER INPUT#
        "???": " stuff ",
    }
    




def test_read_item_bad_token():
    response = client.get("/items/foo", headers={"X-Token": "hailhydra"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}
