from fastapi import FastAPI
import requests
import pytest

data_post=[
    ('b8ef27f3-643b-4876-9cfa-b4984d565f86',
     {
        "taggedCoWorkers": [
            {
            "id": "100",
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
    ('b8ef27f3-643b-4876-9cfa-b4984d565f86',{"id": "1"},200)
]


@pytest.mark.parametrize("post_id,json_data,status",data_post)
def test_Tag(post_id,json_data,status):
    assert len(post_id)!=0
    url="http://127.0.0.1:8000/api/tag_coworkers/"+post_id
    response=requests.post(url, data =json_data)
    assert response.status_code==status
    
    

@pytest.mark.parametrize("post_id,json_data,status",data_delete)
def test_Untag(post_id,json_data,status):
    assert len(post_id)!=0
    url="http://127.0.0.1:8000/api/untag_coworkers/"+post_id
    response=requests.post(url, data =json_data)
    assert response.status_code==status