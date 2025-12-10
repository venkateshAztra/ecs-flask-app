import requests

API_KEY = "27d4e24fa03eeeab8e23cc3ebc8898ed"
city = "London"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

print("im done")
print("Status code : ", response.status_code)
print("📡 Status Code:", response.status_code)
print("Response:")
print(response.text)
print("im done")

