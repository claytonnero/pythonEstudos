from PIL import Image
import PIL.ImageOps as ops


im = Image.open("jujuEeu.jpg")
#inverte = ops.invert(im)
#inverte.save("inverso.png")

def inverteCores(imagem):
        
    arq = Image.open(imagem)
    nome = arq.filename.split(".")
    inverte = ops.invert(arq)
    #inverte.save(f"{nome[0]}.png")
    return inverte

rev =  inverteCores("azul.jpg")