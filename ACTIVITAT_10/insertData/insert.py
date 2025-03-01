import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://user:password@localhost/penjat_db"

engine = create_engine(DATABASE_URL)

df = pd.read_csv("insertDATA/paraules.csv")
df.columns = ["word", "theme"]
df.to_sql("words", con=engine, if_exists="replace", index=False)

print("Dades inserides correctament!")
