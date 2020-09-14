#!/usr/bin/python

weight = float(input("Gewicht in KG: "))
length = float(input("Lengte in M: "))

bmi = (weight / (length * length))

if bmi < 15 :
    print("bmi: ", bmi, "Ondergewicht")
elif bmi < 20 :
    print("bmi: ", bmi, "Licht Ondergewicht")
elif bmi < 25 :
    print("bmi: ", bmi, "Normaal")
elif bmi < 30 :
    print("bmi: ", bmi, "Overgewicht")
elif bmi < 35 :
    print("bmi: ", bmi, "Obesitas")
else :
    print("bmi: ", bmi, "Morbide Obesitas")
