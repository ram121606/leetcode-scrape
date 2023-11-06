from fastapi import FastAPI
import uvicorn 
from scrape import scrape as sc

app = FastAPI()

@app.get('/')
def home():
    return '🙌'

@app.get('/{name}')
def scrape(name : str):
    url = 'https://www.leetcode.com/'+name
    res = sc(url)
    return res

if __name__ == '__main__':
    uvicorn.run('server:app' , port=6969 , reload=True)