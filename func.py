def print_sec_per_day():
    hours = 24
    minu  = hours * 60
    sec = minu * 60
    print (sec)

print_sec_per_day()

def print_se_per_day(days):
    hours = days * 24
    minu = hours * 60
    sec = minu * 60
    print(sec)

print_se_per_day(100)

def comvert_days_to_sec(days):
    hours = days * 24
    minu = hours * 60
    sec = minu * 60
    return sec

total_sec = comvert_days_to_sec(70000)
millisec = total_sec * 1000
print(millisec)


