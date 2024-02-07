##################################################
from itertools import count
from tkinter import *
import tkinter.font
import numpy as np
import os
import re
script_dir = os.path.dirname(__file__)

root = Tk()
label= tkinter.Label()
root.title('Simple Statistics Calc')

root.geometry('750x650')
root.config(bg='#576d94')




global arrSum ,DisPerCounter
DisPerCounter = 0

arrSum = None

root.iconbitmap(os.path.join(script_dir, "87578.ico"))


Desired_font = tkinter.font.Font( family = "Roboto Mono", 
                                 size = 10, 
                                 weight = "bold")
##################################################
global DisplayResults1

def DisplayResults1():
    global DataLabel,MinLabel,MaxLabel,SampleSizeLabel,SumOfObservationsLabel
    global MeanLabel,ModeLabel,MedianLabel,RangeLabel,IQRLabel,VarianceLabel
    global StdLabel,COVLabel
    DataLabel = Label(root, text='Data:\t-',bg='#576d94',fg='#fff',font=Desired_font)
    DataLabel.place(x=10,y=60)
    MinLabel = Label(root, text='Min:\t-',bg='#576d94',fg='#fff',font=Desired_font)
    MinLabel.place(x=10,y=100)
    MaxLabel = Label(root, text='Max:\t-',bg='#576d94',fg='#fff',font=Desired_font)
    MaxLabel.place(x=10,y=140)
    
    SampleSizeLabel = Label(root, text='Size:\t-',bg='#576d94',fg='#fff',font=Desired_font)
    SampleSizeLabel.place(x=10,y=180)
    SumOfObservationsLabel = Label(root, text='Sum Of Observations:\t-',bg='#576d94',fg='#fff',font=Desired_font)
    SumOfObservationsLabel.place(x=10,y=220)
    MeanLabel = Label(root, text='Mean:\t-',bg='#576d94',fg='#fff',font=Desired_font)
    MeanLabel.place(x=10,y=260)
    ModeLabel = Label(root, text='Mode:\t-',bg='#576d94',fg='#fff',font=Desired_font)
    ModeLabel.place(x=10,y=300)
    MedianLabel = Label(root, text='Median:\t-',bg='#576d94',fg='#fff',font=Desired_font)
    MedianLabel.place(x=10,y=340)
    RangeLabel = Label(root, text='Range:\t-',bg='#576d94',fg='#fff',font=Desired_font)
    RangeLabel.place(x=10,y=380)
    IQRLabel = Label(root, text='Interquartile Range (IQR):\t-',bg='#576d94',fg='#fff',font=Desired_font)
    IQRLabel.place(x=10,y=420)
    VarianceLabel = Label(root, text='Variance:\t-',bg='#576d94',fg='#fff',font=Desired_font)
    VarianceLabel.place(x=10,y=460)
    StdLabel = Label(root, text='Standard Deviation:\t-',bg='#576d94',fg='#fff',font=Desired_font)
    StdLabel.place(x=10,y=500)
    COVLabel = Label(root, text='Coefficient Of Variation:\t-',bg='#576d94',fg='#fff',font=Desired_font)
    COVLabel.place(x=10,y=540)
    if DisPerCounter>=1:
        disablePerc()

    



def DisplayPercentilies():
    global DisPerCounter
    global PerLabel
    DisPerCounter+=1
    PerLabel = Label(root, text='Pk:\t-',bg='#576d94',fg='#fff',font=Desired_font)
    PerLabel.place(x=10,y=650)    
    global options_list2,value_inside2,inputOrder,question_menu2,myButton2
    options_list2 = {0:"Pk",1:"Qr",2:'Di'}
    value_inside2 = tkinter.StringVar(root)
    value_inside2.set(options_list2[0])
    question_menu2 = OptionMenu(root,value_inside2, *options_list2.values())    
    question_menu2.place(x=10,y=580)
    inputOrder = Entry(root,width=50,bg='#222222',fg='#fff')
    inputOrder.place(x=100,y=580,height=30,width=70)
    myButton2 = Button(root, text='Get Results',command=lambda:[CalcPerc()],bg='#2474a8',fg='#fff',font=Desired_font)
    myButton2.place(x=10,y=700)





def CalcPerc():
    global PerLabel
    PerLabel.destroy()
    CalcPerc2()


