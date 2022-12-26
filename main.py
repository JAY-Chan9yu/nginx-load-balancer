import threading
from time import sleep

from fastapi import FastAPI

app = FastAPI()
print(f'now t: {threading.currentThread().getName()}')


@app.get("/")
def root():
    print(f'start root ({threading.currentThread().getName()})')
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    print(f'start say_hello ({threading.currentThread().getName()})')
    return {"message": f"Hello {name}"}


def long_task():
    print(f'start long_task ({threading.currentThread().getName()})')
    sleep(5)
    print('task is done')
