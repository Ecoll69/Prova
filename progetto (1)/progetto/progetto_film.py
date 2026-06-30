from fastapi import APIRouter, HTTPException
import sqlite3

router = APIRouter()

 
   @router.get("/film/{id_film}")
def dettaglio_film(id_film: int):
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row  # Fondamentale per leggere i dati come dizionario
    cursor = conn.cursor()
    # Query mirata usando il Path Parameter id_film passato dall'URL
    cursor.execute("SELECT * FROM film WHERE id = ?", (id_film,))
    risultato = cursor.fetchone()  # Recuperiamo un solo risultato (il singolo film)
    conn.close()
    if not risultato:
        raise HTTPException(status_code=404, detail="Film non trovato")
    return risultato
