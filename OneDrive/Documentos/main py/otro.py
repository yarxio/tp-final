
#Imports
import tkinter as tk


class app():
    #interfaz
    def __init__(self,L_CUADRADA):
        self.L_CUADRADO=L_CUADRADA
        self.imagenes={}

        self.ventana=tk()
        self.ventana.title('ajedrez de yarxio')
        self.ventana.iconbitmap('mekk_avramax.ico')
        self.ventana.geometry(f'({str(L_CUADRADA)*8}x{L_CUADRADA*8})')

        self.tablero=tk.Canvas(self.ventana)
        self.tablero.pack(fill='both',expand=True)

    def __call__(self):
        self.ventana.mainloop()


    def dibujotablero(self):
        #recuadro del tablero
        for i in range(8):

            for j in range(8):

                if (i+j)%2==0:
                    #cuadros azules
                    self.tablero.create_rectangle(i*self.L_CUADRADO,j**self.L_CUADRADO,(i+1)**self.L_CUADRADO,(j+1)*self.L_CUADRADO,)
                else:
                    #cuadros celeste
                    self.tablero.create_rectangle(i*self.L_CUADRADO,j**self.L_CUADRADO,(i+1)**self.L_CUADRADO,(j+1)*self.L_CUADRADO,)

    

    



