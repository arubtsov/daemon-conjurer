import os
import json
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from back.models import Event

@app.route('/hooks/', methods=['POST'])
def on_github_event():
    try:
        data = json.loads(request.data)
        event = Event(json_string=data)

        db.session.add(event)
        db.session.commit()

        return "Event added. event id={}".format(data.id)
    except Exception as e:
        print(str(e))
        return str(e)


@app.route('/', methods=['GET'])
def show():
    try:
        events = Event.query.all()

        return jsonify([ev.serialize() for ev in events])

    except Exception as e:
        print(str(e))
        return str(e)


if __name__ == '__main__':
    app.run()
