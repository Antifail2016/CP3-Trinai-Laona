def vatCalculator(totalprice):
    result = totalprice+(totalprice*7/100)
    return result

print(vatCalculator(int(input("Number :"))))
