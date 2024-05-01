# Create a program to greet with respect to time
import time
class Greet:
    def __init__(self,name) -> None:
        self.name = name
        
    def goodMorning(self) ->None:
        print("Good Morning! ",self.name)
        
    def goodAfternoon(self) -> None:
        print("Good Afternoon! ",self.name)
        
    def goodEvening(self) -> None:
        print("Good Evening ! ",self.name)
        
    def goodNight(self) -> None:
        print("Good Night !",self.name)
 
greet = Greet("Hari Bahadur")       
t = int(time.strftime("%H"))
# tm = t - 12 if t > 12 else t

if t > 0 and t < 12:
    greet.goodMorning()
elif t > 12 and t < 17:
    greet.goodAfternoon()
elif t > 17 and t < 19:
    greet.goodEvening()
else:
    greet.goodNight()