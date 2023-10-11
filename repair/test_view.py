from django.urls import reverse 
import pytest
import requests
import login
import django.test.client
import pytest
import django.test.utils
from django.conf import settings

'''
@pytest.fixture
def admin_client():
    # Создаем пользователя с правами администратора
    user = User.objects.create_superuser(username='yras1337', password='yras1337')
    client = Client()
    client.login(username='yras1337', password='yras1337')
    return client
'''

def test_home_page(): # Get the home page 
    url = 'http://127.0.0.1:8000/'
    response = requests.get(url)
    assert response.status_code == 200




def test_detail_page(): # Get the home page 
    url = 'http://127.0.0.1:8000/2'
    response = requests.get(url)
    assert response.status_code == 200

def test_1():
    url = 'http://127.0.0.1:8000/?sort=ascending'
    response = requests.get(url)
    assert response.status_code == 200

def test_2():
    url = 'http://127.0.0.1:8000/?sort=descending'
    response = requests.get(url)
    assert response.status_code == 200

def test_3():
    url = 'http://127.0.0.1:8000/cart/'
    response = requests.get(url)
    assert response.status_code == 403

def test_4():
    url = 'http://127.0.0.1:8000/order/create/'
    response = requests.get(url)
    assert response.status_code == 403

def test_5():
    url = 'http://127.0.0.1:8000/statistic/'
    response = requests.get(url)
    assert response.status_code == 403

def test_6():
    url = 'http://127.0.0.1:8000/statistic/graph/'
    response = requests.get(url)
    assert response.status_code == 403

def test_7():
    url = 'http://127.0.0.1:8000/statistic/tables/'
    response = requests.get(url)
    assert response.status_code == 403

def test_8():
    url = 'http://127.0.0.1:8000/statistic/stupid/'
    response = requests.get(url)
    assert response.status_code == 403

def test_9():
    url = 'http://127.0.0.1:8000/statistic/predict/1/'
    response = requests.get(url)
    assert response.status_code == 403

def test_10():
    url = 'http://127.0.0.1:8000/%D0%9F%D0%BE%D0%BB%D1%8B/'
    response = requests.get(url)
    assert response.status_code == 200

def test_11():
    url = 'http://127.0.0.1:8000/%D0%9A%D0%BE%D0%B2%D1%80%D1%8B/'
    response = requests.get(url)
    assert response.status_code == 200

def test_12():
    url = 'http://127.0.0.1:8000/%D0%9F%D0%BE%D0%BB%D0%BD%D0%B0%D1%8F%20%D1%83%D0%B1%D0%BE%D1%80%D0%BA%D0%B0/'
    response = requests.get(url)
    assert response.status_code == 200

def test_13():
    url = 'http://127.0.0.1:8000/order/create/'
    response = requests.get(url)
    assert response.status_code == 200


'''
def test_with_authenticated_client_4(admin_client):
    response = admin_client.get('http://127.0.0.1:8000/statistic/predict/1/')
    assert response.status_code == 200
'''







    

