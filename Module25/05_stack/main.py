class Stack:
    def __init__(self):
        self.__stack = []

    def __str__(self):
        return str(self.__stack)

    def get_stack(self):
        return self.__stack

    def push(self, element):
        self.__stack.append(element)

    def pop(self):
        if len(self.__stack) == 0:
            return None
        else:
            return self.__stack.pop()

    def delete(self, task):
        if task in self.__stack:
            resolve_add_top_elements = True
            top_elements = []
            for index, element in enumerate(reversed(self.__stack)):
                if element == task:
                    self.pop()
                    resolve_add_top_elements = False
                elif element != task and resolve_add_top_elements:
                    last_element = self.pop()
                    top_elements.append(last_element)
                elif element != task and not resolve_add_top_elements:
                    continue
            for index, element in enumerate(top_elements):
                self.push(element)
        else:
            print('Такого задания с таким приоритетом, нет')


class TaskManager:
    def __init__(self):
        self.tasks = dict()

    def __str__(self):
        if self.tasks:
            sorted_tasks = [f'{sorted_task[0]} {"; ".join(sorted_task[1].get_stack())}' for sorted_task in sorted(self.tasks.items())]
            string_tasks = '\n'.join(sorted_tasks)
            return f'Результат:\n{string_tasks}'
        else:
            print('Список задач пока пуст!')

    def new_task(self, task, priority):
        if priority not in self.tasks:
            self.tasks[priority] = Stack()
        self.tasks[priority].push(task)

    def delete_task(self, task, priority):
        if priority not in self.tasks:
            print('Такого приоритета не существует!')
        else:
            self.tasks[priority].delete(task)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("попить", 2)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
manager.delete_task("поесть", 2)
print(manager)
