from typing import Sized
import urllib.request
import shutil
...
# Download the file from `url` and save it locally under `http_access_log`:
with urllib.request.urlopen('https://s3.amazonaws.com/tcmg476/http_access_log') as response, open('http_access_log', 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

file = open("http_access_log", "r")
# Create a list
requests_list = []
# Loop through all lines of text file and append each line to the list
for x in file:
    line = x.strip()
    line_list = line.split()
    requests_list.append(line_list)
file.close()

file = open("http_access_log", "r")
data = file.read()
# Count the number pf occurrences of each of the last six months
may = data.count(f"May/1995")
june = data.count(f"Jun/1995")
july = data.count(f"Jul/1995")
aug = data.count(f"Aug/1995")
sept = data.count(f"Sep/1995")
oct = data.count(f"Oct/1995")

logs_months = may+june+july+aug+sept+oct
# Print result
print(f"Number of requests made in the last six months: ", logs_months)

file.close()
 
    
    
        

# Close the file
file.close()


totalResquests = len(requests_list)

print("Successfully parsed log file...")
print("Number of requests in the period: ", totalResquests)


