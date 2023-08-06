import customtkinter as ctk 


labels_and_buttons = []

def delete_task(index):
    if len(labels_and_buttons) > index:
        label, button = labels_and_buttons[index]
        label.grid_remove()
        button.grid_remove()

    #labels_and_buttons.pop(index)

def add_task(labels_and_buttons):
    todo = entry.get()
    if todo == "":
        pass
    else:
        global label

        label = ctk.CTkLabel(scrollable_frame, text=todo)
        label.grid()

        delete_task_button = ctk.CTkButton(scrollable_frame, text="Remove task", command=lambda idx=len(labels_and_buttons): delete_task(idx))
        delete_task_button.grid()

        labels_and_buttons.append((label, delete_task_button))

        entry.delete(0, ctk.END)

def eva_tasks():
    root = ctk.CTk()
    root.geometry("700x450")
    root.title("EVA Tasks")
    
    title_label = ctk.CTkLabel(root, text="Tasks List", font=ctk.CTkFont(size=30, weight="bold"))
    title_label.grid(padx=275, pady=(40, 20))

    global scrollable_frame
    scrollable_frame = ctk.CTkScrollableFrame(root, width=500, height=100)
    scrollable_frame.grid()

    global entry
    entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add task todo")
    entry.grid(padx=175)
    #entry.grid(fill="x")

    add_button = ctk.CTkButton(root, text="Add task", width=500, height=50, command=lambda: add_task(labels_and_buttons))
    add_button.grid(pady=20)

    root.mainloop()
