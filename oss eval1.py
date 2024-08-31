# Task Management System

class TaskManagementSystem:
    def __init__(self):
        self.tasks = {}  

    def add_task(self, task_id, task_name, task_status):
        if task_id in self.tasks:
            print(f"Task with ID {task_id} already exists.")
        else:
            self.tasks[task_id] = {'name': task_name, 'status': task_status}
            print(f"Task added: ID={task_id}, Name={task_name}, Status={task_status}")

    def update_task(self, task_id, new_name=None, new_status=None):
        if task_id in self.tasks:
            if new_name:
                self.tasks[task_id]['name'] = new_name
            if new_status:
                self.tasks[task_id]['status'] = new_status
            print(f"Task updated: ID={task_id}, New Name={self.tasks[task_id]['name']}, New Status={self.tasks[task_id]['status']}")
        else:
            print(f"Task with ID {task_id} does not exist.")

    def delete_task(self, task_name):
        to_delete = [task_id for task_id, task_info in self.tasks.items() 
                     if task_info['name'] == task_name]
        if to_delete:
            for task_id in to_delete:
                del self.tasks[task_id]
            print(f"Task with name '{task_name}' have been deleted.")
        else:
            print(f"No task found with name '{task_name}'.")

    def list_tasks(self):
        if self.tasks:
            print("Listing all tasks:")
            for task_id, task_info in self.tasks.items():
                print(f"ID: {task_id}, Name: {task_info['name']}, Status: {task_info['status']}")
        else:
            print("No tasks available.")
            
            ##def searching_task(self):
                ##to_search = [task_id for tasl_id,task info in self.tasks.items()
                            ##if task_info['name'] == task_name]
                #if to_search:
                    ##for task_id in to_search:
                        ##del self.tasks[task_id]

def main():
    tms = TaskManagementSystem()
    
    # Example usage
    tms.add_task(1, "Ankush Gautam", "In Progress")
    tms.add_task(2, "Ayush Raina", "Not Started")
    tms.list_tasks()
    
    tms.update_task(1, new_status="Completed")
    tms.list_tasks()
    
    tms.delete_task("Read book")
    tms.list_tasks()

if __name__ == "__main__":
    main()
