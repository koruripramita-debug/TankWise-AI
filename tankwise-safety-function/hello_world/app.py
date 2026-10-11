
import json

def lambda_handler(event, context):
    params = event.get("queryStringParameters") or {}

    body = event.get("body")
    if isinstance(body, str):
        try:
            body = json.loads(body)
        except json.JSONDecodeError:
            body = {}
    if isinstance(body, dict):
        params = {**body, **params}

    try:
        water = float(params.get("water_percent", 50))
        temperature = float(params.get("temperature_c", 35))
        humidity = float(params.get("humidity", 50))
    except (TypeError, ValueError):
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Inputs must be numbers"})
        }

    if not all(map(lambda x: x == x and abs(x) != float("inf"),
                   [water, temperature, humidity])):
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Inputs must be finite numbers"})
        }

    if not 0 <= water <= 100 or not -50 <= temperature <= 70 or not 0 <= humidity <= 100:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Input is outside the accepted range"})
        }

    if water < 20:
        water_advice = "Critical: refill the tank soon."
    elif water < 50:
        water_advice = "Water is running low. Plan your usage."
    else:
        water_advice = "Water level looks adequate for now."

    if temperature >= 40:
        heat_advice = "Extreme heat: avoid strenuous outdoor activity and seek a cool place."
    elif temperature >= 35:
        heat_advice = "High heat: drink water regularly and limit strenuous outdoor activity."
    else:
        heat_advice = "Stay hydrated and monitor local weather guidance."

    if humidity >= 70 and temperature >= 30:
        heat_advice += " High humidity can make it harder for sweat to cool the body."

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "project": "TankWise AI",
            "water_percent": water,
            "temperature_c": temperature,
            "humidity_percent": humidity,
            "water_advice": water_advice,
            "heat_advice": heat_advice
        })
    }
