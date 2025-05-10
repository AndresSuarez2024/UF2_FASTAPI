from pydantic import BaseModel

# Esquema per als intents de joc
class JocIntent(BaseModel):
    id_usuario: int
    id_paraula: int
    lletra: str
    encertat: bool
    errors: int

# Esquema per les estadístiques d'un jugador
class EstadistiquesJugador(BaseModel):
    id_usuario: int
    nom: str
    punts_actuals: int
    partides_totals: int
    partides_guanyades: int
    partida_mes_punts: int
