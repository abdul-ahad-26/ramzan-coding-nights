# Imports
import click
import json
import os

TODO_FILE = "todo.json"


# Function to load task from json
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)


# Function to save tasks to the JSON file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


@click.group()
def cli():
    """Simple To-Do List_tasks Manager"""
    pass


@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list_tasks"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    click.echo(f"Task added: {task} ")


@click.command()
def list_tasks():
    """List_tasks all tasks"""
    tasks = load_tasks()
    if not tasks:
        click.echo("No tasks found!")
        return
    for index, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        click.echo(f"{index }. {task['task']} [{status}]")


@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as completed"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_tasks(tasks)
        click.echo(f"Task {tasks[task_number-1]['task']} marked as completed! ✅")
    else:
        click.echo("Invalid task number.")


@click.command()
@click.argument("task_number", type=int)
def remove(task_number):
    """Remove a task from a list_tasks"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_tasks = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"Task {removed_tasks['task']} removed 🚮")

    else:
        click.echo("Invalid task number.")


cli.add_command(add)
cli.add_command(list_tasks)
cli.add_command(complete)
cli.add_command(remove)


if __name__ == "__main__":
    cli()
