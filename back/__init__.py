from flask import Flask, request
import json

app = Flask(__name__)
events = []

@app.route('/hooks/', methods=['POST'])
def foo():
   data = json.loads(request.data)
   events.append(data)
   print("New commit info: {}".format(data))
   return "OK"

@app.route('/', methods=['GET'])
def show():
    return "{}".format(events)

if __name__ == '__main__':
   app.run()
