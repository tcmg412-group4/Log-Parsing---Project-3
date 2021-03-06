# Beginning of code
# Import to retrieve log file from url
import urllib.request
import shutil
import collections
import re 
# Download the file from `url` and save it locally under `logs_file.log`:
with urllib.request.urlopen('https://s3.amazonaws.com/tcmg476/http_access_log') as response, open('logs_file.log', 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
    
# Open file to append lines of text into a list
# Lines of text refer to total requests in the log
file = open("logs_file.log", "r")
# Create a list
requests_list = []
# Loop through all lines of text file and append each line to the list
for x in file:
    line = x.strip()
    line_list = line.split()
    requests_list.append(line_list)

# Close the file
file.close()

# 1. How many total requests have been made in the last year?

# Open file again to count the number of occurrences of text
# By counting the number a year is logged we can see how many requests happened last year
file = open("logs_file.log", "r")
# Read the contents of text file
data = file.read()
# Count the number of requests of each of the last six months
months = ["May","Jun", "Jul", "Aug", "Sep", "Oct"]
m_requests = []
for m in months:
    requests = data.count(f'{m}/1995')
    m_requests.append(requests)
# Sum the total of requests per month
total_requests = sum(m_requests)
# Print result
print("Number of requests made in the last six months:", total_requests)
# Close file
file.close()

# 2. How many total requests were made in the time period represented by the log?

# Since all lines, or requests, have been appended into the list, we only need to know the length or number of items on
# a list to know the total number of requests in the log file
n_requests = len(requests_list)

# Print the length or number of requests of the text file
print("Number of requests in the period:", n_requests)

# Print if the file was successfully parsed or not
print("Successfully parsed log file...")
print()

print("---------------------------------------------------------------------------------------------------")

# Create list of months
year = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct",
    "Nov", "Dec"
]
# Create list of days that goes from 01 to 31
days = []
for i in range(1, 32):
    nums = str(i).zfill(2)
    days.append(nums)
      
# Create dictionaries for every month and year
oct_94 = {}
nov_94 = {}
dec_94 = {}
jan_95 = {}
feb_95 = {}
mar_95 = {}
apr_95 = {}
may_95 = {}
jun_95 = {}
jul_95 = {}
aug_95 = {}
sept_95 = {}
oct_95 = {}

# Open file
file = open("logs_file.log", "r")
# Read the contents of text file
data = file.read()
# Add key (day) and value (number of requests on that specific day) to the dictionary based on the month
for n in days:
    request = data.count(f"{n}/{year[9]}/1994")
    oct_94[n] = request
    request = data.count(f"{n}/{year[10]}/1994")
    nov_94[n] = request
    request = data.count(f"{n}/{year[11]}/1994")
    dec_94[n] = request

    request = data.count(f"{n}/{year[0]}/1995")
    jan_95[n] = request
    request = data.count(f"{n}/{year[1]}/1995")
    feb_95[n] = request
    request = data.count(f"{n}/{year[2]}/1995")
    mar_95[n] = request
    request = data.count(f"{n}/{year[3]}/1995")
    apr_95[n] = request
    request = data.count(f"{n}/{year[4]}/1995")
    may_95[n] = request
    request = data.count(f"{n}/{year[5]}/1995")
    jun_95[n] = request
    request = data.count(f"{n}/{year[6]}/1995")
    jul_95[n] = request
    request = data.count(f"{n}/{year[7]}/1995")
    aug_95[n] = request
    request = data.count(f"{n}/{year[8]}/1995")
    sept_95[n] = request
    request = data.count(f"{n}/{year[9]}/1995")
    oct_95[n] = request
# Close file
file.close()

print("Records retrieved from October 1994 to October 1995...")
print()
# Daily requests
print("----------Daily Requests Records----------")
print()
print("Please abbreviate month names to the first three letters.")
print()
      
# Question 1.How many requests were made on each day? 
# Ask user for input on the day, month and year from which they want to retrieve daily information 
day, month, year = input("Enter day, month, and year to retrieve records (format dd/mm/yyyy): ").split("/")
# Based o the input from the user, the dictionary looks for the value of the day and month that the user asks for
if month == "Oct" and year == "1994":
    print(f"On {day}/{month}/{year} there were {oct_94.get(day)} requests.")
