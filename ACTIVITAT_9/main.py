from fastapi import FastAPI
from pydantic import List
import read, read_sch

app = FastAPI()


@app.get("/users/", response_model=List[dict])
async def reding_users():
    return read_sch.users_schema(read.read_users())