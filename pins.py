from tkinter import *
import os
import json
import ftplib
import pyfirmata

root = Tk()
root.title("Arduino IO pins Manager")
root.configure(bg="#2B2B2B")
# ----------------CENTer SCreeN-----------
width = 910
height = 675

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = ((screen_width / 2) - (width / 2))
y = ((screen_height / 2) - (height / 2))

root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
# -------------------eND----------------------
root.resizable(False, False)

font1 = ('Montserrat ExtraBold', 11)


# ----------------------------FUNCTIONS-----------------------------------
def openPort():
    global arduino
    arduino = pyfirmata.Arduino('COM7')


openPort()
# define IO pins
IO2 = arduino.get_pin('d:2:o')
IO3 = arduino.get_pin('d:3:o')
IO4 = arduino.get_pin('d:4:o')
IO5 = arduino.get_pin('d:5:o')
IO6 = arduino.get_pin('d:6:o')
IO7 = arduino.get_pin('d:7:o')
IO8 = arduino.get_pin('d:8:o')
IO9 = arduino.get_pin('d:9:o')
IO10 = arduino.get_pin('d:10:o')
IO11 = arduino.get_pin('d:11:o')
IO12 = arduino.get_pin('d:12:o')
IO13 = arduino.get_pin('d:13:o')
# IOA0 = arduino.get_pin('a:0:o')
# IOA1 = arduino.get_pin('a:1:o')
# IOA2 = arduino.get_pin('a:2:o')
# IOA3 = arduino.get_pin('a:3:o')
# IOA4 = arduino.get_pin('a:4:o')
# IOA5 = arduino.get_pin('a:5:o')


def loadDefaults():
    global x, current_row, my_pins
    try:
        if os.path.isfile('pins.json'):
            my_pins = json.load(open('pins.json'))
    except:
        current_row = 0
        pass
    try:
        x = len(my_pins["pins"])
        current_row = my_pins["pins"][x - 1][0]
    except:
        current_row = 0
        pass


try:
    loadDefaults()
except:
    pass


def addPin():
    global prompt_label
    max_label = Label(root, text="***NO DATA TO BE SAVED!!!***", font=font1, bg="#2B2B2B",
                      fg="red")

    if addPin.counter > 17:
        max_label.config(text="***your arduino has no more pins available***")
        max_label.place(x=(width / 2) - int((len(max_label.cget("text")) * 4)), y=height - 53)
        prompt_label = max_label
        addPin.counter = 18

    if 0 < addPin.counter < 19:
        ifEmpty()
        if saveData.i == 0:
            return
        elif saveData.i == 1:
            # print(addPin.counter)
            saveData()
            saveData.i = 0
    if addPin.counter == 18:
        return
    createEntry()

    addPin.counter += 1
    # print(addPin.counter)


def deleteCell():
    addPin.counter = addPin.counter - 1
    # print(addPin.counter)
    max_label = Label(root, text="***NO DATA TO BE SAVED!!!***", font=font1, bg="#2B2B2B",
                      fg="red")
    if addPin.counter < 0:
        max_label.config(text="***THERE's NOTHING TO BE DELETED***")
        max_label.place(x=(width / 2) - int((len(max_label.cget("text")) * 4)), y=height - 53)
        addPin.counter = 0
        return
    if addPin.counter == 0:
        name0.grid_remove()
        pin0.grid_remove()
        state0.grid_remove()
        checkValidity()
        addPin.counter = 0
        saveData()
        try:
            pinNumber(int(bin1), 0)
        except:
            pass
        # os.remove("pins.json")
        open('pins.json', 'w').close()
    if addPin.counter == 1:
        name1.grid_remove()
        pin1.grid_remove()
        state1.grid_remove()
        checkValidity()
        addPin.counter = 1
        saveData()
        try:
            pinNumber(int(bin2), 0)
        except:
            pass
    if addPin.counter == 2:
        name2.grid_remove()
        pin2.grid_remove()
        state2.grid_remove()
        checkValidity()
        addPin.counter = 2
        saveData()
        try:
            pinNumber(int(bin3), 0)
        except:
            pass
    if addPin.counter == 3:
        name3.grid_remove()
        pin3.grid_remove()
        state3.grid_remove()
        checkValidity()
        addPin.counter = 3
        saveData()
        try:
            pinNumber(int(bin4), 0)
        except:
            pass
    if addPin.counter == 4:
        name4.grid_remove()
        pin4.grid_remove()
        state4.grid_remove()
        checkValidity()
        addPin.counter = 4
        saveData()
        try:
            pinNumber(int(bin5), 0)
        except:
            pass
    if addPin.counter == 5:
        name5.grid_remove()
        pin5.grid_remove()
        state5.grid_remove()
        checkValidity()
        addPin.counter = 5
        saveData()
        try:
            pinNumber(int(bin6), 0)
        except:
            pass
    if addPin.counter == 6:
        name6.grid_remove()
        pin6.grid_remove()
        state6.grid_remove()
        checkValidity()
        addPin.counter = 6
        saveData()
        try:
            pinNumber(int(bin7), 0)
        except:
            pass
    if addPin.counter == 7:
        name7.grid_remove()
        pin7.grid_remove()
        state7.grid_remove()
        checkValidity()
        addPin.counter = 7
        saveData()
        try:
            pinNumber(int(bin8), 0)
        except:
            pass
    if addPin.counter == 8:
        name8.grid_remove()
        pin8.grid_remove()
        state8.grid_remove()
        checkValidity()
        addPin.counter = 8
        saveData()
        try:
            pinNumber(int(bin9), 0)
        except:
            pass
    if addPin.counter == 9:
        name9.grid_remove()
        pin9.grid_remove()
        state9.grid_remove()
        checkValidity()
        addPin.counter = 9
        saveData()
        try:
            pinNumber(int(bin10), 0)
        except:
            pass
    if addPin.counter == 10:
        name10.grid_remove()
        pin10.grid_remove()
        state10.grid_remove()
        checkValidity()
        addPin.counter = 10
        saveData()
        try:
            pinNumber(int(bin11), 0)
        except:
            pass
    if addPin.counter == 11:
        name11.grid_remove()
        pin11.grid_remove()
        state11.grid_remove()
        checkValidity()
        addPin.counter = 11
        saveData()
        try:
            pinNumber(int(bin12), 0)
        except:
            pass
    if addPin.counter == 12:
        name12.grid_remove()
        pin12.grid_remove()
        state12.grid_remove()
        checkValidity()
        addPin.counter = 12
        saveData()
        try:
            pinNumber(int(bin13), 0)
        except:
            pass
    if addPin.counter == 13:
        name13.grid_remove()
        pin13.grid_remove()
        state13.grid_remove()
        checkValidity()
        addPin.counter = 13
        saveData()
        try:
            pinNumber(int(bin14), 0)
        except:
            pass
    if addPin.counter == 14:
        name14.grid_remove()
        pin14.grid_remove()
        state14.grid_remove()
        checkValidity()
        addPin.counter = 14
        saveData()
        try:
            pinNumber(int(bin15), 0)
        except:
            pass
    if addPin.counter == 15:
        name15.grid_remove()
        pin15.grid_remove()
        state15.grid_remove()
        checkValidity()
        addPin.counter = 15
        saveData()
        try:
            pinNumber(int(bin16), 0)
        except:
            pass
    if addPin.counter == 16:
        name16.grid_remove()
        pin16.grid_remove()
        state16.grid_remove()
        checkValidity()
        addPin.counter = 16
        saveData()
        try:
            pinNumber(int(bin17), 0)
        except:
            pass
    if addPin.counter == 17:
        name17.grid_remove()
        pin17.grid_remove()
        state17.grid_remove()
        checkValidity()
        addPin.counter = 17
        saveData()
        try:
            pinNumber(int(bin18), 0)
        except:
            pass


def saveData():
    max_label = Label(root, text="***NO DATA TO BE SAVED!!!***", font=font1, bg="#2B2B2B",
                      fg="red")
    if addPin.counter == 0:
        max_label.place(x=(width / 2) - int((len(max_label.cget("text")) * 4)), y=height - 53)
        return
    try:
        saveEveryStep()
    except:
        pass

    # loadDefaults()


def checkValidity():
    if addPin.counter == 0: addPin.counter = 0
    if addPin.counter == 1: addPin.counter = 1
    if addPin.counter == 2: addPin.counter = 2
    if addPin.counter == 3: addPin.counter = 3
    if addPin.counter == 4: addPin.counter = 4
    if addPin.counter == 5: addPin.counter = 5
    if addPin.counter == 6: addPin.counter = 6
    if addPin.counter == 7: addPin.counter = 7
    if addPin.counter == 8: addPin.counter = 8
    if addPin.counter == 9: addPin.counter = 9
    if addPin.counter == 10: addPin.counter = 10
    if addPin.counter == 11: addPin.counter = 11
    if addPin.counter == 12: addPin.counter = 12
    if addPin.counter == 13: addPin.counter = 13
    if addPin.counter == 14: addPin.counter = 14
    if addPin.counter == 15: addPin.counter = 15
    if addPin.counter == 16: addPin.counter = 16
    if addPin.counter == 17: addPin.counter = 17
    if addPin.counter == 18: addPin.counter = 18


def createEntry():
    global name0, name1, name2, name3, name4, name5, name6, name7, name8, name9, name10, name11, name12, name13, name14, name15, name16, name17, name18
    global pin0, pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, pin9, pin10, pin11, pin12, pin13, pin14, pin15, pin16, pin17, pin18
    global state0, state1, state2, state3, state4, state5, state6, state7, state8, state9, state10, state11, state12, state13, state14, state15, state16, state17, state18

    if addPin.counter == 0:
        name0 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        pin0 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        state0 = Entry(input_frame, width=25, font=font1, borderwidth=2)

        name0.grid(row=addPin.counter, column=0)
        pin0.grid(row=addPin.counter, column=1)
        state0.grid(row=addPin.counter, column=2)
    if addPin.counter == 1:
        name1 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        pin1 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        state1 = Entry(input_frame, width=25, font=font1, borderwidth=2)

        name1.grid(row=addPin.counter, column=0)
        pin1.grid(row=addPin.counter, column=1)
        state1.grid(row=addPin.counter, column=2)
    if addPin.counter == 2:
        name2 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        pin2 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        state2 = Entry(input_frame, width=25, font=font1, borderwidth=2)

        name2.grid(row=addPin.counter, column=0)
        pin2.grid(row=addPin.counter, column=1)
        state2.grid(row=addPin.counter, column=2)
    if addPin.counter == 3:
        name3 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        pin3 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        state3 = Entry(input_frame, width=25, font=font1, borderwidth=2)

        name3.grid(row=addPin.counter, column=0)
        pin3.grid(row=addPin.counter, column=1)
        state3.grid(row=addPin.counter, column=2)
    if addPin.counter == 4:
        name4 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        pin4 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        state4 = Entry(input_frame, width=25, font=font1, borderwidth=2)

        name4.grid(row=addPin.counter, column=0)
        pin4.grid(row=addPin.counter, column=1)
        state4.grid(row=addPin.counter, column=2)
    if addPin.counter == 5:
        name5 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        pin5 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        state5 = Entry(input_frame, width=25, font=font1, borderwidth=2)

        name5.grid(row=addPin.counter, column=0)
        pin5.grid(row=addPin.counter, column=1)
        state5.grid(row=addPin.counter, column=2)
    if addPin.counter == 6:
        name6 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        pin6 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        state6 = Entry(input_frame, width=25, font=font1, borderwidth=2)

        name6.grid(row=addPin.counter, column=0)
        pin6.grid(row=addPin.counter, column=1)
        state6.grid(row=addPin.counter, column=2)
    if addPin.counter == 7:
        name7 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        pin7 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        state7 = Entry(input_frame, width=25, font=font1, borderwidth=2)

        name7.grid(row=addPin.counter, column=0)
        pin7.grid(row=addPin.counter, column=1)
        state7.grid(row=addPin.counter, column=2)
    if addPin.counter == 8:
        name8 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        pin8 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        state8 = Entry(input_frame, width=25, font=font1, borderwidth=2)

        name8.grid(row=addPin.counter, column=0)
        pin8.grid(row=addPin.counter, column=1)
        state8.grid(row=addPin.counter, column=2)
    if addPin.counter == 9:
        name9 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        pin9 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        state9 = Entry(input_frame, width=25, font=font1, borderwidth=2)

        name9.grid(row=addPin.counter, column=0)
        pin9.grid(row=addPin.counter, column=1)
        state9.grid(row=addPin.counter, column=2)
    if addPin.counter == 10:
        name10 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        pin10 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        state10 = Entry(input_frame, width=25, font=font1, borderwidth=2)

        name10.grid(row=addPin.counter, column=0)
        pin10.grid(row=addPin.counter, column=1)
        state10.grid(row=addPin.counter, column=2)
    if addPin.counter == 11:
        name11 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        pin11 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        state11 = Entry(input_frame, width=25, font=font1, borderwidth=2)

        name11.grid(row=addPin.counter, column=0)
        pin11.grid(row=addPin.counter, column=1)
        state11.grid(row=addPin.counter, column=2)
    if addPin.counter == 12:
        name12 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        pin12 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        state12 = Entry(input_frame, width=25, font=font1, borderwidth=2)

        name12.grid(row=addPin.counter, column=0)
        pin12.grid(row=addPin.counter, column=1)
        state12.grid(row=addPin.counter, column=2)
    if addPin.counter == 13:
        name13 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        pin13 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        state13 = Entry(input_frame, width=25, font=font1, borderwidth=2)

        name13.grid(row=addPin.counter, column=0)
        pin13.grid(row=addPin.counter, column=1)
        state13.grid(row=addPin.counter, column=2)
    if addPin.counter == 14:
        name14 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        pin14 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        state14 = Entry(input_frame, width=25, font=font1, borderwidth=2)

        name14.grid(row=addPin.counter, column=0)
        pin14.grid(row=addPin.counter, column=1)
        state14.grid(row=addPin.counter, column=2)
    if addPin.counter == 15:
        name15 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        pin15 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        state15 = Entry(input_frame, width=25, font=font1, borderwidth=2)

        name15.grid(row=addPin.counter, column=0)
        pin15.grid(row=addPin.counter, column=1)
        state15.grid(row=addPin.counter, column=2)
    if addPin.counter == 16:
        name16 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        pin16 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        state16 = Entry(input_frame, width=25, font=font1, borderwidth=2)

        name16.grid(row=addPin.counter, column=0)
        pin16.grid(row=addPin.counter, column=1)
        state16.grid(row=addPin.counter, column=2)
    if addPin.counter == 17:
        name17 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        pin17 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        state17 = Entry(input_frame, width=25, font=font1, borderwidth=2)

        name17.grid(row=addPin.counter, column=0)
        pin17.grid(row=addPin.counter, column=1)
        state17.grid(row=addPin.counter, column=2)
    if addPin.counter == 18:
        name18 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        pin18 = Entry(input_frame, width=25, font=font1, borderwidth=2)
        state18 = Entry(input_frame, width=25, font=font1, borderwidth=2)

        name18.grid(row=addPin.counter, column=0)
        pin18.grid(row=addPin.counter, column=1)
        state18.grid(row=addPin.counter, column=2)


