from flask import Flask, render_template,jsonify
from flask import make_response
from sense_hat import SenseHat
import threading
import time as t

app = Flask(__name__)

data=[
    {
        'time':u'2017-08-08 15:30:00',
        'temperature':u'100',
        'pressure':u'101.325',
        'humidity':u'l'    
    },
    {'time':u'2017-08-08 15:30:00',
        'temperature':u'100',
        'pressure':u'101.325',
        'humidity':u'l' 
    }
    ]
data1={'testStr':'ddddddddddd'}

def insert_data():
    sense = SenseHat()
    ISOTIMEFORMAT='%Y-%m-%d %X'
    temperature = round(sense.get_temperature(),3)
    humidity = round(sense.get_humidity(),3)
    pressure = round(sense.get_pressure(),3)
    time = t.strftime(ISOTIMEFORMAT)
    sensedata={'time':time,'temperature':temperature,
        'pressure':pressure,'humidity':humidity }
    data.append(sensedata)
    print(time)
    print(sensedata)

    count=threading.Timer(10.0,insert_data)
    #if(event.action == "")

@app.route('/data',methods=['GET'])
def get_data():
    return jsonify({'data':data})
    #return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/infos')
def get_infos():
    return render_template('infos.html',datatest=data1,dataStr=data,
                           data=jsonify({'data':data}))
@app.route('/about')
def about():
    return render_template('about.html')

#@app.route('/login')
#def login():
# return render_template('login.html')

@app.route('/page')
def hello():
    return render_template('page.html')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}),404)

if __name__=='__main__':
    #count = threading.Timer(10.0,insert_data)
    #count.start()
    insert_data()
    app.run(debug=True, host='172.20.88.88')
