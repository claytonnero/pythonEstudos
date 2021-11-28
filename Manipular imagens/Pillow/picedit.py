from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen

gerente = """
<Gerente>:
    Principal:
        name:"principal"

"""
class Gerente(ScreenManager):
    Builder.load_string(gerente)

principal = """
<Principal>:
    # bg_light, bg_normal, 
    # bg_dark, bg_darkest
    md_bg_color:app.theme_cls.bg_dark
    MDToolbar:
        id:toolbar
        elevator:10
        title:"Editor de Fotografias"
        specific_text_color:app.theme_cls.accent_dark
        pos_hint:{"center_y": .97}
        md_bg_color:app.theme_cls.primary_dark
    Image:
        id:display
        source:root.imagem

"""  
class Principal(MDScreen):
    Builder.load_string(principal)
    
    imagem = ""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    
class PicEdit(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Purple"
        self.theme_cls.theme_style = "Dark"
        #print(sorted(dir(self.theme_cls)))
        
        
        return Gerente()

PicEdit().run()