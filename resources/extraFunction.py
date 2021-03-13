import json
from datetime import datetime
import os


# gives the time differenc


def TimeDiff(Start, End, Date):
    date = Date.split()
    Start_time = Start.split()
    S_time = Start_time[0].split(":")
    End_time = End.split()
    E_time = End_time[0].split(":")
    Time_Diff = datetime(int(date[0]), int(date[1]), int(date[2]), int(E_time[0]), int(E_time[1]), int(E_time[2])) - datetime(
        int(date[0]), int(date[1]), int(date[2]), int(
            S_time[0]), int(S_time[1]), int(S_time[2])
    )
    working_hours = str(round(Time_Diff.seconds/3600, 3)) + " hrs"
    return working_hours

# gives the json value


def jsonDecoder(data):
    jsonDec = json.decoder.JSONDecoder()
    value = jsonDec.decode(data)
    return value


def filterData(data):
    return {
        'Name': data.get('Name'),
        'Date': data.get('Date'),
        'Check_in_Time': jsonDecoder(data.get('Check_in_Time'))[-1],
        'Check_out_Time': jsonDecoder(data.get('Check_out_Time'))[-1] if data.get('Check_out_Time') else None,
        'Working_Hours': data.get('Working_Hours') if data.get('Working_Hours') else None
    }


def checkTheUser(Name):
    with open('Json/Face_Encoding_Data.json') as f:
        EncodeJsonData = json.load(f)
        personName = list(EncodeJsonData.keys())
    return True if Name in personName else False


def addJWT(jwt):
    jwtJSONFile = 'Json/JWT.json'
    if os.path.isfile(jwtJSONFile):
        os.remove(jwtJSONFile)
    with open(jwtJSONFile, 'w') as outfile:
        json.dump({'token': jwt}, outfile)
        return True


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
