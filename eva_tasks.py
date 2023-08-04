import customtkinter as ctk 



def add_task_todo():
    todo = entry.get()
    label = ctk.CTkLabel(scrollable_frame, text=todo)
    label.pack()

    entry.delete(0, ctk.END)

def eva_tasks():
    root = ctk.CTk()
    root.geometry("700x450")
    root.title("EVA Tasks")
    
    title_label = ctk.CTkLabel(root, text="Tasks List", font=ctk.CTkFont(size=30, weight="bold"))
    title_label.pack(padx=10, pady=(40, 20))

    global scrollable_frame
    scrollable_frame = ctk.CTkScrollableFrame(root, width=500, height=100)
    scrollable_frame.pack()

    global entry
    entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add task todo")
    entry.pack(fill="x")

    add_button = ctk.CTkButton(root, text="Add task", width=500, height=50, command=add_task_todo)
    add_button.pack(pady=20)

    root.mainloop()

eva_tasks()