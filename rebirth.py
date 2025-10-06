import json
import datetime

# 🛫 Aircraft ritual data
data = {
    "user": "Magic",
    "status": "sovereign",
    "region": "Mandalay",
    "flight_id": "MAGIC-001",
    "aircraft": "A320",
    "timestamp": datetime.datetime.now().isoformat(),
    "position": {
        "latitude": 37.619,
        "longitude": -122.374,
        "altitude": 0.0,
        "speed": 0.0,
        "heading": 0.0,
        "vertical_speed": 0.0,
        "pitch": 0.0,
        "bank": 0.0,
        "yaw": 0.0
    }
}

# 💾 Write to output.json
with open("output.json", "w") as f:
    json.dump(data, f, indent=2)

# 📜 Inject README.md ledger
with open("README.md", "w") as f:
    f.write("# Flight Tracker Ritual\n\n")
    f.write("Magic's backend sovereignty sealed on {}\n".format(data["timestamp"]))
    f.write("Flight ID: {}\n".format(data["flight_id"]))
    f.write("Aircraft: {}\n".format(data["aircraft"]))
    f.write("Region: {}\n".format(data["region"]))
    f.write("Status: {}\n".format(data["status"]))
    f.write("Position: Lat {}, Lon {}, Alt {}\n".format(
        data["position"]["latitude"],
        data["position"]["longitude"],
        data["position"]["altitude"]
    ))