def ifEmpty():
    if addPin.counter == 1:
        if name0.get() == '' or pin0.get() == '' or state0.get() == '':
            checkValidity()
            saveData.i = 0
            # print(addPin.counter)
            # print("NOT SAVED")
        else:
            saveData.i = 1
            # print(addPin.counter)
            # print("DATA SAVED")
    if addPin.counter == 2:
        if name1.get() == '' or pin1.get() == '' or state1.get() == '':
            checkValidity()
            saveData.i = 0
            # print(addPin.counter)
            # print("NOT SAVED")
        else:
            saveData.i = 1
            # print(addPin.counter)
            # print("DATA SAVED")
    if addPin.counter == 3:
        if name2.get() == '' or pin2.get() == '' or state2.get() == '':
            checkValidity()
            saveData.i = 0
            # print(addPin.counter)
            # print("NOT SAVED")
        else:
            saveData.i = 1
            # print(addPin.counter)
            # print("DATA SAVED")
    if addPin.counter == 4:
        if name3.get() == '' or pin3.get() == '' or state3.get() == '':
            checkValidity()
            saveData.i = 0
            # print(addPin.counter)
            # print("NOT SAVED")
        else:
            saveData.i = 1
            # print(addPin.counter)
            # print("DATA SAVED")
    if addPin.counter == 5:
        if name4.get() == '' or pin4.get() == '' or state4.get() == '':
            checkValidity()
            saveData.i = 0
            # print(addPin.counter)
            # print("NOT SAVED")
        else:
            saveData.i = 1
            # print(addPin.counter)
            # print("DATA SAVED")
    if addPin.counter == 6:
        if name5.get() == '' or pin5.get() == '' or state5.get() == '':
            checkValidity()
            saveData.i = 0
            # print(addPin.counter)
            # print("NOT SAVED")
        else:
            saveData.i = 1
            # print(addPin.counter)
            # print("DATA SAVED")
    if addPin.counter == 7:
        if name6.get() == '' or pin6.get() == '' or state6.get() == '':
            checkValidity()
            saveData.i = 0
            # print(addPin.counter)
            # print("NOT SAVED")
        else:
            saveData.i = 1
            # print(addPin.counter)
            # print("DATA SAVED")
    if addPin.counter == 8:
        if name7.get() == '' or pin7.get() == '' or state7.get() == '':
            checkValidity()
            saveData.i = 0
            # print(addPin.counter)
            # print("NOT SAVED")
        else:
            saveData.i = 1
            # print(addPin.counter)
            # print("DATA SAVED")
    if addPin.counter == 9:
        if name8.get() == '' or pin8.get() == '' or state8.get() == '':
            checkValidity()
            saveData.i = 0
            # print(addPin.counter)
            # print("NOT SAVED")
        else:
            saveData.i = 1
            # print(addPin.counter)
            # print("DATA SAVED")
    if addPin.counter == 10:
        if name9.get() == '' or pin9.get() == '' or state9.get() == '':
            checkValidity()
            saveData.i = 0
            # print(addPin.counter)
            # print("NOT SAVED")
        else:
            saveData.i = 1
            # print(addPin.counter)
            # print("DATA SAVED")
    if addPin.counter == 11:
        if name10.get() == '' or pin10.get() == '' or state10.get() == '':
            checkValidity()
            saveData.i = 0
            # print(addPin.counter)
            # print("NOT SAVED")
        else:
            saveData.i = 1
            # print(addPin.counter)
            # print("DATA SAVED")
    if addPin.counter == 12:
        if name11.get() == '' or pin11.get() == '' or state11.get() == '':
            checkValidity()
            saveData.i = 0
            # print(addPin.counter)
            # print("NOT SAVED")
        else:
            saveData.i = 1
            # print(addPin.counter)
            # print("DATA SAVED")
    if addPin.counter == 13:
        if name12.get() == '' or pin12.get() == '' or state12.get() == '':
            checkValidity()
            saveData.i = 0
            # print(addPin.counter)
            # print("NOT SAVED")
        else:
            saveData.i = 1
            # print(addPin.counter)
            # print("DATA SAVED")
    if addPin.counter == 14:
        if name13.get() == '' or pin13.get() == '' or state13.get() == '':
            checkValidity()
            saveData.i = 0
            # print(addPin.counter)
            # print("NOT SAVED")
        else:
            saveData.i = 1
            # print(addPin.counter)
            # print("DATA SAVED")
    if addPin.counter == 15:
        if name14.get() == '' or pin14.get() == '' or state14.get() == '':
            checkValidity()
            saveData.i = 0
            # print(addPin.counter)
            # print("NOT SAVED")
        else:
            saveData.i = 1
            # print(addPin.counter)
            # print("DATA SAVED")
    if addPin.counter == 16:
        if name15.get() == '' or pin15.get() == '' or state15.get() == '':
            checkValidity()
            saveData.i = 0
            # print(addPin.counter)
            # print("NOT SAVED")
        else:
            saveData.i = 1
            # print(addPin.counter)
            # print("DATA SAVED")
    if addPin.counter == 17:
        if name16.get() == '' or pin16.get() == '' or state16.get() == '':
            checkValidity()
            saveData.i = 0
            # print(addPin.counter)
            # print("NOT SAVED")
        else:
            saveData.i = 1
            # print(addPin.counter)
            # print("DATA SAVED")
    if addPin.counter == 18:
        if name17.get() == '' or pin17.get() == '' or state17.get() == '':
            checkValidity()
            saveData.i = 0
            # print(addPin.counter)
            # print("NOT SAVED")
        else:
            saveData.i = 1
            # print(addPin.counter)
            # print("DATA SAVED")
    if addPin.counter == 19:
        if name18.get() == '' or pin18.get() == '' or state18.get() == '':
            checkValidity()
            saveData.i = 0
            # print(addPin.counter)
            # print("NOT SAVED")
        else:
            saveData.i = 1
            # print(addPin.counter)
            # print("DATA SAVED")


def saveToFile():
    y = json.dumps(addPin.combined)
    # print(y)
    x = json.dumps(addPin.combined)
    with open('pins.json', 'w') as f:
        f.write(x)
        f.close()


def saveEveryStep():
    if addPin.counter == 1:
        addPin.combined = {"pins": [[1, name0.get(), pin0.get(), state0.get()]]}
        saveToFile()
    if addPin.counter == 2:
        addPin.combined = {"pins": [[1, name0.get(), pin0.get(), state0.get()],
                                    [2, name1.get(), pin1.get(), state1.get()]]}
        saveToFile()
    if addPin.counter == 3:
        addPin.combined = {"pins": [[1, name0.get(), pin0.get(), state0.get()],
                                    [2, name1.get(), pin1.get(), state1.get()],
                                    [3, name2.get(), pin2.get(), state2.get()]]}
        saveToFile()
    if addPin.counter == 4:
        addPin.combined = {"pins": [[1, name0.get(), pin0.get(), state0.get()],
                                    [2, name1.get(), pin1.get(), state1.get()],
                                    [3, name2.get(), pin2.get(), state2.get()],
                                    [4, name3.get(), pin3.get(), state3.get()]]}
        saveToFile()
    if addPin.counter == 5:
        addPin.combined = {"pins": [[1, name0.get(), pin0.get(), state0.get()],
                                    [2, name1.get(), pin1.get(), state1.get()],
                                    [3, name2.get(), pin2.get(), state2.get()],
                                    [4, name3.get(), pin3.get(), state3.get()],
                                    [5, name4.get(), pin4.get(), state4.get()]]}
        saveToFile()
    if addPin.counter == 6:
        addPin.combined = {"pins": [[1, name0.get(), pin0.get(), state0.get()],
                                    [2, name1.get(), pin1.get(), state1.get()],
                                    [3, name2.get(), pin2.get(), state2.get()],
                                    [4, name3.get(), pin3.get(), state3.get()],
                                    [5, name4.get(), pin4.get(), state4.get()],
                                    [6, name5.get(), pin5.get(), state5.get()]]}
        saveToFile()
    if addPin.counter == 7:
        addPin.combined = {"pins": [[1, name0.get(), pin0.get(), state0.get()],
                                    [2, name1.get(), pin1.get(), state1.get()],
                                    [3, name2.get(), pin2.get(), state2.get()],
                                    [4, name3.get(), pin3.get(), state3.get()],
                                    [5, name4.get(), pin4.get(), state4.get()],
                                    [6, name5.get(), pin5.get(), state5.get()],
                                    [7, name6.get(), pin6.get(), state6.get()]]}
        saveToFile()
    if addPin.counter == 8:
        addPin.combined = {"pins": [[1, name0.get(), pin0.get(), state0.get()],
                                    [2, name1.get(), pin1.get(), state1.get()],
                                    [3, name2.get(), pin2.get(), state2.get()],
                                    [4, name3.get(), pin3.get(), state3.get()],
                                    [5, name4.get(), pin4.get(), state4.get()],
                                    [6, name5.get(), pin5.get(), state5.get()],
                                    [7, name6.get(), pin6.get(), state6.get()],
                                    [8, name7.get(), pin7.get(), state7.get()]]}
        saveToFile()
    if addPin.counter == 9:
        addPin.combined = {"pins": [[1, name0.get(), pin0.get(), state0.get()],
                                    [2, name1.get(), pin1.get(), state1.get()],
                                    [3, name2.get(), pin2.get(), state2.get()],
                                    [4, name3.get(), pin3.get(), state3.get()],
                                    [5, name4.get(), pin4.get(), state4.get()],
                                    [6, name5.get(), pin5.get(), state5.get()],
                                    [7, name6.get(), pin6.get(), state6.get()],
                                    [8, name7.get(), pin7.get(), state7.get()],
                                    [9, name8.get(), pin8.get(), state8.get()]]}
        saveToFile()
    if addPin.counter == 10:
        addPin.combined = {"pins": [[1, name0.get(), pin0.get(), state0.get()],
                                    [2, name1.get(), pin1.get(), state1.get()],
                                    [3, name2.get(), pin2.get(), state2.get()],
                                    [4, name3.get(), pin3.get(), state3.get()],
                                    [5, name4.get(), pin4.get(), state4.get()],
                                    [6, name5.get(), pin5.get(), state5.get()],
                                    [7, name6.get(), pin6.get(), state6.get()],
                                    [8, name7.get(), pin7.get(), state7.get()],
                                    [9, name8.get(), pin8.get(), state8.get()],
                                    [10, name9.get(), pin9.get(), state9.get()]]}
        saveToFile()
    if addPin.counter == 11:
        addPin.combined = {"pins": [[1, name0.get(), pin0.get(), state0.get()],
                                    [2, name1.get(), pin1.get(), state1.get()],
                                    [3, name2.get(), pin2.get(), state2.get()],
                                    [4, name3.get(), pin3.get(), state3.get()],
                                    [5, name4.get(), pin4.get(), state4.get()],
                                    [6, name5.get(), pin5.get(), state5.get()],
                                    [7, name6.get(), pin6.get(), state6.get()],
                                    [8, name7.get(), pin7.get(), state7.get()],
                                    [9, name8.get(), pin8.get(), state8.get()],
                                    [10, name9.get(), pin9.get(), state9.get()],
                                    [11, name10.get(), pin10.get(), state10.get()]]}
        saveToFile()
    if addPin.counter == 12:
        addPin.combined = {"pins": [[1, name0.get(), pin0.get(), state0.get()],
                                    [2, name1.get(), pin1.get(), state1.get()],
                                    [3, name2.get(), pin2.get(), state2.get()],
                                    [4, name3.get(), pin3.get(), state3.get()],
                                    [5, name4.get(), pin4.get(), state4.get()],
                                    [6, name5.get(), pin5.get(), state5.get()],
                                    [7, name6.get(), pin6.get(), state6.get()],
                                    [8, name7.get(), pin7.get(), state7.get()],
                                    [9, name8.get(), pin8.get(), state8.get()],
                                    [10, name9.get(), pin9.get(), state9.get()],
                                    [11, name10.get(), pin10.get(), state10.get()],
                                    [12, name11.get(), pin11.get(), state11.get()]]}
        saveToFile()
    if addPin.counter == 13:
        addPin.combined = {"pins": [[1, name0.get(), pin0.get(), state0.get()],
                                    [2, name1.get(), pin1.get(), state1.get()],
                                    [3, name2.get(), pin2.get(), state2.get()],
                                    [4, name3.get(), pin3.get(), state3.get()],
                                    [5, name4.get(), pin4.get(), state4.get()],
                                    [6, name5.get(), pin5.get(), state5.get()],
                                    [7, name6.get(), pin6.get(), state6.get()],
                                    [8, name7.get(), pin7.get(), state7.get()],
                                    [9, name8.get(), pin8.get(), state8.get()],
                                    [10, name9.get(), pin9.get(), state9.get()],
                                    [11, name10.get(), pin10.get(), state10.get()],
                                    [12, name11.get(), pin11.get(), state11.get()],
                                    [13, name12.get(), pin12.get(), state12.get()]]}
        saveToFile()
    if addPin.counter == 14:
        addPin.combined = {"pins": [[1, name0.get(), pin0.get(), state0.get()],
                                    [2, name1.get(), pin1.get(), state1.get()],
                                    [3, name2.get(), pin2.get(), state2.get()],
                                    [4, name3.get(), pin3.get(), state3.get()],
                                    [5, name4.get(), pin4.get(), state4.get()],
                                    [6, name5.get(), pin5.get(), state5.get()],
                                    [7, name6.get(), pin6.get(), state6.get()],
                                    [8, name7.get(), pin7.get(), state7.get()],
                                    [9, name8.get(), pin8.get(), state8.get()],
                                    [10, name9.get(), pin9.get(), state9.get()],
                                    [11, name10.get(), pin10.get(), state10.get()],
                                    [12, name11.get(), pin11.get(), state11.get()],
                                    [13, name12.get(), pin12.get(), state12.get()],
                                    [14, name13.get(), pin13.get(), state13.get()]]}
        saveToFile()
    if addPin.counter == 15:
        addPin.combined = {"pins": [[1, name0.get(), pin0.get(), state0.get()],
                                    [2, name1.get(), pin1.get(), state1.get()],
                                    [3, name2.get(), pin2.get(), state2.get()],
                                    [4, name3.get(), pin3.get(), state3.get()],
                                    [5, name4.get(), pin4.get(), state4.get()],
                                    [6, name5.get(), pin5.get(), state5.get()],
                                    [7, name6.get(), pin6.get(), state6.get()],
                                    [8, name7.get(), pin7.get(), state7.get()],
                                    [9, name8.get(), pin8.get(), state8.get()],
                                    [10, name9.get(), pin9.get(), state9.get()],
                                    [11, name10.get(), pin10.get(), state10.get()],
                                    [12, name11.get(), pin11.get(), state11.get()],
                                    [13, name12.get(), pin12.get(), state12.get()],
                                    [14, name13.get(), pin13.get(), state13.get()],
                                    [15, name14.get(), pin14.get(), state14.get()]]}
        saveToFile()
    if addPin.counter == 16:
        addPin.combined = {"pins": [[1, name0.get(), pin0.get(), state0.get()],
                                    [2, name1.get(), pin1.get(), state1.get()],
                                    [3, name2.get(), pin2.get(), state2.get()],
                                    [4, name3.get(), pin3.get(), state3.get()],
                                    [5, name4.get(), pin4.get(), state4.get()],
                                    [6, name5.get(), pin5.get(), state5.get()],
                                    [7, name6.get(), pin6.get(), state6.get()],
                                    [8, name7.get(), pin7.get(), state7.get()],
                                    [9, name8.get(), pin8.get(), state8.get()],
                                    [10, name9.get(), pin9.get(), state9.get()],
                                    [11, name10.get(), pin10.get(), state10.get()],
                                    [12, name11.get(), pin11.get(), state11.get()],
                                    [13, name12.get(), pin12.get(), state12.get()],
                                    [14, name13.get(), pin13.get(), state13.get()],
                                    [15, name14.get(), pin14.get(), state14.get()],
                                    [16, name15.get(), pin15.get(), state15.get()]]}
        saveToFile()
    if addPin.counter == 17:
        addPin.combined = {"pins": [[1, name0.get(), pin0.get(), state0.get()],
                                    [2, name1.get(), pin1.get(), state1.get()],
                                    [3, name2.get(), pin2.get(), state2.get()],
                                    [4, name3.get(), pin3.get(), state3.get()],
                                    [5, name4.get(), pin4.get(), state4.get()],
                                    [6, name5.get(), pin5.get(), state5.get()],
                                    [7, name6.get(), pin6.get(), state6.get()],
                                    [8, name7.get(), pin7.get(), state7.get()],
                                    [9, name8.get(), pin8.get(), state8.get()],
                                    [10, name9.get(), pin9.get(), state9.get()],
                                    [11, name10.get(), pin10.get(), state10.get()],
                                    [12, name11.get(), pin11.get(), state11.get()],
                                    [13, name12.get(), pin12.get(), state12.get()],
                                    [14, name13.get(), pin13.get(), state13.get()],
                                    [15, name14.get(), pin14.get(), state14.get()],
                                    [16, name15.get(), pin15.get(), state15.get()],
                                    [17, name16.get(), pin16.get(), state16.get()]]}
        saveToFile()
    if addPin.counter == 18:
        addPin.combined = {"pins": [[1, name0.get(), pin0.get(), state0.get()],
                                    [2, name1.get(), pin1.get(), state1.get()],
                                    [3, name2.get(), pin2.get(), state2.get()],
                                    [4, name3.get(), pin3.get(), state3.get()],
                                    [5, name4.get(), pin4.get(), state4.get()],
                                    [6, name5.get(), pin5.get(), state5.get()],
                                    [7, name6.get(), pin6.get(), state6.get()],
                                    [8, name7.get(), pin7.get(), state7.get()],
                                    [9, name8.get(), pin8.get(), state8.get()],
                                    [10, name9.get(), pin9.get(), state9.get()],
                                    [11, name10.get(), pin10.get(), state10.get()],
                                    [12, name11.get(), pin11.get(), state11.get()],
                                    [13, name12.get(), pin12.get(), state12.get()],
                                    [14, name13.get(), pin13.get(), state13.get()],
                                    [15, name14.get(), pin14.get(), state14.get()],
                                    [16, name15.get(), pin15.get(), state15.get()],
                                    [17, name16.get(), pin16.get(), state16.get()],
                                    [18, name17.get(), pin17.get(), state17.get()]]}
        saveToFile()


