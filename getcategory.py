import urllib2
import urllib
import json
from urllib2 import URLError, HTTPError
import sqlite3
import re

api_key = '67929F4F6AEAC2F250AE188343D01BA6'
apiurl = 'http://api.eia.gov/category/'
root_id = 40
#connect_db = 'testdb.sqlite3'
skip_id = [32,33,34,1017,41145];
connect_db = 'db.sqlite3'

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
    print 'search-- '+ str(category_id)
    data = set_param(category_id)
    full_url = create_url(data)
    jsonData = request_get(full_url)
    return jsonData

def get_children(self_catid, data, level):
    global outChildren, meta
    seriesid = {};
    print 'childseries--     '+ str(len(data['category']['childseries']))
    print 'childcategories-- '+ str(len(data['category']['childcategories']))
    #found last children(series_id)
    if len(data['category']['childseries']) != 0:
        for e in data['category']['childseries']:
            #get child category_id, self category_id, data level
            outSeriesid.append([e['series_id'], self_catid, level]) 
            return outChildren, meta; #! intend
    #get children categories
    if len(data['category']['childcategories']) != 0:
        for child in data['category']['childcategories']:
            #get category_id, and its name
            meta.append([child['category_id'], child['name']])
            seriesid[child['category_id']] = self_catid;
        if level in outChildren:
            outChildren[level].update(seriesid);
        else:
            outChildren[level] = seriesid;
        return outChildren, meta;

def get_series_id(param):
    global outChildren, meta
    if not param in outChildren:
        #no child category_id to search
        return False, outChildren, meta;
    for child_id in outChildren[param]:
        if(child_id not in skip_id):
            current_id = child_id;
            #call api
            data = get_cat_data(current_id);
            #extract data
            outChildren, meta = get_children(current_id, data, param+1);
    return True, outChildren, meta;

def get_parentsId(record, level, p):
    record = [p];
    #search category_id from the bottom to top
    while(level >= 0):
        #get parent_id of p
        p = outChildren[level][p]
        record.insert(0, p);
        level -= 1;
    return record;

def data_flatten(series):
    record = [];
    #the data level(how deep)
    level = series[2] -1;
    #parent_id
    p = series[1];
    record = get_parentsId(record, level, p);
    #insert at first column
    record.insert(0, series[0]);
    return record;

def output_file():
    out_file = open("Out_series_tree.txt", "w");
    text_file = open("Out_series_id.txt", "w");
    meta_file = open("Out_meta.txt", "w");
    for f in output:
        for g in f:
            out_file.write(str(g)+',');
        #need 10 columns
        add_col = ','*(11 - len(f));
        out_file.write(add_col+'\n');
    for e in outSeriesid:
        text_file.write("%s,%d,%d\n" % (e[0],e[1],e[2]));
    for d in meta:
        meta_file.write("%s,%s\n" % (d[0],d[1]));
    out_file.close();
    text_file.close();
    meta_file.close();

#conver to tuple
def convert_to_tuple(data):
    tup =[];
    for rec in data:
        tup.append(tuple(rec));
    return tup;

def db_insert(data, meta):
    #DB connection
    conn = sqlite3.connect(connect_db);
    c = conn.cursor();
    for rec in data:
        val = "?,"*len(rec)
        val = val[:-1] #remove last comma
        col = "series_id, "
        for i in range(1,len(rec)): 
            col += " category" + str(i) + "_id,"
        col = col[:-1] #remove last comma
        sql = 'INSERT INTO graphs_scategory ('+col+') Values ('+val+')'
        c.execute(sql, rec)   
    #c.executemany('INSERT INTO graphs_scategory Values (?,?,?,?)', data)
    c.executemany('INSERT INTO graphs_metacategory (category_id, name) Values (?,?)', meta)
    conn.commit()
    conn.close()

def update_geoset_id():
    #DB connection
    conn = sqlite3.connect(connect_db);
    c = conn.cursor();
    sql = 'SELECT series_id, geoset_id FROM graphs_scategory'
    keys = [];
    for row in c.execute(sql):
        keys.append(row);
    #create geoset_id
    p = re.compile("[A-Z]+-([0-9A-Z]+\.)[AMQ]$")
    #original - ELEC.SALES.AL-ALL.Q
    #getset_id- ELEC.SALES.ALL.Q
    for key in keys:
        sql=('UPDATE graphs_scategory SET geoset_id = ?'
         + 'WHERE series_id = ?')
        geoset_id = p.sub(r"\1A", key[0])
        args = [geoset_id] + [key[0]]
        c.execute(sql,args)
    conn.commit()
    conn.close()

#initialize
outChildren = {};
meta = [];
outSeriesid = [];
childlist = [];
current_id = root_id;

#search series_id first level
data = get_cat_data(current_id);
meta.append([root_id, 'Root category'])
outChildren, meta = get_children(current_id, data,0);

#search series_id second to the last level
result = True;
param = 0;
while(result == True):
    result, outChildren, meta = get_series_id(param)
    param += 1;

#change data structure
output = [];
for series in outSeriesid:
    record = data_flatten(series);
    output.append(record);

#export text file for checking data
output_file();

#conver for sqlite update
tupData = [];
tupMeta = [];

tupData = convert_to_tuple(output)
tupMeta = convert_to_tuple(meta)

#Db insert
db_insert(tupData, tupMeta)
update_geoset_id()
