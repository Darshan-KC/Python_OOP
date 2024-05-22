# Command line utilities are programs that can be run from the terminal or command line interface, and they are an essential part of many development workflows.
# In python, you can create your own command line utilities using the built-in argprase module.

import argparse
import requests

def download_file(url,local_filename):
    if local_filename is None:
        local_filename = url.split('/'[-1])
    
    # Note the stream=True parameter below
    with requests.get(url,stream=True) as r:
        r.raise_for_status()
        
        with open(local_filename, 'wb') as f:
            # for chunk in r.ilter_content(chunk_size=8192):
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
        return local_filename

parser = argparse.ArgumentParser()

# Add command line arguments 
parser.add_argument("url", help = "Url of the file to download")
parser.add_argument("-o", "--output", help="Name of the file to save", default=None)

# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code 
print(args.url)
print(args.output)

download_file(args.url,args.output)