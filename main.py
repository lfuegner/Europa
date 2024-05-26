import requests

url = "https://data.europarl.europa.eu/api/v2/meps?parliamentary-term=0&format=application%2Fld%2Bjson&offset=0&limit=50"

# Endpoint for getting MEP information
endpoint = 'meps'

# Parameters (example, adjust as needed)
params = {
    'country': 'FR',
    'term': '9'
}

# Make the GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    mep_data = response.json()
    # Print the data or process it as needed
    print(mep_data)
else:
    # Print the error
    print(f"Error: {response.status_code}")
    print(response.text)