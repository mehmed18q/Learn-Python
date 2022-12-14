class Person:
    def __init__(self, name, family, age, money):
        self.name = name
        self.family = family
        self.age = age
        self.money = money

    def __repr__(self):
        return f"{self.name} {self.family}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        return self.money + other.money

    def __mul__(self, other):
        return self.money * other.money

    def __truediv__(self, other):
        return self.money / other.money


person_1 = Person('mohammad', 'ordookhani', 24, 1000)
person_2 = Person('sara', 'moradi', 18, 2000)

# print(person_1)
# print(len(person_1))

# numbers = [1, 2, 3, 4, 5, 6]
# print(len(numbers))

print(person_1 + person_2)
print(person_1 * person_2)
print(person_1 / person_2)
