from datetime import datetime


def get_status():
    current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {
        "status": "success",
        "data": {
            "timestamp": current_timestamp,
        },
    }
