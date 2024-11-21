import os
import numpy as np
from PIL import Image
from imagens_base import path_reprovado
from requests_imagens import classify_image

output_dir = "imagens_perturbadas"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

original_image = Image.open(path_reprovado)

def perturb_image(image, epsilon=0.1, noise_type='uniform'):
    img_array = np.array(image).astype(np.float32) / 255.0
    
    if noise_type == 'uniform':
        noise = np.random.uniform(-epsilon, epsilon, img_array.shape)
    elif noise_type == 'gaussian':
        noise = np.random.normal(0, epsilon, img_array.shape)
    elif noise_type == 'salt_pepper':
        noise = np.zeros(img_array.shape)
        pepper = np.random.random(img_array.shape) < epsilon/2
        salt = np.random.random(img_array.shape) < epsilon/2
        noise[pepper] = -1
        noise[salt] = 1
    
    perturbed_img_array = np.clip(img_array + noise * 2, 0, 1)
    perturbed_img_array = (perturbed_img_array - 0.5) * 1.5 + 0.5
    perturbed_img_array = np.clip(perturbed_img_array, 0, 1)
    
    return Image.fromarray((perturbed_img_array * 255).astype(np.uint8))


noise_types = ['uniform', 'gaussian', 'salt_pepper']
for noise_type in noise_types:
    for i in range(20):  
        epsilon = 0.1 * (i + 1)  
        perturbed_image = perturb_image(original_image, epsilon=epsilon, noise_type=noise_type)
        
        temp_path = os.path.join(output_dir, f"perturbed_{noise_type}_{i}.jpg")
        perturbed_image.save(temp_path)
        
        result = classify_image(temp_path)
        print(f"Tipo: {noise_type}, Iteração {i+1}, Epsilon: {epsilon:.2f}: {result}")
        
        if "aprovado" in result.lower():
            print(f"Sucesso! Imagem aprovada com {noise_type}, epsilon={epsilon:.2f}")
            break