# Beginning of code
# Import to retrieve log file from url
import urllib.request
import shutil
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
                print(match_text)
    else:
        data = file.read()
        for match in re.finditer(regex, data, re.S):
            match_text = match.group()
            match_list.append(match.text)

# print(match_list)
for match_list
# Close the file
file.close()
