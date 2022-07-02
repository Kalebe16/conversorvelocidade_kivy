from kivymd.app import MDApp
from kivy.lang import Builder   
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import webbrowser



class JanelaGerenciadora(ScreenManager):
    pass

class JanelaPrincipal(Screen):
   pass

    
class Janela1(Screen):

    def limpar(self):
        self.ids.caixa_texto.text = ""
        self.ids.resposta.text = ""
        

    def calcular(self):
        # declarando variavel e atribuindo o seu tipo como float, e atribuindo seu 
        # valor ao input digitado na caixa de texto
        self.dialog = MDDialog(title = "ERRO", text="Algo deu errado, repita!", buttons=[MDFlatButton(text="OK", on_release = self.liberar)])
        try:
            v1 = float(self.ids.caixa_texto.text) 
            v2 = v1 / 3.6 # calculo necessario para se converter km em ms
            self.ids.resposta.text = "{:0.2f}".format(v2) + "m/s"
        except ValueError:
            self.dialog.open()

    def liberar(self, obj):
        self.dialog.dismiss()


class Janela2(Screen):
    def limpar(self):
        self.ids.caixa_texto.text = ""
        self.ids.resposta.text = ""

    def calcular(self):
        # declarando variavel e atribuindo o seu tipo como float, e atribuindo seu 
        # valor ao input digitado na caixa de texto
        self.dialog = MDDialog(title = "ERRO", text="Algo errado, repita!", buttons=[MDFlatButton(text="OK", on_release = self.liberar)])
        try:
            v1 = float(self.ids.caixa_texto.text) 
            v2 = v1 * 3.6 # calculo necessario para se converter km em ms
            self.ids.resposta.text = "{:0.2f}".format(v2) + "km/h"
        except ValueError:
            self.dialog.open()

    def liberar(self, obj):
        self.dialog.dismiss()
        
    
class ConversorApp(MDApp):

    def abrir_link(self):
        meu_site = "https://kalebeportfolio.netlify.app/"
        webbrowser.open(meu_site)


    # MUDA O TEMA DO APP
    def mudar_cor(self):
        tema = self.theme_cls.theme_style
        if tema == "Dark":
            self.theme_cls.theme_style = 'Light'
        else:
            self.theme_cls.theme_style = 'Dark'

    # Fecha a aplicação quando a função for chamada
    def fechar(self):
        self.stop()


    def voltar(self):
        # ESTA FUNÇÃO É NECESSARIA PORQUE O TOOLBAR NÃO RECONHECE ESSES METODOS NO LAMBDAX :
        ConversorApp.get_running_app().root.current = "janelaprincipal"
        ConversorApp.get_running_app().root.transition.direction='right'
        

    def build(self):
        self.theme_cls.primary_palette = "Amber"

        return Builder.load_file("app/style.kv")

    


