# functions

def statement_generator(statement, decor):
    print(f"\n{decor * 5} {statement} {decor * 5} \n" )

def instructions():
    print("Instructions are displayed")


def num_check(question):


    error = "please enter a number that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            response = int(response)

            if 1 <= response <= 200:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

def factor(var_to_factor):

    factor_list = []

    for i in range(1,var_to_factor + 1):
        n = var_to_factor
        
        if n % i == 0:
            factor_list.append(i)
    
    factor_list.sort()
    return factor_list







# main routine
statement_generator("The ultimate factor finder", "-")      

want_instructions = input("Press <enter> to read or any key to continue: ")
    
if want_instructions == "":
    instructions()

while True:

    comment = ""

    to_factor = num_check("To factor: ")

    if to_factor == "xxx":
        break

    elif to_factor != 1:
        all_factors = factor(to_factor)

    else:
        all_factors = ""
        comment = "One is UNITY! it only have one factor. itself :)"


    if len(all_factors) == 2:
        comment = f"{to_factor} is a prime number"

    elif len(all_factors) % 2 == 1:
        comment = f"{to_factor} is a perfect square"
    
    if to_factor > 1:
        heading = f"Factors of {to_factor}"
    else:
        heading = "One is special..."

    #output
    print()
    statement_generator(heading, "*")
    print(all_factors)
    print(comment)
print("Thank you for using the factors calculator")