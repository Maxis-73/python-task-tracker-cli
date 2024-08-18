import click
import JsonManager
from datetime import datetime
from tabulate import tabulate

@click.group()
def cli():
    pass

# Listing tasks
@cli.command()
def list():
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
    try:
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
    except:
        print("An exception occurred")

if __name__ == '__main__':
    cli()