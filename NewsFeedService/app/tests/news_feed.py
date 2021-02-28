from ..main import app
from fastapi.testclient import TestClient
from fastapi import FastAPI
import requests
import pytest


    
# testdata = [
#     (0,2,200,0,2),
#     (0,0,422,"ensure this value is greater than 0","value_error.number.not_gt"),
#     (0,1,200,0,1),
#     (0,5,200,0,5),
#     (1,5,200,1,5),
#     (0,10,200,0,10),
#     (2,5,200,2,5),
# ]

# @pytest.mark.parametrize("p,s,status,page,size",testdata)
# def test_get_all_user(p,s,status,page,size):
#     response =requests.get("http://127.0.0.1:8000/api/people/60263c56fe615b45578b026b?page="+str(p)+"&size="+str(s))
#     assert response.status_code==status
#     if status==422:
#         assert response.json()['detail'][0]['msg']==page
#         assert response.json()['detail'][0]['type']==size
#     else:
#         assert response.json()['people_data']['page']==page
#         assert response.json()['people_data']['size']==size



