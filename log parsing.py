# Beginning of code
# Import to retrieve log file from url
from urllib.request import urlretrieve
# url
url_path = 'https://s3.amazonaws.com/tcmg476/http_access_log'
# Name of the file file
log_file = 'logs_file.log'

# Copy and save file
local_file, headers = urlretrieve(url_path, log_file)
