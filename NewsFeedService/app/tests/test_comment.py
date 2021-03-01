from fastapi import FastAPI
import requests
import pytest

data_post=[
    ('b8ef27f3-643b-4876-9cfa-b4984d565f86',
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
    ('b8ef27f3-643b-4876-9cfa-b4984d565f86',{"id": "string"},200)
]

post_reply=[
    ('b8ef27f3-643b-4876-9cfa-b4984d565f86','b8ef27f3-645b-4876-9cfa-b4984d565f86',
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
    ('b8ef27f3-643b-4876-9cfa-b4984d565f86','b8ef27f3-645b-4876-9cfa-b4984d565f86',{"id": "string"},200)
]


@pytest.mark.parametrize("post_id,json_data,status",data_post)
def test_Add_Comment(post_id,json_data,status):
    assert len(post_id)!=0
    url="http://127.0.0.1:8000/api/add_comment/"+post_id
    response=requests.post(url, data=json_data)
    assert response.status_code==status
    
    

@pytest.mark.parametrize("post_id,json_data,status",data_delete)
def test_Delete_Comment(post_id,json_data,status):
    assert len(post_id)!=0
    url="http://127.0.0.1:8000/api/delete_comment/"+post_id
    response=requests.post(url,data=json_data)
    assert response.status_code==status
    
@pytest.mark.parametrize("post_id,comment_id,json_data,status",post_reply)
def test_Add_Reply(post_id,comment_id,json_data,status):
    assert len(post_id)!=0
    assert len(comment_id)!=0
    url="http://127.0.0.1:8000/api/add_reply/"+post_id+"/"+comment_id
    response=requests.post(url, data =json_data)
    assert response.status_code==status
    
    

@pytest.mark.parametrize("post_id,comment_id,json_data,status",post_reply)
def test_Delete_Reply(post_id,comment_id,json_data,status):
    assert len(post_id)!=0
    assert len(comment_id)!=0
    url="http://127.0.0.1:8000/api/delete_reply/"+post_id+"/"+comment_id
    response=requests.post(url, data =json_data)
    assert response.status_code==status