import sqlite3

conn = sqlite3.connect("Final Project.db")
c = conn.cursor()


def submitPerson(newPerson):
    sql = '''INSERT INTO People (FirstName, LastName, Address, City, State, Zip, Phone, Email, IsBeliever, IsMember)
          VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    c.execute(sql, newPerson)

    conn.commit()
    c.close()
    conn.close()


def searchPeople(firstName, lastName):
    c.execute("SELECT * FROM People WHERE FirstName = ? AND LastName = ?", (firstName, lastName))
    searchResults = c.fetchall()

    conn.commit()
    c.close()
    conn.close()
    return searchResults


def updatePerson(update, firstName, lastName):
    sql = '''UPDATE People 
        SET FirstName = ?,
            LastName = ?,
            Address = ?,
            City = ?,
            State = ?,
            Zip = ?, 
            Phone = ?, 
            Email = ?, 
            IsBeliever = ?, 
            IsMember = ? 
        WHERE FirstName = ? AND LastName = ?'''
    c.execute(sql, (update, firstName, lastName))

    conn.commit()
    c.close()
    conn.close()


def deletePerson(firstName, lastName):
    c.execute("DELETE FROM People WHERE FirstName = ? AND LastName = ?", (firstName, lastName))

    conn.commit()
    c.close()
    conn.close()


def submitEvent(eventNew):
    sql = 'INSERT INTO EventInfo (EventName, EventTime, EventDate, EventDesc) VALUES (?, ?, ?, ?)'
    c.execute(sql, eventNew)

    conn.commit()
    c.close()
    conn.close()


def viewEvent(eventName):
    c.execute("SELECT * FROM EventInfo WHERE EventName = ?", (eventName,))
    searchResults = c.fetchall()

    conn.commit()
    c.close()
    conn.close()
    return searchResults


def deleteEvent(eventName):
    c.execute("DELETE FROM EventInfo WHERE EventName = ?", (eventName))

    conn.commit()
    c.close()
    conn.close()


def eventAttendAdd(person):
    sql = "SELECT ID FROM People WHERE FirstName = ? AND LastName = ?"
    c.execute(sql, (person[0],))
    nameArray = c.fetchall()
    for row in nameArray:
        nameID = row[0]

    sql = "SELECT EventID FROM EventInfo WHERE EventName = ?"
    c.execute(sql, (person[2],))
    eventArray = c.fetchall()
    for row in eventArray:
        eventID = row[0]

    sql = "INSERT INTO Attendance VALUES (?, ?, ?)"
    c.execute(sql, (eventID, nameID, person[3]))

    conn.commit()
    c.close()
    conn.close()


def eventAttendRemove(person):
    sql = "SELECT ID FROM People WHERE FirstName = ? AND LastName = ?"
    c.execute(sql, (person[0], person[1],))
    nameArray = c.fetchall()
    for row in nameArray:
        nameID = row[0]

    sql = "SELECT EventID FROM EventInfo WHERE EventName = ?"
    c.execute(sql, (person[2],))
    eventArray = c.fetchall()
    for row in eventArray:
        eventID = row[0]

    sql = "DELETE FROM Attendance WHERE EventID = ? AND PersonID = ?"
    c.execute(sql, (eventID, nameID,))

    conn.commit()
    c.close()
    conn.close()


def viewAttendance(eventName):
    c.execute("SELECT EventID FROM EventInfo WHERE EventName = ?", (eventName,))
    eventArray = c.fetchall()
    for row in eventArray:
        searchResults = row[0]

    c.execute("SELECT * FROM Attendance WHERE EventID = ?", (searchResults,))
    attendance = c.fetchall()
    conn.commit()
    c.close()
    conn.close()
    return attendance


def viewAll():
    c.execute("SELECT * FROM People")
    records = c.fetchall()
    conn.commit()
    c.close()
    conn.close()
    return records