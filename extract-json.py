import json

import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



while True:
    url = input('Enter url: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    info = json.loads(data)
    print('User count:', len(info["comments"]))

    count = 0

    for item in info['comments']:
      count += int(item['count'])
    
    print('total comments: ', count)




