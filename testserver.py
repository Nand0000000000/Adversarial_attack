import requests

def test_server():
    try:
        response = requests.get(
            'http://ec2-54-85-67-162.compute-1.amazonaws.com:8080/',
            timeout=5
        )
        print(f"Status: {response.status_code}")
        print(f"Headers: {response.headers}")
    except Exception as e:
        print(f"Erro ao testar servidor: {e}")