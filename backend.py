import requests

API_KEY = "783ac17e0b57c3264e31e8424474c8de"


def get_data(place, forecast_days=None, conditions=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if conditions == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if conditions == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(len(get_data(place="Nairobi", forecast_days=3, conditions="Temperature")))


