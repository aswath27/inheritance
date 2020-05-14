def select_car():
    print("select the type of car you need to travel")
    select = int(input("1.Alto\n"
                            "2.Swift\n"
                            "3.Innova\n"
                            "4.jeep\n"
                            "5.indica    : "))
    if select == 1:
        x = int(2.50) 
                             
    elif select == 2: 
        x = int(4.50)
                             
    elif select == 3: 
        x = int(5.50)                
                             
    elif select == 4: 
        x = int(6.50)
    
    elif select == 5:
        x = int(7.50)
    else: 
        print("Invalid input") 
    
    return x


def calculate_fare():
    x = select_car()
    distance = float(input("Enter the kilometer covered : "))
    distance = distance * 1000
    fare = 4.00 + ((distance / 140) * x)
    
    return fare
    
def print_fare(fare):
        print("%0s%.2f" % ("Fare is: ", fare))
    
def main():
    fare = calculate_fare()
    print_fare(fare)

main()