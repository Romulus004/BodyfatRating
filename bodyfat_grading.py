age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
fat = int(input("Enter your fat percentage: "))
cond =""
pronoun = ""

if age > 79:
    sen = "Invalid age."
    print(f'{"+"*(len(sen)+2)}\n+{sen}+\n{"+"*(len(sen)+2)}')

else:
    if gender.upper() == "M":
        pronoun = "Sir"
        if 20 <= age <= 39:
            if fat < 8:
                cond = "underfat"
            elif 8 <= fat <= 19:
                cond = "Ideal"
            elif 20 <= fat <= 25:
                cond = "overfat"
            else:
                cond = "obese"
        elif 40 <= age <= 59:
            if fat < 11:
                cond = "underfat"
            elif 11 <= fat <= 21:
                cond = "Ideal"
            elif 22 <= fat <= 28:
                cond = "overfat"
            else:
                cond = "obese"

        elif 60 <= age <= 79:
            if fat < 13:
                cond = "underfat"
            elif 13 <= fat <= 24:
                cond = "Ideal"
            elif 25 <= fat <= 30:
                cond = "overfat"
            else:
                cond = "obese"
        sen = f"{pronoun}, your condition is {cond}."
        print(f'{"+"*(len(sen)+2)}\n+{sen}+\n{"+"*(len(sen)+2)}')


    elif gender.upper() == "F":
        pronoun = "My Lady"
        if 20 <= age <= 39:
            if fat < 21:
                cond = "underfat"
            elif 21 <= fat <= 33:
                cond = "Ideal"
            elif 34 <= fat <= 39:
                cond = "overfat"
            else:
                cond = "obese"
            
        elif 40 <= age <= 59:
            if fat < 23:
                cond = "underfat"
            elif 23 <= fat <= 34:
                cond = "Ideal"
            elif 35 <= fat <= 40:
               cond = "overfat"
            else:
                cond = "obese"

        elif 60 <= age <= 79:
            if fat < 24:
                cond = "underfat"
            elif 24 <= fat <= 35:
                cond = "Ideal"
            elif 36 <= fat <= 42:
                cond = "overfat"
            else:
                cond = "obese"
        sen = f"{pronoun}, your condition is {cond}."
        print(f'{"+"*(len(sen)+2)}\n+{sen}+\n{"+"*(len(sen)+2)}')

    else:
        sen = "Invalid Gender"
        print(f'{"+"*(len(sen)+2)}\n+{sen}+\n{"+"*(len(sen)+2)}')