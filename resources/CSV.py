import json
from datetime import datetime
import os
from pymongo import MongoClient
import csv
from resources.extraFunction import jsonDecoder


client = MongoClient(
    "mongodb+srv://ezhil55:ezhil55@cluster0.xaim7.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.get_database("Ezhilarasi_5591")
records = db.Ezhil_5591
print("Database Connected ...")
current_date = datetime.now().strftime("%d-%m-%Y")
fileName = '_'.join(['AttendanceReport', current_date, '.csv'])
csv_path = 'Report/'+fileName


# def jsonDecoder(data):
#     jsonDec = json.decoder.JSONDecoder()
#     value = jsonDec.decode(data)
#     return value


def Object_To_Dict(Data):
    new_data = []
    for data in Data:
        if data['Check_out_Time'] == "":
            check_out_Time = ""
        else:
            check_out_Time = jsonDecoder(data['Check_out_Time'])[-1]
        dict_data = {
            "Name": data['Name'],
            "Date": data['Date'],
            "Status": data['Status'],
            "Check_in_Time": jsonDecoder(data['Check_in_Time'])[0],
            "Check_out_Time": check_out_Time,
            "Working_Hours": data['Working_Hours']}
        new_data.append(dict_data)
    return new_data


def ConvertToCSV():
    if not (os.path.isfile(csv_path)):
        with open(csv_path, 'w', newline='') as file:
            csv.writer(file)
    data_file = open(csv_path, 'w', newline="")
    csv_writer = csv.writer(data_file)
    count = 0
    data = list(records.find({"Date": str(current_date)}))
    datas = Object_To_Dict(data)
    for emp in datas:
        if count == 0:
            header = emp.keys()
            headers = list(header)
            csv_writer.writerow(headers)
            count += 1
        csv_writer.writerow(emp.values())
    data_file.close()
    print(f'{fileName} Created')


# print(current_date)
ConvertToCSV()
