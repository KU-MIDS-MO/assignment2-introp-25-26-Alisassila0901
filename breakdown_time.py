def breakdown_time(seconds):
    
    if type(seconds) != int or seconds < 0:
        return -1
    if seconds == 0:
        return {}

    hours =0
    minutes = 0

    while seconds >= 3600:
        hours += 1
        seconds -= 3600
    
    while seconds >= 60:
        minutes += 1
        seconds -= 60


    if minutes == 0:
        return {3600: hours}
    

    return {3600: hours, 60: minutes, 1: seconds}


