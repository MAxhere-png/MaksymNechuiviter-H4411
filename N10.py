class Task:
    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.is_completed = False

    def mark_as_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "Виконано" if self.is_completed else "Не виконано"
        return f"[{status}] {self.name} (Дедлайн до:{self.deadline}): {self.description}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description, deadline):
       new_task = Task(name, description, deadline)
       self.tasks.append(new_task)
       print(f"Завдання '{name}' додано")

    def delete_task(self, name):
       self.tasks = [task for task in self.tasks if task.name != name]
       print(f"Завдання '{name}' видалено")

    def mark_task_completed(self, name):
        for task in self.tasks:
            if task.name == name:
                task.mark_as_completed()
                print(f"Завдання {name} відмічене як виконане.")
                return
        print(f"Завдання {name} не знайдене.")

    def list_tasks(self):
        if not self.tasks:
            print("Список завдань порожній")
        else:
            print("\nСписок завдань:")
            for task in self.tasks:
                print(task)

manager = TaskManager()

manager.add_task("Купити молоко", "В магазині біля дому", "2026-02-03")
manager.add_task("Зробити дз", "з фізики", "2026-02-06")

manager.list_tasks()

manager.mark_task_completed("Купити молоко")

manager.list_tasks()

manager.delete_task("Зробити дз")

manager.list_tasks()