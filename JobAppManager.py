from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkcalendar import DateEntry
import webbrowser

class Application:
    def __init__(self, job_title='', company='', salary='', date='', resume='', status = 0): 
        self.job_title = job_title
        self.company = company
        self.salary = salary
        self.resume = resume
        self.date = date
        self.status = status

job_app = {} 

def add_application():
    job_title = job_title_input.get()
    company = company_input.get()
    salary = salary_input.get()
    date = date_input.get()
    resume = resume_path.get()
    status = status_var.get()

    new_job = Application(job_title, company, salary, date, resume, status) 
    job_app[job_title] = new_job 
    display(new_job) 
    table.insert("", "end", values=(new_job.job_title, new_job.company, new_job.salary, new_job.date, status_labels.get(new_job.status, ''))) 
    clear_input() 

def resume(): 
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")],) 
    if file_path: 
        resume_path.set(file_path) 
        resume_link.config(text=file_path)

def open_pdf():
    file_path = resume_path.get()
    if file_path: 
        webbrowser.open(file_path)

def browse_resume_action():
    resume() 

def open_pdf_action(event=''):
    open_pdf() 

def clear_input(): 
    job_title_input.delete(0, 'end') 
    company_input.delete(0, 'end')
    salary_input.delete(0, 'end')
    status_var.set(0)  

def get_resume_path():
    resume_path.set(filedialog.askopenfilename) 

def display(current_job):
    job_app[current_job.job_title] = current_job

def delete_application(): 
    selected_item = table.selection() 
    if selected_item:
        job_title = table.item(selected_item, 'values')[0] 
        table.delete(selected_item) 
        job_app.pop(job_title) 

def edit_application():
    selected_item = table.selection()
    if selected_item:
        job_title = table.item(selected_item, 'values')[0]
        current_job = job_app.get(job_title) 
        if current_job:
            job_title_edit.delete(0, 'end')
            job_title_edit.insert(0, current_job.job_title)
            company_edit.delete(0, 'end')
            company_edit.insert(0, current_job.company)
            salary_edit.delete(0, 'end')
            salary_edit.insert(0, current_job.salary)
            date_input_edit.set_date(current_job.date)
            status_combobox.set(status_labels.get(current_job.status, '')) 
            switch_to_edit_window()

def save_changes():
    selected_item = table.selection()
    if selected_item:
        job_title = table.item(selected_item, 'values')[0]
        current_job = job_app.get(job_title)
        if current_job: 
            current_job.job_title = job_title_edit.get()
            current_job.company = company_edit.get()
            current_job.salary = salary_edit.get()
            current_job.date = date_input_edit.get()
            current_job.status = status_combobox.current()
            display(current_job)
            table.delete(selected_item)
            table.insert("", "end", values=(current_job.job_title, current_job.company, current_job.salary, current_job.date, status_labels.get(current_job.status, '')))
            switch_to_menu_window()

def save_changes_notes(): 
    selected_item = table.selection()
    if selected_item:
        job_title = table.item(selected_item, 'values')[0]
        current_job = job_app.get(job_title)
        if current_job:
            current_job.notes = additional_info_var.get() 

def switch_to_menu_window():
    menu_window.tkraise() 

def switch_to_edit_window():
    edit_window.tkraise()

window = Tk()
window.title('Application')
window.geometry('1100x700') 

job_title_edit = StringVar()
company_edit = StringVar()
salary_edit = StringVar()
date_input_edit = StringVar()
additional_info_var = StringVar()
resume_path = StringVar()

status_var = IntVar()
status_labels = {0: 'Applied', 1: 'Rejected', 2: 'Accepted'} 

menu_window = tk.Frame(window, borderwidth=2) 
menu_window.grid(row=0, column=0, sticky="nsew") 

edit_window = tk.Frame(window)
edit_window.grid(row=0, column=0, sticky="nsew")

switch_to_menu_window()

job_title_label = tk.Label(menu_window, text='Job Title: ')
job_title_label.grid(column=0, row=3, padx=10, pady=5)
job_title_input = tk.Entry(menu_window) 
job_title_input.grid(column=1, row=3, padx=10, pady=5)

