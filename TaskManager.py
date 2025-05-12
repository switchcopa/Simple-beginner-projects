import json
from datetime import datetime
import uuid

path = "C:\\Users\\100TR\\OneDrive\\PythonStartlearning\\python_basically\\tasks.json"

class Task:
    def __init__(self):
        self.id = None
        self.title = None
        self.completed = None
        self.description = None
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
        self.priority = None
        self.due_date = None
        self.group = None
        self.tags = []
        self.starred = False

    def create_task(self, id, title, description=None, priority=None, due_date=None, completed=False, group=None, tags=[], starred=False):
        data = {
            "id": id,
            "title" : title,
            "priority" : priority,
            "due_date" : due_date,
            "created_at": self.created_at,
            "updated_at" : self.updated_at,
            "description" : description,
            "completed": completed,
            "group": group,
            "tags": tags,
            "starred": starred
            }

        try:
            with open(path, 'r') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            tasks = {}

        k = f"task {len(tasks) + 1}"
        tasks[k] = data

        with open(path, 'w') as file:
            json.dump(tasks, file, indent=4)

    def check_task(self, id):
        try:
            with open(path, 'r') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            print("File not found")
            return False

        for task, data in tasks.items():
            if data["id"] == id:
                data["completed"] = True
                break
        else:
            return False
        
        with open(path, 'w') as file:
            json.dump(tasks, file, indent=4)

        return True
    
    def delete_task(self, id):
        try:
            with open(path, 'r') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("File not found")
        
        for task, data in tasks.items():
            if data["id"] == id:
                tasks.pop(task)
                break
        else: 
            print("Task id not found")
            return False

        with open(path, 'w') as file:
            json.dump(tasks, file, indent=4)

        return True
    
    def find_group(self, group):
        try:
            with open(path, 'r') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("File not found")
        
        items = []

        for task, data in tasks.items():
            if data["group"] == group:
                items.append((task ,data["title"]))
        
        if not items:
            print("Group not found")
            return False
        
        
        return items
    
    def completed_tasks(self):
        try:
            with open(path, 'r') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("File not found")
        
        items = []

        for task, data in tasks.items():
            if data["completed"] == True:
                items.append((task ,data["title"]))

        if not items:
            print("No completed task")  
            return False

        return items
    
    def update_task(self, id, **kwargs):
        try:
            with open(path, 'r') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("File not found")
        
        for task, data in tasks.items():
            if data["id"] == id:
                data.update(kwargs)
                data["updated_at"] = datetime.now().isoformat()
                break
        else:
            print("Task id not found")
            return False
        
        with open(path, 'w') as file:
            json.dump(tasks, file, indent=4)

        return True
    
    def star_unstar_task(self, id):
        try:
            with open(path, 'r') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("File not found")
        
        for task, data in tasks.items():
            if data["id"] == id:
                if data["starred"] == False:
                    data["starred"] = True
                    break
                elif data["starred"] == True:
                    data["starred"] = False
                    break
        else:
            print("Task id not found")
            return False
        
        with open(path, 'w') as file:
            json.dump(tasks, file, indent=4)

        return True
    
    def starred_tasks(self):
        try:
            with open(path, 'r') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("File not found")
        
        l = []
        for task, data in tasks.items():
            if data["starred"] == True:
                l.append((task ,data["title"]))
        
        if not l:
            print("No starred task found")
            return False
        
        with open(path, 'w') as file:
            json.dump(tasks, file, indent=4)

        return l

    def display_data(self, id):
        try: 
            with open(path, 'r') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError
        
        for task, data in tasks.items():
            if data["id"] == id:
                for k, v in data.items():
                    print(k, ":", v)
                break  
        else:
            print("Task not found")
        
        return False
    
    def display_tasks(self):
        try: 
            with open(path, 'r') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError
        
        for task, data in tasks.items():
            print("Task:", task + " | " + "Title", data["title"], " | " + "ID", data["id"])
        
def loop():

    print("##-------> Task Manager <-------##\n")

    while True:
        t = Task()
        option = input("Select option:\n1. Display tasks (❁´◡`❁)\n2. Add Task ➕\n3. Delete Task 🗑️\n4. Check task ✅\n5. Update Task\n6. Display tasks in a group 🌇\n7. Completed tasks ☑️\n8. Star/Unstar a task ⭐\n9. Show starred tasks ⭐\n10. Leave ⬅️\n")

        if option == "1":
            t.display_tasks()
        elif option == "2":
            task_id = str(uuid.uuid4()) 
            title = input("Enter task title: ")
            description = input("Enter a description for your task: ")
            priority = int(input("Enter (integer) priority for task: "))

            while True:
                due_date = input("Enter due date (DD/MM/YYYY HH:MM): ")
                try:
                    dt = datetime.strptime(due_date, "%d/%m/%Y %H:%M")
                    break
                except ValueError:
                    print("Invalid format! (Please use DD/MM/YYYY HH:MM)")

            t.create_task(task_id, title=title, description=description, priority=priority, due_date=dt.strftime("%d/%m/%Y %H:%M"))
            print("Task created successfully! ✅")
        elif option == "3":
            task_id = input("Enter task id: ")
            b = t.delete_task(task_id)
            if b:
                print("Task deleted successfuly ✅")
            else:
                print("Task id doens't exist ❌")
        elif option == "4":
            task_id = input("Enter task id: ")
            b = t.check_task(task_id)
            if b:
                print("Task cheked ✅ Keep it up!")
            else:
                print("Task id doens't exist ❌")
        elif option == "5":
            fields = ["title", "priority", "description", "group", "tags", "due_date"]
            try:
                task_id = input("Enter task ID: ")
            except ValueError:
                print("Invalid ID format ❌")
                continue

            print("\nCurrent Task Data:")
            t.display_data(task_id)

            print("\nFields you can update:")
            for field in fields:
                print("-", field)

            field = input("\nEnter the field to update: ").strip().lower()
            if field not in fields:
                print("Invalid field ❌")
                continue

            if field == "priority":
                try:
                    new_value = int(input("Enter new priority (integer): "))
                except ValueError:
                    print("Priority must be an integer ❌")
                    continue

            elif field == "tags":
                new_value = input("Enter tags separated by spaces: ").split()

            elif field == "due_date":
                try:
                    new_value = input("Enter new due date (DD/MM/YYYY HH:MM): ")
                    new_value = datetime.strptime(new_value, "%d/%m/%Y %H:%M").strftime("%d/%m/%Y %H:%M")
                except ValueError:
                    print("Invalid date format ❌")
                    continue

            else:
                new_value = input(f"Enter new value for {field}: ")

            updated = t.update_task(task_id, **{field: new_value})
            if updated:
                print(f"{field.capitalize()} updated successfully ✅")
            else:
                print("Task not found or update failed ❌")


        elif option == "6":
            group = input("Enter a group name: ")
            t.find_group(group)
        elif option == "7":
            t.completed_tasks()

        elif option == "8":
            task_id = input("Enter task id ")
            t.star_unstar_task(task_id)

        elif option == "9":
            l = t.starred_tasks()
            print(l)
        elif option == "10":
            break
        else:
            print("Enter a valid option")
            
if __name__ == '__main__':
    loop()