elif month == "Nov" and year == "1994":
    print(f"On {day}/{month}/{year} there were {nov_94.get(day)} requests.")
elif month == "Dec" and year == "1994":
    print(f"On {day}/{month}/{year} there were {dec_94.get(day)} requests.")

elif month == "Jan" and year == "1995":
    print(f"On {day}/{month}/{year} there were {jan_95.get(day)} requests.")
elif month == "Feb" and year == "1995":
    print(f"On {day}/{month}/{year} there were {feb_95.get(day)} requests.")
elif month == "Mar" and year == "1995":
    print(f"On {day}/{month}/{year} there were {mar_95.get(day)} requests.")
elif month == "Apr" and year == "1995":
    print(f"On {day}/{month}/{year} there were {apr_95.get(day)} requests.")
elif month == "May" and year == "1995":
    print(f"On {day}/{month}/{year} there were {may_95.get(day)} requests.")
elif month == "Jun" and year == "1995":
    print(f"On {day}/{month}/{year} there were {jun_95.get(day)} requests.")
elif month == "Jul" and year == "1995":
    print(f"On {day}/{month}/{year} there were {jul_95.get(day)} requests.")
elif month == "Aug" and year == "1995":
    print(f"On {day}/{month}/{year} there were {aug_95.get(day)} requests.")
elif month == "Sep" and year == "1995":
    print(f"On {day}/{month}/{year} there were {sept_95.get(day)} requests.")
elif month == "Oct" and year == "1995":
    print(f"On {day}/{month}/{year} there were {oct_95.get(day)} requests.")
else:
    print("Daily records could not be retrieved.")
print()
print("-------------------------------------------")
# Weekly requests
print()
print("----------Weekly Requests Records----------")
print()
print("Every month is divided by 4 weeks.")
print()
      
# Question 2.1 How many requests were made on a week-by-week basis? 
# Ask user to input the week, month, and year from which they want to retrieve weekly information.
w, x, z = input("Enter week number, month, and year (separate answers with a space): ").split()
# Check the input of the user and print the sum of values of the week selected.
# Seven values are added to a list and they are added up through the zoom function
if w == "1" and x == "Oct" and z == "1994":
    print(f"There were {sum(list(oct_94.values())[:7])} requests on the first week of {x}/{z}")
elif w == "2" and x == "Oct" and z == "1994":
    print(f"There were {sum(list(oct_94.values())[8:15])} requests on the second week of {x}/{z}")
elif w == "3" and x == "Oct" and z == "1994":
    print(f"There were {sum(list(oct_94.values())[16:23])} requests on the third week of {x}/{z}")
elif w == "4" and x == "Oct" and z == "1994":
    print(f"There were {sum(list(oct_94.values())[24:31])} requests on the fourth week of {x}/{z}")

elif w == "1" and x == "Nov" and z == "1994":
    print(f"There were {sum(list(nov_94.values())[:7])} requests on the first week of {x}/{z}")
elif w == "2" and x == "Nov" and z == "1994":
    print(f"There were {sum(list(nov_94.values())[8:15])} requests on the second week of {x}/{z}")
elif w == "3" and x == "Nov" and z == "1994":
    print(f"There were {sum(list(nov_94.values())[16:23])} requests on the third week of {x}/{z}")
elif w == "4" and x == "Nov" and z == "1994":
    print(f"There were {sum(list(nov_94.values())[24:31])} requests on the fourth week of {x}/{z}")

elif w == "1" and x == "Dec" and z == "1994":
    print(f"There were {sum(list(dec_94.values())[:7])} requests on the first week of {x}/{z}")
elif w == "2" and x == "Dec" and z == "1994":
    print(f"There were {sum(list(dec_94.values())[8:15])} requests on the second week of {x}/{z}")
elif w == "3" and x == "Dec" and z == "1994":
    print(f"There were {sum(list(dec_94.values())[16:23])} requests on the third week of {x}/{z}")
elif w == "4" and x == "Dec" and z == "1994":
    print(f"There were {sum(list(dec_94.values())[24:31])} requests on the fourth week of {x}/{z}")


elif w == "1" and x == "Jan" and z == "1995":
    print(f"There were {sum(list(jan_95.values())[:7])} requests on the first week of {x}/{z}")
