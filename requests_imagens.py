import requests

def classify_image(image_path):
    try:
        with open(image_path, 'rb') as image_file:
            files = {'file': image_file}
            headers = {
                'Accept': '*/*',
                'User-Agent': 'python-requests'
            }
            
            response = requests.post(
                'http://ec2-54-85-67-162.compute-1.amazonaws.com:8080/classify',
                files=files,
                headers=headers,
                timeout=10
            )
            
            response.raise_for_status()
            return response.text
            
    except requests.exceptions.Timeout:
        return "Erro: Tempo limite excedido"
    except requests.exceptions.RequestException as e:
        return f"Erro na requisição: {str(e)}"
    except Exception as e:
        return f"Erro: {str(e)}"