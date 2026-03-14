from fastapi import FastAPI
from caluladora import multiplicación,suma
from cda import ColasVehiculo
app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


# crear una ruta llamada factorial que reciba un numero y devuelva su factorial
@app.get("/factorial/{numero}")
def calcular_factorial(numero: int):
    factorial = 1

    for i in range(1, numero + 1):
        factorial *= i

    return {"numero": numero, "factorial": factorial}

@app.get("/suma/{a}/{b}")
def sumar(a: int, b: int):
    resultado = suma(a,b)
    return {"resultado":resultado}

@app.post("/registriar_vehiculo/")
def registrar_vehiculo(marca: str, modelo: str, año: int, tipo: str):
    colas_vehiculo = ColasVehiculo()
    vehiculo = colas_vehiculo.agregar_vehiculo(marca, modelo, año, tipo)
    return {"vehiculo": vehiculo}

@app.get("/despachar_vehiculo/")
def despachar_vehiculo():
    colas_vehiculo = ColasVehiculo()
    vehiculo_despachado = colas_vehiculo.despachar_vehiculo()
    return {"vehiculo_despachado": vehiculo_despachado}