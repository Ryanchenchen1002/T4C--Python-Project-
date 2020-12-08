import tkinter as tk
from tkinter import ttk
from Manager import databaseInterface


class AttendeeNew:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)
        master.title("Add Attendee Information")

        # create GUI labels and entry boxes

        self.firstName = tk.StringVar()
        tk.Label(self.frame, text="First Name", width=15).grid(column=1, row=1, sticky=tk.E)
        self.firstNameEntry = tk.Entry(self.frame, width=20, textvariable=self.firstName).grid(column=2, row=1)

        self.lastName = tk.StringVar()
        tk.Label(self.frame, text="Last Name", width=15).grid(column=1, row=2, sticky=tk.E)
        self.lastNameEntry = tk.Entry(self.frame, width=20, textvariable=self.lastName).grid(column=2, row=2)

        self.address = tk.StringVar()
        tk.Label(self.frame, text="Address", width=15).grid(column=1, row=3, sticky=tk.E)
        self.addressEntry = tk.Entry(self.frame, width=20, textvariable=self.address).grid(column=2, row=3)

        self.city = tk.StringVar()
        tk.Label(self.frame, text="City", width=15).grid(column=1, row=4, sticky=tk.E)
        self.cityEntry = tk.Entry(self.frame, width=20, textvariable=self.city).grid(column=2, row=4)

        self.state = tk.StringVar()
        tk.Label(self.frame, text="State", width=15).grid(column=1, row=5, sticky=tk.E)
        self.stateEntry = tk.Entry(self.frame, width=20, textvariable=self.state).grid(column=2, row=5)

        self.zipcode = tk.StringVar()
        tk.Label(self.frame, text="Zip Code", width=15).grid(column=1, row=6, sticky=tk.E)
        self.zipcodeEntry = tk.Entry(self.frame, width=20, textvariable=self.zipcode).grid(column=2, row=6)

        self.phone = tk.StringVar()
        tk.Label(self.frame, text="Phone Number", width=15).grid(column=1, row=7, sticky=tk.E)
        self.phoneEntry = tk.Entry(self.frame, width=20, textvariable=self.phone).grid(column=2, row=7)

        self.email = tk.StringVar()
        tk.Label(self.frame, text="Email", width=15).grid(column=1, row=8, sticky=tk.E)
        self.emailEntry = tk.Entry(self.frame, width=20, textvariable=self.email).grid(column=2, row=8)

        self.isbeliever = tk.StringVar()
        tk.Label(self.frame, text="Christian?", width=15).grid(column=1, row=9, sticky=tk.E)
        self.isbelieverValues = ("Yes", "No")
        self.isbelieverBox = ttk.Combobox(self.frame, textvariable=self.isbeliever, values=self.isbelieverValues,
                                          width=17, state="readonly").grid(column=2, row=9)
        self.ismember = tk.StringVar()
        tk.Label(self.frame, text="Church Member?", width=15).grid(column=1, row=10, sticky=tk.W)
        self.ismemberValues = ("Yes", "No")
        self.ismemberBox = ttk.Combobox(self.frame, textvariable=self.ismember, values=self.ismemberValues, width=17,
                                        state="readonly").grid(column=2, row=10)

        # pad grid
        for child in self.frame.winfo_children():
            child.grid_configure(padx=5, pady=3)

        # attendee page buttons
        tk.Button(self.frame, width=10, text="Add", command=self.DatabaseNew).grid(pady=5, padx=5,
                                                                                   column=1, row=12)
        tk.Button(self.frame, width=10, text="Clear", command=self.ResetEntries).grid(pady=5, padx=5,
                                                                                      column=2, row=12)
        tk.Button(self.frame, width=10, text="Close", command=self.master.destroy).grid(pady=5, padx=5,
                                                                                        column=1, row=13)

    # add attendee's information to the database
    def DatabaseNew(self):
        newAttendee = [
            self.firstName.get(),
            self.lastName.get(),
            self.address.get(),
            self.city.get(),
            self.state.get(),
            self.zipcode.get(),
            self.phone.get(),
            self.email.get(),
            self.isbeliever.get(),
            self.ismember.get()
        ]

        databaseInterface.submitPerson(newAttendee)

        tk.messagebox.showinfo(title=None, message="Entry added to Database")

    # reset all boxes
    def ResetEntries(self):
        self.firstName.set("")
        self.lastName.set("")
        self.address.set("")
        self.phone.set("")
        self.email.set("")
        self.city.set("")
        self.state.set("")
        self.zipcode.set("")
        self.isbeliever.set("")
        self.ismember.set("")


