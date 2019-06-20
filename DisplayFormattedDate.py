"""
Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""
import datetime

exam_st_date = (11, 12, 2014)
day = exam_st_date[0]
month = exam_st_date[1]
year = exam_st_date[2]
given_date = datetime.datetime(year, month, day)
print('The examination will start from:', given_date.strftime("%d") + ' / '
        + given_date.strftime("%m") + ' / ' + given_date.strftime("%Y"))
print('The examination will start from: %i / %i / %i'%exam_st_date)
