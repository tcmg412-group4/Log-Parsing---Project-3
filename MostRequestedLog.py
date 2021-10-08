# Beginning of code
# Import to retrieve log file from url
import urllib.request
import shutil
import collections
# Download the file from `url` and save it locally under `logs_file.log`:
with urllib.request.urlopen(
        'https://s3.amazonaws.com/tcmg476/http_access_log') as response, open(
            'logs_file.log', 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

logfile = open("logs_file.log", "r")

clean_log = []

for line in logfile:
    try:
        # copy the URLS to an empty list.
        # We get the part between GET and HTTP
        clean_log.append(line[line.index("GET")+4:line.index("HTTP")])
    except:
        pass

counter = collections.Counter(clean_log)

# get the most popular URL
for count in counter.most_common(1):
    print(str(count[1]) + "    " + str(count[0]))

logfile.close()
