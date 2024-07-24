import random 




moods = ['Happy', 'Sad', 'Angry', 'Suspicious', 'Inquisitive']

days = ['Monday', 'Tuesday','Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']


for day in days:
    day_final = random.choice(days)
    for mood in moods:
        mood_final = random.choice(moods)
        print("On ", day_final, " you were feeling ", mood_final)