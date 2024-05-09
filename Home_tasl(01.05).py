from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    student = ['Влад', "Вадим", "Женя", "Діана", "Василь", "Ярослав", "Вова", "Аріна", "Владислав", "Вальтер", "Микита", "Матвій"]
    return {"Всі студенти": f"{student}"}


@app.get('/tech')
async def root():
    return {"Викладач tech skills": 'Максим Шарко'}


@app.get('/soft')
async def root():
    return {"Викладач soft skills": 'Анастасія Іванченко'}
