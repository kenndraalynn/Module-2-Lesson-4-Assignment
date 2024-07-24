

time = ['Morning', 'Afternoon', 'Evening']
day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
mood = ['happy', 'tired', 'sad', 'sleepy']

import random


for days in day:
    for times in time:
        for moods in mood:
            mood_final = random.choice(mood)
        print("On ", days, times, " you were ", mood_final)