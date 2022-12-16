from fastapi import FastAPI

app = FastAPI()

_dict = {
        1 : {'Name' : 'Huawei Matebook X', 'Price' : 35000},
        2 : {'Name' : 'Macbook Pro', 'Price' : 45000},
        3 : {'Name' : 'Samsung j7 Prime', 'Price' : 35000}
        }

@app.get('/')
def index():
    return 'Hello World!'

@app.get('/Products')
def GetAll():
    return _dict

@app.get('/Products/id/{id}')
def GetById(id : int):
    return _dict[id]

@app.get('/Products/price/{price}')
def GetByName(price : int):
    return [{'id' : x, 'data' : _dict[x]} for x in _dict if _dict[x]['Price'] == price]