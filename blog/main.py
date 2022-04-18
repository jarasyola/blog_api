from fastapi import FastAPI
from . import schemas,models
from . database import engine



#Line for creating the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()




@app.post('/blog')
def create(request: schemas.Blog):
    return request