# Beginning of code
# Import to retrieve log file from url
from urllib.request import urlretrieve
# url
url_path = 'https://s3.amazonaws.com/tcmg476/http_access_log'
# Name of the file
log_file = 'logs_file.log'

# Copy and save file
local_file, headers = urlretrieve(url_path, log_file)


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

# 2. How many total requests were made in the time period represented by the log?

# Since all lines, or requests, have been appended into the list, we only need to know the length or number of items on
# a list to know the total number of requests in the log file
n_requests = len(requests_list)

# Print the length or number of requests of the text file
print("Number of requests in the period:", n_requests)

print("Successfully parsed log file...")
print()
