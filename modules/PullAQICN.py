import requests


class AirInfo:
    def __init__(self, city, token):
        self.city = city
        self.token = token

    def pull(self):
        url = 'http://api.waqi.info/feed/' + self.city + '/?token=' + self.token
        d = requests.get(url, auth=('user', 'pass'))
        data = d.json()
        aqi = data['data']['iaqi']['pm25']['v']
        temp = data['data']['iaqi']['t']['v']

        return aqi, temp
