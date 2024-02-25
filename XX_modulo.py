# modulo is a programming term for remainder.
# for example: 5 mod 2 = 1, 5 mod 3 = 2. y? because u have a remainder of 2 when u divide 5 / 3.

for item in range(1,13):
    num_lollies = 12
    num_students = item

    division = num_lollies / num_students
    per_student = num_lollies // num_students # returns the integer only
    lollies_left = num_lollies % num_students

    if lollies_left == 0:
        print(f"{item} is a factor of 12!")

    print(f"each student gets {per_student} and we have {lollies_left} left over")