import os
from random import randint

# Set your desired start and end dates (in terms of days ago) and the maximum number of commits per day
startdate = 2300
enddate = 2400
max_commits_per_day = 11

for day in range(startdate, enddate):
    # Generate a random number of commits for the current day, up to the specified maximum
    for commits in range(0, randint(1, max_commits_per_day)):
        current_day = str(day) + ' days ago'
        with open('file.txt', 'a') as file:
            file.write(current_day + '\n')  # Add a newline character for better readability
        os.system('git add .')
        os.system('git commit --date="' + current_day + '" -m "commit"')

os.system('git push -u origin main ')
