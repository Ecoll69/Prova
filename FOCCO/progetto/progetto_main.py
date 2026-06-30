from fastapi import FastAPI

# Uso del punto per l'import relativo corretto (Lezione 7, Slide 5)
from .progetto_db import dbinit
from .progetto_prodotti import router as prodotti_router
from .progetto_utente import router as utenti_router
from .progetto_film import router as film_router
<<<<<<< HEAD:progetto (1)/progetto/progetto_main.py
from FastApi.middleware.cors import CORSMiddleware
=======
from fastapi.middleware.cors import CORSMiddleware
>>>>>>> c70283a (progetto film):FOCCO/progetto/progetto_main.py

# Inizializzazione database all'avvio
dbinit()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    

# Agganciamo entrambi i router all'applicazione principale (Lezione 7, Slide 5)
app.include_router(prodotti_router)
app.include_router(utenti_router)
app.include_router(film_router)

@app.get("/")
def home():
    return {"info": "Server principale attivo!"}