def loadCells():
    addPin.current_row = current_row
    # print(addPin.current_row)
    if addPin.current_row == 1:
        addPin.counter = 0
        addPin()

        name0.insert(0, my_pins["pins"][0][1])
        pin0.insert(0, my_pins["pins"][0][2])
        state0.insert(0, my_pins["pins"][0][3])

        addPin.counter = 1
        addPin()

        name0.insert(0, "")
        pin0.insert(0, "")
        state0.insert(0, "")

    if addPin.current_row == 2:
        addPin.counter = 0
        addPin()

        name0.insert(0, my_pins["pins"][0][1])
        pin0.insert(0, my_pins["pins"][0][2])
        state0.insert(0, my_pins["pins"][0][3])

        addPin.counter = 1
        addPin()

        name1.insert(0, my_pins["pins"][1][1])
        pin1.insert(0, my_pins["pins"][1][2])
        state1.insert(0, my_pins["pins"][1][3])

        addPin.counter = 2
        addPin()

        name1.insert(0, "")
        pin1.insert(0, "")
        state1.insert(0, "")

    if addPin.current_row == 3:
        addPin.counter = 0
        addPin()

        name0.insert(0, my_pins["pins"][0][1])
        pin0.insert(0, my_pins["pins"][0][2])
        state0.insert(0, my_pins["pins"][0][3])

        addPin.counter = 1
        addPin()

        name1.insert(0, my_pins["pins"][1][1])
        pin1.insert(0, my_pins["pins"][1][2])
        state1.insert(0, my_pins["pins"][1][3])

        addPin.counter = 2
        addPin()

        name2.insert(0, my_pins["pins"][2][1])
        pin2.insert(0, my_pins["pins"][2][2])
        state2.insert(0, my_pins["pins"][2][3])

        addPin.counter = 3
        addPin()

        name2.insert(0, "")
        pin2.insert(0, "")
        state2.insert(0, "")

    if addPin.current_row == 4:
        addPin.counter = 0
        addPin()

        name0.insert(0, my_pins["pins"][0][1])
        pin0.insert(0, my_pins["pins"][0][2])
        state0.insert(0, my_pins["pins"][0][3])

        addPin.counter = 1
        addPin()

        name1.insert(0, my_pins["pins"][1][1])
        pin1.insert(0, my_pins["pins"][1][2])
        state1.insert(0, my_pins["pins"][1][3])

        addPin.counter = 2
        addPin()

        name2.insert(0, my_pins["pins"][2][1])
        pin2.insert(0, my_pins["pins"][2][2])
        state2.insert(0, my_pins["pins"][2][3])

        addPin.counter = 3
        addPin()

        name3.insert(0, my_pins["pins"][3][1])
        pin3.insert(0, my_pins["pins"][3][2])
        state3.insert(0, my_pins["pins"][3][3])

        addPin.counter = 4
        addPin()

        name3.insert(0, "")
        pin3.insert(0, "")
        state3.insert(0, "")

    if addPin.current_row == 5:
        addPin.counter = 0
        addPin()

        name0.insert(0, my_pins["pins"][0][1])
        pin0.insert(0, my_pins["pins"][0][2])
        state0.insert(0, my_pins["pins"][0][3])

        addPin.counter = 1
        addPin()

        name1.insert(0, my_pins["pins"][1][1])
        pin1.insert(0, my_pins["pins"][1][2])
        state1.insert(0, my_pins["pins"][1][3])

        addPin.counter = 2
        addPin()

        name2.insert(0, my_pins["pins"][2][1])
        pin2.insert(0, my_pins["pins"][2][2])
        state2.insert(0, my_pins["pins"][2][3])

        addPin.counter = 3
        addPin()

        name3.insert(0, my_pins["pins"][3][1])
        pin3.insert(0, my_pins["pins"][3][2])
        state3.insert(0, my_pins["pins"][3][3])

        addPin.counter = 4
        addPin()

        name4.insert(0, my_pins["pins"][4][1])
        pin4.insert(0, my_pins["pins"][4][2])
        state4.insert(0, my_pins["pins"][4][3])

        addPin.counter = 5
        addPin()

        name4.insert(0, "")
        pin4.insert(0, "")
        state4.insert(0, "")

    if addPin.current_row == 6:
        addPin.counter = 0
        addPin()

        name0.insert(0, my_pins["pins"][0][1])
        pin0.insert(0, my_pins["pins"][0][2])
        state0.insert(0, my_pins["pins"][0][3])

        addPin.counter = 1
        addPin()

        name1.insert(0, my_pins["pins"][1][1])
        pin1.insert(0, my_pins["pins"][1][2])
        state1.insert(0, my_pins["pins"][1][3])

        addPin.counter = 2
        addPin()

        name2.insert(0, my_pins["pins"][2][1])
        pin2.insert(0, my_pins["pins"][2][2])
        state2.insert(0, my_pins["pins"][2][3])

        addPin.counter = 3
        addPin()

        name3.insert(0, my_pins["pins"][3][1])
        pin3.insert(0, my_pins["pins"][3][2])
        state3.insert(0, my_pins["pins"][3][3])

        addPin.counter = 4
        addPin()

        name4.insert(0, my_pins["pins"][4][1])
        pin4.insert(0, my_pins["pins"][4][2])
        state4.insert(0, my_pins["pins"][4][3])

        addPin.counter = 5
        addPin()

        name5.insert(0, my_pins["pins"][5][1])
        pin5.insert(0, my_pins["pins"][5][2])
        state5.insert(0, my_pins["pins"][5][3])

        addPin.counter = 6
        addPin()

        name5.insert(0, "")
        pin5.insert(0, "")
        state5.insert(0, "")

    if addPin.current_row == 7:
        addPin.counter = 0
        addPin()

        name0.insert(0, my_pins["pins"][0][1])
        pin0.insert(0, my_pins["pins"][0][2])
        state0.insert(0, my_pins["pins"][0][3])

        addPin.counter = 1
        addPin()

        name1.insert(0, my_pins["pins"][1][1])
        pin1.insert(0, my_pins["pins"][1][2])
        state1.insert(0, my_pins["pins"][1][3])

        addPin.counter = 2
        addPin()

        name2.insert(0, my_pins["pins"][2][1])
        pin2.insert(0, my_pins["pins"][2][2])
        state2.insert(0, my_pins["pins"][2][3])

        addPin.counter = 3
        addPin()

        name3.insert(0, my_pins["pins"][3][1])
        pin3.insert(0, my_pins["pins"][3][2])
        state3.insert(0, my_pins["pins"][3][3])

        addPin.counter = 4
        addPin()

        name4.insert(0, my_pins["pins"][4][1])
        pin4.insert(0, my_pins["pins"][4][2])
        state4.insert(0, my_pins["pins"][4][3])

        addPin.counter = 5
        addPin()

        name5.insert(0, my_pins["pins"][5][1])
        pin5.insert(0, my_pins["pins"][5][2])
        state5.insert(0, my_pins["pins"][5][3])

        addPin.counter = 6
        addPin()

        name6.insert(0, my_pins["pins"][6][1])
        pin6.insert(0, my_pins["pins"][6][2])
        state6.insert(0, my_pins["pins"][6][3])

        addPin.counter = 7
        addPin()

        name6.insert(0, "")
        pin6.insert(0, "")
        state6.insert(0, "")

    if addPin.current_row == 8:
        addPin.counter = 0
        addPin()

        name0.insert(0, my_pins["pins"][0][1])
        pin0.insert(0, my_pins["pins"][0][2])
        state0.insert(0, my_pins["pins"][0][3])

        addPin.counter = 1
        addPin()

        name1.insert(0, my_pins["pins"][1][1])
        pin1.insert(0, my_pins["pins"][1][2])
        state1.insert(0, my_pins["pins"][1][3])

        addPin.counter = 2
        addPin()

        name2.insert(0, my_pins["pins"][2][1])
        pin2.insert(0, my_pins["pins"][2][2])
        state2.insert(0, my_pins["pins"][2][3])

        addPin.counter = 3
        addPin()

        name3.insert(0, my_pins["pins"][3][1])
        pin3.insert(0, my_pins["pins"][3][2])
        state3.insert(0, my_pins["pins"][3][3])

        addPin.counter = 4
        addPin()

        name4.insert(0, my_pins["pins"][4][1])
        pin4.insert(0, my_pins["pins"][4][2])
        state4.insert(0, my_pins["pins"][4][3])

        addPin.counter = 5
        addPin()

        name5.insert(0, my_pins["pins"][5][1])
        pin5.insert(0, my_pins["pins"][5][2])
        state5.insert(0, my_pins["pins"][5][3])

        addPin.counter = 6
        addPin()

        name6.insert(0, my_pins["pins"][6][1])
        pin6.insert(0, my_pins["pins"][6][2])
        state6.insert(0, my_pins["pins"][6][3])

        addPin.counter = 7
        addPin()

        name7.insert(0, my_pins["pins"][7][1])
        pin7.insert(0, my_pins["pins"][7][2])
        state7.insert(0, my_pins["pins"][7][3])

        addPin.counter = 8
        addPin()

        name7.insert(0, "")
        pin7.insert(0, "")
        state7.insert(0, "")

    if addPin.current_row == 9:
        addPin.counter = 0
        addPin()

        name0.insert(0, my_pins["pins"][0][1])
        pin0.insert(0, my_pins["pins"][0][2])
        state0.insert(0, my_pins["pins"][0][3])

        addPin.counter = 1
        addPin()

        name1.insert(0, my_pins["pins"][1][1])
        pin1.insert(0, my_pins["pins"][1][2])
        state1.insert(0, my_pins["pins"][1][3])

        addPin.counter = 2
        addPin()

        name2.insert(0, my_pins["pins"][2][1])
        pin2.insert(0, my_pins["pins"][2][2])
        state2.insert(0, my_pins["pins"][2][3])

        addPin.counter = 3
        addPin()

        name3.insert(0, my_pins["pins"][3][1])
        pin3.insert(0, my_pins["pins"][3][2])
        state3.insert(0, my_pins["pins"][3][3])

        addPin.counter = 4
        addPin()

        name4.insert(0, my_pins["pins"][4][1])
        pin4.insert(0, my_pins["pins"][4][2])
        state4.insert(0, my_pins["pins"][4][3])

        addPin.counter = 5
        addPin()

        name5.insert(0, my_pins["pins"][5][1])
        pin5.insert(0, my_pins["pins"][5][2])
        state5.insert(0, my_pins["pins"][5][3])

        addPin.counter = 6
        addPin()

        name6.insert(0, my_pins["pins"][6][1])
        pin6.insert(0, my_pins["pins"][6][2])
        state6.insert(0, my_pins["pins"][6][3])

        addPin.counter = 7
        addPin()

        name7.insert(0, my_pins["pins"][7][1])
        pin7.insert(0, my_pins["pins"][7][2])
        state7.insert(0, my_pins["pins"][7][3])

        addPin.counter = 8
        addPin()

        name8.insert(0, my_pins["pins"][8][1])
        pin8.insert(0, my_pins["pins"][8][2])
        state8.insert(0, my_pins["pins"][8][3])

        addPin.counter = 9
        addPin()

        name8.insert(0, "")
        pin8.insert(0, "")
        state8.insert(0, "")

    if addPin.current_row == 10:
        addPin.counter = 0
        addPin()

        name0.insert(0, my_pins["pins"][0][1])
        pin0.insert(0, my_pins["pins"][0][2])
        state0.insert(0, my_pins["pins"][0][3])

        addPin.counter = 1
        addPin()

        name1.insert(0, my_pins["pins"][1][1])
        pin1.insert(0, my_pins["pins"][1][2])
        state1.insert(0, my_pins["pins"][1][3])

        addPin.counter = 2
        addPin()

        name2.insert(0, my_pins["pins"][2][1])
        pin2.insert(0, my_pins["pins"][2][2])
        state2.insert(0, my_pins["pins"][2][3])

        addPin.counter = 3
        addPin()

        name3.insert(0, my_pins["pins"][3][1])
        pin3.insert(0, my_pins["pins"][3][2])
        state3.insert(0, my_pins["pins"][3][3])

        addPin.counter = 4
        addPin()

        name4.insert(0, my_pins["pins"][4][1])
        pin4.insert(0, my_pins["pins"][4][2])
        state4.insert(0, my_pins["pins"][4][3])

        addPin.counter = 5
        addPin()

        name5.insert(0, my_pins["pins"][5][1])
        pin5.insert(0, my_pins["pins"][5][2])
        state5.insert(0, my_pins["pins"][5][3])

        addPin.counter = 6
        addPin()

        name6.insert(0, my_pins["pins"][6][1])
        pin6.insert(0, my_pins["pins"][6][2])
        state6.insert(0, my_pins["pins"][6][3])

        addPin.counter = 7
        addPin()

        name7.insert(0, my_pins["pins"][7][1])
        pin7.insert(0, my_pins["pins"][7][2])
        state7.insert(0, my_pins["pins"][7][3])

        addPin.counter = 8
        addPin()

        name8.insert(0, my_pins["pins"][8][1])
        pin8.insert(0, my_pins["pins"][8][2])
        state8.insert(0, my_pins["pins"][8][3])

        addPin.counter = 9
        addPin()

        name9.insert(0, my_pins["pins"][9][1])
        pin9.insert(0, my_pins["pins"][9][2])
        state9.insert(0, my_pins["pins"][9][3])

        addPin.counter = 10
        addPin()

        name9.insert(0, "")
        pin9.insert(0, "")
        state9.insert(0, "")

    if addPin.current_row == 11:
        addPin.counter = 0
        addPin()

        name0.insert(0, my_pins["pins"][0][1])
        pin0.insert(0, my_pins["pins"][0][2])
        state0.insert(0, my_pins["pins"][0][3])

        addPin.counter = 1
        addPin()

        name1.insert(0, my_pins["pins"][1][1])
        pin1.insert(0, my_pins["pins"][1][2])
        state1.insert(0, my_pins["pins"][1][3])

        addPin.counter = 2
        addPin()

        name2.insert(0, my_pins["pins"][2][1])
        pin2.insert(0, my_pins["pins"][2][2])
        state2.insert(0, my_pins["pins"][2][3])

        addPin.counter = 3
        addPin()

        name3.insert(0, my_pins["pins"][3][1])
        pin3.insert(0, my_pins["pins"][3][2])
        state3.insert(0, my_pins["pins"][3][3])

        addPin.counter = 4
        addPin()

        name4.insert(0, my_pins["pins"][4][1])
        pin4.insert(0, my_pins["pins"][4][2])
        state4.insert(0, my_pins["pins"][4][3])

        addPin.counter = 5
        addPin()

        name5.insert(0, my_pins["pins"][5][1])
        pin5.insert(0, my_pins["pins"][5][2])
        state5.insert(0, my_pins["pins"][5][3])

        addPin.counter = 6
        addPin()

        name6.insert(0, my_pins["pins"][6][1])
        pin6.insert(0, my_pins["pins"][6][2])
        state6.insert(0, my_pins["pins"][6][3])

        addPin.counter = 7
        addPin()

        name7.insert(0, my_pins["pins"][7][1])
        pin7.insert(0, my_pins["pins"][7][2])
        state7.insert(0, my_pins["pins"][7][3])

        addPin.counter = 8
        addPin()

        name8.insert(0, my_pins["pins"][8][1])
        pin8.insert(0, my_pins["pins"][8][2])
        state8.insert(0, my_pins["pins"][8][3])

        addPin.counter = 9
        addPin()

        name9.insert(0, my_pins["pins"][9][1])
        pin9.insert(0, my_pins["pins"][9][2])
        state9.insert(0, my_pins["pins"][9][3])

        addPin.counter = 10
        addPin()

        name10.insert(0, my_pins["pins"][10][1])
        pin10.insert(0, my_pins["pins"][10][2])
        state10.insert(0, my_pins["pins"][10][3])

        addPin.counter = 11
        addPin()

        name10.insert(0, "")
        pin10.insert(0, "")
        state10.insert(0, "")

    if addPin.current_row == 12:
        addPin.counter = 0
        addPin()

        name0.insert(0, my_pins["pins"][0][1])
        pin0.insert(0, my_pins["pins"][0][2])
        state0.insert(0, my_pins["pins"][0][3])

        addPin.counter = 1
        addPin()

        name1.insert(0, my_pins["pins"][1][1])
        pin1.insert(0, my_pins["pins"][1][2])
        state1.insert(0, my_pins["pins"][1][3])

        addPin.counter = 2
        addPin()

        name2.insert(0, my_pins["pins"][2][1])
        pin2.insert(0, my_pins["pins"][2][2])
        state2.insert(0, my_pins["pins"][2][3])

        addPin.counter = 3
        addPin()

        name3.insert(0, my_pins["pins"][3][1])
        pin3.insert(0, my_pins["pins"][3][2])
        state3.insert(0, my_pins["pins"][3][3])

        addPin.counter = 4
        addPin()

        name4.insert(0, my_pins["pins"][4][1])
        pin4.insert(0, my_pins["pins"][4][2])
        state4.insert(0, my_pins["pins"][4][3])

        addPin.counter = 5
        addPin()

        name5.insert(0, my_pins["pins"][5][1])
        pin5.insert(0, my_pins["pins"][5][2])
        state5.insert(0, my_pins["pins"][5][3])

        addPin.counter = 6
        addPin()

        name6.insert(0, my_pins["pins"][6][1])
        pin6.insert(0, my_pins["pins"][6][2])
        state6.insert(0, my_pins["pins"][6][3])

        addPin.counter = 7
        addPin()

        name7.insert(0, my_pins["pins"][7][1])
        pin7.insert(0, my_pins["pins"][7][2])
        state7.insert(0, my_pins["pins"][7][3])

        addPin.counter = 8
        addPin()

        name8.insert(0, my_pins["pins"][8][1])
        pin8.insert(0, my_pins["pins"][8][2])
        state8.insert(0, my_pins["pins"][8][3])

        addPin.counter = 9
        addPin()

        name9.insert(0, my_pins["pins"][9][1])
        pin9.insert(0, my_pins["pins"][9][2])
        state9.insert(0, my_pins["pins"][9][3])

        addPin.counter = 10
        addPin()

        name10.insert(0, my_pins["pins"][10][1])
        pin10.insert(0, my_pins["pins"][10][2])
        state10.insert(0, my_pins["pins"][10][3])

        addPin.counter = 11
        addPin()

        name11.insert(0, my_pins["pins"][11][1])
        pin11.insert(0, my_pins["pins"][11][2])
        state11.insert(0, my_pins["pins"][11][3])

        addPin.counter = 12
        addPin()

        name11.insert(0, "")
        pin11.insert(0, "")
        state11.insert(0, "")

    if addPin.current_row == 13:
        addPin.counter = 0
        addPin()

        name0.insert(0, my_pins["pins"][0][1])
        pin0.insert(0, my_pins["pins"][0][2])
        state0.insert(0, my_pins["pins"][0][3])

        addPin.counter = 1
        addPin()

        name1.insert(0, my_pins["pins"][1][1])
        pin1.insert(0, my_pins["pins"][1][2])
        state1.insert(0, my_pins["pins"][1][3])

        addPin.counter = 2
        addPin()

        name2.insert(0, my_pins["pins"][2][1])
        pin2.insert(0, my_pins["pins"][2][2])
        state2.insert(0, my_pins["pins"][2][3])

        addPin.counter = 3
        addPin()

        name3.insert(0, my_pins["pins"][3][1])
        pin3.insert(0, my_pins["pins"][3][2])
        state3.insert(0, my_pins["pins"][3][3])

        addPin.counter = 4
        addPin()

        name4.insert(0, my_pins["pins"][4][1])
        pin4.insert(0, my_pins["pins"][4][2])
        state4.insert(0, my_pins["pins"][4][3])

        addPin.counter = 5
        addPin()

        name5.insert(0, my_pins["pins"][5][1])
        pin5.insert(0, my_pins["pins"][5][2])
        state5.insert(0, my_pins["pins"][5][3])

        addPin.counter = 6
        addPin()

        name6.insert(0, my_pins["pins"][6][1])
        pin6.insert(0, my_pins["pins"][6][2])
        state6.insert(0, my_pins["pins"][6][3])

        addPin.counter = 7
        addPin()

        name7.insert(0, my_pins["pins"][7][1])
        pin7.insert(0, my_pins["pins"][7][2])
        state7.insert(0, my_pins["pins"][7][3])

        addPin.counter = 8
        addPin()

        name8.insert(0, my_pins["pins"][8][1])
        pin8.insert(0, my_pins["pins"][8][2])
        state8.insert(0, my_pins["pins"][8][3])

        addPin.counter = 9
        addPin()

        name9.insert(0, my_pins["pins"][9][1])
        pin9.insert(0, my_pins["pins"][9][2])
        state9.insert(0, my_pins["pins"][9][3])

        addPin.counter = 10
        addPin()

        name10.insert(0, my_pins["pins"][10][1])
        pin10.insert(0, my_pins["pins"][10][2])
        state10.insert(0, my_pins["pins"][10][3])

        addPin.counter = 11
        addPin()

        name11.insert(0, my_pins["pins"][11][1])
        pin11.insert(0, my_pins["pins"][11][2])
        state11.insert(0, my_pins["pins"][11][3])

        addPin.counter = 12
        addPin()

        name12.insert(0, my_pins["pins"][12][1])
        pin12.insert(0, my_pins["pins"][12][2])
        state12.insert(0, my_pins["pins"][12][3])

        addPin.counter = 13
        addPin()

        name12.insert(0, "")
        pin12.insert(0, "")
        state12.insert(0, "")

    if addPin.current_row == 14:
        addPin.counter = 0
        addPin()

        name0.insert(0, my_pins["pins"][0][1])
        pin0.insert(0, my_pins["pins"][0][2])
        state0.insert(0, my_pins["pins"][0][3])

        addPin.counter = 1
        addPin()

        name1.insert(0, my_pins["pins"][1][1])
        pin1.insert(0, my_pins["pins"][1][2])
        state1.insert(0, my_pins["pins"][1][3])

        addPin.counter = 2
        addPin()

        name2.insert(0, my_pins["pins"][2][1])
        pin2.insert(0, my_pins["pins"][2][2])
        state2.insert(0, my_pins["pins"][2][3])

        addPin.counter = 3
        addPin()

        name3.insert(0, my_pins["pins"][3][1])
        pin3.insert(0, my_pins["pins"][3][2])
        state3.insert(0, my_pins["pins"][3][3])

        addPin.counter = 4
        addPin()

        name4.insert(0, my_pins["pins"][4][1])
        pin4.insert(0, my_pins["pins"][4][2])
        state4.insert(0, my_pins["pins"][4][3])

        addPin.counter = 5
        addPin()

        name5.insert(0, my_pins["pins"][5][1])
        pin5.insert(0, my_pins["pins"][5][2])
        state5.insert(0, my_pins["pins"][5][3])

        addPin.counter = 6
        addPin()

        name6.insert(0, my_pins["pins"][6][1])
        pin6.insert(0, my_pins["pins"][6][2])
        state6.insert(0, my_pins["pins"][6][3])

        addPin.counter = 7
        addPin()

        name7.insert(0, my_pins["pins"][7][1])
        pin7.insert(0, my_pins["pins"][7][2])
        state7.insert(0, my_pins["pins"][7][3])

        addPin.counter = 8
        addPin()

        name8.insert(0, my_pins["pins"][8][1])
        pin8.insert(0, my_pins["pins"][8][2])
        state8.insert(0, my_pins["pins"][8][3])

        addPin.counter = 9
        addPin()

        name9.insert(0, my_pins["pins"][9][1])
        pin9.insert(0, my_pins["pins"][9][2])
        state9.insert(0, my_pins["pins"][9][3])

        addPin.counter = 10
        addPin()

        name10.insert(0, my_pins["pins"][10][1])
        pin10.insert(0, my_pins["pins"][10][2])
        state10.insert(0, my_pins["pins"][10][3])

        addPin.counter = 11
        addPin()

        name11.insert(0, my_pins["pins"][11][1])
        pin11.insert(0, my_pins["pins"][11][2])
        state11.insert(0, my_pins["pins"][11][3])

        addPin.counter = 12
        addPin()

        name12.insert(0, my_pins["pins"][12][1])
        pin12.insert(0, my_pins["pins"][12][2])
        state12.insert(0, my_pins["pins"][12][3])

        addPin.counter = 13
        addPin()

        name13.insert(0, my_pins["pins"][13][1])
        pin13.insert(0, my_pins["pins"][13][2])
        state13.insert(0, my_pins["pins"][13][3])

        addPin.counter = 14
        addPin()

        name13.insert(0, "")
        pin13.insert(0, "")
        state13.insert(0, "")

    if addPin.current_row == 15:
        addPin.counter = 0
        addPin()

        name0.insert(0, my_pins["pins"][0][1])
        pin0.insert(0, my_pins["pins"][0][2])
        state0.insert(0, my_pins["pins"][0][3])

        addPin.counter = 1
        addPin()

        name1.insert(0, my_pins["pins"][1][1])
        pin1.insert(0, my_pins["pins"][1][2])
        state1.insert(0, my_pins["pins"][1][3])

        addPin.counter = 2
        addPin()

        name2.insert(0, my_pins["pins"][2][1])
        pin2.insert(0, my_pins["pins"][2][2])
        state2.insert(0, my_pins["pins"][2][3])

        addPin.counter = 3
        addPin()

        name3.insert(0, my_pins["pins"][3][1])
        pin3.insert(0, my_pins["pins"][3][2])
        state3.insert(0, my_pins["pins"][3][3])

        addPin.counter = 4
        addPin()

        name4.insert(0, my_pins["pins"][4][1])
        pin4.insert(0, my_pins["pins"][4][2])
        state4.insert(0, my_pins["pins"][4][3])

        addPin.counter = 5
        addPin()

        name5.insert(0, my_pins["pins"][5][1])
        pin5.insert(0, my_pins["pins"][5][2])
        state5.insert(0, my_pins["pins"][5][3])

        addPin.counter = 6
        addPin()

        name6.insert(0, my_pins["pins"][6][1])
        pin6.insert(0, my_pins["pins"][6][2])
        state6.insert(0, my_pins["pins"][6][3])

        addPin.counter = 7
        addPin()

        name7.insert(0, my_pins["pins"][7][1])
        pin7.insert(0, my_pins["pins"][7][2])
        state7.insert(0, my_pins["pins"][7][3])

        addPin.counter = 8
        addPin()

        name8.insert(0, my_pins["pins"][8][1])
        pin8.insert(0, my_pins["pins"][8][2])
        state8.insert(0, my_pins["pins"][8][3])

        addPin.counter = 9
        addPin()

        name9.insert(0, my_pins["pins"][9][1])
        pin9.insert(0, my_pins["pins"][9][2])
        state9.insert(0, my_pins["pins"][9][3])

        addPin.counter = 10
        addPin()

        name10.insert(0, my_pins["pins"][10][1])
        pin10.insert(0, my_pins["pins"][10][2])
        state10.insert(0, my_pins["pins"][10][3])

        addPin.counter = 11
        addPin()

        name11.insert(0, my_pins["pins"][11][1])
        pin11.insert(0, my_pins["pins"][11][2])
        state11.insert(0, my_pins["pins"][11][3])

        addPin.counter = 12
        addPin()

        name12.insert(0, my_pins["pins"][12][1])
        pin12.insert(0, my_pins["pins"][12][2])
        state12.insert(0, my_pins["pins"][12][3])

        addPin.counter = 13
        addPin()

        name13.insert(0, my_pins["pins"][13][1])
        pin13.insert(0, my_pins["pins"][13][2])
        state13.insert(0, my_pins["pins"][13][3])

        addPin.counter = 14
        addPin()

        name14.insert(0, my_pins["pins"][14][1])
        pin14.insert(0, my_pins["pins"][14][2])
        state14.insert(0, my_pins["pins"][14][3])

        addPin.counter = 15
        addPin()

        name14.insert(0, "")
        pin14.insert(0, "")
        state14.insert(0, "")

    if addPin.current_row == 16:
        addPin.counter = 0
        addPin()

        name0.insert(0, my_pins["pins"][0][1])
        pin0.insert(0, my_pins["pins"][0][2])
        state0.insert(0, my_pins["pins"][0][3])

        addPin.counter = 1
        addPin()

        name1.insert(0, my_pins["pins"][1][1])
        pin1.insert(0, my_pins["pins"][1][2])
        state1.insert(0, my_pins["pins"][1][3])

        addPin.counter = 2
        addPin()

        name2.insert(0, my_pins["pins"][2][1])
        pin2.insert(0, my_pins["pins"][2][2])
        state2.insert(0, my_pins["pins"][2][3])

        addPin.counter = 3
        addPin()

        name3.insert(0, my_pins["pins"][3][1])
        pin3.insert(0, my_pins["pins"][3][2])
        state3.insert(0, my_pins["pins"][3][3])

        addPin.counter = 4
        addPin()

        name4.insert(0, my_pins["pins"][4][1])
        pin4.insert(0, my_pins["pins"][4][2])
        state4.insert(0, my_pins["pins"][4][3])

        addPin.counter = 5
        addPin()

        name5.insert(0, my_pins["pins"][5][1])
        pin5.insert(0, my_pins["pins"][5][2])
        state5.insert(0, my_pins["pins"][5][3])

        addPin.counter = 6
        addPin()

        name6.insert(0, my_pins["pins"][6][1])
        pin6.insert(0, my_pins["pins"][6][2])
        state6.insert(0, my_pins["pins"][6][3])

        addPin.counter = 7
        addPin()

        name7.insert(0, my_pins["pins"][7][1])
        pin7.insert(0, my_pins["pins"][7][2])
        state7.insert(0, my_pins["pins"][7][3])

        addPin.counter = 8
        addPin()

        name8.insert(0, my_pins["pins"][8][1])
        pin8.insert(0, my_pins["pins"][8][2])
        state8.insert(0, my_pins["pins"][8][3])

        addPin.counter = 9
        addPin()

        name9.insert(0, my_pins["pins"][9][1])
        pin9.insert(0, my_pins["pins"][9][2])
        state9.insert(0, my_pins["pins"][9][3])

        addPin.counter = 10
        addPin()

        name10.insert(0, my_pins["pins"][10][1])
        pin10.insert(0, my_pins["pins"][10][2])
        state10.insert(0, my_pins["pins"][10][3])

        addPin.counter = 11
        addPin()

        name11.insert(0, my_pins["pins"][11][1])
        pin11.insert(0, my_pins["pins"][11][2])
        state11.insert(0, my_pins["pins"][11][3])

        addPin.counter = 12
        addPin()

        name12.insert(0, my_pins["pins"][12][1])
        pin12.insert(0, my_pins["pins"][12][2])
        state12.insert(0, my_pins["pins"][12][3])

        addPin.counter = 13
        addPin()

        name13.insert(0, my_pins["pins"][13][1])
        pin13.insert(0, my_pins["pins"][13][2])
        state13.insert(0, my_pins["pins"][13][3])

        addPin.counter = 14
        addPin()

        name14.insert(0, my_pins["pins"][14][1])
        pin14.insert(0, my_pins["pins"][14][2])
        state14.insert(0, my_pins["pins"][14][3])

        addPin.counter = 15
        addPin()

        name15.insert(0, my_pins["pins"][15][1])
        pin15.insert(0, my_pins["pins"][15][2])
        state15.insert(0, my_pins["pins"][15][3])

        addPin.counter = 16
        addPin()

        name15.insert(0, "")
        pin15.insert(0, "")
        state15.insert(0, "")

    if addPin.current_row == 17:
        addPin.counter = 0
        addPin()

        name0.insert(0, my_pins["pins"][0][1])
        pin0.insert(0, my_pins["pins"][0][2])
        state0.insert(0, my_pins["pins"][0][3])

        addPin.counter = 1
        addPin()

        name1.insert(0, my_pins["pins"][1][1])
        pin1.insert(0, my_pins["pins"][1][2])
        state1.insert(0, my_pins["pins"][1][3])

        addPin.counter = 2
        addPin()

        name2.insert(0, my_pins["pins"][2][1])
        pin2.insert(0, my_pins["pins"][2][2])
        state2.insert(0, my_pins["pins"][2][3])

        addPin.counter = 3
        addPin()

        name3.insert(0, my_pins["pins"][3][1])
        pin3.insert(0, my_pins["pins"][3][2])
        state3.insert(0, my_pins["pins"][3][3])

        addPin.counter = 4
        addPin()

        name4.insert(0, my_pins["pins"][4][1])
        pin4.insert(0, my_pins["pins"][4][2])
        state4.insert(0, my_pins["pins"][4][3])

        addPin.counter = 5
        addPin()

        name5.insert(0, my_pins["pins"][5][1])
        pin5.insert(0, my_pins["pins"][5][2])
        state5.insert(0, my_pins["pins"][5][3])

        addPin.counter = 6
        addPin()

        name6.insert(0, my_pins["pins"][6][1])
        pin6.insert(0, my_pins["pins"][6][2])
        state6.insert(0, my_pins["pins"][6][3])

        addPin.counter = 7
        addPin()

        name7.insert(0, my_pins["pins"][7][1])
        pin7.insert(0, my_pins["pins"][7][2])
        state7.insert(0, my_pins["pins"][7][3])

        addPin.counter = 8
        addPin()

        name8.insert(0, my_pins["pins"][8][1])
        pin8.insert(0, my_pins["pins"][8][2])
        state8.insert(0, my_pins["pins"][8][3])

        addPin.counter = 9
        addPin()

        name9.insert(0, my_pins["pins"][9][1])
        pin9.insert(0, my_pins["pins"][9][2])
        state9.insert(0, my_pins["pins"][9][3])

        addPin.counter = 10
        addPin()

        name10.insert(0, my_pins["pins"][10][1])
        pin10.insert(0, my_pins["pins"][10][2])
        state10.insert(0, my_pins["pins"][10][3])

        addPin.counter = 11
        addPin()

        name11.insert(0, my_pins["pins"][11][1])
        pin11.insert(0, my_pins["pins"][11][2])
        state11.insert(0, my_pins["pins"][11][3])

        addPin.counter = 12
        addPin()

        name12.insert(0, my_pins["pins"][12][1])
        pin12.insert(0, my_pins["pins"][12][2])
        state12.insert(0, my_pins["pins"][12][3])

        addPin.counter = 13
        addPin()

        name13.insert(0, my_pins["pins"][13][1])
        pin13.insert(0, my_pins["pins"][13][2])
        state13.insert(0, my_pins["pins"][13][3])

        addPin.counter = 14
        addPin()

        name14.insert(0, my_pins["pins"][14][1])
        pin14.insert(0, my_pins["pins"][14][2])
        state14.insert(0, my_pins["pins"][14][3])

        addPin.counter = 15
        addPin()

        name15.insert(0, my_pins["pins"][15][1])
        pin15.insert(0, my_pins["pins"][15][2])
        state15.insert(0, my_pins["pins"][15][3])

        addPin.counter = 16
        addPin()

        name16.insert(0, my_pins["pins"][16][1])
        pin16.insert(0, my_pins["pins"][16][2])
        state16.insert(0, my_pins["pins"][16][3])

        addPin.counter = 17
        addPin()

        name16.insert(0, "")
        pin16.insert(0, "")
        state16.insert(0, "")

    if addPin.current_row == 18:
        addPin.counter = 0
        addPin()

        name0.insert(0, my_pins["pins"][0][1])
        pin0.insert(0, my_pins["pins"][0][2])
        state0.insert(0, my_pins["pins"][0][3])

        addPin.counter = 1
        addPin()

        name1.insert(0, my_pins["pins"][1][1])
        pin1.insert(0, my_pins["pins"][1][2])
        state1.insert(0, my_pins["pins"][1][3])

        addPin.counter = 2
        addPin()

        name2.insert(0, my_pins["pins"][2][1])
        pin2.insert(0, my_pins["pins"][2][2])
        state2.insert(0, my_pins["pins"][2][3])

        addPin.counter = 3
        addPin()

        name3.insert(0, my_pins["pins"][3][1])
        pin3.insert(0, my_pins["pins"][3][2])
        state3.insert(0, my_pins["pins"][3][3])

        addPin.counter = 4
        addPin()

        name4.insert(0, my_pins["pins"][4][1])
        pin4.insert(0, my_pins["pins"][4][2])
        state4.insert(0, my_pins["pins"][4][3])

        addPin.counter = 5
        addPin()

        name5.insert(0, my_pins["pins"][5][1])
        pin5.insert(0, my_pins["pins"][5][2])
        state5.insert(0, my_pins["pins"][5][3])

        addPin.counter = 6
        addPin()

        name6.insert(0, my_pins["pins"][6][1])
        pin6.insert(0, my_pins["pins"][6][2])
        state6.insert(0, my_pins["pins"][6][3])

        addPin.counter = 7
        addPin()

        name7.insert(0, my_pins["pins"][7][1])
        pin7.insert(0, my_pins["pins"][7][2])
        state7.insert(0, my_pins["pins"][7][3])

        addPin.counter = 8
        addPin()

        name8.insert(0, my_pins["pins"][8][1])
        pin8.insert(0, my_pins["pins"][8][2])
        state8.insert(0, my_pins["pins"][8][3])

        addPin.counter = 9
        addPin()

        name9.insert(0, my_pins["pins"][9][1])
        pin9.insert(0, my_pins["pins"][9][2])
        state9.insert(0, my_pins["pins"][9][3])

        addPin.counter = 10
        addPin()

        name10.insert(0, my_pins["pins"][10][1])
        pin10.insert(0, my_pins["pins"][10][2])
        state10.insert(0, my_pins["pins"][10][3])

        addPin.counter = 11
        addPin()

        name11.insert(0, my_pins["pins"][11][1])
        pin11.insert(0, my_pins["pins"][11][2])
        state11.insert(0, my_pins["pins"][11][3])

        addPin.counter = 12
        addPin()

        name12.insert(0, my_pins["pins"][12][1])
        pin12.insert(0, my_pins["pins"][12][2])
        state12.insert(0, my_pins["pins"][12][3])

        addPin.counter = 13
        addPin()

        name13.insert(0, my_pins["pins"][13][1])
        pin13.insert(0, my_pins["pins"][13][2])
        state13.insert(0, my_pins["pins"][13][3])

        addPin.counter = 14
        addPin()

        name14.insert(0, my_pins["pins"][14][1])
        pin14.insert(0, my_pins["pins"][14][2])
        state14.insert(0, my_pins["pins"][14][3])

        addPin.counter = 15
        addPin()

        name15.insert(0, my_pins["pins"][15][1])
        pin15.insert(0, my_pins["pins"][15][2])
        state15.insert(0, my_pins["pins"][15][3])

        addPin.counter = 16
        addPin()

        name16.insert(0, my_pins["pins"][16][1])
        pin16.insert(0, my_pins["pins"][16][2])
        state16.insert(0, my_pins["pins"][16][3])

        addPin.counter = 17
        addPin()

        name17.insert(0, my_pins["pins"][17][1])
        pin17.insert(0, my_pins["pins"][17][2])
        state17.insert(0, my_pins["pins"][17][3])

        addPin.counter = 18
        addPin()

        name17.insert(0, "")
        pin17.insert(0, "")
        state17.insert(0, "")


