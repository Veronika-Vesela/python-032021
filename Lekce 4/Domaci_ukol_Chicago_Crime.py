# Tabulka crime v naší databázi obsahuje informace o kriminalitě v Chicagu. Data si můžete i interaktivně prohlédnout na mapě zde.
# Dataset je poměrně velký, a tak si určitě vytáhneme vždy jen nějaký výběr, se kterým budeme dále pracovat.

import os
import pandas
import psycopg2
from sqlalchemy import create_engine, inspect
import matplotlib.pyplot as plt

HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "verca.mala.mala"
USERNAME = f"{USER}@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "I6dtS3.E5SG035=="

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=True)
# inspector = inspect(engine)
# print(inspector.get_table_names())

# Pomocí SQL dotazu si připrav tabulku o krádeži motorových vozidel (sloupec PRIMARY_DESCRIPTION by měl mít hodnotu "MOTOR VEHICLE THEFT").
kradeze_mot_vozidel=pandas.read_sql("SELECT * FROM crime where \"PRIMARY_DESCRIPTION\" = 'MOTOR VEHICLE THEFT'", con=engine)
# print(kradeze_mot_vozidel.head())

# Tabulku dále pomocí pandasu vyfiltruj tak, aby obsahovala jen informace o krádeži aut (hodnota "AUTOMOBILE" ve sloupci SECONDARY_DESCRIPTION).

kradeze_aut=kradeze_mot_vozidel[kradeze_mot_vozidel["SECONDARY_DESCRIPTION"]=="AUTOMOBILE"]

# Ve kterém měsíci dochází nejčastěji ke krádeži auta?
kradeze_aut["DATE_OF_OCCURRENCE"]=pandas.to_datetime(kradeze_aut["DATE_OF_OCCURRENCE"])
kradeze_aut["MONTH"]=kradeze_aut["DATE_OF_OCCURRENCE"].dt.month
kradeze_aut_mesice=kradeze_aut.groupby("MONTH")[["CASE#"]].count().sort_values(by="CASE#", ascending=False)

print(kradeze_aut_mesice)
