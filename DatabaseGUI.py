import tkinter as tk
from tkinter import ttk
from Manager import databaseInterface


# Search for and Delete from database
class ManageDatabase:
    def __init__(self, master, task):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)
        master.title(task + " data")

        self.heading = "Enter name to " + task + " a person."
        tk.Label(self.frame, text=self.heading).grid(pady=20, row=1, column=1)

        self.firstName = tk.StringVar()
        tk.Label(self.frame, text="First Name:", width=10).grid(pady=5, row=2, column=1)
        self.firstNameEntry = tk.Entry(self.frame, width=10, textvariable=self.firstName).grid(pady=5, padx=5,
                                                                                               row=2, column=2)

        self.lastName = tk.StringVar()
        tk.Label(self.frame, text="Last Name:", width=10).grid(pady=5, row=3, column=1)
        self.lastNameEntry = tk.Entry(self.frame, width=10, textvariable=self.lastName).grid(pady=5, padx=5,
                                                                                             row=3, column=2)

        # Button
        if task == "Search":
            tk.Button(self.frame, width=20, text=task, command=self.Search).grid(pady=15, padx=5, row=4, column=1)
        elif task == "Delete":
            tk.Button(self.frame, width=20, text=task, command=self.Delete).grid(pady=15, padx=5, row=4, column=1)

    # search function

    def Search(self):
        data = databaseInterface.searchPeople(self.firstName.get(), self.lastName.get())
        DatabaseView(self.master, data)

    def Delete(self):
        databaseInterface.deletePerson(self.firstName.get(), self.lastName.get())
        tk.messagebox.showinfo(title=None, message=('Successfully deleted "' + self.firstName.get() + ' '
                                                    + self.lastName.get() + '" from the database'))


# Show Full Database
class DatabaseView:
    def __init__(self, master, data):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(self.frame, text="View Database", width=25).grid(pady=5, column=1, row=1)

        self.databaseView = tk.ttk.Treeview(self.frame)
        self.databaseView.grid(pady=5, column=1, row=2)
        self.databaseView["show"] = "headings"
        self.databaseView["columns"] = ("attendeeid", "firstName", "lastName",
                                        "email", "address", "city", "state", "zipcode",
                                        "phone", "ismember", "isbeliever")

        # all treeview column headings
        self.databaseView.heading("attendeeid", text="Attendee ID")
        self.databaseView.heading("firstName", text="First Name")
        self.databaseView.heading("lastName", text="Last Name")
        self.databaseView.heading("email", text="Email")
        self.databaseView.heading("address", text="Address")
        self.databaseView.heading("city", text="City")
        self.databaseView.heading("state", text="State")
        self.databaseView.heading("zipcode", text="Zip Code")
        self.databaseView.heading("phone", text="Phone")
        self.databaseView.heading("ismember", text="Member?")
        self.databaseView.heading("isbeliever", text="Christian?")

        # create all treeview columns
        self.databaseView.column("attendeeid", width=100)
        self.databaseView.column("firstName", width=100)
        self.databaseView.column("lastName", width=100)
        self.databaseView.column("city", width=100)
        self.databaseView.column("email", width=100)
        self.databaseView.column("state", width=40)
        self.databaseView.column("zipcode", width=50)
        self.databaseView.column("address", width=100)
        self.databaseView.column("phone", width=100)
        self.databaseView.column("email", width=100)
        self.databaseView.column("ismember", width=60)
        self.databaseView.column("isbeliever", width=60)

        for value in data:
            self.databaseView.insert('', 'end', values=value)