def upload():
    saveData()
    loadDefaults()
    max_label = Label(root, text="***FAILED TO UPLOAD. PLEASE RETRY***", font=font1, bg="#2B2B2B",
                      fg="red")
    # sendToArduino()
    try:
        sendToArduino()
    except:
        max_label.config(text="***Invalid entry or empty field(delete empty row)***")
        max_label.place(x=(width / 2) - int((len(max_label.cget("text")) * 4)), y=height - 53)

    # disable upload to the web - remove return to enable this feature
    return
    try:
        session = ftplib.FTP('ftp-server-name', 'username', 'your-password')
        file = open('pins.json', 'rb')  # file to send
        session.storbinary('STOR htdocs/python-pins/pins.json', file)  # send the file
        file.close()  # close file and FTP
        session.quit()
        max_label.config(text="***SUCCESSFULLY UPLOADED***")
        max_label.place(x=(width / 2) - int((len(max_label.cget("text")) * 4)), y=height - 53)
    except:
        max_label.place(x=(width / 2) - int((len(max_label.cget("text")) * 4)), y=height - 53)

def disableCells(y):
    if y == 1:
        pin0["state"] = DISABLED
    if y == 2:
        pin0["state"] = DISABLED
        pin1["state"] = DISABLED
    if y == 3:
        pin0["state"] = DISABLED
        pin1["state"] = DISABLED
        pin2["state"] = DISABLED
    if y == 4:
        pin0["state"] = DISABLED
        pin1["state"] = DISABLED
        pin2["state"] = DISABLED
        pin3["state"] = DISABLED
    if y == 5:
        pin0["state"] = DISABLED
        pin1["state"] = DISABLED
        pin2["state"] = DISABLED
        pin3["state"] = DISABLED
        pin4["state"] = DISABLED
    if y == 6:
        pin0["state"] = DISABLED
        pin1["state"] = DISABLED
        pin2["state"] = DISABLED
        pin3["state"] = DISABLED
        pin4["state"] = DISABLED
        pin5["state"] = DISABLED
    if y == 7:
        pin0["state"] = DISABLED
        pin1["state"] = DISABLED
        pin2["state"] = DISABLED
        pin3["state"] = DISABLED
        pin4["state"] = DISABLED
        pin5["state"] = DISABLED
        pin6["state"] = DISABLED
    if y == 8:
        pin0["state"] = DISABLED
        pin1["state"] = DISABLED
        pin2["state"] = DISABLED
        pin3["state"] = DISABLED
        pin4["state"] = DISABLED
        pin5["state"] = DISABLED
        pin6["state"] = DISABLED
        pin7["state"] = DISABLED
    if y == 9:
        pin0["state"] = DISABLED
        pin1["state"] = DISABLED
        pin2["state"] = DISABLED
        pin3["state"] = DISABLED
        pin4["state"] = DISABLED
        pin5["state"] = DISABLED
        pin6["state"] = DISABLED
        pin7["state"] = DISABLED
        pin8["state"] = DISABLED
    if y == 10:
        pin0["state"] = DISABLED
        pin1["state"] = DISABLED
        pin2["state"] = DISABLED
        pin3["state"] = DISABLED
        pin4["state"] = DISABLED
        pin5["state"] = DISABLED
        pin6["state"] = DISABLED
        pin7["state"] = DISABLED
        pin8["state"] = DISABLED
        pin9["state"] = DISABLED
    if y == 11:
        pin0["state"] = DISABLED
        pin1["state"] = DISABLED
        pin2["state"] = DISABLED
        pin3["state"] = DISABLED
        pin4["state"] = DISABLED
        pin5["state"] = DISABLED
        pin6["state"] = DISABLED
        pin7["state"] = DISABLED
        pin8["state"] = DISABLED
        pin9["state"] = DISABLED
        pin10["state"] = DISABLED
    if y == 12:
        pin0["state"] = DISABLED
        pin1["state"] = DISABLED
        pin2["state"] = DISABLED
        pin3["state"] = DISABLED
        pin4["state"] = DISABLED
        pin5["state"] = DISABLED
        pin6["state"] = DISABLED
        pin7["state"] = DISABLED
        pin8["state"] = DISABLED
        pin9["state"] = DISABLED
        pin10["state"] = DISABLED
        pin11["state"] = DISABLED
    if y == 13:
        pin0["state"] = DISABLED
        pin1["state"] = DISABLED
        pin2["state"] = DISABLED
        pin3["state"] = DISABLED
        pin4["state"] = DISABLED
        pin5["state"] = DISABLED
        pin6["state"] = DISABLED
        pin7["state"] = DISABLED
        pin8["state"] = DISABLED
        pin9["state"] = DISABLED
        pin10["state"] = DISABLED
        pin11["state"] = DISABLED
        pin12["state"] = DISABLED
    if y == 14:
        pin0["state"] = DISABLED
        pin1["state"] = DISABLED
        pin2["state"] = DISABLED
        pin3["state"] = DISABLED
        pin4["state"] = DISABLED
        pin5["state"] = DISABLED
        pin6["state"] = DISABLED
        pin7["state"] = DISABLED
        pin8["state"] = DISABLED
        pin9["state"] = DISABLED
        pin10["state"] = DISABLED
        pin11["state"] = DISABLED
        pin12["state"] = DISABLED
        pin13["state"] = DISABLED
    if y == 15:
        pin0["state"] = DISABLED
        pin1["state"] = DISABLED
        pin2["state"] = DISABLED
        pin3["state"] = DISABLED
        pin4["state"] = DISABLED
        pin5["state"] = DISABLED
        pin6["state"] = DISABLED
        pin7["state"] = DISABLED
        pin8["state"] = DISABLED
        pin9["state"] = DISABLED
        pin10["state"] = DISABLED
        pin11["state"] = DISABLED
        pin12["state"] = DISABLED
        pin13["state"] = DISABLED
        pin14["state"] = DISABLED
    if y == 16:
        pin0["state"] = DISABLED
        pin1["state"] = DISABLED
        pin2["state"] = DISABLED
        pin3["state"] = DISABLED
        pin4["state"] = DISABLED
        pin5["state"] = DISABLED
        pin6["state"] = DISABLED
        pin7["state"] = DISABLED
        pin8["state"] = DISABLED
        pin9["state"] = DISABLED
        pin10["state"] = DISABLED
        pin11["state"] = DISABLED
        pin12["state"] = DISABLED
        pin13["state"] = DISABLED
        pin14["state"] = DISABLED
        pin15["state"] = DISABLED
    if y == 17:
        pin0["state"] = DISABLED
        pin1["state"] = DISABLED
        pin2["state"] = DISABLED
        pin3["state"] = DISABLED
        pin4["state"] = DISABLED
        pin5["state"] = DISABLED
        pin6["state"] = DISABLED
        pin7["state"] = DISABLED
        pin8["state"] = DISABLED
        pin9["state"] = DISABLED
        pin10["state"] = DISABLED
        pin11["state"] = DISABLED
        pin12["state"] = DISABLED
        pin13["state"] = DISABLED
        pin14["state"] = DISABLED
        pin15["state"] = DISABLED
        pin16["state"] = DISABLED
    if y == 17:
        pin0["state"] = DISABLED
        pin1["state"] = DISABLED
        pin2["state"] = DISABLED
        pin3["state"] = DISABLED
        pin4["state"] = DISABLED
        pin5["state"] = DISABLED
        pin6["state"] = DISABLED
        pin7["state"] = DISABLED
        pin8["state"] = DISABLED
        pin9["state"] = DISABLED
        pin10["state"] = DISABLED
        pin11["state"] = DISABLED
        pin12["state"] = DISABLED
        pin13["state"] = DISABLED
        pin14["state"] = DISABLED
        pin15["state"] = DISABLED
        pin16["state"] = DISABLED
        pin17["state"] = DISABLED


