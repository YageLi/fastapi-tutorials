from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {'data':{'name':'Li'}}

@app.get("/about")
def about():
    return {'data':'about page'}