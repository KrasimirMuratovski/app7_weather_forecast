import requests as re
import os

API_key = '065bf142b3830d473ebf487943efcb32'


def get_data(place, forecast_days):
	# API = os.getenv('API_OPENWEATHERMAP')

	url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&units=metric&lang=bg&appid={API_key}'
	request = re.get(url)
	data = request.json()
	filtered_data = data['list']
	nr_values = 8 * forecast_days
	filtered_data = filtered_data[:nr_values]
	# filtered_data = [((x - 32.0) * 5.0/9.0) for x in filtered_data]
	return filtered_data


# if __name__ == '__main__':
# 	print(get_data('Tokyo', 2, ))
