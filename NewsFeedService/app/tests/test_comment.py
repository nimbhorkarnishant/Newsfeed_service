from fastapi import FastAPI
import requests
import pytest

data_post=[
    ("9f28de3f-33e9-4a59-a33b-12f52e41e93c",
    {
        "isLiked": True,
        "user": {
            "id": "string",
            "profileImg": "string",
            "firstName": "string",
            "lastName": "string"
        },
        "comment": "string",
        "createdAt": "2021-03-01T14:54:58.384Z",
        "replies": []
    },
     200
     )
    
]

data_delete=[
    ("9f28de3f-33e9-4a59-a33b-12f52e41e93c",{"id": "string"},200)
]

post_reply=[
    ("9f28de3f-33e9-4a59-a33b-12f52e41e93c","e232776a-ff71-4600-8f53-3eac638c3843",
    {
        "isLiked": True,
        "user": {
            "id": "string",
            "profileImg": "string",
            "firstName": "string",
            "lastName": "string"
        },
        "comment": "string",
        "createdAt": "2021-03-01T14:54:58.384Z",
        "replies": []
    },
     200
     )
    
]

delete_reply=[
    ("9f28de3f-33e9-4a59-a33b-12f52e41e93c","e232776a-ff71-4600-8f53-3eac638c3843",{"id": "1"},200)
]


@pytest.mark.parametrize("post_id,json_data,status",data_post)
def test_Add_Comment(post_id,json_data,status):
    assert len(post_id)!=0
    url="http://127.0.0.1:8000/api/add_comment/"+post_id
    response=requests.post(url, json=json_data)
    assert response.json()['status_code']==status
    assert response.status_code==status
    
    

@pytest.mark.parametrize("post_id,json_data,status",data_delete)
def test_Delete_Comment(post_id,json_data,status):
    assert len(post_id)!=0
    url="http://127.0.0.1:8000/api/delete_comment/"+post_id
    response=requests.delete(url,json=json_data)
    assert response.json()['status_code']==status
    assert response.status_code==status
    
@pytest.mark.parametrize("post_id,comment_id,json_data,status",post_reply)
def test_Add_Reply(post_id,comment_id,json_data,status):
    assert len(post_id)!=0
    assert len(comment_id)!=0
    url="http://127.0.0.1:8000/api/add_reply/"+post_id+"/"+comment_id
    response=requests.post(url, json=json_data)
    assert response.json()['status_code']==status
    assert response.status_code==status
    
    

@pytest.mark.parametrize("post_id,comment_id,json_data,status",delete_reply)
def test_Delete_Reply(post_id,comment_id,json_data,status):
    assert len(post_id)!=0
    assert len(comment_id)!=0
    url="http://127.0.0.1:8000/api/delete_reply/"+post_id+"/"+comment_id
    response=requests.delete(url,json=json_data)
    assert response.json()['status_code']==200
    assert response.status_code==status