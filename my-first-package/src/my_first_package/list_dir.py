import os

def list_directories() -> str:
    for dir in os.listdir():
        yield dir
