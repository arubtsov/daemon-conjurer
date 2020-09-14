from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/hooks/', methods=['POST'])
def foo():
   data = json.loads(request.data)
   print("New commit info: {}".format(data))
   return "OK"

if __name__ == '__main__':
   app.run()
