from fastapi import FastAPI



app = FastAPI()



@app.get('/')
def index():
    return {"data":{"name": "James"}}

@app.get('/About')
def about():
    return {'data':'About Page'}
