# Import the time module and set start time
import time
start_time = time.time()

# Import the urllib module
import urllib.request

# Import the csv module
import csv

# Define the input and output files
ihandle = "C:/Users/jamie.laird/OD/My Documents/2017/2017-06-22 TEF 2017/URLs.csv"

# Open the target csv file
with open (ihandle) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        # Read from the specified fields
        url = row["URL"]
        filename = row["Filename"]

        # Set the output file and url
        outfilename = "C:/Users/jamie.laird/OD/My Documents/2017/2017-06-22 TEF 2017/Excel/"+filename
        url_of_file = url

        # Retrieve from url and save to disk
        urllib.request.urlretrieve(url_of_file, outfilename)

# Print runtime info
print('Completed in %s seconds' % (time.time() - start_time))
