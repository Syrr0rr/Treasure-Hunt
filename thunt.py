import utilities as u 
import random
import os
locations = ["Dark Cave (1)", "Sandy Beach (2)", "Ancient Ruins(3)"]

def clear_screen(): 
    '''Clears screen'''
    os.system('cls' if os.name == 'nt' else 'clear')

def generate():
    '''generates where the trap,treasure, and nothing spawn'''
    global v_trea, v_trap
    treasure, trap, empty = random.sample(locations, 3)
    v_trea = treasure
    v_trap = trap
    return treasure, trap, empty
    
def set_dif(): #uses global variable, need to fix 
    '''sets the difficulty of the game'''
    global f_trap,f_treasure
    dif = u.getvalidint("1 = Easy | 3 = Hard: ", 1, 3)
    set_dif = dif - 1
    if set_dif == 0:     #easy
        f_treasure = 10
        f_trap = -5      
    elif set_dif == 1:   #med
        f_treasure = 20
        f_trap = -10
    elif set_dif == 2:   #hard
        f_treasure = 30
        f_trap = -20
    else:
        print("Error Restart program")

def go(attemps): #works
    '''updates total as a global varaible and changes by if you found treasure and is different bassed on difficulty'''
    u.clear_keyboard_buffer()
    go_to = u.getvalidint("Enter your choice (1-3): ", 1, 3)
    choice = locations[go_to - 1]
    score = 0
    if choice == v_trea:
        print(f"You found the treasure! (+{f_treasure})")
        score += f_treasure
        attemps.append(f_treasure)
    elif choice == v_trap:
        print(f"It's a trap! ({f_trap})")
        score += f_trap
        attemps.append(f_trap)
    else:
        print("Nothing here.")
        attemps.append(0)
    return score

def score(val):
    '''score the user based on total'''
    if val < 0:
        print("Lost Explorer")
    elif 0 <= val <= 19:
        print("Beginner Explorer")
    elif 20 <= val <= 49:
        print("Treasure Hunter")
    elif val > 50:
        print("Master Treasure Hunter")

def main(): #mainloop

    while True:
        attemps = []
        total = 0  
        set_dif() #gv
        for i in range(5): #has the main components, is not done 
            treasure, trap, empty = generate() 
            clear_screen()
            print(f"Round {i+1} of 5")
            print("")
            u.printnumberedlist(locations)
            print("")
            total += go(attemps)
            print(f"current total: {total} ")
            u.pause("Press enter to coninue")
        #The game results starts now
        clear_screen()
        nums, pos_num, neg_num, zeros = u.analyze_numbers(attemps)
        treasure_rounds = len(nums)
        amt_zeros = len(zeros)
        trap_rounds = len(neg_num)
        print(f"Treasure found: {treasure_rounds} | Nothing found {amt_zeros} | Trap found {trap_rounds}")
        score(total)
        restart = input("Q to quit  |  Other to Restart: ").lower().strip()
        if restart == "q":
            break

#Maybe print the attempts

if __name__ == "__main__":
    main()