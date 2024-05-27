# Exercise 10

# Use the NewsAPI and the requests module to fetch the daily news related to different topics. 
# Go to https://newsapi.org/ and explore the various options to build you application

import requests

url = "https://newsapi.org/v2/top-headlines"

category = ['business','entertainment','general','health','science','sport','technology']

def user_input(category):
    print("Enter your choice of news : ")
    i = 1
    for x in category:
        print(f"{i}. {x}")
        i = i + 1
    try:
        ch = int(input("Enter your choice: "))
    except:
        print("Choice must be of type integer")
        exit()
        
    

if __name__ == "__main__":
    pass