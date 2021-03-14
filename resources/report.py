import glob
import os
from datetime import datetime
from resources.extraFunction import ConvertToCSV, MailAttendance
from flask_restful import Resource, reqparse
from pymongo import MongoClient
from flask import send_file

client = MongoClient(
    "mongodb+srv://ezhil55:ezhil55@cluster0.xaim7.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.get_database("Ezhilarasi_5591")
records = db.Ezhil_5591
print("Database Connected ...")
dir = 'Report'
current_date = datetime.now().strftime("%d-%m-%Y")
fileNamePath = 'Report/'+'_'.join(['AttendanceReport', current_date, '.csv'])


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
        data = list(records.find(
            {"Date": {"$gte": request_data['from'], "$lt": request_data['to']}}))
        if ConvertToCSV(fileNamePath, data):
            if request_data["email"]:
                if MailAttendance(fileNamePath, request_data['email']):
                    return send_file(fileNamePath, as_attachment=True)
            else:
                return send_file(fileNamePath, as_attachment=True)
        else:
            return {'Message': 'Wrong Request'}, 400
