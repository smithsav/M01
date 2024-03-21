# 3.1 How many seconds are in an hour? 
# Use the interactive interpreter as a calculator and multiply the number of seconds in a minute (60) by the number of
# minutes in an hour (also 60).

60 *60

# 3.2 Assign the result from the previous task (seconds in an hour) to a variable called seconds_per_hour.

seconds_per_hour = 3600

# 3.3 How many seconds are in a day? Use your seconds_per_hour variable.

seconds_per_hour * 24

# 3.4 Calculate seconds per day again, but this time save the result in a variable called seconds_per_day.

seconds_per_day = seconds_per_hour * 24 #seconds per hour times hours in a day.
print(seconds_per_day)

# 3.5 Divide seconds_per_day by seconds_per_hour. Use floating-point (/) division.

seconds_per_day / seconds_per_hour

# 3.6 Divide seconds_per_day by seconds_per_hour, using integer (//) division.
# Did this number agree with the floating-point value from the previous question, aside from the final .0?

seconds_per_day // seconds_per_hour
# yes same value, aside from the final .0.