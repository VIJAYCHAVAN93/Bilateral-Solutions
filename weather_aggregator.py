def aggregate_weather_data(records):
    city_data = {}
    
    for record in records:
        city = record['city']
        if city not in city_data:
            city_data[city] = {
                'temperature_sum': 0,
                'temperature_count': 0,
                'humidity_sum': 0,
                'humidity_count': 0
            }
        
        if 'temperature' in record:
            city_data[city]['temperature_sum'] += record['temperature']
            city_data[city]['temperature_count'] += 1
        
        if 'humidity' in record:
            city_data[city]['humidity_sum'] += record['humidity']
            city_data[city]['humidity_count'] += 1
    
    
    average_data = {}
    for city, data in city_data.items():
        average_data[city] = {}
        if data['temperature_count'] > 0:
            average_data[city]['average_temperature'] = data['temperature_sum'] / data['temperature_count']
        else:
            average_data[city]['average_temperature'] = None
        
        if data['humidity_count'] > 0:
            average_data[city]['average_humidity'] = data['humidity_sum'] / data['humidity_count']
        else:
            average_data[city]['average_humidity'] = None
    
    return average_data

# Example usage:
if __name__ == "__main__":
    weather_records = [
        {'city': 'New York', 'temperature': 75, 'humidity': 65},
        {'city': 'New York', 'temperature': 80},
        {'city': 'Los Angeles', 'temperature': 85, 'humidity': 40},
        {'city': 'Los Angeles', 'humidity': 45},
        {'city': 'Chicago', 'temperature': 70, 'humidity': 50}
    ]
    
    result = aggregate_weather_data(weather_records)
    print(result)
