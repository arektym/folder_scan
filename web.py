from flask import Flask, render_template, request, Response, json
from string import Template
from db import get_file, get_file_list
folder_scan = Flask(__name__)

@folder_scan.route("/")
def js_sample():
    return render_template('index.html')

@folder_scan.route("/file_list/")
def file_list():
    '''file list view'''
    result =[]
    for f in get_file_list():
        result.append({'file':f.name, 'size':f.size,})# file_m_time=f.time_modified, file_c_time=f.time_created))
    return Response(json.dumps(result), mimetype='application/json')

@folder_scan.route("/file_info/")
def file_info(file_name=None):
    '''file info view'''
    file_name=request.args.get('file',0, type=str)
    #TODO: file_name validation goes here
    f=get_file(file_name)
    if f:
       t='''{"file": {
            filename: $name,
            size: $size,
            m_time: $m_time,
            c_time: $c_time,
        },
        }
       '''
       template= Template(t)    
       return template.substitute(name=f.name, size=f.size, m_time=f.time_modified, c_time=f.time_created)
    else:
       return 'Error, file not found in db'


if __name__ == "__main__":
    folder_scan.run()

