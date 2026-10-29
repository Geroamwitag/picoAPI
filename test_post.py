import requests


def main():
    test_activity_logs_post()


def test_activity_logs_post():
    url = "https://picoapi.onrender.com/activity-logs"

    payload = [
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

    try:
        response = requests.post(
            url,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=30
        )

        print("Status code:", response.status_code)
        print("Response:", response.text)

        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
    

if __name__ == "__main__":
    main()