from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
app = FastAPI()

@app.get('/blog')
def index(limit, published:bool = True, sort: Optional[str] = None):
    if published:
        return {'data' : f'{limit} Published Blogs from the db'}
    else:
        return {'data' : f'{limit} unpublished blogs from the db'}

@app.get('/about')
def about():
    return "This is the about page."

@app.get('/blog/unpublished')
def unpublished():
    return {'data' : 'All Unpublished Blogs'}

@app.get('/blog/{id}')
def blog(id:int):
    return {'data' : id}

@app.get('/blog/{id}')
def blog(id):
    return {'data' : id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data' : {'comments' : ['comment1', 'comment2']}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    return {'data' : f'Blog is created with title as {request.title}'}


# if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)