from fastapi import FastAPI


app = FastAPI()


@app.get('/{name}')
async def name(name: str):
    async def hello():
        return {"message": f"Hello, {name}"}
    result = await hello()
    return result
