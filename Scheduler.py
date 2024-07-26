from random import randrange
from datetime import datetime, date, time, timedelta


# Unsure whether will be using sheets or not, so placeholder for now
def sheetParse(file):
    parsed_file = file
    return parsed_file

def checkClash(item, days, times):
    
    return 


items = [
    {
        "item": "scene 1",
        "people": ['Isabel', 'Melissa'],
        "time": 2,
        "scheduled": False
    },
        {
        "item": "scene 2",
        "people": ['Matt', 'Isabel', 'Emily'],
        "time": 6,
        "scheduled": False
    },
        {
        "item": "scene 3",
        "people": ['Alex', 'Isabel', 'Matt'],
        "time": 4,
        "scheduled": False
    },
        {
        "item": "scene 4",
        "people": ['Emily', 'Alex'],
        "time": 2,
        "scheduled": False
    }
]


#5 and 6 are Weekend, 0 to 4 are Monday to Friday
specific_date = date(2024, 9, 14)
period_length = 4
day_of_week = specific_date.weekday()
days = []
for i in range(period_length):
    days.append((day_of_week + i)%7)


people = ['Isabel', 'Matt', 'Melissa', 'Emily', 'Alex']
times = []
for i in people:
    person_times = []
    for j in days:
        temp_day = [randrange(9, 20)]
        person_times.append(temp_day)
    cast_member = {
        "name": i,
        "availability": person_times
    }
    times.append(cast_member)

for i in times:
    print(i)



# Will treat everyday the same for now, will need to adjust for weekdays vs weekends in future
# schedule = [[None for _ in range(9)] for _ in days]
schedule = []
for i in (days):
    if i > 4:
        schedule.append([None]*12)
    else:
        schedule.append([None]*3)
print(schedule)
for i in items:
    scheduled = False
    for j in range(len(days)):
        if i["scheduled"] == True:
            break
        print(schedule[j].count(None))
        if schedule[j].count(None) >= i["time"]:
            for k in range(len(schedule[j])):
                if schedule[j][k] == None:
                    for l in range(i["time"]):
                        schedule[j][k+l] = i["item"]
                    i["scheduled"] = True
                    break

print(schedule)