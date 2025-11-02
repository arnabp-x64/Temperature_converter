#inro
print("\n Welcome\nTo this Temperature converter🌡️\n")
print("INSTRUCTIONS:\n")
print("1. Type 1,2,3,4,5 or 6 to set what do you want to convert")
print("2. type 1 to  Celsius -> Fahrenheit")
print("3. type 2 to  Fahrenheit -> Celsius")
print("4. type 3 to  Fahrenheit -> Kelvin")
print("4. type 4 to  Kelvin -> Fahrenheit")
print("5. type 5 to  Celsius -> Kelvin")
print("6. type 6 to  Kelvin -> Celsius\n")

#taking input
while True:
    y_d = str(input("type e to exit❌ and r to resume✅"))
    if y_d =="e":
        break
    elif y_d == "r":
        inp = int(input("type 1,2,3,4,5 or 6 : "))

        if inp == 1:
            C = int(input("Type the value to convert : " ))
            F = (9/5) * C + 32
            print("The Result is "+str(F) + " ∘F")

        elif inp == 2:
            F = int(input("Type the value to convert : "))
            C = (F - 32) * 5 / 9
            print("The Result is "+str(C) + " ∘C")

        elif inp == 3:
            F = int(input("Type the value to convert : "))
            K = (F - 32) * 5/9 + 273.15
            print("The Result is "+str(K) + " K")  

        elif inp == 4:
            K = int(input("Type the value to convert : "))#
            F = (K - 273.15) * 9/5 + 32
            print("The Result is "+str(F) + " ∘F")

        elif inp == 5:
            C = int(input("Type the value to convert : "))
            K = C + 273.15
            print("The Result is "+str(K) + " K")

        elif inp == 6:
            K = int(input("Type the value to convert : "))
            C = K - 273.15
            print("The Result is "+str(C) + " ∘C")
        else:
            print("type something valid✔️")



    else:
        print("type something valid")

print("Thank you for using my program😀")
input("Press enter to exit")