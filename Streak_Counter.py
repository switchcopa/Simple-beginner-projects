import json
from datetime import datetime, timedelta
import uuid

path = "C:\\Users\\100TR\\OneDrive\\PythonStartlearning\\Streaks.json"

class streak:
    def __init__(self):
        self.id = None
        self.title = None
        self.description = None
        self.start_date = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.end_date = datetime.now() + timedelta(days=1)
        self.last_updated = datetime.now()
        self.count = 1
        
    def create_streak(self, id, title, start_date, end_date, description=None):
        data = {
            "id" : id,
            "title" : title,
            "start_date" : start_date,
            "end_date" : end_date.strftime("%d/%m/%Y %H:%M"),
            "last_updated" : self.last_updated.strftime("%d/%m/%Y %H:%M"),
            "streak_count" : self.count,
            "description" : description
        }

        try:
            with open(path, 'r') as file:
                streaks = json.load(file)

        except FileNotFoundError:
            streaks = {}

        s = f"Streak {len(streaks) + 1}"
        streaks[s] = data

        with open(path, 'w') as file:
            json.dump(streaks, file, indent=4)

        return True
        
    def delete_streak(self, id):
        try:
            with open(path, 'r') as file:
                streaks = json.load(file)

        except FileNotFoundError:
            raise FileNotFoundError("File not found")
        

        for streak, data in streaks.items():
            if data["id"] == id:
                streaks.pop(streak)
                break
        else:
            print("Streak ID not found")
            return False
    
        with open(path, 'w') as file:
            json.dump(streaks, file, indent=4)

        return True
    
    def update_streak(self, id):
        try:
            with open(path, 'r') as file:
                streaks = json.load(file)

        except FileNotFoundError:
            raise FileNotFoundError("File not found")
        
        update_date = datetime.now()
        for streak, data in streaks.items():

            if data["id"] == id:
                end_date = datetime.strptime(data["end_date"], "%d/%m/%Y %H:%M")
                last_updated = datetime.strptime(data["last_updated"], "%d/%m/%Y %H:%M")

                if last_updated.date() == update_date.date():
                    print("You've already updated your streak today! ⛔")
                    return False
                
                if update_date < end_date:
                    data["streak_count"] += 1
                else:

                    print("Streak broken ☹️")
                    data["streak_count"] = 1
                
                data["end_date"] = (update_date + timedelta(days=1)).strftime("%d/%m/%Y %H:%M")
                    
                break
        else:
            print("Streak ID not found")
            return False

        with open(path, 'w') as file:
            json.dump(streaks, file, indent=4)
        
        return True
    
    def show_streaks(self):
        try: 
            with open(path, 'r') as file:
                streaks = json.load(file)

        except FileNotFoundError:
            raise FileNotFoundError
        
        for streak, data in streaks.items():
            if data["streak_count"] == 1:
                print(data["title"] + ":", data["streak_count"], "Day 🔥\nID:", data["id"])
                continue

            print(data["title"] + ":", data["streak_count"], "Days 🔥\nID:", data["id"])

    
def loop():
    s = streak()

    while True:
        option = input("Choose an option:\n1. Create New Streak 📅\n2. Update Streak ⭐\n3. Delete Streak 🗑️\n4. Show Streaks ❤️\n")

        if option == "1":
            id = str(uuid.uuid4())
            title = input("Enter a title: ")
            description = input("Enter a description: ")

            b = s.create_streak(id, title, s.start_date, s.end_date, description)
            if b:
                print("Streak created successfully! ✅")
            else:
                print("Failed to create streak ❌")

        elif option == "2":
            id = str(input("Enter streak ID: "))
            b = s.update_streak(id)

            if b:
                print("Updated streak successfully! ✅")
            else:
                print("Failed to update streak ❌")

        elif option == "3":
            id = str(input("Enter streak ID: "))

            b = s.delete_streak(id)

            if b:
                print("Deleted streak successfully! ✅") 
            else:
                print("Failed to delete streak ❌")

        elif option == "4":
            s.show_streaks()
            
if __name__ == '__main__':
    loop()