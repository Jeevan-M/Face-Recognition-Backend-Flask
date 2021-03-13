import glob
import os
from resources.extraFunction import Object_To_Dict
from flask_restful import Resource, reqparse
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://ezhil55:ezhil55@cluster0.xaim7.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.get_database("Ezhilarasi_5591")
records = db.Ezhil_5591
print("Database Connected ...")
dir = 'Report'


class Report(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'from',
        type=str,
        required=True,
        help='from date is required'
    )
    parser.add_argument(
        'to',
        type=str,
        required=True,
        help='to date is required'
    )
    parser.add_argument(
        'email',
        type=str,
        help="email is required")

    def post(self):
        if os.listdir(dir):
            for f in os.listdir(dir):
                os.remove(os.path.join(dir, f))
        request_data = Report.parser.parse_args()

        # data = list(records.find(
        #     {"Date": {"$gte": request_data['from'], "$lt": request_data['to']}}))

        # return {"data": "Asdasd"}
        # if request_data['email']
