names = []
prices = []

while True:
    print("\n1.Show 2.Add 3.Update 4.Search 5.Exit")
    c = input("Choose: ")

    if c=="1":
        if names==[]: print("No products.")
        else:
            for n,p in zip(names,prices): print(n,"-",p)

    elif c=="2":
        names.append(input("Name: "))
        prices.append(float(input("Price: ")))
        print("Added!")

    elif c=="3":
        n=input("Name to update: ")
        if n in names:
            prices[names.index(n)] = float(input("New price: "))
            print("Updated!")
        else: print("Not found.")

    elif c=="4":
        n=input("Search name: ")
        if n in names: print(n,"-",prices[names.index(n)])
        else: print("Not found.")

    elif c=="5":
        break
    else:
        print("Invalid.")