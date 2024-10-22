def time_string(hours, minutes, time_format):
    result = ''
    if time_format != '12' and time_format != '24' :
        return("Your time format is wrong")
    
    if time_format == "12":
        if hours == '0':
            result = "12" + ':' + minutes
        else:
            result = hours + ":" + minutes
        if int(hours) <= 12:
            result = result + "am"
        else:
            result = result + "pm"
    elif time_format == "24":
        if int(hours) < 10:
            result = '0' + hours + ':' + minutes
        else:
            result = hours + ':' + minutes
    
    return result



time = time_string('11','15','12')
print(time)
    

