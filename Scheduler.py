from random import randrange

# Unsure whether will be using sheets or not, so placeholder for now
def sheetParse(file):
    parsed_file = file
    return parsed_file


items = [
    {
        "item": "scene 1",
        "people": ['Isabel', 'Melissa'],
        "time": 2
    },
        {
        "item": "scene 2",
        "people": ['Matt', 'Isabel', 'Emily'],
        "time": 3
    },
        {
        "item": "scene 3",
        "people": ['Alex', 'Isabel', 'Matt'],
        "time": 4
    },
        {
        "item": "scene 4",
        "people": ['Emily', 'Alex'],
        "time": 2
    }
]

days = [1, 2, 3]
people = ['Isabel', 'Matt', 'Melissa', 'Emily', 'Alex']
times = []
for i in people:
    person_times = []
    for j in days:
        temp_day = [randrange(12), randrange(13, 24)]
        person_times.append(temp_day)
    my_dict = {
        "name": i,
        "availability": person_times
    }
    times.append(my_dict)

for i in times:
    print(i)

schedule = [[]*9]*len(days)
print(schedule)
for i in days:
    None








