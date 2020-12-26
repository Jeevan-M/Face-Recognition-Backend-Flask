import json
from datetime import datetime

# gives the time difference


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
