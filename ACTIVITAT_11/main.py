from fastapi import FastAPI, HTTPException
from models import get_informacio_principal, get_lletres_disponibles, registrar_intent, get_estadistiques_jugador
from schemas import JocIntent, EstadistiquesJugador

app = FastAPI()

# Endpoint per obtenir la informació de la pantalla principal
@app.get("/api/informacio")
async def informacio_principal():
    informacio = get_informacio_principal()
    return {"informacio": informacio}

# Endpoint per obtenir lletres disponibles
@app.get("/api/lletres")
async def lletres():
    lletres = get_lletres_disponibles()
    return {"lletres": lletres}

# Endpoint per registrar un intent de joc
@app.post("/api/registre_joc")
async def registre_joc(intent: JocIntent):
    registrar_intent(intent.id_usuario, intent.id_paraula, intent.lletra, intent.encertat, intent.errors)
    return {"message": "Intent registrat correctament"}

# Endpoint per obtenir les estadístiques del jugador
@app.get("/api/jugador/{id_usuario}", response_model=EstadistiquesJugador)
async def estadistiques_jugador(id_usuario: int):
    jugador = get_estadistiques_jugador(id_usuario)
    if jugador:
        return {
            "id_usuario": jugador[0],
            "nom": jugador[1],
            "punts_actuals": jugador[2],
            "partides_totals": jugador[3],
            "partides_guanyades": jugador[4],
            "partida_mes_punts": jugador[5]
        }
    else:
        raise HTTPException(status_code=404, detail="Jugador no trobat")
