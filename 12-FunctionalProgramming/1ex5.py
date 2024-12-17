def avg_speed(distance,hours,minutes):
    time = hours + minutes/60
    return distance/time

print(avg_speed(100,2,50))