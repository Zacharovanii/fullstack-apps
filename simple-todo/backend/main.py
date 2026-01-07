import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"data": "hello world!"}

def main():
    uvicorn.run("main:app")


if __name__ == '__main__':
    main()