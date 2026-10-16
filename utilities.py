import os

def clear_screen(): #works
    os('cls' if os.name == 'nt' else 'clear')

def getvalidint(prompt, min, max): #works most likely
    '''gets valid input between a min and max (prompt, min, max)'''
    answer = input(prompt)
    while answer.isdigit == False or int(answer) > max or int(answer) < min:
        print("Error")
        answer = input(prompt)
    return int(answer)

def getnonemptyinput(prompt): #works
    prompt = prompt.strip()
    while True:
        resp = input(prompt).strip()
        if (resp == ""):
            print("Try again")
        else:
            return resp

        
def pause(message = "Press Anything to continue:"): # need to make only enter
    
    answer = input(message)


def printnumberedlist(list): #work
    for i in range(len(list)):
        print (i)
    if list == []:
        print("No items to display")

def redo_input(prompt):
    reponse = input(prompt)
    return reponse
def analyze_numbers(numbers_list): #works for most part
    '''Use a list comprehension to collect positive numbers. Return four values: positive-number list, positive count, negative count, zero count. '''
    total = 0
    pos_nums = [num for num in numbers_list if num > 0]
    pos_totl = [num for num in numbers_list if num > 0] #need to find way to add positive total
    zeros = [num for num in numbers_list if num == 0] 
    neg_nums = [num for num in numbers_list if num < 0] 
    return pos_nums, pos_totl, zeros ,neg_nums
#           works   dont work  works   works



num = [1,2,3,4,5,6,7,8,9,-1,0,-5]
no = []
def main(): #mainloop
    print("name: " + __name__) #__name__ is a variable you cant change in python, the file that runs is __main__
    while True:
        all_nums = analyze_numbers(num)
        print(all_nums)
        printnumberedlist(no)
if __name__ == "__main__": #runs the mainloop only if this is the file that will run
    main()