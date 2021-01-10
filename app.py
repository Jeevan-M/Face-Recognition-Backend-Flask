from flask_jwt_extended import create_access_token, jwt_required, JWTManager
from flask import Flask, render_template
from flask_restful import Api, Resource
from dotenv import load_dotenv
from flask_cors import CORS
import datetime
import logging
import sys
import os


from resources.addToDB import UserToDB, todayAttendance
from resources.checkFace import CheckUserFace, GetStaffName
from resources.extraFunction import addJWT


app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
CORS(app)
jwt = JWTManager(app)  # /auth
endPointApi = Api(app)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


@app.route('/')
def index():
    return render_template('index.html')


class Testtoken(Resource):
    @jwt_required
    def get(self):
        return {'Name': 'Jeevan'}


@app.route('/createNewJWT')
def createNewJWT():
    token = create_access_token(app.config['SECRET_KEY'], fresh=True)
    if addJWT(token):
        return {'token': token}
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


endPointApi.add_resource(Testtoken, '/test')
endPointApi.add_resource(CheckUserFace, '/face')
endPointApi.add_resource(UserToDB, '/saveUser/<string:check>')
endPointApi.add_resource(GetStaffName, '/getName')
endPointApi.add_resource(todayAttendance, '/todayPresent')


if __name__ == "__main__":
    app.run(debug=True)
