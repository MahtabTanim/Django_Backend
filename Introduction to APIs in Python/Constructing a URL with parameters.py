# Construct the URL string and pass it to the requests.get() function
import requests
query_params = {'artist':'Deep Prple', 'include_track':'True'}
response = requests.get('http://localhost:3000/lyrics/random/',params=query_params)

print(response.text)

# Print the response URL
print(response.url)

# Print the lyric
print(response.text)