def sendToArduino():
    global bin1, bin2, bin3, bin4, bin5, bin6, bin7, bin8, bin9, bin10, bin11, bin12, bin13, bin14, bin15, bin16, bin17, bin18
    global stateC
    stateC = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if x == 1:
        pin1 = my_pins["pins"][0][2]
        # print(pin1)
        state1 = my_pins["pins"][0][3]

        bin1 = pin1

        disableCells(x)

        stateC[0] = int(state1)

        pinNumber(int(pin1), stateC[0])

    if x == 2:
        pin1 = my_pins["pins"][0][2]
        pin2 = my_pins["pins"][1][2]
        # print(pin1, pin2)

        bin1 = pin1
        bin2 = pin2

        disableCells(x)

        state1 = my_pins["pins"][0][3]
        state2 = my_pins["pins"][1][3]

        stateC[0] = int(state1)
        stateC[1] = int(state2)

        pinNumber(int(pin1), stateC[0])
        pinNumber(int(pin2), stateC[1])
    if x == 3:
        pin1 = my_pins["pins"][0][2]
        pin2 = my_pins["pins"][1][2]
        pin3 = my_pins["pins"][2][2]
        # print(pin1, pin2, pin3)

        bin1 = pin1
        bin2 = pin2
        bin3 = pin3

        disableCells(x)

        state1 = my_pins["pins"][0][3]
        state2 = my_pins["pins"][1][3]
        state3 = my_pins["pins"][2][3]

        stateC[0] = int(state1)
        stateC[1] = int(state2)
        stateC[2] = int(state3)

        pinNumber(int(pin1), stateC[0])
        pinNumber(int(pin2), stateC[1])
        pinNumber(int(pin3), stateC[2])
    if x == 4:
        pin1 = my_pins["pins"][0][2]
        pin2 = my_pins["pins"][1][2]
        pin3 = my_pins["pins"][2][2]
        pin4 = my_pins["pins"][3][2]
        # print(pin1, pin2, pin3, pin4)

        bin1 = pin1
        bin2 = pin2
        bin3 = pin3
        bin4 = pin4

        disableCells(x)

        state1 = my_pins["pins"][0][3]
        state2 = my_pins["pins"][1][3]
        state3 = my_pins["pins"][2][3]
        state4 = my_pins["pins"][3][3]

        stateC[0] = int(state1)
        stateC[1] = int(state2)
        stateC[2] = int(state3)
        stateC[3] = int(state4)

        pinNumber(int(pin1), stateC[0])
        pinNumber(int(pin2), stateC[1])
        pinNumber(int(pin3), stateC[2])
        pinNumber(int(pin4), stateC[3])
    if x == 5:
        pin1 = my_pins["pins"][0][2]
        pin2 = my_pins["pins"][1][2]
        pin3 = my_pins["pins"][2][2]
        pin4 = my_pins["pins"][3][2]
        pin5 = my_pins["pins"][4][2]
        # print(pin1, pin2, pin3, pin4, pin5)

        bin1 = pin1
        bin2 = pin2
        bin3 = pin3
        bin4 = pin4
        bin5 = pin5

        disableCells(x)

        state1 = my_pins["pins"][0][3]
        state2 = my_pins["pins"][1][3]
        state3 = my_pins["pins"][2][3]
        state4 = my_pins["pins"][3][3]
        state5 = my_pins["pins"][4][3]

        stateC[0] = int(state1)
        stateC[1] = int(state2)
        stateC[2] = int(state3)
        stateC[3] = int(state4)
        stateC[4] = int(state5)

        pinNumber(int(pin1), stateC[0])
        pinNumber(int(pin2), stateC[1])
        pinNumber(int(pin3), stateC[2])
        pinNumber(int(pin4), stateC[3])
        pinNumber(int(pin5), stateC[4])
    if x == 6:
        pin1 = my_pins["pins"][0][2]
        pin2 = my_pins["pins"][1][2]
        pin3 = my_pins["pins"][2][2]
        pin4 = my_pins["pins"][3][2]
        pin5 = my_pins["pins"][4][2]
        pin6 = my_pins["pins"][5][2]
        # print(pin1, pin2, pin3, pin4, pin5, pin6)

        bin1 = pin1
        bin2 = pin2
        bin3 = pin3
        bin4 = pin4
        bin5 = pin5
        bin6 = pin6

        disableCells(x)

        state1 = my_pins["pins"][0][3]
        state2 = my_pins["pins"][1][3]
        state3 = my_pins["pins"][2][3]
        state4 = my_pins["pins"][3][3]
        state5 = my_pins["pins"][4][3]
        state6 = my_pins["pins"][5][3]

        stateC[0] = int(state1)
        stateC[1] = int(state2)
        stateC[2] = int(state3)
        stateC[3] = int(state4)
        stateC[4] = int(state5)
        stateC[5] = int(state6)

        pinNumber(int(pin1), stateC[0])
        pinNumber(int(pin2), stateC[1])
        pinNumber(int(pin3), stateC[2])
        pinNumber(int(pin4), stateC[3])
        pinNumber(int(pin5), stateC[4])
        pinNumber(int(pin6), stateC[5])
    if x == 7:
        pin1 = my_pins["pins"][0][2]
        pin2 = my_pins["pins"][1][2]
        pin3 = my_pins["pins"][2][2]
        pin4 = my_pins["pins"][3][2]
        pin5 = my_pins["pins"][4][2]
        pin6 = my_pins["pins"][5][2]
        pin7 = my_pins["pins"][6][2]
        # print(pin1, pin2, pin3, pin4, pin5, pin6, pin7)

        bin1 = pin1
        bin2 = pin2
        bin3 = pin3
        bin4 = pin4
        bin5 = pin5
        bin6 = pin6
        bin7 = pin7

        disableCells(x)

        state1 = my_pins["pins"][0][3]
        state2 = my_pins["pins"][1][3]
        state3 = my_pins["pins"][2][3]
        state4 = my_pins["pins"][3][3]
        state5 = my_pins["pins"][4][3]
        state6 = my_pins["pins"][5][3]
        state7 = my_pins["pins"][6][3]

        stateC[0] = int(state1)
        stateC[1] = int(state2)
        stateC[2] = int(state3)
        stateC[3] = int(state4)
        stateC[4] = int(state5)
        stateC[5] = int(state6)
        stateC[6] = int(state7)

        pinNumber(int(pin1), stateC[0])
        pinNumber(int(pin2), stateC[1])
        pinNumber(int(pin3), stateC[2])
        pinNumber(int(pin4), stateC[3])
        pinNumber(int(pin5), stateC[4])
        pinNumber(int(pin6), stateC[5])
        pinNumber(int(pin7), stateC[6])
    if x == 8:
        pin1 = my_pins["pins"][0][2]
        pin2 = my_pins["pins"][1][2]
        pin3 = my_pins["pins"][2][2]
        pin4 = my_pins["pins"][3][2]
        pin5 = my_pins["pins"][4][2]
        pin6 = my_pins["pins"][5][2]
        pin7 = my_pins["pins"][6][2]
        pin8 = my_pins["pins"][7][2]
        # print(pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8)

        bin1 = pin1
        bin2 = pin2
        bin3 = pin3
        bin4 = pin4
        bin5 = pin5
        bin6 = pin6
        bin7 = pin7
        bin8 = pin8

        disableCells(x)

        state1 = my_pins["pins"][0][3]
        state2 = my_pins["pins"][1][3]
        state3 = my_pins["pins"][2][3]
        state4 = my_pins["pins"][3][3]
        state5 = my_pins["pins"][4][3]
        state6 = my_pins["pins"][5][3]
        state7 = my_pins["pins"][6][3]
        state8 = my_pins["pins"][7][3]

        stateC[0] = int(state1)
        stateC[1] = int(state2)
        stateC[2] = int(state3)
        stateC[3] = int(state4)
        stateC[4] = int(state5)
        stateC[5] = int(state6)
        stateC[6] = int(state7)
        stateC[7] = int(state8)

        pinNumber(int(pin1), stateC[0])
        pinNumber(int(pin2), stateC[1])
        pinNumber(int(pin3), stateC[2])
        pinNumber(int(pin4), stateC[3])
        pinNumber(int(pin5), stateC[4])
        pinNumber(int(pin6), stateC[5])
        pinNumber(int(pin7), stateC[6])
        pinNumber(int(pin8), stateC[7])
    if x == 9:
        pin1 = my_pins["pins"][0][2]
        pin2 = my_pins["pins"][1][2]
        pin3 = my_pins["pins"][2][2]
        pin4 = my_pins["pins"][3][2]
        pin5 = my_pins["pins"][4][2]
        pin6 = my_pins["pins"][5][2]
        pin7 = my_pins["pins"][6][2]
        pin8 = my_pins["pins"][7][2]
        pin9 = my_pins["pins"][8][2]
        # print(pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, pin9)

        bin1 = pin1
        bin2 = pin2
        bin3 = pin3
        bin4 = pin4
        bin5 = pin5
        bin6 = pin6
        bin7 = pin7
        bin8 = pin8
        bin9 = pin9

        disableCells(x)

        state1 = my_pins["pins"][0][3]
        state2 = my_pins["pins"][1][3]
        state3 = my_pins["pins"][2][3]
        state4 = my_pins["pins"][3][3]
        state5 = my_pins["pins"][4][3]
        state6 = my_pins["pins"][5][3]
        state7 = my_pins["pins"][6][3]
        state8 = my_pins["pins"][7][3]
        state9 = my_pins["pins"][8][3]

        stateC[0] = int(state1)
        stateC[1] = int(state2)
        stateC[2] = int(state3)
        stateC[3] = int(state4)
        stateC[4] = int(state5)
        stateC[5] = int(state6)
        stateC[6] = int(state7)
        stateC[7] = int(state8)
        stateC[8] = int(state9)

        pinNumber(int(pin1), stateC[0])
        pinNumber(int(pin2), stateC[1])
        pinNumber(int(pin3), stateC[2])
        pinNumber(int(pin4), stateC[3])
        pinNumber(int(pin5), stateC[4])
        pinNumber(int(pin6), stateC[5])
        pinNumber(int(pin7), stateC[6])
        pinNumber(int(pin8), stateC[7])
        pinNumber(int(pin9), stateC[8])
    if x == 10:
        pin1 = my_pins["pins"][0][2]
        pin2 = my_pins["pins"][1][2]
        pin3 = my_pins["pins"][2][2]
        pin4 = my_pins["pins"][3][2]
        pin5 = my_pins["pins"][4][2]
        pin6 = my_pins["pins"][5][2]
        pin7 = my_pins["pins"][6][2]
        pin8 = my_pins["pins"][7][2]
        pin9 = my_pins["pins"][8][2]
        pin10 = my_pins["pins"][9][2]
        # print(pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, pin9, pin10)

        bin1 = pin1
        bin2 = pin2
        bin3 = pin3
        bin4 = pin4
        bin5 = pin5
        bin6 = pin6
        bin7 = pin7
        bin8 = pin8
        bin9 = pin9
        bin10 = pin10

        disableCells(x)

        state1 = my_pins["pins"][0][3]
        state2 = my_pins["pins"][1][3]
        state3 = my_pins["pins"][2][3]
        state4 = my_pins["pins"][3][3]
        state5 = my_pins["pins"][4][3]
        state6 = my_pins["pins"][5][3]
        state7 = my_pins["pins"][6][3]
        state8 = my_pins["pins"][7][3]
        state9 = my_pins["pins"][8][3]
        state10 = my_pins["pins"][9][3]

        stateC[0] = int(state1)
        stateC[1] = int(state2)
        stateC[2] = int(state3)
        stateC[3] = int(state4)
        stateC[4] = int(state5)
        stateC[5] = int(state6)
        stateC[6] = int(state7)
        stateC[7] = int(state8)
        stateC[8] = int(state9)
        stateC[9] = int(state10)

        pinNumber(int(pin1), stateC[0])
        pinNumber(int(pin2), stateC[1])
        pinNumber(int(pin3), stateC[2])
        pinNumber(int(pin4), stateC[3])
        pinNumber(int(pin5), stateC[4])
        pinNumber(int(pin6), stateC[5])
        pinNumber(int(pin7), stateC[6])
        pinNumber(int(pin8), stateC[7])
        pinNumber(int(pin9), stateC[8])
        pinNumber(int(pin10), stateC[9])
    if x == 11:
        pin1 = my_pins["pins"][0][2]
        pin2 = my_pins["pins"][1][2]
        pin3 = my_pins["pins"][2][2]
        pin4 = my_pins["pins"][3][2]
        pin5 = my_pins["pins"][4][2]
        pin6 = my_pins["pins"][5][2]
        pin7 = my_pins["pins"][6][2]
        pin8 = my_pins["pins"][7][2]
        pin9 = my_pins["pins"][8][2]
        pin10 = my_pins["pins"][9][2]
        pin11 = my_pins["pins"][10][2]
        # print(pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, pin9, pin10, pin11)

        bin1 = pin1
        bin2 = pin2
        bin3 = pin3
        bin4 = pin4
        bin5 = pin5
        bin6 = pin6
        bin7 = pin7
        bin8 = pin8
        bin9 = pin9
        bin10 = pin10
        bin11 = pin11

        disableCells(x)

        state1 = my_pins["pins"][0][3]
        state2 = my_pins["pins"][1][3]
        state3 = my_pins["pins"][2][3]
        state4 = my_pins["pins"][3][3]
        state5 = my_pins["pins"][4][3]
        state6 = my_pins["pins"][5][3]
        state7 = my_pins["pins"][6][3]
        state8 = my_pins["pins"][7][3]
        state9 = my_pins["pins"][8][3]
        state10 = my_pins["pins"][9][3]
        state11 = my_pins["pins"][10][3]

        stateC[0] = int(state1)
        stateC[1] = int(state2)
        stateC[2] = int(state3)
        stateC[3] = int(state4)
        stateC[4] = int(state5)
        stateC[5] = int(state6)
        stateC[6] = int(state7)
        stateC[7] = int(state8)
        stateC[8] = int(state9)
        stateC[9] = int(state10)
        stateC[10] = int(state11)

        pinNumber(int(pin1), stateC[0])
        pinNumber(int(pin2), stateC[1])
        pinNumber(int(pin3), stateC[2])
        pinNumber(int(pin4), stateC[3])
        pinNumber(int(pin5), stateC[4])
        pinNumber(int(pin6), stateC[5])
        pinNumber(int(pin7), stateC[6])
        pinNumber(int(pin8), stateC[7])
        pinNumber(int(pin9), stateC[8])
        pinNumber(int(pin10), stateC[9])
        pinNumber(int(pin11), stateC[10])
    if x == 12:
        pin1 = my_pins["pins"][0][2]
        pin2 = my_pins["pins"][1][2]
        pin3 = my_pins["pins"][2][2]
        pin4 = my_pins["pins"][3][2]
        pin5 = my_pins["pins"][4][2]
        pin6 = my_pins["pins"][5][2]
        pin7 = my_pins["pins"][6][2]
        pin8 = my_pins["pins"][7][2]
        pin9 = my_pins["pins"][8][2]
        pin10 = my_pins["pins"][9][2]
        pin11 = my_pins["pins"][10][2]
        pin12 = my_pins["pins"][11][2]
        # print(pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, pin9, pin10, pin11, pin12)

        bin1 = pin1
        bin2 = pin2
        bin3 = pin3
        bin4 = pin4
        bin5 = pin5
        bin6 = pin6
        bin7 = pin7
        bin8 = pin8
        bin9 = pin9
        bin10 = pin10
        bin11 = pin11
        bin12 = pin12

        disableCells(x)

        state1 = my_pins["pins"][0][3]
        state2 = my_pins["pins"][1][3]
        state3 = my_pins["pins"][2][3]
        state4 = my_pins["pins"][3][3]
        state5 = my_pins["pins"][4][3]
        state6 = my_pins["pins"][5][3]
        state7 = my_pins["pins"][6][3]
        state8 = my_pins["pins"][7][3]
        state9 = my_pins["pins"][8][3]
        state10 = my_pins["pins"][9][3]
        state11 = my_pins["pins"][10][3]
        state12 = my_pins["pins"][11][3]

        stateC[0] = int(state1)
        stateC[1] = int(state2)
        stateC[2] = int(state3)
        stateC[3] = int(state4)
        stateC[4] = int(state5)
        stateC[5] = int(state6)
        stateC[6] = int(state7)
        stateC[7] = int(state8)
        stateC[8] = int(state9)
        stateC[9] = int(state10)
        stateC[10] = int(state11)
        stateC[11] = int(state12)

        pinNumber(int(pin1), stateC[0])
        pinNumber(int(pin2), stateC[1])
        pinNumber(int(pin3), stateC[2])
        pinNumber(int(pin4), stateC[3])
        pinNumber(int(pin5), stateC[4])
        pinNumber(int(pin6), stateC[5])
        pinNumber(int(pin7), stateC[6])
        pinNumber(int(pin8), stateC[7])
        pinNumber(int(pin9), stateC[8])
        pinNumber(int(pin10), stateC[9])
        pinNumber(int(pin11), stateC[10])
        pinNumber(int(pin12), stateC[11])
    if x == 13:
        pin1 = my_pins["pins"][0][2]
        pin2 = my_pins["pins"][1][2]
        pin3 = my_pins["pins"][2][2]
        pin4 = my_pins["pins"][3][2]
        pin5 = my_pins["pins"][4][2]
        pin6 = my_pins["pins"][5][2]
        pin7 = my_pins["pins"][6][2]
        pin8 = my_pins["pins"][7][2]
        pin9 = my_pins["pins"][8][2]
        pin10 = my_pins["pins"][9][2]
        pin11 = my_pins["pins"][10][2]
        pin12 = my_pins["pins"][11][2]
        pin13 = my_pins["pins"][12][2]
        # print(pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, pin9, pin10, pin11, pin12, pin13)

        bin1 = pin1
        bin2 = pin2
        bin3 = pin3
        bin4 = pin4
        bin5 = pin5
        bin6 = pin6
        bin7 = pin7
        bin8 = pin8
        bin9 = pin9
        bin10 = pin10
        bin11 = pin11
        bin12 = pin12
        bin13 = pin13

        disableCells(x)

        state1 = my_pins["pins"][0][3]
        state2 = my_pins["pins"][1][3]
        state3 = my_pins["pins"][2][3]
        state4 = my_pins["pins"][3][3]
        state5 = my_pins["pins"][4][3]
        state6 = my_pins["pins"][5][3]
        state7 = my_pins["pins"][6][3]
        state8 = my_pins["pins"][7][3]
        state9 = my_pins["pins"][8][3]
        state10 = my_pins["pins"][9][3]
        state11 = my_pins["pins"][10][3]
        state12 = my_pins["pins"][11][3]
        state13 = my_pins["pins"][12][3]

        stateC[0] = int(state1)
        stateC[1] = int(state2)
        stateC[2] = int(state3)
        stateC[3] = int(state4)
        stateC[4] = int(state5)
        stateC[5] = int(state6)
        stateC[6] = int(state7)
        stateC[7] = int(state8)
        stateC[8] = int(state9)
        stateC[9] = int(state10)
        stateC[10] = int(state11)
        stateC[11] = int(state12)
        stateC[12] = int(state13)

        pinNumber(int(pin1), stateC[0])
        pinNumber(int(pin2), stateC[1])
        pinNumber(int(pin3), stateC[2])
        pinNumber(int(pin4), stateC[3])
        pinNumber(int(pin5), stateC[4])
        pinNumber(int(pin6), stateC[5])
        pinNumber(int(pin7), stateC[6])
        pinNumber(int(pin8), stateC[7])
        pinNumber(int(pin9), stateC[8])
        pinNumber(int(pin10), stateC[9])
        pinNumber(int(pin11), stateC[10])
        pinNumber(int(pin12), stateC[11])
        pinNumber(int(pin13), stateC[12])
    if x == 14:
        pin1 = my_pins["pins"][0][2]
        pin2 = my_pins["pins"][1][2]
        pin3 = my_pins["pins"][2][2]
        pin4 = my_pins["pins"][3][2]
        pin5 = my_pins["pins"][4][2]
        pin6 = my_pins["pins"][5][2]
        pin7 = my_pins["pins"][6][2]
        pin8 = my_pins["pins"][7][2]
        pin9 = my_pins["pins"][8][2]
        pin10 = my_pins["pins"][9][2]
        pin11 = my_pins["pins"][10][2]
        pin12 = my_pins["pins"][11][2]
        pin13 = my_pins["pins"][12][2]
        pin14 = my_pins["pins"][13][2]
        # print(pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, pin9, pin10, pin11, pin12, pin13, pin14)

        bin1 = pin1
        bin2 = pin2
        bin3 = pin3
        bin4 = pin4
        bin5 = pin5
        bin6 = pin6
        bin7 = pin7
        bin8 = pin8
        bin9 = pin9
        bin10 = pin10
        bin11 = pin11
        bin12 = pin12
        bin13 = pin13
        bin14 = pin14

        disableCells(x)

        state1 = my_pins["pins"][0][3]
        state2 = my_pins["pins"][1][3]
        state3 = my_pins["pins"][2][3]
        state4 = my_pins["pins"][3][3]
        state5 = my_pins["pins"][4][3]
        state6 = my_pins["pins"][5][3]
        state7 = my_pins["pins"][6][3]
        state8 = my_pins["pins"][7][3]
        state9 = my_pins["pins"][8][3]
        state10 = my_pins["pins"][9][3]
        state11 = my_pins["pins"][10][3]
        state12 = my_pins["pins"][11][3]
        state13 = my_pins["pins"][12][3]
        state14 = my_pins["pins"][13][3]

        stateC[0] = int(state1)
        stateC[1] = int(state2)
        stateC[2] = int(state3)
        stateC[3] = int(state4)
        stateC[4] = int(state5)
        stateC[5] = int(state6)
        stateC[6] = int(state7)
        stateC[7] = int(state8)
        stateC[8] = int(state9)
        stateC[9] = int(state10)
        stateC[10] = int(state11)
        stateC[11] = int(state12)
        stateC[12] = int(state13)
        stateC[13] = int(state14)

        pinNumber(int(pin1), stateC[0])
        pinNumber(int(pin2), stateC[1])
        pinNumber(int(pin3), stateC[2])
        pinNumber(int(pin4), stateC[3])
        pinNumber(int(pin5), stateC[4])
        pinNumber(int(pin6), stateC[5])
        pinNumber(int(pin7), stateC[6])
        pinNumber(int(pin8), stateC[7])
        pinNumber(int(pin9), stateC[8])
        pinNumber(int(pin10), stateC[9])
        pinNumber(int(pin11), stateC[10])
        pinNumber(int(pin12), stateC[11])
        pinNumber(int(pin13), stateC[12])
        pinNumber(int(pin14), stateC[13])
    if x == 15:
        pin1 = my_pins["pins"][0][2]
        pin2 = my_pins["pins"][1][2]
        pin3 = my_pins["pins"][2][2]
        pin4 = my_pins["pins"][3][2]
        pin5 = my_pins["pins"][4][2]
        pin6 = my_pins["pins"][5][2]
        pin7 = my_pins["pins"][6][2]
        pin8 = my_pins["pins"][7][2]
        pin9 = my_pins["pins"][8][2]
        pin10 = my_pins["pins"][9][2]
        pin11 = my_pins["pins"][10][2]
        pin12 = my_pins["pins"][11][2]
        pin13 = my_pins["pins"][12][2]
        pin14 = my_pins["pins"][13][2]
        pin15 = my_pins["pins"][14][2]
        # print(pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, pin9, pin10, pin11, pin12, pin13, pin14, pin15)

        bin1 = pin1
        bin2 = pin2
        bin3 = pin3
        bin4 = pin4
        bin5 = pin5
        bin6 = pin6
        bin7 = pin7
        bin8 = pin8
        bin9 = pin9
        bin10 = pin10
        bin11 = pin11
        bin12 = pin12
        bin13 = pin13
        bin14 = pin14
        bin15 = pin15

        disableCells(x)

        state1 = my_pins["pins"][0][3]
        state2 = my_pins["pins"][1][3]
        state3 = my_pins["pins"][2][3]
        state4 = my_pins["pins"][3][3]
        state5 = my_pins["pins"][4][3]
        state6 = my_pins["pins"][5][3]
        state7 = my_pins["pins"][6][3]
        state8 = my_pins["pins"][7][3]
        state9 = my_pins["pins"][8][3]
        state10 = my_pins["pins"][9][3]
        state11 = my_pins["pins"][10][3]
        state12 = my_pins["pins"][11][3]
        state13 = my_pins["pins"][12][3]
        state14 = my_pins["pins"][13][3]
        state15 = my_pins["pins"][14][3]

        stateC[0] = int(state1)
        stateC[1] = int(state2)
        stateC[2] = int(state3)
        stateC[3] = int(state4)
        stateC[4] = int(state5)
        stateC[5] = int(state6)
        stateC[6] = int(state7)
        stateC[7] = int(state8)
        stateC[8] = int(state9)
        stateC[9] = int(state10)
        stateC[10] = int(state11)
        stateC[11] = int(state12)
        stateC[12] = int(state13)
        stateC[13] = int(state14)
        stateC[14] = int(state15)

        pinNumber(int(pin1), stateC[0])
        pinNumber(int(pin2), stateC[1])
        pinNumber(int(pin3), stateC[2])
        pinNumber(int(pin4), stateC[3])
        pinNumber(int(pin5), stateC[4])
        pinNumber(int(pin6), stateC[5])
        pinNumber(int(pin7), stateC[6])
        pinNumber(int(pin8), stateC[7])
        pinNumber(int(pin9), stateC[8])
        pinNumber(int(pin10), stateC[9])
        pinNumber(int(pin11), stateC[10])
        pinNumber(int(pin12), stateC[11])
        pinNumber(int(pin13), stateC[12])
        pinNumber(int(pin14), stateC[13])
        pinNumber(int(pin15), stateC[14])
    if x == 16:
        pin1 = my_pins["pins"][0][2]
        pin2 = my_pins["pins"][1][2]
        pin3 = my_pins["pins"][2][2]
        pin4 = my_pins["pins"][3][2]
        pin5 = my_pins["pins"][4][2]
        pin6 = my_pins["pins"][5][2]
        pin7 = my_pins["pins"][6][2]
        pin8 = my_pins["pins"][7][2]
        pin9 = my_pins["pins"][8][2]
        pin10 = my_pins["pins"][9][2]
        pin11 = my_pins["pins"][10][2]
        pin12 = my_pins["pins"][11][2]
        pin13 = my_pins["pins"][12][2]
        pin14 = my_pins["pins"][13][2]
        pin15 = my_pins["pins"][14][2]
        pin16 = my_pins["pins"][15][2]
        # print(pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, pin9, pin10, pin11, pin12, pin13, pin14, pin15, pin16)

        bin1 = pin1
        bin2 = pin2
        bin3 = pin3
        bin4 = pin4
        bin5 = pin5
        bin6 = pin6
        bin7 = pin7
        bin8 = pin8
        bin9 = pin9
        bin10 = pin10
        bin11 = pin11
        bin12 = pin12
        bin13 = pin13
        bin14 = pin14
        bin15 = pin15
        bin16 = pin16

        disableCells(x)

        state1 = my_pins["pins"][0][3]
        state2 = my_pins["pins"][1][3]
        state3 = my_pins["pins"][2][3]
        state4 = my_pins["pins"][3][3]
        state5 = my_pins["pins"][4][3]
        state6 = my_pins["pins"][5][3]
        state7 = my_pins["pins"][6][3]
        state8 = my_pins["pins"][7][3]
        state9 = my_pins["pins"][8][3]
        state10 = my_pins["pins"][9][3]
        state11 = my_pins["pins"][10][3]
        state12 = my_pins["pins"][11][3]
        state13 = my_pins["pins"][12][3]
        state14 = my_pins["pins"][13][3]
        state15 = my_pins["pins"][14][3]
        state16 = my_pins["pins"][15][3]

        stateC[0] = int(state1)
        stateC[1] = int(state2)
        stateC[2] = int(state3)
        stateC[3] = int(state4)
        stateC[4] = int(state5)
        stateC[5] = int(state6)
        stateC[6] = int(state7)
        stateC[7] = int(state8)
        stateC[8] = int(state9)
        stateC[9] = int(state10)
        stateC[10] = int(state11)
        stateC[11] = int(state12)
        stateC[12] = int(state13)
        stateC[13] = int(state14)
        stateC[14] = int(state15)
        stateC[15] = int(state16)

        pinNumber(int(pin1), stateC[0])
        pinNumber(int(pin2), stateC[1])
        pinNumber(int(pin3), stateC[2])
        pinNumber(int(pin4), stateC[3])
        pinNumber(int(pin5), stateC[4])
        pinNumber(int(pin6), stateC[5])
        pinNumber(int(pin7), stateC[6])
        pinNumber(int(pin8), stateC[7])
        pinNumber(int(pin9), stateC[8])
        pinNumber(int(pin10), stateC[9])
        pinNumber(int(pin11), stateC[10])
        pinNumber(int(pin12), stateC[11])
        pinNumber(int(pin13), stateC[12])
        pinNumber(int(pin14), stateC[13])
        pinNumber(int(pin15), stateC[14])
        pinNumber(int(pin16), stateC[15])
    if x == 17:
        pin1 = my_pins["pins"][0][2]
        pin2 = my_pins["pins"][1][2]
        pin3 = my_pins["pins"][2][2]
        pin4 = my_pins["pins"][3][2]
        pin5 = my_pins["pins"][4][2]
        pin6 = my_pins["pins"][5][2]
        pin7 = my_pins["pins"][6][2]
        pin8 = my_pins["pins"][7][2]
        pin9 = my_pins["pins"][8][2]
        pin10 = my_pins["pins"][9][2]
        pin11 = my_pins["pins"][10][2]
        pin12 = my_pins["pins"][11][2]
        pin13 = my_pins["pins"][12][2]
        pin14 = my_pins["pins"][13][2]
        pin15 = my_pins["pins"][14][2]
        pin16 = my_pins["pins"][15][2]
        pin17 = my_pins["pins"][16][2]
        # print(pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, pin9, pin10, pin11, pin12, pin13, pin14, pin15, pin16, pin17)

        bin1 = pin1
        bin2 = pin2
        bin3 = pin3
        bin4 = pin4
        bin5 = pin5
        bin6 = pin6
        bin7 = pin7
        bin8 = pin8
        bin9 = pin9
        bin10 = pin10
        bin11 = pin11
        bin12 = pin12
        bin13 = pin13
        bin14 = pin14
        bin15 = pin15
        bin16 = pin16
        bin17 = pin17

        disableCells(x)

        state1 = my_pins["pins"][0][3]
        state2 = my_pins["pins"][1][3]
        state3 = my_pins["pins"][2][3]
        state4 = my_pins["pins"][3][3]
        state5 = my_pins["pins"][4][3]
        state6 = my_pins["pins"][5][3]
        state7 = my_pins["pins"][6][3]
        state8 = my_pins["pins"][7][3]
        state9 = my_pins["pins"][8][3]
        state10 = my_pins["pins"][9][3]
        state11 = my_pins["pins"][10][3]
        state12 = my_pins["pins"][11][3]
        state13 = my_pins["pins"][12][3]
        state14 = my_pins["pins"][13][3]
        state15 = my_pins["pins"][14][3]
        state16 = my_pins["pins"][15][3]
        state17 = my_pins["pins"][16][3]

        stateC[0] = int(state1)
        stateC[1] = int(state2)
        stateC[2] = int(state3)
        stateC[3] = int(state4)
        stateC[4] = int(state5)
        stateC[5] = int(state6)
        stateC[6] = int(state7)
        stateC[7] = int(state8)
        stateC[8] = int(state9)
        stateC[9] = int(state10)
        stateC[10] = int(state11)
        stateC[11] = int(state12)
        stateC[12] = int(state13)
        stateC[13] = int(state14)
        stateC[14] = int(state15)
        stateC[15] = int(state16)
        stateC[16] = int(state17)

        pinNumber(int(pin1), stateC[0])
        pinNumber(int(pin2), stateC[1])
        pinNumber(int(pin3), stateC[2])
        pinNumber(int(pin4), stateC[3])
        pinNumber(int(pin5), stateC[4])
        pinNumber(int(pin6), stateC[5])
        pinNumber(int(pin7), stateC[6])
        pinNumber(int(pin8), stateC[7])
        pinNumber(int(pin9), stateC[8])
        pinNumber(int(pin10), stateC[9])
        pinNumber(int(pin11), stateC[10])
        pinNumber(int(pin12), stateC[11])
        pinNumber(int(pin13), stateC[12])
        pinNumber(int(pin14), stateC[13])
        pinNumber(int(pin15), stateC[14])
        pinNumber(int(pin16), stateC[15])
        pinNumber(int(pin17), stateC[16])
    if x == 18:
        pin1 = my_pins["pins"][0][2]
        pin2 = my_pins["pins"][1][2]
        pin3 = my_pins["pins"][2][2]
        pin4 = my_pins["pins"][3][2]
        pin5 = my_pins["pins"][4][2]
        pin6 = my_pins["pins"][5][2]
        pin7 = my_pins["pins"][6][2]
        pin8 = my_pins["pins"][7][2]
        pin9 = my_pins["pins"][8][2]
        pin10 = my_pins["pins"][9][2]
        pin11 = my_pins["pins"][10][2]
        pin12 = my_pins["pins"][11][2]
        pin13 = my_pins["pins"][12][2]
        pin14 = my_pins["pins"][13][2]
        pin15 = my_pins["pins"][14][2]
        pin16 = my_pins["pins"][15][2]
        pin17 = my_pins["pins"][16][2]
        pin18 = my_pins["pins"][17][2]
        # print(pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, pin9, pin10, pin11, pin12, pin13, pin14, pin15, pin16, pin17, pin18)

        bin1 = pin1
        bin2 = pin2
        bin3 = pin3
        bin4 = pin4
        bin5 = pin5
        bin6 = pin6
        bin7 = pin7
        bin8 = pin8
        bin9 = pin9
        bin10 = pin10
        bin11 = pin11
        bin12 = pin12
        bin13 = pin13
        bin14 = pin14
        bin15 = pin15
        bin16 = pin16
        bin17 = pin17
        bin18 = pin18

        disableCells(x)

        state1 = my_pins["pins"][0][3]
        state2 = my_pins["pins"][1][3]
        state3 = my_pins["pins"][2][3]
        state4 = my_pins["pins"][3][3]
        state5 = my_pins["pins"][4][3]
        state6 = my_pins["pins"][5][3]
        state7 = my_pins["pins"][6][3]
        state8 = my_pins["pins"][7][3]
        state9 = my_pins["pins"][8][3]
        state10 = my_pins["pins"][9][3]
        state11 = my_pins["pins"][10][3]
        state12 = my_pins["pins"][11][3]
        state13 = my_pins["pins"][12][3]
        state14 = my_pins["pins"][13][3]
        state15 = my_pins["pins"][14][3]
        state16 = my_pins["pins"][15][3]
        state17 = my_pins["pins"][16][3]
        state18 = my_pins["pins"][17][3]

        stateC[0] = int(state1)
        stateC[1] = int(state2)
        stateC[2] = int(state3)
        stateC[3] = int(state4)
        stateC[4] = int(state5)
        stateC[5] = int(state6)
        stateC[6] = int(state7)
        stateC[7] = int(state8)
        stateC[8] = int(state9)
        stateC[9] = int(state10)
        stateC[10] = int(state11)
        stateC[11] = int(state12)
        stateC[12] = int(state13)
        stateC[13] = int(state14)
        stateC[14] = int(state15)
        stateC[15] = int(state16)
        stateC[16] = int(state17)
        stateC[17] = int(state18)

        pinNumber(int(pin1), stateC[0])
        pinNumber(int(pin2), stateC[1])
        pinNumber(int(pin3), stateC[2])
        pinNumber(int(pin4), stateC[3])
        pinNumber(int(pin5), stateC[4])
        pinNumber(int(pin6), stateC[5])
        pinNumber(int(pin7), stateC[6])
        pinNumber(int(pin8), stateC[7])
        pinNumber(int(pin9), stateC[8])
        pinNumber(int(pin10), stateC[9])
        pinNumber(int(pin11), stateC[10])
        pinNumber(int(pin12), stateC[11])
        pinNumber(int(pin13), stateC[12])
        pinNumber(int(pin14), stateC[13])
        pinNumber(int(pin15), stateC[14])
        pinNumber(int(pin16), stateC[15])
        pinNumber(int(pin17), stateC[16])
        pinNumber(int(pin18), stateC[17])


