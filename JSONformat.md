## JSON format:
url: https://picoapi.onrender.com/activity-logs
Activity tracking:
```
[
  {
    "accuracy": 5,
    "actionType": "Start",
    "activityName": "Eating",
    "activitySessionID": "055277c1-4eb0-4322-a23d-defef8cdfaf4",
    "latitude": 37.4219983,
    "logType": "Manual",
    "longitude": -122.084,
    "timestamp": 1791948306916
  },
  {
    "accuracy": 5,
    "actionType": "Stop",
    "activityName": "Eating",
    "activitySessionID": "055277c1-4eb0-4322-a23d-defef8cdfaf4",
    "latitude": 37.4219983,
    "logType": "Manual",
    "longitude": -122.084,
    "timestamp": 1791948310163
  }
]
```

url: https://picoapi.onrender.com/gps-locations
GPS location:
```

[
  {
    "accuracy": 12.5,
    "id": 1,
    "latitude": 51.4416,
    "longitude": 5.4697,
    "timestamp": 1791942084255
  }
]
```

url: https://picoapi.onrender.com/sleeping-logs
Sleeping:
status flag: 0 = Successful, 1 = Missing Data, 2 = Not Detected).
```
[
  {
    "actionType": "Start",
    "activityName": "Sleeping",
    "activitySessionID": "849815b8-35a2-4f18-b17d-7e7afa8e2c2b",
    "logType": "Auto",
    "status": 0,
    "timestamp": 1791913277834
  },
  {
    "actionType": "Stop",
    "activityName": "Sleeping",
    "activitySessionID": "849815b8-35a2-4f18-b17d-7e7afa8e2c2b",
    "logType": "Auto",
    "status": 0,
    "timestamp": 1791942077834
  }
]
```

url: https://picoapi.onrender.com/commute-logs
Commute (Auto):
```
[
  {
    "actionType": "Start",
    "activityName": "Commuting (In Vehicle)",
    "activitySessionID": "cc0a5476-19b1-4c89-b8fe-39c327f51b1c",
    "logType": "Auto",
    "timestamp": 1791941999238
  },
  {
    "actionType": "Stop",
    "activityName": "Commuting (In Vehicle)",
    "activitySessionID": "cc0a5476-19b1-4c89-b8fe-39c327f51b1c",
    "logType": "Auto",
    "timestamp": 1791943799238
  }
]
```

url: https://picoapi.onrender.com/survey_responses
Survey:
```
{
  "activities": [
    {
      "activityName": "Sleeping",
      "actualHours": 0,
      "targetHours": 8
    },
    {
      "activityName": "Studying",
      "actualHours": 0,
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
  "satisfactionScore": 9,
  "surveyDate": "2026-10-287",
  "surveyTimestamp": 1791946954947
}
```
