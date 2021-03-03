from fastapi import FastAPI
import requests
import pytest

data_post=[
    ("9f28de3f-33e9-4a59-a33b-12f52e41e93c",
     {
        "taggedCoWorkers": [
            {
            "id": "1001",
            "profileImg": "string",
            "firstName": "string",
            "lastName": "string"
            }
        ]
    },
     200
     )
    
]

data_delete=[
    ("9f28de3f-33e9-4a59-a33b-12f52e41e93c",{"id": "100"},200)
]


@pytest.mark.parametrize("post_id,json_data,status",data_post)
def test_Tag(post_id,json_data,status):
    assert len(post_id)!=0
    url="http://127.0.0.1:8000/api/tag_coworkers/"+post_id
    response=requests.put(url, json =json_data)
    assert response.json()['status_code']==status
    assert response.status_code==status
    
    

@pytest.mark.parametrize("post_id,json_data,status",data_delete)
def test_Untag(post_id,json_data,status):
    assert len(post_id)!=0
    url="http://127.0.0.1:8000/api/untag_coworkers/"+post_id
    response=requests.delete(url, json =json_data)
    assert response.json()['status_code']==status
    assert response.status_code==status