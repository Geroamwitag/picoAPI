from fastapi import FastAPI
import os
import psycopg
from fastapi.responses import PlainTextResponse
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
# http://127.0.0.1:8000/text


DATABASE_URL = os.environ["ALEKS_DB_URL"]

app = FastAPI()

# temperature post reading to be put on the pico, the class defines the expected structure
class TemperatureReading(BaseModel):
    device_id: str
    temperature: float



@app.post("/temperature")
def receive_temperature(reading: TemperatureReading):
    print(f"Temperature reading recieved: {reading}")
    with psycopg.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO pico_readings (device_id, temperature_c)
                VALUES (%s, %s)
                """,
                (reading.device_id, reading.temperature),
            )
    print(f"Temperature reading sent to DB: {reading}")

    return {
        "success": True,
        "message": "Temperature stored in database!"
    }


#
# Playing around with FASTAPI to learn
#
@app.get("/")
def home():
    return {"message": "Hello from my API!"}


@app.get("/hello")
def hello():
    return {"message": "Hello from the second endpoint!"}


@app.get("/text", response_class=PlainTextResponse)
def text():
    return "Hello as plain text!"


@app.get("/page", response_class=HTMLResponse)
def page():
    return "<h1>Hello from FastAPI</h1>"