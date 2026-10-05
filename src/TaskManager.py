class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title: str):
        if not title.strip():
            raise ValueError("Название задачи не может быть пустым")
        self.tasks.append({"title": title, "completed": False})

    def complete_task(self, title: str):
        for task in self.tasks:
            if task["title"] == title:
                task["completed"] = True
                return
        raise KeyError("Задача не найдена")

    def get_pending_tasks(self) -> list:
        return [t for t in self.tasks if not t["completed"]]

    def get_completed_tasks(self) -> list:
        return [t for t in self.tasks if t["completed"]]

    # def clear_completed(self):
    #     # БАГ: Удаление элементов из списка во время итерации по нему.
    #     # Если идут две выполненные задачи подряд, вторая будет пропущена.
    #     for task in self.tasks:
    #         if task["completed"]:
    #             self.tasks.remove(task)

    def clear_completed(self):
        # ИСПРАВЛЕНО: Формирование нового списка только с незавершёнными задачами
        self.tasks = [task for task in self.tasks if not task["completed"]]

    def get_total_tasks_count(self) -> int:
        return len(self.tasks)