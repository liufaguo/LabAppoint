# @Author  : Harrison
# @Time   : 2023/5/12 23:23
# @Function: 实验室预约
#修改phone,userId,roomSeatId(先登录）,开始日期,预约天数
import datetime

import datetime
import requests

url = "http://172.19.231.2:10269/reservation/reserveRecord/doReserve"
params = {
    "roomId": "36",
    "purpose": "实验室",
    "phone": "18324983064",
    "userId": "212503028",
    # "roomSeatId": "3619",
    "roomSeatId": "3618",
    # "roomSeatId": "3404",
    "_": "1683901200122"
}



reserveDay=datetime.datetime(2023, 6, 13) #开始的日期的前一天
start_time = datetime.time(8, 0)
time_ranges = [(start_time, datetime.time(8, 45)),
               (datetime.time(8, 46), datetime.time(9, 30)),
               (datetime.time(9, 45), datetime.time(10, 30)),
               (datetime.time(10, 31), datetime.time(11, 15)),
               (datetime.time(11, 16), datetime.time(12, 0)),
               (datetime.time(12, 1), datetime.time(12, 59)),
               (datetime.time(13, 1), datetime.time(13, 45)),
               (datetime.time(13, 46), datetime.time(14, 30)),
               (datetime.time(14, 45), datetime.time(15, 30)),
               (datetime.time(15, 31), datetime.time(16, 15)),
               (datetime.time(16, 16), datetime.time(17, 0)),
               (datetime.time(17, 1), datetime.time(17, 59)),
               (datetime.time(18, 0), datetime.time(18, 45)),
               (datetime.time(18, 46), datetime.time(19, 30)),
               (datetime.time(19, 40), datetime.time(22, 25))]

# 这里30代表往后预约30天（最好看下预约界面最晚能预约到哪一天，小心管理员找你谈话）

for i in range(120):
    reserveDay += datetime.timedelta(days=1)
    print(reserveDay.strftime('%Y-%m-%d'))
    params["reserveDay"]=reserveDay.strftime('%Y-%m-%d')
    reserveTimeId=0
    for start, end in time_ranges:
        # print(f"{start.strftime('%H:%M')}-{end.strftime('%H:%M')}")
        reserveTimeId += 1
        start_str = start.strftime("%H:%M")
        end_str = end.strftime('%H:%M')
        print(end_str)
        params["startTime"] = start_str
        params["endTime"] = end_str
        print(start_str, end_str, reserveTimeId)
        if (end_str == '12:59'):
            params["reserveTimeId"]=str(19)
            reserveTimeId-=1
        elif (end_str == '17:59'):
            params["reserveTimeId"] = str(20)
            reserveTimeId-=1
        else:
            params["reserveTimeId"] = str(reserveTimeId)
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print(response.text)
        else:
            print("Error: ", response.status_code)


