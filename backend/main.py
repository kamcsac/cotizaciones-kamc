from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Cotizaciones KAMC S.A.C.")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# USUARIO FIJO (por ahora)
USUARIO = "BCASTILLO"
PASSWORD = "KAMCSAC"

@app.get("/")
def inicio():
    return {"mensaje": "API KAMC funcionando"}

@app.post("/login")
def login(usuario: str, password: str):
    if usuario == USUARIO and password == PASSWORD:
        return {"usuario_id": 1, "rol": "ADMIN"}
    return {"error": "Credenciales incorrectas"}

@app.post("/cotizacion")
def guardar_cotizacion(data: dict):
    return {"mensaje": "Cotización guardada"}
