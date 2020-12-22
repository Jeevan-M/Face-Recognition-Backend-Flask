from flask import Flask
from addToDB import UserToDB
from checkFace import CheckUserFace
from flask_restful import Api
from flask_cors import CORS
import logging
import sys

app = Flask(__name__)
CORS(app)
endPointApi = Api(app)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


@app.route('/')
def index():
    return 'Face Recognition Attendance System!'


endPointApi.add_resource(CheckUserFace, '/face')
endPointApi.add_resource(UserToDB, '/saveUser/<string:check>')


if __name__ == "__main__":
    app.run(debug=True)
