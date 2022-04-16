from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel



app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


# where @app is  Routes/Endpoint/Decorator/Path(Python)
# .get/post/put - operation
# def index - function operation
@app.get('/blog')
def index(limit = 20 ,published: bool = True, sort : Optional[str]= None):
   
    if published==True:
         return {f'{limit} published blogs from the db'}
    else:
        return {f'{limit}  blogs from the db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'List of all unpublished blogs'}


# Dynamic routing should be below static routing
@app.get('/blog/{id}')
def show(id:int):
# accepting blogs with id=id
    return {'data':id}



@app.get('/blog/{id}/comments')
# return comments of id=id
def comments(id):
    return {'data':{'1','2',id}}

@app.post('/blog')
def create_blog(result:Blog):
    return {f"Blog is created with blog title as {result.title}"}