def CalcPerc2():
    global PerLabel,options_list2,value_inside2,inputOrder
    global PkFunction
    global Pk,Qr,Di
    if  format(value_inside2.get())==options_list2[0]:
        global Pk
        Pk = int(inputOrder.get())
        PerLabel = Label(root, text=f'Pk:\t{PkFunction(Pk)}',bg='#576d94',fg='#fff',font=Desired_font)
        PerLabel.place(x=10,y=650)    
    elif format(value_inside2.get())==options_list2[1]:
        global Qr
        Qr = (int(inputOrder.get())  * 25)  
        PerLabel = Label(root, text=f'Qr:\t{PkFunction(Qr)}',bg='#576d94',fg='#fff',font=Desired_font)
        PerLabel.place(x=10,y=650)    
    elif format(value_inside2.get())==options_list2[2]:
        global Di
        Di = (int(inputOrder.get())  * 10)  
        PerLabel = Label(root, text=f'Di:\t{PkFunction(Di)}',bg='#576d94',fg='#fff',font=Desired_font)
        PerLabel.place(x=10,y=650)    

def disablePerc():
    global DisPerCounter
    if DisPerCounter>=1:
        PerLabel.destroy()
        question_menu2.destroy()
        myButton2.destroy()
        inputOrder.destroy()
    pass


def ClearResults():
    global DataLabel,MinLabel,MaxLabel,SampleSizeLabel,SumOfObservationsLabel
    global MeanLabel,ModeLabel,MedianLabel,RangeLabel,IQRLabel,VarianceLabel
    global StdLabel,COVLabel,arrSum,DisplayResults1
    DataLabel.destroy();MinLabel.destroy();MaxLabel.destroy();SampleSizeLabel.destroy()
    SumOfObservationsLabel.destroy();MeanLabel.destroy();ModeLabel.destroy()
    MedianLabel.destroy();RangeLabel.destroy();IQRLabel.destroy();VarianceLabel.destroy()
    StdLabel.destroy();COVLabel.destroy()
    userInput = input1.get()
    #userInput = any((not char.isdigit() and char != ',') for char in userInput)

    #userInput = re.findall(r'^[+-]?\d*\.?\d+(?:,\d*\.?\d+)*$', userInput)
    userInput = re.findall(r'^[+-]?\d*\.?\d+(?:,\d*\.?\d+)*$', userInput)
    userInput = ''.join(userInput)
    print("input:\t",userInput)
    if (userInput=="")  or (userInput==','):
        DisplayResults1()
    else:
        NewResults(userInput)



def clickEnter(event):
    ClearResults()

