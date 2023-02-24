 #Computer Application In Civil Engineering (CE 257)
"""
PRECIOUS BORKETEY
6933121

Github account: Precious-Naa
Github link: http://github.com/Precious-Naa/Data-Structures-
"""


#List of available cars and their prices
car_inventory={
    'Toyota Camry': 30000,
    'Honda Civic':25000,
    'Nissan Altima':28000,
    'Ford Mustang':45000,
    'Chevrolet Corvette':60000,
    'BMW 3 Series':50000,
    'Mercedes-Benz C-Class':55000,
    'Audi A4':40000,
    'Lexus ES':45000,
    'Infinity Q50':35000,
    'Tesla Model s':80000,
    'Porsche 911':90000,
    'Mazda CX-5':35000,
    'Subaru Forester':30000,
    'Jeep Wrangler':45000,
    'Land Rover Range Rover':90000,
    'Volvo XC90':55000,
    'Toyota Highlander':40000,
    'Honda CR-V':35000,
    'Nissan Rogue':30000,
    'Ford Escape': 30000,
    'Chevrolet Equinox':28000,
    'BMW X5':65000,
    'Mercedes-Benz GLC':55000,
    'Audi Q5':50000,
    'Lexus RX':55000,
    'Infinity QX50':45000,
    'Tesla Model Y':60000,
    'Porsche Cayenne':80000,
    'Mazda MX-5 Miata':25000,
    'Jeep Grand Cherokee':50000,
}


#Ask user for their car brand
CarBrand= input("Enter your car brand: ")

#Check if car brand is in the car_inventory dictionary
if CarBrand in car_inventory:
    print("The", CarBrand, "is available.")
    print("The price for the", CarBrand, "is",car_inventory[CarBrand], "$")
else:
    print("Sorry, the", Car,"is not availble.")















    
