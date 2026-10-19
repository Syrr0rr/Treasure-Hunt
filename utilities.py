import os
import msvcrt

def clear_keyboard_buffer(): 
    """Remove any pending keystrokes from the keyboard buffer.""" 
    while msvcrt.kbhit(): 
        msvcrt.getwch() 
msvcrt.kbhit()# checks for waiting keystrokes; msvcrt.getwch() removes one. Call the function after clearing the screen and immediately before accepting the player’s guess: 

def getvalidint(prompt, min, max): #works most likely
    ''' (prompt, min, max) Gets valid input between a min and max'''
    answer = input(prompt)
    while answer.isdigit() == False or int(answer) > max or int(answer) < min:
        print("Error")
        answer = input(prompt)
    return int(answer)

def getnonemptyinput(prompt):
    '''(prompt) Reject empty or whitespace only input'''
    while True:
        resp = input(prompt).strip()
        if (resp == ""):
            print("Try again")
        else:
            return resp

def pause(message = "Press Anything to continue:"): 
    '''(message) Waits for user input '''
    answer = input(message)

def printnumberedlist(list):   
    '''(list) Prints a list character by character or by each list if the input list is 2d '''
    for i in list:
        print (i)
    if list == []:
        print("No items to display")

def getvalidresponse(prompt, valid_response): #valid response will be exact string 
    '''(prompt, valid response) Repeat until an accepted response is entered use a list comprehension to lowercase valid responses. Return lowercase input. valid response cant be a number, strings work for example'''
    attempts = []
    reponse = input(prompt)
    attempts.append(reponse)
    while reponse != valid_response:
        reponse = input(prompt)
        attempts.append(reponse)
    print(attempts)


def analyze_numbers(numbers_list): 
    '''(numbers_list) Use a list comprehension to collect positive numbers. Return four values: positive-number list, positive count, negative count, zero count. '''
    total = 0
    pos_nums = [num for num in numbers_list if num > 0]
    zeros = [num for num in numbers_list if num == 0] 
    neg_nums = [num for num in numbers_list if num < 0] 
    pos_total = 0
    for num in numbers_list:
        if num > 0:
            pos_total += num
    return pos_nums, pos_total, zeros ,neg_nums

if __name__ == "__main__": #tests start inside if statement
    print("Hello")