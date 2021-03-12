import random


def banner():
    print("="*40)
    print("   Welcome to number guessing game")
    print("="*40)



def exit_message():
    print("="*40)
    print("            Ending the game              ")
    print("="*40)




def generate_random_number():
    return random.randint(1,10)


def message(rand,attempt):
    print("You picked the correct number {}".format(rand))
    print("Number of attempt : {}".format(attempt))

def start_game():
    banner()
    rand = generate_random_number()
    attempt = 0
    guess = 0
    user_input = None
    while True:
        print(rand)
        try:
            guess = int(input("Guess the number : "))
        except ValueError:
            print("Please enter a number!!!")
        else:
            if guess > 0 and guess < 11:

                if guess > rand:
                    attempt += 1
                    print("It's high")
                elif guess < rand:
                    attempt += 1
                    print("It's low")

            else:
                attempt += 1
                print("Ops,out of the range")
      
        if rand == guess:
            attempt += 1
            message(rand,attempt)
            user_input = input("Would you like to continue (y/n) : ")
            if user_input.lower() == "y":
                attempt = 0
                banner()
                rand = generate_random_number()
                continue
            else:
                exit_message()
                break
        

               
                

        
            
            
    

start_game()
