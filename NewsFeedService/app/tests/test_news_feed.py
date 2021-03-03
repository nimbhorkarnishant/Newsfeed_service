from fastapi import FastAPI
import requests
import pytest

    
testdata = [
    (0,1,200,0,1),
    (0,0,422,"ensure this value is greater than 0","value_error.number.not_gt"),
    # (0,1,200,0,1),
    # (0,5,200,0,5),
    # (1,5,200,1,5),
    # (0,10,200,0,10),
    # (2,5,200,2,5),
]

Data={
  "user": {
    "id": "2",
    "profileImg": "url",
    "firstName": "Sam",
    "lastName": "Willings"
  },
  "isLiked": False,
  "createdAt": "2021-03-01T06:47:30.197Z",
  "group": {
    "id": "1",
    "name": "Discussion",
    "profile": "url"
  },
  "media": [],
  "description": "But that was life: Nobody got a guided tour to their own theme park. You had to hop on the rides as they presented themselves, never knowing whether you would like the one you were in line for...or if the bastard was going to make you throw up your corn dog and your cotton candy all over the place.",
  "taggedCoWorkers": [],
  "totalComments": 0,
  "likes": [],
  "totallikes": 0,
  "comments": []
}

put_data=[(
  "29dd227e-b223-497e-a61c-cc1995050949",
  {
  "isLiked": False,
  "createdAt": "2021-03-02T04:56:09.433Z",
  "description": "Test Case Done!"
},
200)
]
delete_data=[
  (
    "29dd227e-b223-497e-a61c-cc1995050949",200
  )
]

@pytest.mark.parametrize("p,s,status,page,size",testdata)
def test_Read_News_Feed(p,s,status,page,size):
    response =  requests.get("http://127.0.0.1:8000/api/get_news_posts?page="+str(p)+"&size="+str(s))

    assert response.status_code==status
    if status==422:
        assert response.json()['detail'][0]['msg']==page
        assert response.json()['detail'][0]['type']==size
    else: 
        assert response.json()['posts']['page']==page
        assert response.json()['posts']['size']==size
        
def test_News_Feed(status=200):
    url="http://127.0.0.1:8000/api/news_posts/"
    response=requests.post(url, json=Data)
    assert response.json()['status_code']==200
    assert response.status_code==status
    
@pytest.mark.parametrize("post_id,Data,status",put_data)
def test_Update_News_Feed(post_id,Data,status):
    assert len(post_id)!=0
    url="http://127.0.0.1:8000/api/update_news_post/"+post_id
    response=requests.put(url, json=Data)
    assert response.json()['status_code']==status
    assert response.status_code==status
    
@pytest.mark.parametrize("post_id,status",delete_data)
def test_Delete_News_Feed(post_id,status):
    assert len(post_id)!=0
    url="http://127.0.0.1:8000/api/delete_news_post/"+post_id
    response=requests.delete(url)
    assert response.json()['status_code']==status
    assert response.status_code==status






