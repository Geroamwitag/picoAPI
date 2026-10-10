from fastapi import FastAPI
from datetime import datetime
import os
import psycopg
from fastapi.responses import PlainTextResponse
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


DATABASE_URL = os.environ["ALEKS_DB_URL"]

app = FastAPI()

# -------------------------
# Pico Stuff
# -------------------------

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


# -------------------------
# Request models
# used to validate, fix and structure post jsons. Essentially a schema
# -------------------------
class UserCreate(BaseModel):
    username: str


class AreaCreate(BaseModel):
    name: str
    latitude: float
    longitude: float
    radius_meters: float


class LocationCreate(BaseModel):
    user_id: int
    area_id: int | None = None
    latitude: float
    longitude: float
    timestamp: datetime


class ActivityTypeCreate(BaseModel):
    name: str
    category: str | None = None


class ActivityCreate(BaseModel):
    user_id: int
    activity_type_id: int
    start_time: datetime
    end_time: datetime | None = None


class SleepCreate(BaseModel):
    user_id: int
    sleep_start_time: datetime
    sleep_end_time: datetime | None = None


class LightMeasurementCreate(BaseModel):
    user_id: int
    sensor_type: str
    value: float
    unit: str
    timestamp: datetime


class GoalCreate(BaseModel):
    user_id: int
    name: str
    target_duration_minutes: int
    period: str


class AppSessionCreate(BaseModel):
    user_id: int
    start_time: datetime
    end_time: datetime | None = None



# -------------------------
# POST endpoints
# -------------------------

# simplify insert queries
def insert_row(query, values):
    with psycopg.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(query, values)
            new_id = cur.fetchone()[0]
    return new_id


@app.post("/users")
def create_user(user: UserCreate):
    new_id = insert_row(
        """
        INSERT INTO users (username)
        VALUES (%s)
        RETURNING id
        """,
        (user.username,)
    )

    return {"message": "User created", "id": new_id}


@app.post("/areas")
def create_area(area: AreaCreate):
    new_id = insert_row(
        """
        INSERT INTO areas
            (name, latitude, longitude, radius_meters)
        VALUES (%s, %s, %s, %s)
        RETURNING id
        """,
        (
            area.name,
            area.latitude,
            area.longitude,
            area.radius_meters
        )
    )

    return {"message": "Area created", "id": new_id}


@app.post("/locations")
def create_location(location: LocationCreate):
    new_id = insert_row(
        """
        INSERT INTO locations
            (user_id, area_id, latitude, longitude, timestamp)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id
        """,
        (
            location.user_id,
            location.area_id,
            location.latitude,
            location.longitude,
            location.timestamp
        )
    )

    return {"message": "Location created", "id": new_id}


@app.post("/activity-types")
def create_activity_type(activity_type: ActivityTypeCreate):
    new_id = insert_row(
        """
        INSERT INTO activity_types (name, category)
        VALUES (%s, %s)
        RETURNING id
        """,
        (
            activity_type.name,
            activity_type.category
        )
    )

    return {"message": "Activity type created", "id": new_id}


@app.post("/activities")
def create_activity(activity: ActivityCreate):
    new_id = insert_row(
        """
        INSERT INTO activities
            (user_id, activity_type_id, start_time, end_time)
        VALUES (%s, %s, %s, %s)
        RETURNING id
        """,
        (
            activity.user_id,
            activity.activity_type_id,
            activity.start_time,
            activity.end_time
        )
    )

    return {"message": "Activity created", "id": new_id}


@app.post("/sleep")
def create_sleep(sleep: SleepCreate):
    new_id = insert_row(
        """
        INSERT INTO sleep
            (user_id, sleep_start_time, sleep_end_time)
        VALUES (%s, %s, %s)
        RETURNING id
        """,
        (
            sleep.user_id,
            sleep.sleep_start_time,
            sleep.sleep_end_time
        )
    )

    return {"message": "Sleep record created", "id": new_id}


@app.post("/light-measurements")
def create_light_measurement(measurement: LightMeasurementCreate):
    new_id = insert_row(
        """
        INSERT INTO light_measurements
            (user_id, sensor_type, value, unit, timestamp)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id
        """,
        (
            measurement.user_id,
            measurement.sensor_type,
            measurement.value,
            measurement.unit,
            measurement.timestamp
        )
    )

    return {"message": "Light measurement created", "id": new_id}


@app.post("/goals")
def create_goal(goal: GoalCreate):
    new_id = insert_row(
        """
        INSERT INTO goals
            (user_id, name, target_duration_minutes, period)
        VALUES (%s, %s, %s, %s)
        RETURNING id
        """,
        (
            goal.user_id,
            goal.name,
            goal.target_duration_minutes,
            goal.period
        )
    )

    return {"message": "Goal created", "id": new_id}


@app.post("/app-sessions")
def create_app_session(session: AppSessionCreate):
    new_id = insert_row(
        """
        INSERT INTO app_sessions
            (user_id, start_time, end_time)
        VALUES (%s, %s, %s)
        RETURNING id
        """,
        (
            session.user_id,
            session.start_time,
            session.end_time
        )
    )

    return {"message": "App session created", "id": new_id}




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