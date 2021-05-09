a = int(input("Adja meg az a oldal hosszúságát méterben: "))
b = int(input("Adja meg az b oldal hosszúságát méterben: "))
c = int(input("Adja meg az c oldal hosszúságát méterben: "))
térfogat = a*b*c
felszin = 2*(a*b+a*c+b*c)
print("A Háromszög térfogat:", térfogat, ("m3"))
print("A Háromszög felszín:", felszin, ("m2"))
