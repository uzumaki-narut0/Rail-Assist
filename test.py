import requests
api_key = "beiifc3h3m";
base_url = "http://api.railwayapi.com/v2/pnr-status/pnr/";
pnr_no = str(6306534268);
full_url = base_url + pnr_no + "/apikey/" + api_key;
print(full_url)
r = requests.get(full_url)
print(r.json())