import pandas as pd

flights = pd.read_csv('data/flight_delays_data.csv')
flights = flights.drop(columns=['delay_time', 'is_claim'])
flights.to_csv('data/test_data.csv', index=False)
