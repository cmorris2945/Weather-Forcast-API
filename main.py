import requests


def get_weather(city, units='metrics', api_key= '99e07b5c10d550fd7f4b60a532026'):
  url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid= {api_key}&units{units}"
  r = requests.get(url)
  content = r.json()
  return content

print(get_weather(city='San Antonio'))
 
