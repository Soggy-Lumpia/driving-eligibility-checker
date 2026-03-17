import colorama


def askUserAge() -> int:
    getAge = int(input("What is your age?:"))
    # Get variable data type
    print(f"getAge data type: {type(getAge)}\n")
    # initialization
    validAge = False
    agePass = getAge
    
    # First successful User-Case
    if agePass == int(getAge):
        getAgeDataType = type(getAge)
        print(f"getAge == int(getAge) conditional: \n{getAgeDataType}\n")
        return getAge
        
        
    return agePass
        

def checkUserAge(age) -> bool: 
        
        age = askUserAge()
        while age >= 18:
            
            # Ask User if they want a valid driver's license
            askDL = input("Do you want to apply for a driver's license?\n Y/N?\n")
            break;
            
            if askDL == 'Y' or  askDL == 'y' or askDL == 'Yes' or askDL == "yes" or askDL == "yEs" or askDL == "yeS" or askDL == "yES" or askDL == "YES":
                print("Yes condition!")
                break;
                
            elif askDL == 'N' or askDL == 'n' or askDL == "No" or askDL == "no" or askDL == "nO" or askDL == "NO":
                print("No conditon!")
                break;
                
        # emulate do-while loop
        while age < 18:
            age == getAgeDataType
            if (age < 18 or getAgeDataType != type(INT)):
                print(f"You need to be 18 years or older to apply!\n")
            else:
                break;
            

        
    

    
    
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
    
    
    
    

#     print(f"getAge_type:{type(getAge)}\n")
#     validAge = True

#     if getAge < 18: 
#         validAge = False

#         print("You are not eligible to drive yet!\n")
#         return validAge
    
#     elif getAge >= 18:
#         print("You are old enough to drive!\n")
#         validAge = True
    
#     elif getAge is type(str):  
    
#         if validAge == True:
#             return True
    
#     if validAge == False: 
#         print("Need a driving age!\n")
#         return validAge
    
#     else:
#         print("else condition: validAge == True")
        


def main():
    print("Hello from drivingEligibilityCheck_zed!")
    checkUserAge(askUserAge())


if __name__ == "__main__":
    main()
