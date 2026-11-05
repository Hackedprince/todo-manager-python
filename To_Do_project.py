import json

class TODO:
    def __init__(self,title):
        self.title = title
        self.completed = False

    #add method to complete
    def mark_done(self):
        self.completed = True

    #update todo class
    def to_dict(self):
        return{
            "title" : self.title,
            "completed" : self.completed
        }



    
#create todo manager
class TodoManager:

    def __init__(self):
        self.todos = []

    #add todo
    def add_todo(self,title):
        todo = TODO(title)
        self.todos.append(todo)

        #Update task
    def update_todo(self,index,new_title):
        if 0<= index < len(self.todos):
            self.todos[index].title = new_title

    #Delete task
    def delete_todo(self,index):
        if 0<= index <len(self.todos):
            del self.todos[index]

    #Save task to json
    def save_task(self):
        data = []

        for todo in self.todos:
            data.append(todo.to_dict())

        with open("tasks.json", "w") as file:
            json.dump(data, file, indent = 4)

    #show todo
    def show_todos(self):
        for index, todo in enumerate(self.todos,start=1):
            status = "Done" if todo.completed else "Pending"

            print(f"{index}. {todo.title} - {status}")

    #mark todo as completed
    def completed_todo(self, index):
        if 0<= index < len(self.todos):
            self.todos[index].mark_done()

    #Load Task from json
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                data = json.load(file)

                for item in data:
                    todo = TODO(item['title'])
                    todo.completed = item['completed']
                    self.todos.append(todo)

        except FileNotFoundError:
            pass

##-----user input------------##

manager = TodoManager()
manager.load_tasks()

while True:
    print("\n============TODO MENU==========")
    print("1. Add Task")
    print("2. View Task")
    print("3. Complete Task")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Save Task")
    print("7. Exit Task")


    choice = input("Enter Your Choice: ")

    if choice == "1":
        title = input("Enter Task: ")
        manager.add_todo(title)

        print("Task Added!")

    elif choice == "2":
        manager.show_todos()

    elif choice == "3":
        manager.show_todos()

        task_no = int(input("Enter Task number: "))
        manager.completed_todo(task_no - 1)

        print("Task Completed!")

    elif choice == "4":
        manager.show_todos()

        task_no = int(input("Enter Task Number: "))
        new_title = input("Enter New Title: ")

        manager.update_todo(task_no -1 , new_title)

        print("Task Updated!")

    elif choice == "5":
        manager.show_todos()

        task_no = int(input("Enter Task Number: "))
        manager.delete_todo(task_no - 1)

        print("Task Completed")

    elif choice == "6":
        manager.save_task()

        print("Task Saved!")

    elif choice == "7":
        manager.save_task()
        break


    else:
        print("Invalid Choice!")
