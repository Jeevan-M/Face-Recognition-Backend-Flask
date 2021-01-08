from flask import Flask, render_template
from addToDB import UserToDB, todayAttendance
from checkFace import CheckUserFace, GetStaffName
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
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


endPointApi.add_resource(CheckUserFace, '/face')
endPointApi.add_resource(UserToDB, '/saveUser/<string:check>')
endPointApi.add_resource(GetStaffName, '/getName')
endPointApi.add_resource(todayAttendance, '/todayPresent')


if __name__ == "__main__":
    app.run(debug=True)
