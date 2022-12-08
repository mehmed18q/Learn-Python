from distutils.log import info


9# There are an infiite number of ways to solve a problem
#T7
# Mohammad Sadegh Kiomarsi

minimum_age = 10
minimum_height = 140

age = int(input('Enter Your Age: '))

if minimum_age > age:
    print(f'You are {age} years old, the minimum age is {minimum_age} years.')
else:
    height = float(input('Enter Your Height: '))
    if minimum_height > height:
        print(f'Your age is appropriate, but the minimum height allowed is {minimum_height} CM,')
    else:
        name = input('Enter Your Name: ')
        member = {
            "name": name,
            "info": {
                "age":age,
                "height":height
            }
        }
        print('---------------------------------------')
        print('Congratulations, Registration was done.')
        print(f'We see {member["name"]} with {member["info"]["age"]} years old and {member["info"]["height"]} cm')
