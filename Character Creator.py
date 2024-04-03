print("Enter your name:")
name = input()
    
print("Welcome to the character select sir "+name+"!")
print("Please select your class:         (Type the corresponding number)")
print("1.Tinkerer Mage")
print("2.Alien Werewolve")
print("3.Amazonion Bloodletter")

classc = input()
print(type(classc))
while int(classc) <= 3:
    if int(classc) ==1:
        classn = "TinkererMage" 
        Health = 5
        damage = 6
        print("You have selected "+classn+".")
        print("Damage:",damage)
        print("Health:",Health)
    elif int(classc) ==2:
        classn = "AlienWerewolve"
        Health = 10
        damage = 3
        print("You have selected "+classn+".")
        print("Damage:",damage)
        print("Health:",Health)
    elif int(classc) ==3:
        classn = "AmazonionBloodletter"
        Health = 7
        damage = 4
        print("You have selected "+classn+".")
        print("Damage:",damage)
        print("Health:",Health)
    
    print("Lock In?   1=Yes 0=No")
    x = int(input())
    if x==1:
        print("Locked in")
        break
    else:
        print("Please select your class again: (Type the corresponding number)")
        print("1.Tinkerer Mage")
        print("2.Alien Werewolve")
        print("3.Amazonion Bloodletter")
        classc = input()

