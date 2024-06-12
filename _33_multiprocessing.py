# Multiprocessing in Python
# Multiprocessing is a python module that provides a simple way to run multiple process in parallel. It allows you to take advantage of multiple cores or processors on your system and can significantly improve the performance of your code. 

# Importing Multiprocessing 
# We can use multiprocessing by importing the multiprocessing module.

#import multiprocessing

import multiprocessing
import requests
import concurrent.futures

def downloadFile(url,name):
    print(f"Start Downloading file image{name}")
    response = requests.get(url)
    lst = str(url).split(".")
    try:
        extension = lst[-1]
    except:
        print("Not a vaild url")
        exit()
    open(f"files/file{name}.{extension}","wb").write(response.content)
    print(f"Complete downloading file image{name}")
    
if __name__ == "__main__":
    urls = ['https://images.pexels.com/photos/85683/sheep-flock-of-sheep-series-standing-on-85683.jpeg','https://cdn.hashnode.com/res/hashnode/image/upload/v1675269151012/77660837-f802-40e4-90e7-381e344ada3c.png','https://images.pexels.com/photos/59321/pexels-photo-59321.jpeg','https://images.pexels.com/photos/259280/pexels-photo-259280.jpeg']

    # temp = []
    # for i,x in enumerate(urls):
    #     # downloadFile(x,f"-{i+1}")
    #     p = multiprocessing.Process(target=downloadFile,args=[x,f"-{i+1}"])
    #     p.start()
    #     temp.append(p)

    # for a in temp:
    #     a.join()
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        l = [i+1 for i in range(4)]
        
        results = executor.map(downloadFile,urls,l)
        
    for r in results:
        print(r)
            
