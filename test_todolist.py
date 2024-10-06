from todolist import ToDoList
import pytest

@pytest.fixture
def todolist():
    return ToDoList()

def test_add_task():
    todolist = ToDoList()
    todolist.add("task1")
    assert todolist.todo[0]['task'] == "task1"
    assert todolist.todo[0]['id'] == 0
    assert todolist.todo[0]['completed'] == False

def test_add_multiple_task():
    todolist = ToDoList()
    todolist.add("Task 1")
    todolist.add("Task 2")
    assert len(todolist.todo) == 2
    
    

def test_remove_task():
    todolist = ToDoList()
    todolist.add("task1")
    todolist.add("task2")
    todolist.add("task3")
    todolist.remove(1)
    assert todolist.todo[1]['active'] == False

def test_complete_task():
    todolist = ToDoList()
    todolist.add("task1")
    todolist.complete(0)
    assert todolist.todo[0]['completed'] == True

def test_incomplete_task():
    todolist = ToDoList()
    todolist.add("task1")
    todolist.add("task2")
    todolist.incomplete(1)
    assert todolist.todo[1]['completed'] == False

def test_list():
    todolist = ToDoList()
    todolist.add("task1")
    todolist.add("task2")
    assert len(todolist.list()) == 2

def test_value_error():
    todolist = ToDoList()
    with pytest.raises(ValueError, match = "Check the task id provided"):
        # todolist.add(1)
        todolist.remove(1)
    with pytest.raises(ValueError, match = "Check the task id provided"):
        todolist.complete(1)
    with pytest.raises(ValueError, match = "Check the task id provided"):
        todolist.incomplete(1)








