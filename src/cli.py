import click
import JsonManager
from datetime import datetime
from tabulate import tabulate

@click.group()
def cli():
    pass

# Listing tasks
@cli.command()
def tasks():
    data = JsonManager.read_json()
    if len(data) <= 0:
        print('There are no pending tasks')
    else:
        table_data = []
        table_data.append(['ID', 'Description', 'Status', 'Created At', 'Updated At'])
        for task in data:
            aux = [task['id'], task['description'], task['status'], task['createdAt'], task['updatedAt']]
            table_data.append(aux)
        print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))

# Creating a new task
@cli.command()
@click.argument('task', type=str)
def add(task):
    data = JsonManager.read_json()
    newID = len(data) + 1
    now = datetime.now()
    task = {
        'id': newID,
        'description': task,
        'status': 'todo',
        'createdAt': now.strftime("%d/%m/%Y %H:%M:%S"),
        'updatedAt': ''
    }
    data.append(task)
    JsonManager.write_json(data)
    print(f"Task added successfully (ID: {task['id']})")

#Deleting task
@cli.command()
@click.argument('id', type=int)
def delete(id):
    data = JsonManager.read_json()
    for x in data:
        if x['id'] == id:
            task = x
        else:
            task = None
        break
    if task is not None:
        data.remove(task)
        JsonManager.write_json(data)
        print('Task deleted')
    else:
        print('Task not found')

@cli.command()
@click.argument('id', type = int)
@click.option('--task', required=True, help="New task description")
def update(id, task):
    data = JsonManager.read_json()
    item = next((t for t in data if t['id'] == id), None)
    if not item:
        print(f'Task with ID {id} not found')
    else:
        if task is not None:
            item['description'] = task
            now = datetime.now()
            item['updatedAt'] = now.strftime("%d/%m/%Y %H:%M:%S")
        JsonManager.write_json(data)
        print(f'Task with ID {id} has been updated')

if __name__ == '__main__':
    cli()