elif w == "2" and x == "Jan" and z == "1995":
    print(f"There were {sum(list(jan_95.values())[8:15])} requests on the second week of {x}/{z}")
elif w == "3" and x == "Jan" and z == "1995":
    print(f"There were {sum(list(jan_95.values())[16:23])} requests on the third week of {x}/{z}")
elif w == "4" and x == "Jan" and z == "1995":
    print(f"There were {sum(list(jan_95.values())[24:31])} requests on the fourth week of {x}/{z}")

elif w == "1" and x == "Feb" and z == "1995":
    print(f"There were {sum(list(feb_95.values())[:7])} requests on the first week of {x}/{z}")
elif w == "2" and x == "Feb" and z == "1995":
    print(f"There were {sum(list(feb_95.values())[8:15])} requests on the second week of {x}/{z}")
elif w == "3" and x == "Feb" and z == "1995":
    print(f"There were {sum(list(feb_95.values())[16:23])} requests on the third week of {x}/{z}")
elif w == "4" and x == "Feb" and z == "1995":
    print(f"There were {sum(list(feb_95.values())[24:31])} requests on the fourth week of {x}/{z}")

elif w == "1" and x == "Mar" and z == "1995":
    print(f"There were {sum(list(mar_95.values())[:7])} requests on the first week of {x}/{z}")
elif w == "2" and x == "Mar" and z == "1995":
    print(f"There were {sum(list(mar_95.values())[8:15])} requests on the second week of {x}/{z}")
elif w == "3" and x == "Mar" and z == "1995":
    print(f"There were {sum(list(mar_95.values())[16:23])} requests on the third week of {x}/{z}")
elif w == "4" and x == "Mar" and z == "1995":
    print(f"There were {sum(list(mar_95.values())[24:31])} requests on the fourth week of {x}/{z}")

elif w == "1" and x == "Apr" and z == "1995":
    print(f"There were {sum(list(apr_95.values())[:7])} requests on the first week of {x}/{z}")
elif w == "2" and x == "Apr" and z == "1995":
    print(f"There were {sum(list(apr_95.values())[8:15])} requests on the second week of {x}/{z}")
elif w == "3" and x == "Apr" and z == "1995":
    print(f"There were {sum(list(apr_95.values())[16:23])} requests on the third week of {x}/{z}")
elif w == "4" and x == "Apr" and z == "1995":
    print(f"There were {sum(list(apr_95.values())[24:31])} requests on the fourth week of {x}/{z}")

elif w == "1" and x == "May" and z == "1995":
    print(f"There were {sum(list(may_95.values())[:7])} requests on the first week of {x}/{z}")
elif w == "2" and x == "May" and z == "1995":
    print(f"There were {sum(list(may_95.values())[8:15])} requests on the second week of {x}/{z}")
elif w == "3" and x == "May" and z == "1995":
    print(f"There were {sum(list(may_95.values())[16:23])} requests on the third week of {x}/{z}")
elif w == "4" and x == "May" and z == "1995":
    print(f"There were {sum(list(may_95.values())[24:31])} requests on the fourth week of {x}/{z}")

elif w == "1" and x == "Jun" and z == "1995":
    print(f"There were {sum(list(jun_95.values())[:7])} requests on the first week of {x}/{z}")
elif w == "2" and x == "Jun" and z == "1995":
    print(f"There were {sum(list(jun_95.values())[8:15])} requests on the second week of {x}/{z}")
elif w == "3" and x == "Jun" and z == "1995":
    print(f"There were {sum(list(jun_95.values())[16:23])} requests on the third week of {x}/{z}")
elif w == "4" and x == "Jun" and z == "1995":
    print(f"There were {sum(list(jun_95.values())[24:31])} requests on the fourth week of {x}/{z}")

elif w == "1" and x == "Jul" and z == "1995":
    print(f"There were {sum(list(jul_95.values())[:7])} requests on the first week of {x}/{z}")
elif w == "2" and x == "Jul" and z == "1995":
    print(f"There were {sum(list(jul_95.values())[8:15])} requests on the second week of {x}/{z}")
elif w == "3" and x == "Jul" and z == "1995":
    print(f"There were {sum(list(jul_95.values())[16:23])} requests on the third week of {x}/{z}")
