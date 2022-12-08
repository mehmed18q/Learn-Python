# There are an infiite number of ways to solve a problem
#T6
# Mohammad Sadegh Kiomarsi

students_number = int(input('Enter the Number of Students: '))


caterig_cost = 5000
entrance_fee = 20000
travel_expenses = 150000
capacity = 10
vans_count = students_number // capacity
full_vans = vans_count
Total_cost = 0

def calculate_cost():
    Fixed_cost = caterig_cost + entrance_fee
    travel_cost = vans_count * travel_expenses
    e_cost = (travel_cost / students_number) + Fixed_cost
    return round(e_cost)

if students_number % capacity != 0:
    vans_count += 1

Total_cost = calculate_cost()

print(f'The Cost of Scientific Visit for each Student is {Total_cost} Toman')
print(f'You need {vans_count} vans : {full_vans * (str(capacity)+ " ")}{students_number - (full_vans * capacity)}')
