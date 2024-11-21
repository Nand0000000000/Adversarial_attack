from PIL import Image

path_reprovado = "imagens/reprovado.jpg"
path_aprovado = "imagens/aprovado.jpg"

image_reprovado = Image.open(path_reprovado)
image_aprovado = Image.open(path_aprovado)

image_reprovado.show()
image_aprovado.show()
