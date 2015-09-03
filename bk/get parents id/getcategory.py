import urllib2
import urllib
import json
from urllib2 import URLError, HTTPError

api_key = '67929F4F6AEAC2F250AE188343D01BA6'
apiurl = 'http://api.eia.gov/category/'
top_category_id = 378

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
    data = set_param(category_id)
    full_url = create_url(data)
    jsonData = request_get(full_url)
    return jsonData

def get_children(self_catid, data, level):
    global outChildren, meta
    seriesid = {};
    if len(data['category']['childseries']) != 0:
        for e in data['category']['childseries']:
            outSeriesid.append([e['series_id'], self_catid, level])
    if len(data['category']['childcategories']) != 0:
        for child in data['category']['childcategories']:
            meta.append([child['category_id'], child['name']])
            seriesid[child['category_id']] = self_catid;
        outChildren[level] = seriesid
    return outChildren, meta

def get_series_id(param):
    global outChildren, meta
    if not param in outChildren:
        return False;
    for child_id in outChildren[param]:
        current_id = child_id;
        print param, ',',len(meta)
        data = get_cat_data(current_id);
        outChildren, meta = get_children(current_id, data, param+1);
    return True;

outChildren = {};
meta = [];
outSeriesid = [];
childlist = [];
current_id = top_category_id;

#first
data = get_cat_data(current_id)
outChildren, meta = get_children(current_id, data,0)

#second~
result = True;
param = 0;
while(result == True):
    result = get_series_id(param)
    param += 1;
    print param

text_file = open("Out_series_id.txt", "w")
meta_file = open("Out_meta.txt", "w")
for e in outSeriesid:
    text_file.write(e[0]+','+str(e[1])+','+str(e[2])+'\n')

for d in meta:
    meta_file.write(str(d[0])+str(d[1])+'\n')

text_file.close()
meta_file.close()

out = [];
col1 = outSeriesid[0][0]
col2 = outSeriesid[0][1]
col3 = 

p = outSeriesid[0][1]
level = outSeriesid[0][2] -1

def temp(level, p):
    parents = [];
    while(level >= 0):
        p = outChildren[level][p]
        parents.insert(0, p);
        level -= 1;
    return parents;
