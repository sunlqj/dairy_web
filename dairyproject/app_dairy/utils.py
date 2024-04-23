import datetime
from django.utils.timezone import localtime

def get_time():
    """
    获取年月日时间 
    :return str '%Y-%m-%d-%H:%M:%S.%f'
    """
    import datetime
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

def toshanghai(date):
    import pytz
    import datetime
    original_time = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
    original_time = original_time.replace(tzinfo=pytz.utc)
    shanghai_tz = pytz.timezone('Asia/Shanghai')
    shanghai_time = original_time.astimezone(shanghai_tz)

    return shanghai_time.strftime('%Y-%m-%d %H:%M:%S.%f')
    

def time_day_subtraction(time_str, day_num_int):
    """
    时间字符串做减法（time_str 2020-06-29 02:23:45.852, day_num_int 2）
    :return str '%Y-%m-%d-%H:%M:%S'
    """
    delta = datetime.timedelta(days=-day_num_int)
    #time_str = '2020-06-29 02:23:45.852'
    d1 = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')#d1 = datetime.datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S.%f')
    n_days = d1 + delta
    return n_days.strftime('%Y-%m-%d %H:%M:%S.%f') #2020-06-29 02:23:42.352000

def time_subtraction_s(a1,a2):
    """时间减法 a1-a2 时间格式 '%Y-%m-%d %H:%M:%S.%f' 返回秒"""
    #print(a1,a2)
    try:
        b1 = datetime.datetime.strptime(a1, '%Y-%m-%d %H:%M:%S.%f')
    except:
        b1 = datetime.datetime.strptime(a1, '%Y-%m-%d %H:%M:%S')

    try:
        b2 = datetime.datetime.strptime(a2, '%Y-%m-%d %H:%M:%S.%f')
    except:
        b2 = datetime.datetime.strptime(a2, '%Y-%m-%d %H:%M:%S')
        
    c = b1 - b2
    return c.total_seconds()   #105.0

#time_subtraction('2020-06-29 02:25:25.852','2020-06-29 02:23:40.852') #105.0

# a = time_day_subtraction('2020-06-29 02:23:45.852',200)
# print(a)
# def get_time():
#     """获取年月日时间 return %Y-%m-%d-%H-%M-%S-%f"""
#     import datetime
#     return datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
# def get_time_day():
#     """获取年月日  return %Y-%m-%d"""
#     return datetime.datetime.now().strftime('%Y-%m-%d')