def NewResults(userInput):

    global DataLabel,MinLabel,MaxLabel,SampleSizeLabel,SumOfObservationsLabel
    global MeanLabel,ModeLabel,MedianLabel,RangeLabel,IQRLabel,VarianceLabel
    global StdLabel,COVLabel
    global itemsArr,items,variance,arrMean,arrRange
    global PkFunction
    global arrSum
    global DisPerCounter

    itemsArr = []
    items = (userInput)
    variance = 0

    #if userInput=="":
       # disablePerc()

    items = items.split(',')
    integers = [int(item) for item in items if item.isdigit()]
    floats = [float(item) for item in items if not item.isdigit()]
    for i in floats:
        if 1>i>0:
            pass
        elif i/int(i)==1:
            integers.append(int(i))
            floats.remove(i)
    
    itemsArr.extend(integers)
    itemsArr.extend(floats)

    if len(itemsArr) == 1:
        DisplayResults1()

    itemsArr.sort()

    items = (str(itemsArr)[1:-1])
    arrMin = min(itemsArr)
    arrMax = max(itemsArr)
    arrLen = len(itemsArr)
    arrSum = sum(itemsArr)
    arrMean = arrSum/arrLen
    arrRange = max(itemsArr)-min(itemsArr)



    def varianceFunction(itemsArr):
        for i in itemsArr:
            global variance
            variance+= pow((i-arrMean),2)
        return variance/(arrLen-1)

    variance = varianceFunction(itemsArr)

    Std = (np.sqrt(variance)).real
    COV = (Std/arrMean).real

    DataLabel = Label(root, text=f'Data:\t{items}',bg='#576d94',fg='#fff',font=Desired_font)
    DataLabel.place(x=10,y=60)


        
    def modeFunction(itemsArr):
        frequency_dict = {}

    # Count the frequency of each number
        for number in itemsArr:
            if number in frequency_dict:
                frequency_dict[number] += 1
            else:
                frequency_dict[number] = 1

    # Check if all items have a frequency of 1
        all_unique = all(frequency == 1 for frequency in frequency_dict.values())

        # Find the mode(s)
        if all_unique:
            return "{ }"
        else:
            max_frequency = max(frequency_dict.values())
            mode = [num for num, frequency in frequency_dict.items() if frequency == max_frequency]
            return "{" + ", ".join(map(str, mode)) + "}"



    def PkFunction(Pk):
        global OrderPk,newOrderPk
        OrderPk=(Pk/100)*arrLen
        if ((OrderPk - np.fix(OrderPk))==0):
            PercentiliesInt(int(OrderPk))
            return PercResult
        else:
            newOrderPk = np.floor(OrderPk) + 1 
            PercentiliesFloat(int(newOrderPk))
            return PercResult

    def PercentiliesInt(newOrder):
        global PercResult
        PercResult = ((itemsArr[(newOrder-1)]+itemsArr[newOrder])/2)

    def PercentiliesFloat(newOrder):
        global PercResult
        PercResult =  itemsArr[(newOrder-1)]

    arrIQR = PkFunction(75) - PkFunction(25)


    

    MinLabel = Label(root, text=f'Min:\t{arrMin}',bg='#576d94',fg='#fff',font=Desired_font)
    MinLabel.place(x=10,y=100)
    MaxLabel = Label(root, text=f'Max:\t{arrMax}',bg='#576d94',fg='#fff',font=Desired_font)
    MaxLabel.place(x=10,y=140)
    SampleSizeLabel = Label(root, text=f'Size:\t{arrLen}',bg='#576d94',fg='#fff',font=Desired_font)
    SampleSizeLabel.place(x=10,y=180)
    SumOfObservationsLabel = Label(root, text=f'Sum Of Observations:\t{arrSum}',bg='#576d94',fg='#fff',font=Desired_font)
    SumOfObservationsLabel.place(x=10,y=220)
    MeanLabel = Label(root, text=f'Mean:\t{arrMean}',bg='#576d94',fg='#fff',font=Desired_font)
    MeanLabel.place(x=10,y=260)
    ModeLabel = Label(root, text=f'Mode:\t{modeFunction(itemsArr)}',bg='#576d94',fg='#fff',font=Desired_font)
    ModeLabel.place(x=10,y=300)
    MedianLabel = Label(root, text=f'Median:\t{np.median(itemsArr)}',bg='#576d94',fg='#fff',font=Desired_font)
    MedianLabel.place(x=10,y=340)
    RangeLabel = Label(root, text=f'Range:\t{arrRange}',bg='#576d94',fg='#fff',font=Desired_font)
    RangeLabel.place(x=10,y=380)
    IQRLabel = Label(root, text=f'Interquartile Range (IQR):\t{arrIQR}',bg='#576d94',fg='#fff',font=Desired_font)
    IQRLabel.place(x=10,y=420)
    VarianceLabel = Label(root, text=f'Variance:\t{variance}',bg='#576d94',fg='#fff',font=Desired_font)
    VarianceLabel.place(x=10,y=460)
    StdLabel = Label(root, text=f'Standard Deviation:\t{Std}',bg='#576d94',fg='#fff',font=Desired_font)
    StdLabel.place(x=10,y=500)
    COVLabel = Label(root, text=f'Coefficient Of Variation:\t{COV} %',bg='#576d94',fg='#fff',font=Desired_font)
    COVLabel.place(x=10,y=540)

    if DisPerCounter>=1:
        if input1.get()!="":
            disablePerc()
    DisplayPercentilies()

iVar = StringVar(value="opt1")


def on_radiobutton_click():
    global selected_value
    selected_value = iVar.get() 
    
    
    
  
label1 = Label(root, text='Enter Row Data: ',bg='#576d94',fg='#fff',font=Desired_font)
label1.place(x=10,y=15)
input1 = Entry(root,width=50,bg='#222222',fg='#fff')
input1.place(x=130,y=10,height=30,width=300)
myButton = Button(root, text='Get Results',command=lambda:[ClearResults()],bg='#2474a8',fg='#fff',font=Desired_font)
root.bind('<Return>',clickEnter)
myButton.place(x=440,y=8)
#Radiobutton(root, text = "Sample", variable=iVar,value = "opt1" ,bg='#576d94',font=Desired_font,fg='#fff',selectcolor="#000", command=on_radiobutton_click).place(x=550,y=8)
#Radiobutton(root, text = "Population", variable=iVar,value = "opt2" ,bg='#576d94',font=Desired_font,fg='#fff', selectcolor="#000",command=on_radiobutton_click).place(x=640,y=8)
DisplayResults1()
root.mainloop()