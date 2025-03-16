from tkinter import *
from datetime import *
import requests

URL = 'https://api.open-meteo.com/v1/forecast?latitude=35.6944&longitude=51.4215&current=temperature_2m,is_day,rain,snowfall,cloud_cover,wind_speed_10m,wind_direction_10m&hourly=temperature_2m,precipitation,rain,cloud_cover,cloud_cover_low,cloud_cover_mid,cloud_cover_high,wind_speed_10m,wind_speed_80m,wind_speed_120m,wind_speed_180m,wind_direction_10m,wind_direction_80m,wind_direction_120m,wind_direction_180m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,rain_sum&timezone=Europe%2FMoscow'
location = 'delhi technologicaluniversity'
PARAM = {'adress': location}
info = requests.get(url=URL, params=PARAM)
data = info.json()
temps = data['hourly']['temperature_2m']

new_times = datetime.now()
new_hours = new_times.hour

root = Tk()
root.title('Live Weather(Tehran)')
root.geometry('300x320')
root.resizable(False, False)
root.config(bg='#0EB3FA')

# ____Frames____
frm1 = Frame(root, width=300, height=40, bg='#0EB3FA')
frm1.pack(side=TOP)
frm2 = Frame(root, height=40, width=300, bg='#0EB3FA')
frm2.pack(side=TOP)
frm3 = Frame(root, width=300, height=40, bg='#0EB3FA')
frm3.pack(side=TOP)
frm4 = Frame(root, width=300, height=40, bg='#0EB3FA')
frm4.pack(side=TOP)
frm5 = Frame(root, width=300, height=40, bg='#0EB3FA')
frm5.pack(side=TOP)
frm6 = Frame(root, width=300, height=40, bg='#0EB3FA')
frm6.pack(side=TOP)
frm7 = Frame(root, width=300, height=40, bg='#0EB3FA')
frm7.pack(side=TOP)
frm8 = Frame(root, width=300, height=40, bg='#0EB3FA')
frm8.pack(side=TOP)
# ____Labels____
lbl1 = Label(frm6, text='Temp is ?? ℃', bg='#0EB3FA', fg='#202020')
lbl1.pack(padx=10,pady=10)
lbl2 = Label(frm5, text='For Get Temp Of Any Hour,Click On Hour', bg='#0EB3FA', fg='#202020')
lbl2.pack(padx=10, pady=10)
lbl3 = Label(frm7, text='Click To See Live Weather ', bg='#0EB3FA', fg='#202020')
lbl3.pack(padx=10,pady=10)
# ____Variable____
temp = None


# ____Definations____
def glw():
    temp = int(temps[new_hours])
    lbl3.config(text=f'Live Weather Of {new_hours} Is {temp} ℃')


def h00():
    temp = int(temps[0])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h01():
    temp = int(temps[1])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h02():
    temp = int(temps[2])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h03():
    temp = int(temps[3])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h04():
    temp = int(temps[4])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h05():
    temp = int(temps[5])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h06():
    temp = int(temps[6])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h07():
    temp = int(temps[7])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h08():
    temp = int(temps[8])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h09():
    temp = int(temps[9])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h10():
    temp = int(temps[10])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h11():
    temp = int(temps[11])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h12():
    temp = int(temps[12])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h13():
    temp = int(temps[13])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h14():
    temp = int(temps[14])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h15():
    temp = int(temps[15])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h16():
    temp = int(temps[16])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h17():
    temp = int(temps[17])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h18():
    temp = int(temps[18])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h19():
    temp = int(temps[19])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h20():
    temp = int(temps[20])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h21():
    temp = int(temps[21])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h22():
    temp = int(temps[22])
    lbl1.config(text=f'Temp IS {temp} ℃')


def h23():
    temp = int(temps[23])
    lbl1.config(text=f'Temp IS {temp} ℃')


# ____Buttons____
btn0 = Button(frm8, text='Live Weather', command=glw)
btn0.pack(padx=10)
# *******************row1*************************
btn1 = Button(frm1, text='00', command=h00)
btn1.pack(padx=10, pady=10, side=LEFT)

btn2 = Button(frm1, text='01', command=h01)
btn2.pack(padx=10, side=LEFT)

btn3 = Button(frm1, text='02', command=h02)
btn3.pack(padx=10, side=LEFT)

btn4 = Button(frm1, text='03', command=h03)
btn4.pack(padx=10, side=LEFT)

btn5 = Button(frm1, text='04', command=h04)
btn5.pack(padx=10, side=LEFT)

btn6 = Button(frm1, text='05', command=h05)
btn6.pack(padx=10, side=LEFT)
# ***************************row2***************************
btn7 = Button(frm2, text='06', command=h06)
btn7.pack(padx=10, side=LEFT)

btn8 = Button(frm2, text='07', command=h07)
btn8.pack(padx=10, side=LEFT)

btn9 = Button(frm2, text='08', command=h08)
btn9.pack(padx=10, side=LEFT)

btn10 = Button(frm2, text='09', command=h09)
btn10.pack(padx=10, side=LEFT)

btn11 = Button(frm2, text='10', command=h10)
btn11.pack(padx=10, side=LEFT)

btn12 = Button(frm2, text='11', command=h11)
btn12.pack(padx=10, side=LEFT)
# *****************************row3********************
btn13 = Button(frm3, text='12', command=h12)
btn13.pack(padx=10, pady=10, side=LEFT)

btn14 = Button(frm3, text='13', command=h13)
btn14.pack(padx=10, side=LEFT)

btn15 = Button(frm3, text='14', command=h14)
btn15.pack(padx=10, side=LEFT)

btn16 = Button(frm3, text='15', command=h15)
btn16.pack(padx=10, side=LEFT)

btn17 = Button(frm3, text='16', command=h16)
btn17.pack(padx=10, side=LEFT)

btn18 = Button(frm3, text='17', command=h17)
btn18.pack(padx=10, side=LEFT)
# ********************************row4**********************************
btn19 = Button(frm4, text='18', command=h18)
btn19.pack(padx=10, side=LEFT)

btn20 = Button(frm4, text='19', command=h19)
btn20.pack(padx=10, side=LEFT)

btn21 = Button(frm4, text='20', command=h20)
btn21.pack(padx=10, side=LEFT)

btn22 = Button(frm4, text='21', command=h21)
btn22.pack(padx=10, side=LEFT)

btn23 = Button(frm4, text='22', command=h22)
btn23.pack(padx=10, side=LEFT)

btn24 = Button(frm4, text='23', command=h23)
btn24.pack(padx=10, side=LEFT)

root.mainloop()
