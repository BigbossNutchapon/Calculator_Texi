from tkinter import *
import tkinter.messagebox
import math
from turtle import heading

##ปัญหาที่พบบ่อยคือการใช้if กำหนดช่วงผิด ทำให้มีบางช่วงไม่ได้รับการคำนวณ ทำให้ผลลัพธ์คาดเคลื่อนไม่ตามจริง
#และการกำหนดrange ลืม+1 ทำให้ระยะทางสุดท้ายที่จะส่งไปคำนวณไม่ได้คำนวณ
#GUI ปัญหาคือไม่สามารถทำหน้าต่อไปได้เนื่องจากปิดไฟล์ไม่ได้ เพราะไม่ได้สร้างFrame ให้แต่ละWidget หากจะใช้.destroy ในทุกwidget จะทำให้เสียเวลาการทำนาน และLabel ใช้.destroyในการปิดไม่ได้
#File ปัญหาการเก็บลงfile IntVar ไม่รองรับการใช้F-string เกิดerror จะใช้F-String เพราะสามารถกำหนดตำแหน่งของString ได้

root = Tk()
root.title("โปรแกรมคำนวณค่าแท็กซี่")

root.geometry("380x450+700+100")
root.configure(bg="#fff")
root.resizable(False,False)


FONT_TITLE = ('Microsoft Yahei UI Light',18)
FONT_DEFULT = ('Microsoft Yahei UI Light')
FONT_COLOR_DEFULT = "black"

def checkfile():
    try:
        #หาไฟล์
        fr = open("History.txt","r",encoding="utf-8")
        fr.read()
        fr.close()
    except FileNotFoundError:
        #สร้างfile
        fw = open("History.txt","w",encoding="utf-8")
        fw.close()
checkfile()
def history():
    heading = Label(root,text='ประวัติการคำนวณ',fg='#4169E1',bg='white',font=FONT_TITLE)
    heading.place(x=10,y=5)


def mainpage():
    #GUI ปัญหาคือไม่สามารถทำหน้าต่อไปได้เนื่องจากปิดไฟล์ไม่ได้ เพราะไม่ได้สร้างFrame ให้แต่ละWidget หากจะใช้.destroy ในทุกwidget จะทำให้เสียเวลาการทำนาน และLabel ใช้.destroyในการปิดไม่ได้
    heading = Label(root,text='โปรแกรมคำนวณค่าโดยสารแท็กซี่',fg='#4169E1',bg='white',font=FONT_TITLE)
    heading.place(x=10,y=5)
    dev = Label(root,text='By:Nutchapon Kitkram',fg="#808080",bg='white',font=(FONT_DEFULT,9))
    dev.place(x=10,y=40)

    dist = IntVar()

    label1 = Label(root,text='กรอกระยะทาง(KM.)',fg='black',bg='white',font=('Microsoft Yahei UI Light',10),padx=5)
    label1.place(x=10,y=80)

    user = Entry(root,width=35,fg='black',bg='white',font=('Microsoft Yahei UI Light',12),justify='left',textvariable=dist)
    user.place(x=20,y=110)

    label2 = Label(root,text='ผลการคำนวณ :',fg='black',bg='white',font=('Microsoft Yahei UI Light',10),padx=5)
    label2.place(x=10,y=160)

    display = Entry(root,width=35,fg='black',bg='white',font=('Microsoft Yahei UI Light',12),justify='left')
    display.place(x=20,y=190)
    #function
    def taxi():
        #ปัญหาที่พบบ่อยคือการใช้if กำหนดช่วงผิด ทำให้มีบางช่วงไม่ได้รับการคำนวณ ทำให้ผลลัพธ์คาดเคลื่อนไม่ตามจริง
        #และการกำหนดrange ลืม+1 ทำให้ระยะทางสุดท้ายที่จะส่งไปคำนวณไม่ได้คำนวณ
        distance = dist.get() #KM
        distance2 = distance - math.floor(distance)
        distance = math.floor(distance)

        box = 0
        check = {10:6.5, 20:7.5, 40:8.0, 60:9.0, 80:10.5}

        for i in range(1,distance):
            if i == 1:
                tx = 35
            elif i > 1 and i <= 10:
                tx = 5.5
            elif i >= 11 and i <= 20:
                tx = 6.5
            elif i >= 21 and i <= 40:
                tx = 7.5
            elif i >= 41 and i <= 60:
                tx = 8.0
            elif i >= 61 and i <= 80:
                tx = 9.0
            elif i >= 81:
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
        calculate = str(round(box + extra))+" บาท"
        display.insert(0,calculate)
#ปัญหาการเก็บลงfile IntVar ไม่รองรับการใช้F-string เกิดerror
        fw = open("History.txt", "a", encoding="utf-8")
        fw.writelines(str(f"{dist:1} {calculate:12} \n"))
        fw.close()
        print(f"คุณเดินทาง :{dist} \nต้องจ่ายค่าแท็กซี่ :{calculate}")
    #ปุ่มหน้าแรก คำนวณ ดูประวัติ และออกจากโปรแกรม
    Button(root,width=20,pady=7,text='คำนวณ',bg='#4169E1',fg='white',font=('Microsoft Yahei UI Light',11),command=taxi).place(x=80,y=240)
    Button(root,width=20,pady=7,text='ดูประวัติ',bg='#C0C0C0',fg='black',font=('Microsoft Yahei UI Light',11),command=history).place(x=80,y=290)
    Button(root,width=20,pady=7,text='ออกจากโปรแกรม',bg='red',fg='white',font=('Microsoft Yahei UI Light',11),command=root.quit()).place(x=80,y=340)
def main():
    mainpage()
main()
root.mainloop()