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







# main routine
statement_generator("The ultimate factor finder", "-")      

want_instructions = input("Press <enter> to read or any key to continue: ")
    
if want_instructions == "":
    instructions()

while True:
    to_factor = num_check("To factor: ")
    print("You chose to factor", to_factor)

    if to_factor == "xxx":
        break