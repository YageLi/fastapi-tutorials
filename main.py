from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


@app.get('/blog')
def index(limit=10, published:bool=True, sort: Optional[str]=None):
    # only get 10 published blogs
    if published:
        return {'data':f'{limit} published blogs'}
    else:
        return {'data':f'{limit} unpublished blogs'}
      


@app.get('/blog/unpublished')
def unplulished():
    return {'data':'unpublished'}

# in fastapi the route order matters
@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}


@app.get('/about')
def about():
    return {'data':'about page'}

@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {'data':{'1', '2'}}

class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data':f'{blog.title} has been created'}