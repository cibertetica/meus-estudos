def timeConvert(seconds):
    hour = minute = rest_hour = rest_minute = 0
    if seconds >= 3600:
        hour = seconds // 3600
        rest_hour = seconds % 3600
    elif seconds >= 60:
        minute = seconds // 60
        rest_minute = seconds % 60
        remain_sec = rest_hour + rest_minute
    else:
        remain_sec = seconds
    return f'{hour}:{minute}:{remain_sec}'

seconds = int(input('Segundos: '))

print(timeConvert(seconds))