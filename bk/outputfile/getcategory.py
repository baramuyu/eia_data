import urllib2
import urllib
import json
from urllib2 import URLError, HTTPError

api_key = '67929F4F6AEAC2F250AE188343D01BA6'
apiurl = 'http://api.eia.gov/category/'
root_id = 378

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

def get_parentsId(record, level, p):
    record = [p];
    while(level >= 0):
        p = outChildren[level][p]
        record.insert(0, p);
        level -= 1;
    return record;

def data_flatten(series):
    record = [];
    level = series[2] -1;
    p = series[1];
    record = get_parentsId(record, level, p);
    record.insert(0, series[0]);
    return record;

def output_text():
    out_file = open("Out_series_tree.txt", "w");
    text_file = open("Out_series_id.txt", "w");
    meta_file = open("Out_meta.txt", "w");

    for f in output:
        for g in f:
            out_file.write(str(g)+',');
        out_file.write('\n')

    for e in outSeriesid:
        text_file.write("%s,%d,%d\n" % (e[0],e[1],e[2]));

    for d in meta:
        meta_file.write("%s,%s\n" % (d[0],d[1]));

    out_file.close();
    text_file.close();
    meta_file.close();


outChildren = {};
meta = [];
outSeriesid = [];
childlist = [];
current_id = root_id;

#first
data = get_cat_data(current_id);
meta.append([root_id, 'Root category'])
outChildren, meta = get_children(current_id, data,0);

#second~
result = True;
param = 0;
while(result == True):
    result = get_series_id(param)
    param += 1;

output = [];
for series in outSeriesid:
    record = data_flatten(series);
    output.append(record);

output_text();