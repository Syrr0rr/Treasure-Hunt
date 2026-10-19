import os
import msvcrt

def clear_keyboard_buffer(): 
    """Remove any pending keystrokes from the keyboard buffer.""" 
    while msvcrt.kbhit(): 
        msvcrt.getwch() 
msvcrt.kbhit()# checks for waiting keystrokes; msvcrt.getwch() removes one. Call the function after clearing the screen and immediately before accepting the player’s guess: 

def getvalidint(prompt, min, max): #works most likely
    '''Gets valid input between a min and max (prompt, min, max)'''
    answer = input(prompt)
    while answer.isdigit() == False or int(answer) > max or int(answer) < min:
        print("Error")
        answer = input(prompt)
    return int(answer)

def getnonemptyinput(prompt): #works
    '''Reject empty or whitespace only input(prompt)'''
    while True:
        resp = input(prompt).strip()
        if (resp == ""):
            print("Try again")
        else:
            return resp

def pause(message = "Press Anything to continue:"): 
    '''Waits for user input (message)'''
    answer = input(message)

def printnumberedlist(list):              #ju #NOTE idk if this is a function in the treasure hunt program
    '''prints a list character by character or by each list if the input list is 2d (list)'''
    for i in list:
        print (i)
    if list == []:
        print("No items to display")

def getvalidresponse(prompt, valid_response): #valid response will be exact string and lower case 
    '''Repeat until an accepted response is entered use a list comprehension to lowercase valid responses. Return lowercase input. (prompt, valid response) valid response cant be a number, strings work for example'''
    attempts = []
    reponse = input(prompt)
    attempts.append(reponse)
    while reponse != valid_response:
        reponse = input(prompt)
        attempts.append(reponse)
    print(attempts)


def analyze_numbers(numbers_list): #works for most part
    '''Use a list comprehension to collect positive numbers. Return four values: positive-number list, positive count, negative count, zero count. '''
    total = 0
    pos_nums = [num for num in numbers_list if num > 0]
    zeros = [num for num in numbers_list if num == 0] 
    neg_nums = [num for num in numbers_list if num < 0] 
    pos_total = 0
    for num in numbers_list:
        if num > 0:
            pos_total += num
    return pos_nums, pos_total, zeros ,neg_nums

def filter_by_length(items, min, max): #extrenely annnoying to code, 
    """Return strings whose length is between min_len and max_len of a list, preserving order.""" 
    sum_list = []
    place_inrange = -1
    for item in items:
        place_inrange += 1
        if place_inrange >= min and place_inrange <= max:
            sum_list.append(item)
        elif place_inrange > max:
            result_str = ", ".join(sum_list)
            return result_str 


if __name__ == "__main__":
    print("Hello")

    num = [1,2,3,4,5,6,7,8,9,-1,0,-5]
    words = ["hi", "hello", "hey", "greetings", "yo"]
    no = []