company_label = Label(menu_window, text='Company: ')
company_label.grid(column=2, row=3, padx=10, pady=5)
company_input = Entry(menu_window)
company_input.grid(column=3, row=3, padx=10, pady=5)

salary_label = Label(menu_window, text='Salary: ')
salary_label.grid(column=4, row=3, padx=10, pady=5)
salary_input = Entry(menu_window)
salary_input.grid(column=5, row=3, padx=10, pady=5)

status_label = Label(menu_window, text='Status: ')
status_label.grid(column=0, row=4, padx=10, pady=5)

radio_button_applied = Radiobutton(menu_window, text='Applied', padx=20, variable=status_var, value=0).grid(column=1, row=4, padx=10, pady=5)
radio_button_rejected = Radiobutton(menu_window, text='Rejected', padx=20, variable=status_var, value=1).grid(column=2, row=4, padx=10, pady=5)
radio_button_accepted = Radiobutton(menu_window, text='Accepted', padx=20, variable=status_var, value=2).grid(column=3, row=4, padx=10, pady=5)

date_label = Label(menu_window, text='Application Date: ')
date_label.grid(column=4, row=4, padx=10, pady=5)

date_input = DateEntry(menu_window, selectmode='day',date_pattern='yyyy-mm-dd', width=10)
date_input.grid(column=5, row=4, padx=10, pady=5)

resume_label = ttk.Label(menu_window, text='Resume: ')
resume_label.grid(column=0, row=6, padx=10, pady=5)
resume_link = Label(menu_window, textvariable=resume_path, cursor="hand2", fg="blue")
resume_link.grid(column=1, row=6, padx=10, pady=5)

browse_button = ttk.Button(menu_window, text='Browse', command=browse_resume_action).grid(column=2, row=6, padx=10, pady=5)
resume_link.bind("<Button-1>", open_pdf_action)

header = ['Job Title', 'Company', 'Salary', 'Date', 'Status'] 
table = ttk.Treeview(menu_window, columns=header)
table['show'] = 'headings' 
for i in header: 
    table.heading(i, text = i)
table.grid(row = 1, column = 0, columnspan = 70, padx = 20, pady = 10)

delete_button = ttk.Button(menu_window, text="Delete", command=delete_application).grid(row=3, column=21)
edit_button = ttk.Button(menu_window, text="Edit", command=edit_application).grid(row=3, column=20)
save_input_button = ttk.Button(menu_window, text="Save", command=add_application).grid(row=7, column=0, pady=10, padx=10)
save_edit_button = ttk.Button(edit_window, text="Save Changes", command=save_changes).grid(row=5, column=0, pady=10)
save_notes_button = ttk.Button(menu_window, text="Save", command=save_changes_notes).grid(row=16, pady=10)

job_title_edit_label = Label(edit_window, text='Job Title: ').grid(row=0, column=0, padx=10, pady=5)
job_title_edit = Entry(edit_window)
job_title_edit.grid(row=0, column=1, padx=10, pady=5)

company_edit_label = Label(edit_window, text='Company: ').grid(row=1, column=0, padx=10, pady=5)
company_edit = Entry(edit_window)
company_edit.grid(row=1, column=1, padx=10, pady=5)

salary_edit_label = Label(edit_window, text='Salary: ').grid(row=2, column=0, padx=10, pady=5)
salary_edit = Entry(edit_window)
salary_edit.grid(row=2, column=1, padx=10, pady=5)

date_edit_label = Label(edit_window, text='Application Date: ').grid(row=3, column=0, padx=10, pady=5)
date_input_edit = DateEntry(edit_window, selectmode='day', date_pattern='yyyy-mm-dd', width=10)
date_input_edit.grid(row=3, column=1, padx=10, pady=5)

edit_status_label = Label(edit_window, text='Status: ').grid(row=4, column=0, padx=10, pady=5)
status_combobox = ttk.Combobox(edit_window, values=['Applied', 'Rejected', 'Accepted'])
status_combobox.grid(row=4, column=1, padx=10, pady=5)

notes_label = Label(menu_window, text='Notes').grid(row=11, column=0, padx=20, pady=5)
additional_info_input = Text(menu_window, height=10, width=50, relief=GROOVE, borderwidth=5).grid(row=12, column=0, columnspan=70, padx=20, pady=5, sticky="nsew") 

window.mainloop()