def pinNumber(pin, state):
    if pin == 2:
        IO2.write(state)
    if pin == 3:
        IO3.write(state)
    if pin == 4:
        IO4.write(state)
    if pin == 5:
        IO5.write(state)
    if pin == 6:
        IO6.write(state)
    if pin == 7:
        IO7.write(state)
    if pin == 8:
        IO8.write(state)
    if pin == 9:
        IO9.write(state)
    if pin == 10:
        IO10.write(state)
    if pin == 11:
        IO11.write(state)
    if pin == 12:
        IO12.write(state)
    if pin == 13:
        IO13.write(state)
    # if pin == 14:
    #     IOA0.write(state)
    # if pin == 15:
    #     IOA1.write(state)
    # if pin == 16:
    #     IOA2.write(state)
    # if pin == 17:
    #     IOA3.write(state)
    # if pin == 18:
    #     IOA4.write(state)


# ------------------------------END---------------------------------------
addPin.counter = 0
saveData.i = 0
saveToFile.counter = 0
addPin.combined = []
addPin.entry = 0
addPin.current_row = 0

my_canvas = Canvas(root, width=910, height=30, bg="#2B2B2B", highlightthickness=0)
my_canvas.grid(row=0, column=0, columnspan=3)

add_button = Button(root, text="Add Pin", bg="#7E7272", fg="#F6EBEB", padx=30, pady=10, font=font1, borderwidth=0,
                    command=addPin)
