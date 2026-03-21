from colorama import init, Fore, Style

init()

def askUserAge() -> int:
    
    print("Before you can apply for a Driver's License...\n" + "We need to verify your age...\n")
    # Self-fulfilling conditional
    # Infinite loop
    while True:     
        # input() by default --> 'str'
        getAge: str = input("What is your age?:\n")
        
        try: 
            # convert any integer values in string to type 'INT'
            conv_str_int = int(getAge)
            return conv_str_int
            
        # Checking for ValueError (Fail-safe for the 'TRY')
        except ValueError: 
            print(f"Input is invalid! Give a valid age!\n")
            

def checkUserAge() -> bool:
        
        age = askUserAge()

        while age >= 18:

            # Ask User if they want a valid driver's license
            print(Fore.GREEN )
            askDL: str = input("You are eligible for a driver's license, Do you want to apply for a driver's license?\n Y (Yes)/N (No)?\n")
            print(Style.RESET_ALL)
            
            

            #COLORAMA EXTENSION USED HERE
            if askDL == 'Y' or  askDL == 'y' or askDL == 'Yes' or askDL == "yes" or askDL == "yEs" or askDL == "yeS" or askDL == "yES" or askDL == "YES":
                validAge = True
                print(Style.BRIGHT + f"Okay, your application has been sent in for review !\n" + Style.RESET_ALL)
                break

            elif askDL == 'N' or askDL == 'n' or askDL == "No" or askDL == "no" or askDL == "nO" or askDL == "NO":
                
                print("Okay, have a nice day!\n")
                break;
                
        # emulate do-while loop
        while age < 18:
            invalidAge = False
            if (age < 18 and invalidAge == False ):
                print(Fore.RED + f"You need to be 18 years or older to apply!\n" + Style.RESET_ALL)
                break;

            else :
                print(f"invalidAge_value == {invalidAge}")
                return invalidAge


def main():
    checkUserAge()

if __name__ == "__main__":
    main()
