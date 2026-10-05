class TaskManager:
    def __init__(self):
        self.tasks = []


    #MUT-TM-01

    def add_task(self, title: str):
        if not title.strip():
            raise ValueError("Название задачи не может быть пустым")
        self.tasks.append({"title": title, "completed": False})

    # def add_task(self, title: str):
    #     # МУТАЦИЯ: убран not
    #     if title.strip():
    #         raise ValueError("Название задачи не может быть пустым")
    #     self.tasks.append({"title": title, "completed": False})

    # MUT-TM-02

    def complete_task(self, title: str):
        for task in self.tasks:
            if task["title"] == title:
                task["completed"] = True
                return
        raise KeyError("Задача не найдена")

    # def complete_task(self, title: str):
    #     for task in self.tasks:
    #         if task["title"] == title:
    #             # МУТАЦИЯ: присваивается False
    #             task["completed"] = False
    #             return
    #     raise KeyError("Задача не найдена")

    #MUT-TM-03
    def get_pending_tasks(self) -> list:
        return [t for t in self.tasks if not t["completed"]]

    # def get_pending_tasks(self) -> list:
    #     # МУТАЦИЯ: убран not
    #     return [t for t in self.tasks if t["completed"]]

    #MUT-TM-04
    def get_completed_tasks(self) -> list:
        return [t for t in self.tasks if t["completed"]]

    # def get_completed_tasks(self) -> list:
    #     # МУТАЦИЯ: добавлен not
    #     return [t for t in self.tasks if not t["completed"]]

    # MUT-TM-05
    def clear_completed(self):
        # ИСПРАВЛЕНО: Формирование нового списка только с незавершёнными задачами
        self.tasks = [task for task in self.tasks if not task["completed"]]

    # def clear_completed(self):
    #     # МУТАЦИЯ: убран not
    #     self.tasks = [task for task in self.tasks if task["completed"]]

    # MUT-TM-06
    # def get_total_tasks_count(self) -> int:
    #     return len(self.tasks)

    def get_total_tasks_count(self) -> int:
        # МУТАЦИЯ: прибавлена единица
        return len(self.tasks) + 1