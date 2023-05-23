def detafelvan(de_tafel):
    reeks = range(1,11,1) # [1,2,3,4,5,6,7,8,9,10]
    for factor in reeks:
        uitkomst = factor * de_tafel
        print(str(factor) + " x " + str(de_tafel) + " = " + str(uitkomst) )

tafels = range(2,6,1) #[2,3,4,5]
for tafel in tafels:
    print("de tafel van " + str(tafel))
    detafelvan(tafel)
    print()
