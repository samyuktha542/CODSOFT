import json
import os

class Task:
    def __init__(self, description, priority='normal'):
        self.description = description
        self.priority = priority
        self.completed = False

    def to_dict(self):
        return {
            'description': self.description,
            'priority': self.priority,
            'completed': self.completed
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(data['description'], data['priority'])
        task.completed = data['completed']
        return task

class ToDoList:
    def __init__(self, filename='todos.json'):
        self.filename = filename
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.tasks = [Task.from_dict(task) for task in json.load(f)]
        else:
            self.tasks = []

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def add_task(self, description, priority='normal'):
        task = Task(description, priority)
        self.tasks.append(task)
        self.save()

    def remove_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks.pop(task_number)
            self.save()
        else:
            print("Invalid task number.")

    def complete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number].completed = True
            self.save()
        else:
            print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(self.tasks):
                status = "✓" if task.completed else "✗"
                print(f"{index + 1}: [{status}] {task.description} (Priority: {task.priority})")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Complete Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task_description = input("Enter the task description: ")
            priority = input("Enter the task priority (low/normal/high): ").lower()
            if priority not in ['low', 'normal', 'high']:
                print("Invalid priority. Defaulting to 'normal'.")
                priority = 'normal'
            todo_list.add_task(task_description, priority)
            print(f'Task "{task_description}" added with priority "{priority}".')

        elif choice == '2':
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to remove: ")) - 1
                todo_list.remove_task(task_number)
                print("Task removed.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '3':
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to complete: ")) - 1
                todo_list.complete_task(task_number)
                print("Task marked as complete.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == '4':
            todo_list.view_tasks()

        elif choice == '5':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
