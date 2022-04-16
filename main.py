from fastapi import FastAPI



app = FastAPI()


# where @app is  Routes/Endpoint/Decorator/Path(Python)
# .get/post/put - operation
# def index - function operation
@app.get('/')
def index():
    return {"data":{"name": "James"}}

@app.get('/About')
def about():
    return {'data':'About Page'}
