# Multiprocessing in Python
# Multiprocessing is a python module that provides a simple way to run multiple process in parallel. It allows you to take advantage of multiple cores or processors on your system and can significantly improve the performance of your code. 

# Importing Multiprocessing 
# We can use multiprocessing by importing the multiprocessing module.

#import multiprocessing

import multiprocessing
import requests

def downloadFile(url,name):
    response = requests.get(url)
    lst = str(url).split(".")
    try:
        extension = lst[-1]
    except:
        print("Not a vaild url")
        exit()
    open(f"file{name}.{extension}","wb").write(response.content)

url = "https://cdn.hashnode.com/res/hashnode/image/upload/v1675269151012/77660837-f802-40e4-90e7-381e344ada3c.png"
downloadFile(url,"gitVsGithub")