from PIL import Image

# Carregar as imagens fornecidas pelo usuário
path_reprovado = "imagens/reprovado.jpg"
path_aprovado = "imagens/aprovado.jpg"

# Abrir as imagens
image_reprovado = Image.open(path_reprovado)
image_aprovado = Image.open(path_aprovado)

# Mostrar as imagens para garantir que foram carregadas corretamente
image_reprovado.show()
image_aprovado.show()
