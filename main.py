# -*- coding: utf-8 -*-
import forecastio
import datetime
icons_dir = './icons/'

coord = (55.6, 37.7)

icons = {
    'clear-day':'Sun.png',
    'clear-night':'Moon.png',
    'rain':'Cloud-Rain.png',
    'snow':'Cloud-Snow-Alt.png',
    'sleet':'Cloud-Hail.png',
    'wind':'Wind.png',
    'fog':'Cloud-Fog.png',
    'cloudy':'Cloud.png',
    'partly-cloudy-day':'Cloud-Sun.png',
    'partly-cloudy-night':'Cloud-Moon.png',
}

def weather(query):
    results = []
    forecast = forecastio.load_forecast('fa4410dea9d5faaf6b54c606b9f2030c', *coord, units='si')
    d = forecast.currently().d
    # summary for right now
    results.append({
        "Title": '{}'.format(forecast.hourly().summary),
        "SubTitle": 'Temp: {}°C    \tPressure: {:.2f}mm    \tWind: {}m/s    \tRain: {:.2f}%'.format(
                d['temperature'], d['pressure']*0.7501, d['windSpeed'], d['precipProbability']*100),
        "IcoPath": icons_dir + icons.get(d['icon'], '')
    })
    # todo: in 1 hour, 3 hours, 6, 12, 24
    if not results:
        results.append({
            "Title": 'Not found',
            "SubTitle": '',
            "IcoPath":"Images/app.png"
        })
    return results

from wox import Wox

class Weather(Wox):
    def query(self, query):
        return weather(query)

if __name__ == "__main__":
    Weather()