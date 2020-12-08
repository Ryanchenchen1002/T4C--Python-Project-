import tkinter as tk
from tkinter import ttk
from Manager import databaseInterface


class EventNew:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.eventName = tk.StringVar()
        tk.Label(self.frame, text="Event Name", width=15).grid(column=1, row=1, sticky=tk.E)
        tk.Entry(self.frame, width=20, textvariable=self.eventName).grid(column=2, row=1)

        self.eventTime = tk.StringVar()
        tk.Label(self.frame, text="Event Time", width=15).grid(column=1, row=2, sticky=tk.E)
        tk.Entry(self.frame, width=20, textvariable=self.eventTime).grid(column=2, row=2)

        self.eventDate = tk.StringVar()
        tk.Label(self.frame, text="Event Date", width=15).grid(column=1, row=3, sticky=tk.E)
        tk.Entry(self.frame, width=20, textvariable=self.eventDate).grid(column=2, row=3)

        self.eventDesc = tk.StringVar()
        tk.Label(self.frame, text="Event Description", width=15).grid(column=1, row=4, sticky=tk.E)
        tk.Entry(self.frame, width=20, textvariable=self.eventDesc).grid(column=2, row=4, rowspan=2)

        for child in self.frame.winfo_children():
            child.grid_configure(padx=5, pady=3)

        tk.Button(self.frame, width=10, text="Add", command=self.AddEvent).grid(pady=5, padx=5,
                                                                                column=1, row=12)
        tk.Button(self.frame, width=10, text="Clear", command=self.ResetEntries).grid(pady=5, padx=5,
                                                                                      column=2, row=12)
        tk.Button(self.frame, width=10, text="Close", command=self.master.destroy).grid(pady=5, padx=5,
                                                                                        column=1, row=13)

    def AddEvent(self):
        eventNew = (self.eventName.get(), self.eventTime.get(), self.eventDate.get(), self.eventDesc.get())
        databaseInterface.submitEvent(eventNew)

    def ResetEntries(self):
        self.eventName.set("")
        self.eventTime.set("")
        self.eventDate.set("")
        self.eventDesc.set("")


class EventManage:
    def __init__(self, master, task):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)
        master.title(task + " data")

        self.heading = "Search for a Event/Delete a Event."
        tk.Label(self.frame, text=self.heading).grid(pady=20, row=1, column=1)

        self.eventName = tk.StringVar()
        tk.Label(self.frame, text="Event Name", width=10).grid(pady=5, row=2, column=1)
        tk.Entry(self.frame, width=10, textvariable=self.eventName).grid(pady=5, padx=5, row=2, column=2)

        # Button
        if task == "Search":
            tk.Button(self.frame, width=20, text=task, command=self.Search).grid(pady=15, padx=5, row=4, column=1)
        elif task == "Delete":
            tk.Button(self.frame, width=20, text=task, command=self.Delete).grid(pady=15, padx=5, row=4, column=1)

    def Search(self):
        data = databaseInterface.viewEvent(self.eventName.get())
        DatabaseView(self.master, data)

    def Delete(self):
        databaseInterface.deleteEvent(self.eventName.get())
        tk.messagebox.showinfo(title=None, message=('Successfully deleted "' + self.eventName.get()
                                                    + '" from the database'))


class DatabaseView:
    def __init__(self, master, data):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(self.frame, text="View Database", width=25).grid(pady=5, column=1, row=1)

        self.databaseView = tk.ttk.Treeview(self.frame)
        self.databaseView.grid(pady=5, column=1, row=2)
        self.databaseView["show"] = "headings"
        self.databaseView["columns"] = ("eventID", "eventName", "eventTime", "eventDate", "eventDesc")

        # all treeview column headings
        self.databaseView.heading("eventID", text="Event ID")
        self.databaseView.heading("eventName", text="Event Name")
        self.databaseView.heading("eventTime", text="Event Time")
        self.databaseView.heading("eventDate", text="Event Date")
        self.databaseView.heading("eventDesc", text="Event Description")

        # create all treeview columns
        self.databaseView.column("eventID", width=100)
        self.databaseView.column("eventName", width=100)
        self.databaseView.column("eventTime", width=100)
        self.databaseView.column("eventDate", width=100)
        self.databaseView.column("eventDesc", width=400)

        for value in data:
            self.databaseView.insert('', 'end', values=value)


