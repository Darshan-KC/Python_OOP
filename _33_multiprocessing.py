# Multiprocessing in Python
# Multiprocessing is a python module that provides a simple way to run multiple process in parallel. It allows you to take advantage of multiple cores or processors on your system and can significantly improve the performance of your code. 

# Importing Multiprocessing 
# We can use multiprocessing by importing the multiprocessing module.

#import multiprocessing

import multiprocessing
import requests

def downloadFile(url,name):
    response = requests.get(url)
    open(f"file{name}.jpg","wb").write(response.content)

url = "https://www.pexels.com/photo/white-daisy-on-grass-field-409696/"
downloadFile(url,1)