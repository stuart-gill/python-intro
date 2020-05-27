#  In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#     Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#     Actual data: http://py4e-data.dr-chuck.net/comments_584287.xml (Sum ends with 43)

# You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis. 


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
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
    tree = ET.fromstring(data)

    count = 0
    comments = tree.find('comments')
    commentList = comments.findall('comment')
    print(len(commentList))
    for comment in commentList:
      print(comment.find('count').text)
      count += int(comment.find('count').text)

    print('Total count: ', count)
    # Code for parsing google maps location data
    # results = tree.findall('result')
    # lat = results[0].find('geometry').find('location').find('lat').text
    # lng = results[0].find('geometry').find('location').find('lng').text
    # location = results[0].find('formatted_address').text

    # print('lat', lat, 'lng', lng)
    # print(location)
