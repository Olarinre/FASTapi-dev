import random
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlmodel import Session, select
from models import Posts
from dbconnect import get_session








"""try:
    conn = psycopg2.connect(
        host="localhost",
        database="fastapi",
        user="postgres",
        password="Ayobami@090499",
        cursor_factory = RealDictCursor   
    )
    cursor = conn.cursor()
    print("Database connection was successful")
except Exception as error:
    print("Database connection failed")
    print("Error:", error)
#end of db conne
# ction.
"""

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

#get all posts
@app.get('/sqlmodel')
def get_posts(session: Session = Depends(get_session)):
    posts = session.exec(select(Posts)).all()
    return posts








