from fastapi import FastAPI



app = FastAPI()


# where @app is  Routes/Endpoint/Decorator/Path(Python)
# .get/post/put - operation
# def index - function operation
@app.get('/')
def index():
    return {'data':'Blog list'}


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
