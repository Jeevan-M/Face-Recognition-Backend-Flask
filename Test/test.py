from datetime import datetime
from resources.extraFunction import MailAttendance

current_date = datetime.now().strftime("%d-%m-%Y")
fileNamePath = 'Report/'+'_'.join(['AttendanceReport', current_date, '.csv'])


MailAttendance(fileNamePath, "jeevanjeenu007@gmail.com")