# update attendee information
class UpdateDatabase:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)
        master.title("Update Attendee Information")

        # create labels for variable entry boxes
        self.attendeeid = tk.StringVar()
        tk.Label(self.frame, text="Attendee ID", width=25).grid(column=1, row=1, sticky=tk.E)
        self.attendeeidEntry = tk.Entry(self.frame, width=20, textvariable=self.attendeeid).grid(column=2, row=1)

        self.firstName = tk.StringVar()
        tk.Label(self.frame, text="First Name", width=25).grid(column=1, row=2, sticky=tk.E)
        self.firstNameEntry = tk.Entry(self.frame, width=20, textvariable=self.firstName).grid(column=2, row=2)

        self.lastName = tk.StringVar()
        tk.Label(self.frame, text="Last Name", width=25).grid(column=1, row=3, sticky=tk.E)
        self.lastNameEntry = tk.Entry(self.frame, width=20, textvariable=self.lastName).grid(column=2, row=3)

        self.address = tk.StringVar()
        tk.Label(self.frame, text="Address", width=25).grid(column=1, row=4, sticky=tk.E)
        self.addressEntry = tk.Entry(self.frame, width=20, textvariable=self.address).grid(column=2, row=4)

        self.city = tk.StringVar()
        tk.Label(self.frame, text="City", width=25).grid(column=1, row=5, sticky=tk.E)
        self.cityEntry = tk.Entry(self.frame, width=20, textvariable=self.city).grid(column=2, row=5)

        self.state = tk.StringVar()
        tk.Label(self.frame, text="State", width=25).grid(column=1, row=6, sticky=tk.E)
        self.stateEntry = tk.Entry(self.frame, width=20, textvariable=self.state).grid(column=2, row=6)

        self.zipcode = tk.StringVar()
        tk.Label(self.frame, text="Zip Code", width=25).grid(column=1, row=7, sticky=tk.E)
        self.zipcodeEntry = tk.Entry(self.frame, width=20, textvariable=self.zipcode).grid(column=2, row=7)

        self.phone = tk.StringVar()
        tk.Label(self.frame, text="Phone Number", width=25).grid(column=1, row=8, sticky=tk.E)
        self.phoneEntry = tk.Entry(self.frame, width=20, textvariable=self.phone).grid(column=2, row=8)

        self.email = tk.StringVar()
        tk.Label(self.frame, text="Email", width=25).grid(column=1, row=9, sticky=tk.E)
        self.emailEntry = tk.Entry(self.frame, width=20, textvariable=self.email).grid(column=2, row=9)

        self.isbeliever = ["Yes", "No"]
        tk.Label(self.frame, text="Christian?", width=25).grid(column=1, row=10, sticky=tk.E)
        self.isbelieverBox = ttk.Combobox(self.frame, values=self.isbeliever, width=20, state='readonly').grid(column=2,
                                                                                                               row=10)
        self.ismember = ["Yes", "No"]
        tk.Label(self.frame, text="Church Member?", width=25).grid(column=1, row=11, sticky=tk.E)
        self.ismemberBox = ttk.Combobox(self.frame, values=self.ismember, width=20, state='readonly').grid(column=2,
                                                                                                           row=11)

        # pad grid
        for child in self.frame.winfo_children():
            child.grid_configure(padx=5, pady=3)

        # add update page buttons
        tk.Button(self.frame, width=20, text="Add", command=UpdateDatabase.Update).grid(pady=15, padx=5,
                                                                                          column=1, row=12)
        tk.Button(self.frame, width=20, text="Reset", command=AttendeeNew.ResetEntries).grid(pady=15, padx=5,
                                                                                             column=2, row=12)
        tk.Button(self.frame, width=20, text="Close", command=self.master.destroy).grid(pady=15, padx=5,
                                                                                        column=1, row=13)

    def Update(self):
        update = (self.attendeeidEntry.get(), self.firstNameEntry.get(), self.lastNameEntry.get(),
                  self.stateEntry.get(), self.cityEntry.get(), self.zipcodeEntry.get(),
                  self.addressEntry.get(), self.emailEntry.get(),
                  self.isbelieverBox.get(), self.ismemberBox.get())
        databaseinterface.updatePerson(update)
        tk.messagebox.showinfo(title=None, message="Successfully updated the database!")

    def Reset(self):
        self.firstName.set("")
        self.lastName.set("")
        self.state.set("")
        self.city.set("")
        self.zipcode.set("")
        self.address.set("")
        self.isbeliever.set("")
        self.ismember.set("")
