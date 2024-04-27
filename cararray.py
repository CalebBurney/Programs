cars = ['honda', 'toyota', 'lexus', 'hyundai', 'acura']
for x in cars: 
    print(x)
def add_cars(cars, newCar):
    carin = input('please input a car company: ')
    cars.append(carin)
    print(cars)
add_cars(cars, 'ford')