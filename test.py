def detafelvan(de_tafel):
    for factor in range(1,11,1):
        uitkomst = factor * de_tafel
        print(str(factor) + " x " + str(de_tafel) + " = " + str(uitkomst) )

for tafel in range(2,6,1):
    print("de tafel van " + str(tafel))
    detafelvan(tafel)
    print()
