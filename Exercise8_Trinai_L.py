usernameInput = input("username :")
passwordInput = input("password :")

if usernameInput == "admin" and passwordInput == "1234" :
    print("Done !")
    print("----------------------------")
    print("Welcome to my Store")
    print("Prees 1. :bread     1EA  =  50(THB):")
    print("Press 2. :Lay       1EA  =  25(THB):")
    print("Press 3. :RiceBacon 1EA  =  30(THB):")
    print("-----------------------------")
    Selected = int(input("You Press ? :"))
    if Selected == 1 :
        print("You Choose = bread")
        bread = int(30)
        Ea    = int(input("How many? :"))
        print("Total               :",(bread * Ea),("THB"))
    elif Selected ==  2 :
        print("You Choose Lay")
        Lay = int(25)
        Ea  = int(input("How many ? :"))
        print("Total               :",(Lay * Ea),("THB"))
    elif Selected == 3 :
        print("You choose RiceBacon")
        RiceBacon = int(30)
        Ea        = int(input("How many ? :"))
        print("Total                :",(RiceBacon * Ea),("THB"))
else:
    print("----------------------------")
    print("Login Failed !")

