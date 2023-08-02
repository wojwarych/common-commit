from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def get_root():
    return {"Hello": "World!"}

@app.get("/me")
def get_user():
    return {"name": "Joe", "surname": "Doe"}}


@app.post("/foo", status_code=201)
def create_foo():
    return "Okay"
