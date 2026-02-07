class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.name}"

class Department:
    def __init__(self):
        self.list = []

    def add_worker(self, name, position, salary):
        new_worker = Employee(name, position, salary)
        self.list.append(new_worker)
        print(f"Співробітника '{name}' додано")

    def delete_worker(self, name):
        self.list = [worker for worker in self.list if worker.name != name]
        print(f"Співробітника '{name}' видалено")

    def list_workers(self):
        if not self.list:
            print("Список порожній")
        else:
            print("\nСписок робітників:")
            for worker in self.list:
                print(worker)
    
Department_list = Department()

Department_list.add_worker("Микола", "Менеджмент", "32500 грн.")
Department_list.add_worker("Ольга", "Ui/UX дизайнер", "345120 грн.")
Department_list.add_worker("Сергій", "Розробник ПЗ", "44200 грн.")

Department_list.list_workers()

Department_list.delete_worker("Сергій")

Department_list.list_workers()