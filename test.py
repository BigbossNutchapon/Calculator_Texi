#ณัชพล กิตคราม
import math

#set dist = 10 ให้เป็นค่าdefult
def taxi(dist=10):
    distance = dist #KM
    distance2 = distance - math.floor(distance)
    distance = math.floor(distance)

    box = 0
    check = {10:6.5, 20:7.5, 40:8.0, 60:9.0, 80:10.5}

    for i in range(1,distance+1):
        if i == 1:
            tx = 35
        elif i > 1 and i <= 10:
            tx = 5.5
        elif i > 10 and i <= 20:
            tx = 6.5
        elif i > 20 and i <= 40:
            tx = 7.5
        elif i > 40 and i <= 60:
            tx = 8.0
        elif i > 60 and i <= 80:
            tx = 9.0
        elif i > 80:
            tx = 10.5
        else:
            print("error")
        box += tx
    #หากระยะทาง อยู่ในcheck จะดึงราคาสุดท้ายมาคำนวณ 
    if distance in check:
        tx = check[distance]
        #จะเอาค่าสุดท้ายที่เช็ค มาคูณกับtx ที่เซ็ตไว้ในdict
        extra = distance2 * tx
    else:
        #ในกรณีไม่อยู๋ในค่าที่เซ้ตไว้ สามารถใช้ค่าtx จะลูปได้เลย
        tx = tx
        extra = distance2 * tx
    calculate = round(box + extra)
    print(f"คุณเดินทาง :{dist} \nต้องจ่ายค่าแท็กซี่ :{calculate}")
while True:
    dist = float(input("Enter KM.: "))
    taxi(dist)