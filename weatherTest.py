from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

from datetime import datetime

def print_weather(weather):
  refTs     = datetime.fromtimestamp(weather.reference_time())
  # sunRiseTs = datetime.fromtimestamp(weather.sunrise_time())
  # sunSetTs  = datetime.fromtimestamp(weather.sunset_time())
  print("Time       : ", end=''); print(refTs)
  print("Temperature: ", end=''); print(weather.temperature('fahrenheit'))
  print("Status     : ", end=''); print(weather.status)
  print("Detailed   : ", end=''); print(weather.detailed_status)
  print("Humidity   : ", end=''); print(weather.humidity)
  print("Snow       : ", end=''); print(weather.snow)
  print("Rain       : ", end=''); print(weather.rain)
  print("Clouds     : ", end=''); print(weather.clouds)
  # print("Sun rise   : ", end=''); print(sunRiseTs)
  # print("Sun set    : ", end=''); print(sunSetTs)


def main():
  owm = OWM('XXXXXX')
  mgr = owm.weather_manager()

  observation = mgr.weather_at_place('Ashburn,VA,US')
  w = observation.weather

  print("observation now:")
  print_weather(w)

  one_call = mgr.one_call(lat=observation.location.lat, lon=observation.location.lon)

  print("\nCurrent")
  print_weather(one_call.current)

  for i in range(len(one_call.forecast_daily)):
    print("\nDaily " + str(i))
    print_weather(one_call.forecast_daily[i])

  for i in range(len(one_call.forecast_hourly)):
    print("\nHourly " + str(i))
    print_weather(one_call.forecast_hourly[i])

if __name__ == "__main__":
  main()