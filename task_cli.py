#!/usr/bin/env python3
import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def main():
    tasks = load_tasks()
    print("=== Task Manager ===")
    print("Commands: add, list, done, delete, exit\n")

    while True:
        cmd = input("> ").strip().lower()

        if cmd == "exit":
            print("Goodbye!")
            break

        elif cmd == "add":
            task = input("Task: ").strip()
            if task:
                tasks.append({"text": task, "done": False})
                save_tasks(tasks)
                print(f"Added: {task}")
            else:
                print("Task cannot be empty.")

        elif cmd == "list":
            if not tasks:
                print("No tasks.")
            else:
                for i, t in enumerate(tasks, 1):
                    status = "x" if t["done"] else " "
                    print(f"{i}. [{status}] {t['text']}")

        elif cmd == "done":
            try:
                idx = int(input("Task number: ")) - 1
                if 0 <= idx < len(tasks):
                    tasks[idx]["done"] = True
                    save_tasks(tasks)
                    print(f"Marked done: {tasks[idx]['text']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif cmd == "delete":
            try:
                idx = int(input("Task number: ")) - 1
                if 0 <= idx < len(tasks):
                    removed = tasks.pop(idx)
                    save_tasks(tasks)
                    print(f"Deleted: {removed['text']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        else:
            print("Unknown command. Use: add, list, done, delete, exit")

if __name__ == "__main__":
    main()
