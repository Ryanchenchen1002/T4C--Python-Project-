import tkinter as tk
import AttendeeGUI, DatabaseGUI, EventGUI
import sqlite3

conn = sqlite3.connect('Final Project.db')
c = conn.cursor()

# main menu
class MainMenu:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # button dimensions
        x = 25
        y = 4

        tk.Button(self.frame, width=x, height=y, text="Add Person",
                  command=self.AddPerson).grid(column=1, row=1)
        tk.Button(self.frame, width=x, height=y, text="Update Database",
                  command=self.UpdateDatabase).grid(column=2, row=1)
        tk.Button(self.frame, width=x, height=y, text="Search Database",
                  command=self.SearchDatabase).grid(column=2, row=2)
        tk.Button(self.frame, width=x, height=y, text="View Database",
                  command=self.ViewDatabase).grid(column=2, row=3)
        tk.Button(self.frame, width=x, height=y, text="Delete Person",
                  command=self.DeletePerson).grid(column=1, row=2)
        tk.Button(self.frame, width=x, height=y, text="Add Event",
                  command=self.EventNew).grid(column=3, row=1)
        tk.Button(self.frame, width=x, height=y, text="Delete Event",
                  command=self.EventDelete).grid(column=3, row=2)
        tk.Button(self.frame, width=x, height=y, text="View Event",
                  command=self.EventSearch).grid(column=3, row=3)
        tk.Button(self.frame, width=x, height=y, text="Manage Attendance",
                  command=self.AttendanceManage).grid(column=4, row=1)
        tk.Button(self.frame, width=x, height=y, text="View Attendance",
                  command=self.ViewAttendance).grid(column=4, row=2)
        tk.Button(self.frame, width=x, height=y, text="Exit",
                  command=self.master.destroy).grid(column=4, row=4)

        for child in self.frame.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def AddPerson(self):
        AttendeeGUI.AttendeeNew(tk.Toplevel(self.master))

    def DeletePerson(self):
        DatabaseGUI.ManageDatabase(tk.Toplevel(self.master), "Delete")

    def SearchDatabase(self):
        DatabaseGUI.ManageDatabase(tk.Toplevel(self.master), "Search")

    def UpdateDatabase(self):
        AttendeeGUI.UpdateDatabase(tk.Toplevel(self.master))

    def ViewDatabase(self):
        DatabaseGUI.DatabaseView(tk.Toplevel(self.master))

    def EventNew(self):
        EventGUI.EventNew(tk.Toplevel(self.master))

    def EventDelete(self):
        EventGUI.EventManage(tk.Toplevel(self.master), "Delete")

    def EventSearch(self):
        EventGUI.EventManage(tk.Toplevel(self.master), "Search")

    def AttendanceManage(self):
        EventGUI.Attendance(tk.Toplevel(self.master))

    def ViewAttendance(self):
        EventGUI.ViewAttendance(tk.Toplevel(self.master))


def createTables():
    c.execute('''CREATE TABLE IF NOT EXISTS "People" (
        "ID" INTEGER NOT NULL,
        "FirstName" TEXT NOT NULL,
        "LastName" TEXT NOT NULL,
        "Address" TEXT,
        "City" TEXT,
        "State" TEXT,
        "Zip" INTEGER,
        "Phone" TEXT,
        "Email" TEXT,
        "IsBeliever" TEXT,
        "IsMember" TEXT,
        PRIMARY KEY("ID"));''')

    c.execute('''CREATE TABLE IF NOT EXISTS "EventInfo" (
        "EventID" INTEGER NOT NULL PRIMARY KEY,
        "EventName"	TEXT, "EventTime" TEXT, 
        "EventDate" TEXT, "EventDesc" TEXT);''')

    c.execute('''CREATE TABLE IF NOT EXISTS Attendance (
    EventID INTEGER,
    PersonID INTEGER,
    Role TEXT,
    FOREIGN KEY(EventID) REFERENCES EventInfo(EventID),
    FOREIGN KEY(PersonID) REFERENCES People(ID));''')


def main():
    createTables()
    root = tk.Tk()
    root.title("Event Management System")
    app = MainMenu(root)
    root.mainloop()


if __name__ == "__main__":
    main()
