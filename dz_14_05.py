from fastapi import FastAPI, Path, Query


app = FastAPI()


@app.get('/')
async def home():
    return 'Hello, this is the main page'


@app.get('/users/{user_id}')
async def read_car(user_id: int = Path(1, description='this is the first user')):
    return {'User': user_id}


@app.get('/info')
async def read_car(info: int = Query(..., title='Info Page', description='this is an information page')):
    return info
