# Create a program capable of displaying questions to the user like KBC. Use list data type to store the questions and their correct answer. Display the final amount the person is taking home after playing the game.
import _9_1_stage_1_qn as sample1
import _9_2_stage_2_qn as sample2
import _9_3_stage_3_qn as sample3
from random import randint

class KBC:
    def __init__(self,name = "",i=0,totalPrice = 0.0) -> None:
        self.name = name
        self.i = i
        self.totalPrice = totalPrice
        
    def welcome(self) -> None:
        print("""
          *********************************** Welcome to KO BANCHA CORORES PATI **************************************
          ############################################################################################################

          # There are three stages 
          Instructions
          ##  STAGE 1
            1     ₹1000
            2     ₹2000
            3     ₹3000
            4     ₹5000
            5     ₹10,000
          
          ##  STAGE 2
            6     ₹20,000
            7     ₹40,000
            8     ₹80,000
            9     ₹1,60,000
            10    ₹3,20,000
            
          ## Stage 3
            11    ₹6,40,000
            12    ₹12,50,000
            13    ₹25,00,000
            14    ₹50,00,000
            15    ₹1,00,00,000
            16    ₹7,00,00,000
          """)
        
        
    def Question(self,sample) -> int:
        
        indexs = list()
        if sample == sample1:
            n = len(sample1.stage1)
            sample_name = sample1.stage1
        elif sample == sample2:
            n = len(sample2.stage2)
            sample_name = sample2.stage2
        else:
            n = len(sample3.stage3)
            sample_name = sample3.stage3
        for i in range(5):
            while(True):
                rand = randint(1,n)
                x = sample_name.get(str(rand))
                if x not in indexs:
                    indexs.append(x)
                    break
            tem = indexs[i]
            print("The question is => ",end="")
            print(tem.get('question'))
            print("Options are: ")
            for y in tem.get('options'):
                print(f"{(tem.get('options').index(y) + 1)}. {y}")
            # user input
            while(True):
                try:
                    op = int(input("Enter the answer: "))
                    op -=1
                    temx = tem.get('options')
                    if op < 0 or op > 3:
                        print("!!! Option cannot be less than 1 or greater than 4. !!!")
                        continue
                    if op == tem.get('answer'):
                        self.i +=1
                        print("\n!!! You enter correct answer !!!")
                        print(f"Correct answer is {temx[tem.get('answer')]}\n")
                        # logic to increase price
                        if self.i == 16:
                            self.totalPrice *=7
                        elif self.i == 3:
                            self.totalPrice +=2000
                        elif self.i <3:
                            self.totalPrice +=1000
                        else:
                            self.totalPrice *=2
                            
                        print(f"######\t Your total price is RS {self.totalPrice}\n")
                        break
                    else:
                        print("\n!!!Oops! Your answer is incorrect !!!\n")
                        print(f"Correct answer is {temx[tem.get('answer')]}\n")
                        print(f"######\t{(self.name).capitalize()} your total price is RS {self.totalPrice}\n")
                        
                        return -1
                except:
                    print("!!! Invalid input type !!!")
        return 1
                    

if __name__ == "__main__":
    kbc = KBC()
    kbc.welcome()
    print("\n\n")
    name = input("Enter your name: ")
    kbc.name = name
    print("\nLets begin stage 1 questions\n")
    if kbc.Question(sample1) == -1:
        print("\nThanks for playing. \nBetter luck for next time to become crores pati.")
        exit()
    print("\nStage 1 complete\n")
    print("Lets begin stage 2 questions\n")
    if kbc.Question(sample2) == -1:
        print("\nThanks for playing. \nYou try hard. Work a bit hard for next time.")
        exit()
    print("\nStage 2 complete\n")
    print("Lets begin stage 3 questions\n")
    if kbc.Question(sample3) == -1:
        print("\nThanks for playing. \n You almost become crores pati.")

    print(f"Congratulation! {(kbc.name).capitalize()} you have won this game.\nAnd also congratulation for becoming crores pati.")
    
    