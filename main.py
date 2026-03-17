import colorama


def askUserAge() -> int:
    getAge = int(input("What is your age?:"))    # Get variable data type -- DEBUG
    
    # DEBUG
    # print(f"getAge data type: {type(getAge)}\n")
    
    # initialization
    agePass = getAge
    invalid_Input = False

    # First successful User-Case
    if agePass == int(getAge):
        getAgeDataType = type(getAge)
        print(f"getAge == int(getAge) conditional: \n{getAgeDataType}\n")
        return agePass
    
    # Check for STRING input 
    elif agePass == isalpha(getAge):
        # Switch
        invalid_Input = True
        # Checking for STRING --DEBUG
        print("The input is a string!\n")

        # Repeat asking for
        while(invalid_Input == True):
            agePass = int(input("What is your age?:"))
            break;
            if(invalid_Input == True and agePass == isalpha(age)):
                continue;
                

    return agePass


def checkUserAge(age) -> bool:

        age = askUserAge()
        validAge = True
        invalidAge = False

        while age >= 18:

            # Ask User if they want a valid driver's license
            askDL = input("Do you want to apply for a driver's license?\n Y/N?\n")
            break;

            if askDL == 'Y' or  askDL == 'y' or askDL == 'Yes' or askDL == "yes" or askDL == "yEs" or askDL == "yeS" or askDL == "yES" or askDL == "YES":
                print("Yes condition!\n")
                break;

            elif askDL == 'N' or askDL == 'n' or askDL == "No" or askDL == "no" or askDL == "nO" or askDL == "NO":
                print("No conditon!\n")
                break;
            else:
                print("This is a valid age!\n")
                return validAge

        # emulate do-while loop
        while age < 18:
            invalidAge = False
            if (age < 18 and invalidAge == False ):
                print(f"You need to be 18 years or older to apply!\n")
                break;

            else:
                print(f"{invalidAge}")
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
    checkUserAge(askUserAge())


if __name__ == "__main__":
    main()
