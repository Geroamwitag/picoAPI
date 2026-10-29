# PicoAPI JSON Format

## Table of Contents

- [Activity Tracking](#activity-tracking)
- [GPS Location](#gps-location)
- [Sleeping](#sleeping)
- [Commute](#commute-auto)
- [Survey](#survey)
- [Data Types](#data-types)

---

## Activity Tracking

**URL:** 
```
https://picoapi.onrender.com/activity-logs
```

### Field descriptions

- `actionType` is for Start - Stop/End session.
- `activitySessionID` is a unique ID for each session; a start and stop log for the same activity will carry the same session ID ALWAYS! (fingerprint for each session)
- `detectionMethod` tells if the log was manually inputted by the user or an auto-trigger by the app! Manual/Auto.
- `installationId` is a user-unique ID, as suggested by Omar! (prevents mixing test users and the real user)

### `logType`

This can be:

- **Activity**; for the 4 activities logged by the user "(Eating, Studying, Doing Sports, Pursue Hobbies)".
- **Location**; for auto-logged GPS coordinates every 15 mins.
- **Sleeping**; for auto-logged sleep sessions.
- **Commuting**; for auto-logged commuting sessions.
- **Survey**; for survey data logging, can be manual or auto!

### `timestamp`

Unix epoch time, a conversion example found online in Python (please double-check!):

```python
from datetime import datetime
from zoneinfo import ZoneInfo

timestamp_ms = 1792944070458

# Convert milliseconds to datetime in Europe/Amsterdam timezone
dt_amsterdam = datetime.fromtimestamp(
    timestamp_ms / 1000.0, 
    tz=ZoneInfo("Europe/Amsterdam")
)

# Format without milliseconds
readable_time = dt_amsterdam.strftime('%Y-%m-%d %H:%M:%S')

print(readable_time)
# Output: 2026-10-25 17:01:10
```

### Example

```json
[
  {
    "accuracy": 100,
    "actionType": "Start",
    "activityName": "Studying",
    "activitySessionID": "286bc38d-bed0-4faa-9ed1-4f5d3effb800",
    "detectionMethod": "Manual",
    "installationId": "221beb5c-adde-4b4d-b95b-1fe7c23eb0a9",
    "latitude": 51.4685915,
    "logType": "Activity",
    "longitude": 5.4720262,
    "timestamp": 1792944070458
  },
  {
    "accuracy": 100,
    "actionType": "Stop",
    "activityName": "Studying",
    "activitySessionID": "286bc38d-bed0-4faa-9ed1-4f5d3effb800",
    "detectionMethod": "Manual",
    "installationId": "221beb5c-adde-4b4d-b95b-1fe7c23eb0a9",
    "latitude": 51.4685915,
    "logType": "Activity",
    "longitude": 5.4720262,
    "timestamp": 1792944190458
  }
]
```

---

## GPS Location

**URL:** `https://picoapi.onrender.com/gps-locations`

### What `"accuracy": 100` Actually Means

- **Unit:** Meters (Radius of 68% confidence circle).
- `100` means there is a 68% probability that your true real-world location is within a 100-meter radius circle around the recorded latitude and longitude.

### Smaller Numbers = MORE Accurate

- `"accuracy": 5.0` -> High precision! (Accurate within 5 meters)
- `"accuracy": 12.5` -> Good outdoor GPS fix! (Accurate within 12.5 meters).
- `"accuracy": 100.0` -> Low precision! (Accurate only within 100 meters. Usually obtained indoors from Cell Towers or Wi-Fi when satellite signals are blocked).

### Example

```json
[
  {
    "accuracy": 100,
    "detectionMethod": "Auto",
    "installationId": "221beb5c-adde-4b4d-b95b-1fe7c23eb0a9",
    "latitude": 51.4685915,
    "logType": "Location",
    "longitude": 5.4720262,
    "timestamp": 1792943777566
  }
]
```

---

## Sleeping

**URL:** `https://picoapi.onrender.com/sleeping-logs`

### Status flag

- `0` = Successful
- `1` = Missing Data
- `2` = Not Detected

In short, keep the status flag 0 logs and drop the others! Or get creative here :)

### Example

```json
[
  {
    "accuracy": 12.5,
    "actionType": "Start",
    "activityName": "Sleeping",
    "activitySessionID": "4a7c04c5-6ada-4cc9-bc04-7265a4ef84f9",
    "detectionMethod": "Auto",
    "installationId": "221beb5c-adde-4b4d-b95b-1fe7c23eb0a9",
    "latitude": 51.4416,
    "logType": "Sleeping",
    "longitude": 5.4697,
    "status": 0,
    "timestamp": 1792915299229
  },
  {
    "accuracy": 12.5,
    "actionType": "Stop",
    "activityName": "Sleeping",
    "activitySessionID": "4a7c04c5-6ada-4cc9-bc04-7265a4ef84f9",
    "detectionMethod": "Auto",
    "installationId": "221beb5c-adde-4b4d-b95b-1fe7c23eb0a9",
    "latitude": 51.4416,
    "logType": "Sleeping",
    "longitude": 5.4697,
    "status": 0,
    "timestamp": 1792944099229
  }
]
```

---

## Commute (Auto)

**URL:** `https://picoapi.onrender.com/activity-logs`

### `activityName` options

- `"Commuting (In Vehicle)"` — Triggered when driving a car, riding a bus, train, or motor vehicle (DetectedActivity.IN_VEHICLE).
- `"Commuting (On Bicycle)"` — Triggered when riding a bicycle or cycling (DetectedActivity.ON_BICYCLE).
- `"Commuting (Walking)"` — Triggered when walking or jogging (DetectedActivity.WALKING).
- `"Commuting (Running)"` — Triggered when running or jogging (DetectedActivity.RUNNING).
- `"Commuting"` — Generic fallback for any unclassified motion transition.

### Example

```json
[
  {
    "accuracy": 12.5,
    "actionType": "Start",
    "activityName": "Commuting (In Vehicle)",
    "activitySessionID": "0891537b-d355-4033-b683-e33dda199653",
    "detectionMethod": "Auto",
    "installationId": "221beb5c-adde-4b4d-b95b-1fe7c23eb0a9",
    "latitude": 51.4416,
    "logType": "Commuting",
    "longitude": 5.4697,
    "timestamp": 1792942301236
  },
  {
    "accuracy": 12.5,
    "actionType": "Stop",
    "activityName": "Commuting (In Vehicle)",
    "activitySessionID": "0891537b-d355-4033-b683-e33dda199653",
    "detectionMethod": "Auto",
    "installationId": "221beb5c-adde-4b4d-b95b-1fe7c23eb0a9",
    "latitude": 51.4416,
    "logType": "Commuting",
    "longitude": 5.4697,
    "timestamp": 1792944101236
  }
]
```

---

## Survey

**URL:** `https://picoapi.onrender.com/survey_responses`

### Satisfaction score

`satisfactionScore = 99`. The code means that this log was auto-submitted because there was remaining or cross-day active activity, so it can be calculated correctly! This is marked as an auto log! It submits the remaining hours the user didn't submit by the end of the day. Don't use the score; just add up the activity hours!

### Example

```json
{
  "activities": [
    {
      "activityName": "Sleeping",
      "actualHours": 8,
      "targetHours": 8
    },
    {
      "activityName": "Studying",
      "actualHours": 0.03333333333333333,
      "targetHours": 3
    },
    {
      "activityName": "Doing Sports",
      "actualHours": 0,
      "targetHours": 1
    },
    {
      "activityName": "Pursue Hobbies",
      "actualHours": 0,
      "targetHours": 2
    }
  ],
  "detectionMethod": "Manual",
  "installationId": "221beb5c-adde-4b4d-b95b-1fe7c23eb0a9",
  "logType": "Survey",
  "satisfactionScore": 3,
  "surveyDate": "2026-10-25",
  "surveyTimestamp": 1792944276995
}
```

---

# Data Types

## General Activity Logs Payload

- `"activitySessionID": String (UUID string, e.g. "aeda82a5-4583-4a09-a2f7-9f03d81bc4cd")`
- `"activityName": String (e.g. "Eating", "Studying", "Commuting (In Vehicle)")`
- `"actionType": String (e.g. "Start" or "Stop")`
- `"timestamp": Number (Long Integer) (Unix epoch time in milliseconds, e.g. 1792941035011)`
- `"logType": String (e.g. "Activity" or "Commuting")`
- `"detectionMethod": String (e.g. "Manual" or "Auto")`
- `"latitude": Number (Float/Double) or null (e.g. 51.4686011)`
- `"longitude": Number (Float/Double) or null (e.g. 5.4717419)`
- `"accuracy": Number (Float/Double) or null (e.g. 16.685)`
- `"installationId": String (UUID string, e.g. "b7290588-dafb-4962-b75f-0c96881c024a")`

## Auto Sleep Logs Payload

- `"activitySessionID": String (UUID string, e.g. "96ab2ec7-e69f-47c4-9625-de6606491e23")`
- `"activityName": String (Constant "Sleeping")`
- `"actionType": String (e.g. "Start" or "Stop")`
- `"timestamp": Number (Long Integer) (Unix epoch time in milliseconds, e.g. 1792747599340)`
- `"logType": String (Constant "Sleeping")`
- `"detectionMethod": String (Constant "Auto")`
- `"latitude": Number (Float/Double) or null (e.g. 51.4416)`
- `"longitude": Number (Float/Double) or null (e.g. 5.4697)`
- `"accuracy": Number (Float/Double) or null (e.g. 12.5)`
- `"status": Number (Integer) or null (Google Sleep API status flag: 0 = Successful, 1 = Missing, 2 = Not Detected)`
- `"installationId": String (UUID string, e.g. "b7290588-dafb-4962-b75f-0c96881c024a")`

## Background GPS Locations Payload

- `"logType": String (Constant "Location")`
- `"detectionMethod": String (Constant "Auto")`
- `"latitude": Number (Float/Double) (e.g. 51.4685507)`
- `"longitude": Number (Float/Double) (e.g. 5.4718295)`
- `"accuracy": Number (Float/Double) (e.g. 12.5)`
- `"timestamp": Number (Long Integer) (Unix epoch time in milliseconds, e.g. 1792774488530)`
- `"installationId": String (UUID string, e.g. "b7290588-dafb-4962-b75f-0c96881c024a")`

## Daily Satisfaction Survey Payload

- `"surveyDate": String (Date string in "yyyy-MM-dd" format, e.g. "2026-10-22")`
- `"surveyTimestamp": Number (Long Integer) (Unix epoch time in milliseconds, e.g. 1792762106409)`
- `"logType": String (Constant "Survey")`
- `"detectionMethod": String (e.g. "Manual" for user survey, or "Auto" for day-reset reconciliation)`
- `"satisfactionScore": Number (Integer) (Score 1 to 10 for user survey, or 99 for auto-reconciliation)`
- `"installationId": String (UUID string, e.g. "b7290588-dafb-4962-b75f-0c96881c024a")`
- `"activities": Array of Objects, where each object contains:`
  - `"activityName": String (e.g. "Sleeping", "Studying", "Doing Sports", "Pursue Hobbies")`
  - `"targetHours": Number (Float/Double) (e.g. 8.0, 3.0)`
  - `"actualHours": Number (Float/Double) (e.g. 7.5, 2.0)`

---

**END!**