class Attendance:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)
        master.title("Manage Attendance")

        self.firstName = tk.StringVar()
        tk.Label(self.frame, width=25, text="First Name").grid(column=1, row=1)
        tk.Entry(self.frame, width=20, textvariable=self.firstName).grid(column=2, row=1)

        self.lastName = tk.StringVar()
        tk.Label(self.frame, width=25, text="Last Name").grid(column=1, row=2)
        tk.Entry(self.frame, width=20, textvariable=self.lastName).grid(column=2, row=2)

        self.roleName = ("Attendee", "Volunteer")
        tk.Label(self.frame, width=25, text="Role").grid(column=1, row=3)
        ttk.Combobox(self.frame, values=self.roleName, width=20, state='readonly').grid(column=2, row=3)

        self.eventName = tk.StringVar()
        tk.Label(self.frame, width=25, text="Event Name").grid(column=1, row=4)
        tk.Entry(self.frame, width=20, textvariable=self.eventName).grid(column=2, row=4)

        for child in self.frame.winfo_children():
            child.grid_configure(padx=5, pady=3)

        tk.Button(self.frame, width=20, text="Add", command=self.AddNew).grid(padx=5, pady=5, column=1, row=5)
        tk.Button(self.frame, width=20, text="Remove", command=self.Remove).grid(padx=5, pady=5, column=2, row=5)
        tk.Button(self.frame, width=20, text="Exit", command=self.master.destroy).grid(padx=5, pady=5, column=2, row=6)

    def AddNew(self):
        person = (self.firstName.get(), self.lastName.get(), self.eventName.get(), self.roleName.get())
        databaseInterface.eventAttendAdd(person)

    def Remove(self):
        person = (self.firstName.get(), self.lastName.get(), self.eventName.get(), self.roleName.get())
        databaseInterface.eventAttendRemove(person)


class AttendanceDBview:
    def __init__(self, master, data):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)
        master.title("View Attendance")

        self.databaseView = tk.ttk.Treeview(self.frame)
        self.databaseView.grid(pady=5, column=1, row=2)
        self.databaseView["show"] = "headings"
        self.databaseView["columns"] = ('firstName', 'lastName', 'roleName')

        # all treeview column headings
        self.databaseView.heading("firstName", text="First Name")
        self.databaseView.heading("lastName", text="Last Name")
        self.databaseView.heading("roleName", text="Role")

        # create all treeview columns
        self.databaseView.column("firstName", width=100)
        self.databaseView.column("lastName", width=100)
        self.databaseView.column("roleName", width=100)

        for value in data:
            self.databaseView.insert('', 'end', values=value)


class ViewAttendance:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)
        master.title("View Attendance")

        self.eventName = tk.StringVar()
        tk.Label(self.frame, width=25, text="Event Name").grid(column=1, row=1)
        tk.Entry(self.frame, width=20, textvariable=self.eventName).grid(column=1, row=2)

        for child in self.frame.winfo_children():
            child.grid_configure(padx=5, pady=3)

        tk.Button(self.frame, width=20, text="View", command=self.viewAttendDB).grid(padx=5, pady=5, column=1, row=3)
        tk.Button(self.frame, width=20, text="Exit", command=self.master.destroy).grid(padx=5, pady=5, column=1, row=4)

    def viewAttendDB(self):
        data = databaseInterface.viewAttendance(self.eventName.get())
        AttendanceDBview(self.master, data)