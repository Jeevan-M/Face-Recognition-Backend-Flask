import os


# print(os.listdir('Report'))

# from pymongo import MongoClient

# client = MongoClient(
#     "mongodb+srv://ezhil55:ezhil55@cluster0.xaim7.mongodb.net/<dbname>?retryWrites=true&w=majority")
# db = client.get_database("Ezhilarasi_5591")
# records = db.Ezhil_5591

# data = list(records.find(
#     {"Date": {"$gte": "05-03-2021", "$lt": "06-03-2021"}}))

# from datetime import timedelta, date

# import datetime

# def dateRange(date1, date2):
#     for n in range(int((date2 - date1).days)+1):
#         yield date1 + timedelta(n)

# def spliteDate(reportDate):
#     global date
#     listOfDate = list()
#     reportDate = reportDate.split('/')
#     fromYear, fromMonth, fromDate = map(int, reportDate[0].split('-')[::-1])
#     toYear, toMonth, toDate = map(int, reportDate[1].split('-')[::-1])
#     fromDate = date(fromYear, fromMonth, fromDate)
#     toDate = date(toYear, toMonth, toDate)
#     for date in dateRange(fromDate, toDate):
#         listOfDate.append(date.strftime("%d-%m-%Y"))
#     return listOfDate

# reportDate = "01-03-2021/10-03-2021"

# # spliteDate(reportDate)

# print(datetime.datetime.utcnow())
