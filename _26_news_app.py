# Exercise 10

# Use the NewsAPI and the requests module to fetch the daily news related to different topics. 
# Go to https://newsapi.org/ and explore the various options to build you application

import requests

def user_input(url,category):
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
        
    match ch:
        case 1:
            return url + "?category=business"
        case 2:
            return url + "?category=entertainment"
        case 3:
            return url + "?category=general"
        case 4:
            return url + "?category=health"
        case 5:
            return url + "?category=science"
        case 6:
            return url + "?category=sport"
        case 7:
            return url + "?category=technology"
        case 8:
            print("Choice must be between 1 - 8")
            exit()

if __name__ == "__main__":
    
    API_KEY = ""
    
    url = "https://newsapi.org/v2/top-headlines"

    category = ['business','entertainment','general','health','science','sport','technology']
    
    f_url = user_input(url,category)
    
    f_url = f_url + f"&apiKey={API_KEY}"
    
    response = requests.get(f_url)
    print(response.text)
    