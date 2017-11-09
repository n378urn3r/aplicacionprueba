import wpf, ctypes

from models import persona

from System.Windows import Application, Window

class mensajes(object):
    def Mbox(self,title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'aplicacionprueba.xaml')
        self.txt_nombre.Text = 'Ingrese su nombre'
        self.txt_apellido.Text = 'Ingrese su apellido'
    
    def btn_boton_Click(self, sender, e):
        p = persona()
        self.txt_nombre.Text = 'Juan'
        self.txt_apellido.Text = 'Perez'
        p.guardar(self.txt_nombre.Text,self.txt_apellido.Text )
    
    def btn_guardarotro_Click(self, sender, e):
        m = mensajes()
        p = persona()
        p.guardar(self.txt_nombre.Text,self.txt_apellido.Text )
        m.Mbox('Aviso', 'Guardado Correctamente',1)

if __name__ == '__main__':
    Application().Run(MyWindow())
