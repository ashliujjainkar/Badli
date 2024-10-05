import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_list(client):
    response = client.get('/list')
    assert response.status_code == 200

def test_add(client):
    response = client.post('/add', json={'task':'New Task'})
    assert response.status_code == 201

def test_complete(client):
    list_response =client.get('/list')
    assert list_response.status_code == 200
    tasks = list_response.get_json()
    print(tasks)

    incomplete_task = next(task for task in tasks if not task['completed'])
    task_id = incomplete_task['id']
    print("Testing task",incomplete_task)

    complete_response = client.post('/complete',json={'id': task_id})
    assert complete_response.status_code == 200

    updated_list_response = client.get('/list')
    updated_tasks = updated_list_response.get_json()

    completed_task = next(task for task in updated_tasks if task['id']==task_id)
    assert completed_task['completed'] == True


def test_incomplete(client):
    list_response = client.get('/list')
    assert list_response.status_code == 200
    tasks = list_response.get_json()
    print(tasks)

    complete_task = next(task for task in tasks if task['completed'])
    task_id = complete_task['id']
    print("Testing task",complete_task)

    incomplete_response = client.post('/incomplete',json={'id': task_id})
    assert incomplete_response.status_code == 200

    updated_list_response = client.get('/list')
    updated_tasks = updated_list_response.get_json()

    incomplete_task = next(task for task in updated_tasks if task['id'] == task_id)
    assert incomplete_task['completed'] == False


