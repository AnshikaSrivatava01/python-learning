class StudentRecordManager:
    def __init__(self):
        self.records = {}

    def add_or_update(self, name, score):
        self.records[name] = score
        print(f"Recorded {name} with score {score}.")

    def get_top_student(self):
        if not self.records:
            return None, None  
        top_name = max(self.records, key=self.records.get)
        return top_name, self.records[top_name]

    def display_all(self):
        if not self.records:
            print("No records available.")
            return
        for name, score in self.records.items():
            print(f"{name}: {score}")      

manager = StudentRecordManager()
manager.add_or_update("Aman", 88)
manager.add_or_update("Pooja", 94)
manager.add_or_update("Aman", 96)            

top_name, top_score = manager.get_top_student()
print(f"Top student: {top_name} ({top_score})")