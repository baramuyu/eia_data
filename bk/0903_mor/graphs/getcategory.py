import urllib2
import urllib
import json
from urllib2 import URLError, HTTPError

api_key = '67929F4F6AEAC2F250AE188343D01BA6'
apiurl = 'http://api.eia.gov/category/'

def set_param(category_id):
    data = {}
    data = {'api_key' : api_key,
              'category_id' : category_id,
              'out': 'json' }
    return data

def create_url(data):
    url_values = urllib.urlencode(data)
    full_url = apiurl + '?' + url_values
    return full_url

def request_get(url):
    try: 
        response = urllib2.urlopen(url)

    except HTTPError as e:
        print('HTTP error type.')
        print('Error code: ', e.code)

    except URLError as e:
        print('URL type error.')
        print('Reason: ', e.reason)

    bData = response.read()

    sData = unicode(bData, 'utf-8-sig')
    jData = json.loads(sData)
    return jData

def get_cat_data(category_id):
    data = set_param('371')
    full_url = create_url(data)
    jsonData = request_get(full_url)
    return jsonData

data = get_cat_data('371')


