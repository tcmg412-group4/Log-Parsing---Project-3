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

print("Successfully parsed log file...")
print()
