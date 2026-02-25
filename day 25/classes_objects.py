#car class basic - blueprint for car
class car:
    def __init__(self, brand, model, year, km):
        self.brand = brand
        self.model = model
        self.year = year
        self.km = km
    
    def info(self):
        print(f"car details: {self.brand} - {self.model} - {self.year} - {self.km}")

brand_input = input("brandname: ")
model_input = input("model: ")
year_input = int(input("year of the car: "))
km_input = int(input("kilometers: "))

input_car = car(brand_input, model_input, year_input, km_input)
input_car.info()

#oefening 2 person
class person:
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth
    
    def get_age(self):
        year_input = int(input("current year: "))
        age = year_input - self.birth
        return(age)

name_input = input("name: ")
birth_year = int(input("birthyear: "))

info_person = person(name_input, birth_year)
result = info_person.get_age()
print(f"you will be this year {result} years old")