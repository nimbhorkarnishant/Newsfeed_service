from fastapi import FastAPI
import requests
import pytest

data_post=[
    ("9f28de3f-33e9-4a59-a33b-12f52e41e93c",
     {
        "id": "1456",
        "profileImg": "string",
        "firstName": "string",
        "lastName": "string"
    },
     200
     )
    
]

data_delete=[
    ("9f28de3f-33e9-4a59-a33b-12f52e41e93c",{"id": "1456"},200)
]


@pytest.mark.parametrize("post_id,json_data,status",data_post)
def test_Like(post_id,json_data,status):
    assert len(post_id)!=0
    url="http://127.0.0.1:8000/api/like/"+post_id
    response=requests.put(url, json =json_data)
    assert response.json()['status_code']==200
    assert response.status_code==status
    
    

@pytest.mark.parametrize("post_id,json_data,status",data_delete)
def test_Dislike(post_id,json_data,status):
    assert len(post_id)!=0
    url="http://127.0.0.1:8000/api/dislike/"+post_id
    response=requests.delete(url, json =json_data)
    assert response.json()['status_code']==200
    assert response.status_code==status