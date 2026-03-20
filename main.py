from colorama import Fore, init
""" DOC-STRING:
    
# Function Example from AKITO -- TYPE-CASTING
def terminal_Input() -> bool: 
    
    sum = 1 + 1
    
    return sum

...
IN ANOTHER FN:...
return str(terminal_Input()) -> # '2'


def start():
    user_input: str = input("Kindly enter your age.\n")
    age: int = convert_to_int(user_input)
    print(f"age:{age},type:{type(age)}")
    
def convert_to_int(user_input: str)-> int: 
    try:   
        return int(user_input)
    except ValueError:
        print("Please enter a valid integer")
        start()
        
start()


input: 19 √
input: 'abc' X
Output = print(f"age:{None},type:{type(NoneType)}")

"""



def askUserAge() -> int:
    
    # Self-fulfilling conditional
    # Infinite loop
    while True:     
        # input() by default --> 'str'
        getAge: str = input("What is your age?:")
        
        #  ERROR HANDLING ~ ~ ~ ~ ~ ~
        # HOPEFULLY SUCCESSFULLY PASS TO checkUserAge()

        # ..... 

        try: 
            # convert any integer values in string to type 'INT'
            # DEBUG
            conv_str_int = int(getAge)
            print(f"try line: <--> actual value:{conv_str_int}, {type(conv_str_int)}\n")
            # ...passing to checkUserAge()...
              #if successful [no ERRORS]
            return conv_str_int
            
        # Checking for  ValueError (Fail-safe for the 'TRY')
        except ValueError: 
            
            # DEBUG
            print(f"ValueError// age: {getAge} \n age_data_type: {type(getAge)}\n")
            print("Input is invalid! Give a valid age!\n")
            
            # if Type_of_Val != 'int'
                # int(convert_type)
            
            
            
            #  while (invaldInput == True)
                # reprompt USer
                # break
            
            
        # DEBUG
        # print(f"getAge data type: {type(getAge)}\n")
        
        # checking for LAST LOGICAL SWITCH
        # invalid_Input = False
        
        # First successful User-Case: Match INT
        # if type(getAge) == int:
            # DEBUG
            # getAgeDataType = type(getAge)
            # print(f"getAge == int(getAge) conditional: \n{getAgeDataType}\n")
            # return getAge
            
        # TO-DO
        # else: 
            #     print("else condition --> askUserAge()")
            # Using MISTAKES for GOOD 
            # Detect all inputs != 'int'
            
            
    
def checkUserAge() -> bool:
        
        # Returning None Value
        age = askUserAge()
        
        
        # NoneType == DataType (int, char, char*, float, bool ....)
        # None == Value (1,2, or "string" or, 3.4) 
        
        
        # Comparing the VALUE
        #DEBUG
        if age == None:
            print(f"Here is the ValueError type:{age}\n")
            
        print(f"age_var type: {type(age)}")
        
        while type(age) != int: 
            print(f"Line130: if conditional: \n age != int\n")
            # convInt = int(age)
            break
        
            
        print(f"line 135: age value: {age}, age type: {type(age)}\n line 135;\n")
        validAge = True
        invalidAge = False

        while age >= 18:

            # Ask User if they want a valid driver's license
            askDL = input("Do you want to apply for a driver's license?\n Y/N?\n")

            #COLORAMA EXTENSION USED HERE
            if askDL == 'Y' or  askDL == 'y' or askDL == 'Yes' or askDL == "yes" or askDL == "yEs" or askDL == "yeS" or askDL == "yES" or askDL == "YES":
                validAge = True
                print("Yes Condition!\n")
                break

            elif askDL == 'N' or askDL == 'n' or askDL == "No" or askDL == "no" or askDL == "nO" or askDL == "NO":
                print("Okay, have a nice day!\n")
                break;
                
        # emulate do-while loop
        while age < 18:
            invalidAge = False
            if (age < 18 and invalidAge == False ):
                print(f"You need to be 18 years or older to apply!\n")
                break;

            else :
                print(f"invalidAge_value == {invalidAge}")
                return invalidAge




#                      !!Initial PseudoCode!!


    # if input == integer
        # print as INT
        # continue
    # else
        # print as non-INT
        # re-prompt user


    # while (getAge != INT):
        #   repeat user input to be strictly whole numbers
        #   omit any other type of input (including ASCII characs)

    # return INT ONLY



def main():
    print("Hello from drivingEligibilityCheck_zed!")
    checkUserAge()
    
    """If checkUserAge runs:
        print(this route)
    """


if __name__ == "__main__":
    main()