elif w == "4" and x == "Jul" and z == "1995":
    print(f"There were {sum(list(jul_95.values())[24:31])} requests on the fourth week of {x}/{z}")

elif w == "1" and x == "Aug" and z == "1995":
    print(f"There were {sum(list(aug_95.values())[:7])} requests on the first week of {x}/{z}")
elif w == "2" and x == "Aug" and z == "1995":
    print(f"There were {sum(list(aug_95.values())[8:15])} requests on the second week of {x}/{z}")
elif w == "3" and x == "Aug" and z == "1995":
    print(f"There were {sum(list(aug_95.values())[16:23])} requests on the third week of {x}/{z}")
elif w == "4" and x == "Aug" and z == "1995":
    print(f"There were {sum(list(aug_95.values())[24:31])} requests on the fourth week of {x}/{z}")

elif w == "1" and x == "Sep" and z == "1995":
    print(f"There were {sum(list(sept_95.values())[:7])} requests on the first week of {x}/{z}")
elif w == "2" and x == "Sep" and z == "1995":
    print(f"There were {sum(list(sept_95.values())[8:15])} requests on the second week of {x}/{z}")
elif w == "3" and x == "Sep" and z == "1995":
    print(f"There were {sum(list(sept_95.values())[16:23])} requests on the third week of {x}/{z}")
elif w == "4" and x == "Sep" and z == "1995":
    print(f"There were {sum(list(sept_95.values())[24:31])} requests on the fourth week of {x}/{z}")

elif w == "1" and x == "Oct" and z == "1995":
    print(f"There were {sum(list(oct_95.values())[:7])} requests on the first week of {x}/{z}")
elif w == "2" and x == "Oct" and z == "1995":
    print(f"There were {sum(list(oct_95.values())[8:15])} requests on the second week of {x}/{z}")
elif w == "3" and x == "Oct" and z == "1995":
    print(f"There were {sum(list(oct_95.values())[16:23])} requests on the third week of {x}/{z}")
elif w == "4" and x == "Oct" and z == "1995":
    print(f"There were {sum(list(oct_95.values())[24:31])} requests on the fourth week of {x}/{z}")

else:
    print("Weekly records could not be retrieved.")

# Monthly requests
print()
print("--------------------------------------------")
print()
print("----------Monthly Requests Records----------")
print()
      
# Question 2.2 How many requests were made per month?      
# Ask the user to input the month and year from which they want to retrieve monthly requests information.
m, y = input("Please enter the month and year to obtain the number of requests (format mm/yyyy): ").split("/")
# Check for the input from the user and sum the values of the dictionary based on the month.
if m == "Oct" and y == "1994":
    print(f"The total number of requests during {m}/{y} were: {sum(oct_94.values())}")
elif m == "Oct" and y == "1994":
    print(f"The total number of requests during {m}/{y} were: {sum(nov_94.values())}")
elif m == "Oct" and y == "1994":
    print(f"The total number of requests during {m}/{y} were: {sum(dec_94.values())}")

elif m == "Jan" and y == "1995":
    print(f"The total number of requests during {m}/{y} were: {sum(jan_95.values())}")
elif m == "Feb" and y == "1995":
    print(f"The total number of requests during {m}/{y} were: {sum(feb_95.values())}")
elif m == "Mar" and y == "1995":
    print(f"The total number of requests during {m}/{y} were: {sum(mar_95.values())}")
elif m == "Apr" and y == "1995":
    print(f"The total number of requests during {m}/{y} were: {sum(apr_95.values())}")
elif m == "May" and y == "1995":
    print(f"The total number of requests during {m}/{y} were: {sum(may_95.values())}")
elif m == "Jun" and y == "1995":
    print(f"The total number of requests during {m}/{y} were: {sum(jun_95.values())}")
elif m == "Jul" and y == "1995":
    print(f"The total number of requests during {m}/{y} were: {sum(jul_95.values())}")
elif m == "Aug" and y == "1995":
    print(f"The total number of requests during {m}/{y} were: {sum(aug_95.values())}")
elif m == "Sep" and y == "1995":
    print(f"The total number of requests during {m}/{y} were: {sum(sept_95.values())}")
elif m == "Oct" and y == "1995":
    print(f"The total number of requests during {m}/{y} were: {sum(oct_95.values())}")
