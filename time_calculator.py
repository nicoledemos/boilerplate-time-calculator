def get_total(split_start,split_duration):

    split_total = dict()

    split_total["hours"] = split_start["hours"] + split_duration["hours"]
    split_total["mins"] = split_start["mins"] + split_duration["mins"]

    if split_total["mins"] > 60:
        split_total["hours"] = split_total["hours"] + (split_total["mins"] // 60)
        split_total["mins"] = (split_total["mins"] % 60)
    
    if split_total["hours"] > 24:
        split_total["days"] = (split_total["hours"] // 24)
        split_total["hours"] = (split_total["hours"] % 24)
    else:
        split_total["days"] = 0
    
    if split_total["hours"] >= 12:
        split_total["ampm"] = "PM"
    else:
        split_total["ampm"] = "AM"


    if split_total["hours"] > 12:
        split_total["hours"] = split_total["hours"] - 12
    elif split_total["hours"] == 0:
        split_total["hours"] = 12

    
    return split_total

def split_time(hours_mins):
    

    time_dict = dict()

    time = hours_mins.split(':')
    time_dict["hours"] = int(time[0])
    time_dict["mins"] = int(time[1])

    return time_dict

def get_new_time(split_total, start_day):

    new_time = str()

    new_time = new_time + str(split_total["hours"]) + ':' + str(split_total["mins"]).rjust(2,'0') + ' ' + split_total["ampm"]

    if not start_day is None:
        if  split_total["days"] > 0:
            days_of_week = {"MONDAY" : 0 , "TUESDAY" : 1, "WEDNESDAY" : 2, "THURSDAY" : 3, "FRIDAY" : 4, "SATURDAY" : 5, "SUNDAY" : 6}
            new_time = new_time + ', ' + tuple(days_of_week.items())[((days_of_week[start_day.upper()] + (split_total["days"] % 7)) % 7)][0].capitalize()
        else:
            new_time = new_time + ', ' + start_day.capitalize()

    if split_total["days"] > 1:
        new_time = new_time + ' (' + str(split_total["days"]) + ' days later)'
    elif split_total["days"] > 0:
        new_time = new_time + ' (next day)'

    return new_time

def add_time(start, duration, start_day = None):

    split_start = start.split()
    ampm = split_start[1]
    split_start = split_time(split_start[0])
    if ampm == 'PM':
        split_start["hours"] = split_start["hours"] + 12
    
    split_duration = split_time(duration)

    split_total = get_total(split_start,split_duration)

    new_time = get_new_time(split_total, start_day)

    return new_time