

import socketio
import time
from static.plotting import plottingClass
import eventlet.wsgi
from flask import Flask, render_template


from matplotlib import pyplot as plt
from matplotlib.pyplot import ion


import mpld3
from mpld3 import plugins


ion()

start = time.time()

fig1, axes1 = plt.subplots()
fig1.canvas.set_window_title('Accrelation X')
display1 = plottingClass.RealtimePlot(axes1)

"""fig2, axes2 = plt.subplots()
fig2.canvas.set_window_title('Accrelation Y')
display2 = plottingClass.RealtimePlot(axes2)


fig3, axes3 = plt.subplots()
fig3.canvas.set_window_title('Accrelation Z')
display3 = plottingClass.RealtimePlot(axes3)"""



sio = socketio.Server()
app = Flask(__name__)

@sio.on('connect', namespace='/accData')
def connect(sid, environ):
    print("connect ", sid)

@sio.on('message', namespace='/accData')
def message(sid, data):

    if data[0:5] == 'accX ':
        x = float(data[4:15])
        print(x)

        display1.add(time.time() - start, x)

    elif data[0:5] == 'accY ':
        y = float(data[4:15])
        print(y)

        #display2.add(time.time() - start, y)

    elif data[0:5] == 'accZ ':
        z = float(data[4:15])
        print(z)

        #display3.add(time.time() - start, z)
    plt.pause(0.0001)

@sio.on('disconnect', namespace='/accData')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    # wrap Flask application with engineio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5980)), app)