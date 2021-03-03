from fastapi import FastAPI
import requests
import pytest

data_post=[
    ("9f28de3f-33e9-4a59-a33b-12f52e41e93c",
     {
        "media": [
            {
            "media_type": "string",
            "url": "string"
            }
        ]
    },
     200
     )
    
]

data_delete=[
    ("9f28de3f-33e9-4a59-a33b-12f52e41e93c",{"id": "b7a81a15-4748-467b-aa7c-f3e0b12cf9e9"},200)
]


@pytest.mark.parametrize("post_id,json_data,status",data_post)
def test_add_media(post_id,json_data,status):
    assert len(post_id)!=0
    url="http://127.0.0.1:8000/api/add_media/"+post_id
    response=requests.put(url, json =json_data)
    assert response.json()['status_code']==status
    assert response.status_code==status
    
    

@pytest.mark.parametrize("post_id,json_data,status",data_delete)
def test_delete_media(post_id,json_data,status):
    assert len(post_id)!=0
    url="http://127.0.0.1:8000/api/delete_media/"+post_id
    response=requests.delete(url, json =json_data)
    assert response.json()['status_code']==status
    assert response.status_code==status