else:
    print("Monthly records could not be retrieved.")
print()
print("--------------------------------------------")
      
# Questions 3 and 4. What % of HTTP status codes were 4xx and what % were 3xx?
    
# Open file to run regex to split up strings
file = open("logs_file.log", "r")
# Run Regex on log file
regex = '(\d{3})'
# Create a list
match_list = []
read_line = True

with open('logs_file.log', 'r') as file:
    if read_line == True:
        for line in file:
            for match in re.finditer(regex, line, re.S):
                match_text = match.group()
                match_list.append(match_text)
              #  print(match_text)
    else:
        data = file.read()
        for match in re.finditer(regex, data, re.S):
            match_text = match.group()
            match_list.append(match.text)

count3xx = 0 #counter to keep track of total 3xx codes in list
for res in match_list: #loop through contents of list
    if(res[0] == '3'): # returns first digit of codes, checks if = 3
        count3xx = count3xx + 1 #add 1 to count for each 3xx code

print ("Percent of 3xx status codes =", str((count3xx / len(match_list)) * 100), "%")

count4xx = 0 #counter to keep track of total 4xx codes in list
for res in match_list: #loop through contents of list
    if(res[0] == '4'): # returns first digit of codes, checks if = 4
        count4xx = count4xx + 1 #add 1 to count for each 4xx code

print ("Percent of 4xx status codes =", str((count4xx / len(match_list)) * 100), "%")
# Close the file
file.close()
      
# question 5: What was the most requested file?
logfile = open("logs_file.log", "r")
clean_log = []
for line in logfile:
    try:
        # copy the URLS to an empty list.
        # We get the part between GET and HTTP
        clean_log.append(line[line.index("GET") + 4:line.index("HTTP")])
    except:
        pass
counter = collections.Counter(clean_log)
# get the most popular URL
for count in counter.most_common(1):
    print(f"The most requested file is: {str(count[0])} with {str(count[1])} requests." )

# question 6: what was the least requested file?
for count in counter.most_common()[-2:-1]:
    print(f"The least requested file is: {str(count[0])} with {str(count[1])} request.")
logfile.close()
# Opens log file to read and monthly files to write
logfile = open("logs_file.log", "r")
jan_file = open("jan.txt", "w")
feb_file = open("feb.txt", "w")
mar_file = open("mar.txt", "w")
apr_file = open("apr.txt", "w")
may_file = open("may.txt", "w")
jun_file = open("jun.txt", "w")
jul_file = open("jul.txt", "w")
aug_file = open("aug.txt", "w")
sep_file = open("sep.txt", "w")
oct_file = open("oct.txt", "w")
nov_file = open("nov.txt", "w")
dec_file = open("dec.txt", "w")
oct_1994_file = open("oct_1994.txt", "w")

# Reads data from log file and writes into corresponding file per month

with open("logs_file.log", "r") as f:
    data = f.readlines()
    for line in data:
        if re.search(r'Jan/1995', line):
            jan_file.write(line)
        elif re.search(r'Feb/1995', line):
            feb_file.write(line)
        elif re.search(r'Mar/1995', line):
            mar_file.write(line)
        elif re.search(r'Apr/1995', line):
            apr_file.write(line)
        elif re.search(r'May/1995', line):
            may_file.write(line)
        elif re.search(r'Jun/1995', line):
            jun_file.write(line)
        elif re.search(r'Jul/1995', line):
            jul_file.write(line)
        elif re.search(r'Aug/1995', line):
            aug_file.write(line)
        elif re.search(r'Sep/1995', line):
            sep_file.write(line)
        elif re.search(r'Oct/1995', line):
            oct_file.write(line)
        elif re.search(r'Nov/1994', line):
            nov_file.write(line)
        elif re.search(r'Dec/1994', line):
            dec_file.write(line)
        elif re.search(r'Oct/1994', line):
            oct_1994_file.write(line)

# Closes files
logfile.close()
jan_file.close()
feb_file.close()
mar_file.close()
apr_file.close()
may_file.close()
jun_file.close()
jul_file.close()
aug_file.close()
sep_file.close()
oct_file.close()
nov_file.close()
dec_file.close()
oct_1994_file.close()

print("Data has been registered successfully!")

