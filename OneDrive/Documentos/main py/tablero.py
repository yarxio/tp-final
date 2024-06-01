from tkinter import *
import piezas
import chess

ventana=Tk()

ventana.title('ajedrez de yarxio')

ventana.geometry('660x700')

lbl11=Label(ventana,bg='blue')
lbl11.place(x=10,y=10,width=80,height=80)

lbl21=Label(ventana,bg='skyblue')
lbl21.place(x=90,y=10,width=80,height=80)

lbl31=Label(ventana,bg='blue')
lbl31.place(x=170,y=10,width=80,height=80)

lbl41=Label(ventana,bg='sky blue')
lbl41.place(x=250,y=10,width=80,height=80)

lbl51=Label(ventana,bg='blue')
lbl51.place(x=330,y=10,width=80,height=80)

lbl61=Label(ventana,bg='sky blue')
lbl61.place(x=410,y=10,width=80,height=80)

lbl71=Label(ventana,bg='blue')
lbl71.place(x=490,y=10,width=80,height=80)

lbl81=Label(ventana,bg='skyblue')
lbl81.place(x=570,y=10,width=80,height=80)

lbl12=Label(ventana,bg='skyblue')
lbl12.place(x=10,y=90,width=80,height=80)

lbl22=Label(ventana,bg='blue')
lbl22.place(x=90,y=90,width=80,height=80)

lbl32=Label(ventana,bg='sky blue')
lbl32.place(x=170,y=90,width=80,height=80)

lbl42=Label(ventana,bg='blue')
lbl42.place(x=250,y=90,width=80,height=80)

lbl52=Label(ventana,bg='sky blue')
lbl52.place(x=330,y=90,width=80,height=80)

lbl62=Label(ventana,bg='blue')
lbl62.place(x=410,y=90,width=80,height=80)

lbl72=Label(ventana,bg='sky blue')
lbl72.place(x=490,y=90,width=80,height=80)

lbl82=Label(ventana,bg='blue')
lbl82.place(x=570,y=90,width=80,height=80)

lbl13=Label(ventana,bg='blue')
lbl13.place(x=10,y=170,width=80,height=80)

lbl23=Label(ventana,bg='skyblue')
lbl23.place(x=90,y=170,width=80,height=80)

lbl33=Label(ventana,bg='blue')
lbl33.place(x=170,y=170,width=80,height=80)

lbl43=Label(ventana,bg='sky blue')
lbl43.place(x=250,y=170,width=80,height=80)

lbl53=Label(ventana,bg='blue')
lbl53.place(x=330,y=170,width=80,height=80)

lbl63=Label(ventana,bg='sky blue')
lbl63.place(x=410,y=170,width=80,height=80)

lbl73=Label(ventana,bg='blue')
lbl73.place(x=490,y=170,width=80,height=80)

lbl83=Label(ventana,bg='skyblue')
lbl83.place(x=570,y=170,width=80,height=80)

lbl14=Label(ventana,bg='skyblue')
lbl14.place(x=10,y=250,width=80,height=80)

lbl24=Label(ventana,bg='blue')
lbl24.place(x=90,y=250,width=80,height=80)

lbl34=Label(ventana,bg='skyblue')
lbl34.place(x=170,y=250,width=80,height=80)

lbl44=Label(ventana,bg='blue')
lbl44.place(x=250,y=250,width=80,height=80)

lbl54=Label(ventana,bg='skyblue')
lbl54.place(x=330,y=250,width=80,height=80)

lbl64=Label(ventana,bg='blue')
lbl64.place(x=410,y=250,width=80,height=80)

lbl74=Label(ventana,bg='skyblue')
lbl74.place(x=490,y=250,width=80,height=80)

lbl84=Label(ventana,bg='blue')
lbl84.place(x=570,y=250,width=80,height=80)

bl15=Label(ventana,bg='blue')
bl15.place(x=10,y=330,width=80,height=80)

lbl25=Label(ventana,bg='skyblue')
lbl25.place(x=90,y=330,width=80,height=80)

lbl35=Label(ventana,bg='blue')
lbl35.place(x=170,y=330,width=80,height=80)

lbl45=Label(ventana,bg='sky blue')
lbl45.place(x=250,y=330,width=80,height=80)

lbl55=Label(ventana,bg='blue')
lbl55.place(x=330,y=330,width=80,height=80)

lbl65=Label(ventana,bg='sky blue')
lbl65.place(x=410,y=330,width=80,height=80)

lbl75=Label(ventana,bg='blue')
lbl75.place(x=490,y=330,width=80,height=80)

lbl85=Label(ventana,bg='skyblue')
lbl85.place(x=570,y=330,width=80,height=80)

lbl16=Label(ventana,bg='skyblue')
lbl16.place(x=10,y=410,width=80,height=80)

lbl26=Label(ventana,bg='blue')
lbl26.place(x=90,y=410,width=80,height=80)

lbl36=Label(ventana,bg='skyblue')
lbl36.place(x=170,y=410,width=80,height=80)

lbl46=Label(ventana,bg='blue')
lbl46.place(x=250,y=410,width=80,height=80)

lbl56=Label(ventana,bg='skyblue')
lbl56.place(x=330,y=410,width=80,height=80)

lbl66=Label(ventana,bg='blue')
lbl66.place(x=410,y=410,width=80,height=80)

lbl76=Label(ventana,bg='skyblue')
lbl76.place(x=490,y=410,width=80,height=80)

lbl86=Label(ventana,bg='blue')
lbl86.place(x=570,y=410,width=80,height=80)

lbl17=Label(ventana,bg='blue')
lbl17.place(x=10,y=490,width=80,height=80)

lbl27=Label(ventana,bg='skyblue')
lbl27.place(x=90,y=490,width=80,height=80)

lbl37=Label(ventana,bg='blue')
lbl37.place(x=170,y=490,width=80,height=80)

lbl47=Label(ventana,bg='sky blue')
lbl47.place(x=250,y=490,width=80,height=80)

lbl57=Label(ventana,bg='blue')
lbl57.place(x=330,y=490,width=80,height=80)

lbl67=Label(ventana,bg='sky blue')
lbl67.place(x=410,y=490,width=80,height=80)

lbl77=Label(ventana,bg='blue')
lbl77.place(x=490,y=490,width=80,height=80)

lbl87=Label(ventana,bg='skyblue')
lbl87.place(x=570,y=490,width=80,height=80)

lbl18=Label(ventana,bg='skyblue')
lbl18.place(x=10,y=570,width=80,height=80)

lbl28=Label(ventana,bg='blue')
lbl28.place(x=90,y=570,width=80,height=80)

lbl38=Label(ventana,bg='skyblue')
lbl38.place(x=170,y=570,width=80,height=80)

lbl48=Label(ventana,bg='blue')
lbl48.place(x=250,y=570,width=80,height=80)

lbl58=Label(ventana,bg='skyblue')
lbl58.place(x=330,y=570,width=80,height=80)

lbl68=Label(ventana,bg='blue')
lbl68.place(x=410,y=570,width=80,height=80)

lbl78=Label(ventana,bg='skyblue')
lbl78.place(x=490,y=570,width=80,height=80)

lbl88=Label(ventana,bg='blue')
lbl88.place(x=570,y=570,width=80,height=80)



ventana.mainloop()
