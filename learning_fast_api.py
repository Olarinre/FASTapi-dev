import random
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
import dbconnect

#postgresql db connection
dbconnect.connect_db()
#end of db connection.


posts_db = [

    {'title': 'first post', 'content': 'this is the content of the first post', 'id': 1},
    {'title': 'second post', 'content': 'this is the content of the second post', 'id': 2}
]

#findpost function
def find_post(id):
    for post in posts_db:
        if post['id'] == id:
            return post
    return None


#pydantic schema
class New_post(BaseModel):
    title: str
    content: str
    published: bool = True
    


app = FastAPI()

@app.get("/")
async def root():
    return {'message': 'hello world1'}

@app.get("/posts")
def get_post():
    return {'message': posts_db}

@app.post('/posts')
def create_post(newpost: New_post):
    post_dict = newpost.dict()
    post_dict['id'] = random.randint(1, 1000000)
    posts_db.append(post_dict)

    return {'message': post_dict}



@app.get('/posts/{id}')
def get_singlepost(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'post with id: {id} was not found')
        #response.status_code = status.HTTP_404_NOT_FOUND
    return {'details': post}












