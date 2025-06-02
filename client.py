import requests

BASE_URL = "http://127.0.0.1:8000"

def test_get_root():
    try:
        response = requests.get(f"{BASE_URL}/")
        print("GET /:", response.status_code, response.json())
    except Exception as e:
        print("Erreur GET /:", e)

def test_get_test():
    try:
        response = requests.get(f"{BASE_URL}/test")
        print("GET /test:", response.status_code, response.json())
    except Exception as e:
        print("Erreur GET /test:", e)

if __name__ == "__main__":
    test_get_root()
    test_get_test()