add_button.grid(row=1, column=1)

my_canvas2 = Canvas(root, width=910, height=10, bg="#2B2B2B", highlightthickness=0)
my_canvas2.grid(row=2, column=0, columnspan=3)

name_label = Label(root, text="NAME", fg="white", bg="#2B2B2B", font=font1)
name_label.grid(row=3, column=0)

pin_label = Label(root, text="PIN NO.", fg="white", bg="#2B2B2B", font=font1)
pin_label.grid(row=3, column=1)

state_label = Label(root, text="STATE", fg="white", bg="#2B2B2B", font=font1)
state_label.grid(row=3, column=2)

input_frame = Frame(root, width=800, height=250, bg="#2B2B2B", highlightthickness=0)
input_frame.grid(row=4, column=0, columnspan=3)

if not (current_row == 0):
    try:
        loadCells()
    except:
        pass

# ADDING A SCROLLBAR
my_scrollbar = Scrollbar(root, orient="vertical")
# my_scrollbar.grid()

my_canvas3 = Canvas(root, width=910, height=7, bg="#2B2B2B", highlightthickness=0)
my_canvas3.grid(row=5, column=0, columnspan=3)

save_button = Button(root, text="UPLOAD", bg="#0C8CE9", fg="#F6EBEB", padx=30, pady=10, font=font1, borderwidth=0,
                     command=upload)
save_button.place(x=width - 160, y=height - 67, anchor='nw')
# save_button.grid(row=6, column=1)

delete_button = Button(root, text="DELETE", bg="#0C8CE9", fg="#F6EBEB", padx=30, pady=10, font=font1, borderwidth=0,
                       command=deleteCell)
delete_button.place(x=50, y=height - 67, anchor='nw')

deleteCell()
upload()

root.mainloop()
arduino.exit()
