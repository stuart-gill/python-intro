import urllib.request, urllib.parse, urllib.error
import json
import ssl
import config

api_key = config.GMAPS_API_KEY

serviceurl = 'https://maps.googleapis.com/maps/api/distancematrix/json?'

# destinations = [
#   'Yakima, WA',
#   'Tacoma, WA',
#   'Bellingham, WA',
#   'Leavenworth, WA',
#   'Portland, OR',
#   'Lopez Island, WA',
#   'Bend, OR'
# ]

# destinations_parm = ''
# for destination in destinations:
#   destinations_parm += destination + '|'

# Read JSON to build destinations parameter, as opposed to hard coded array above 
# Should be able to extent this to reading from a database
str_data = open('sunny65.json').read()
json_data = json.loads(str_data)

destinations_parm = ''
for loc in json_data:
  destinations_parm += str(loc["lat"]) + "," + str(loc["lng"]) + '|'


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter your location: ')
    if len(address) < 1: break

    parms = dict()
    parms['origins'] = address
    parms['destinations']= destinations_parm
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    travel = float(input('How long are you willing to travel in hours? '))
    travel_seconds = travel * 3600
    acceptable_results = []

    elements = js["rows"][0]["elements"]

    # BAD NAMING -- change json_data and js names to indicate diff between json from file and from google
    for i in range(len(elements)):
      if elements[i]["duration"]["value"] < travel_seconds:
        acceptable_results.append(json_data[i]["name"])
    
    print(acceptable_results)







    # lat = js['results'][0]['geometry']['location']['lat']
    # lng = js['results'][0]['geometry']['location']['lng']
    # print('lat', lat, 'lng', lng)
    # location = js['results'][0]['formatted_address']
    # placeid = js['results'][0]['place_id']
    # print(location)
    # print("place id: ", placeid)
