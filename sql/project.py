import sqlite3
import pandas as pd

connection = sqlite3.connect('pawsome-paws.db')
column_data = {
    'columns': {},
    'data': {}
}
dataframes = {}

cursor = connection.cursor()

#RELATION 1
# Create table for Clinic
cursor.execute('''CREATE TABLE IF NOT EXISTS Clinic (
                    clinicNo INTEGER PRIMARY KEY,
                    name TEXT,
                    address TEXT,
                    telephone TEXT
                )''')

# Insert data into Clinic table
cursor.execute('INSERT INTO Clinic (clinicNo, name, address, telephone) VALUES (?, ?, ?, ?)', (1, 'Pawsome Clinic', '123 Elm St', '555-1234'))
cursor.execute('INSERT INTO Clinic (clinicNo, name, address, telephone) VALUES (?, ?, ?, ?)', (2, 'Happy Pets Veterinary Clinic', '456 Maple Ave', '555-5678'))
cursor.execute('INSERT INTO Clinic (clinicNo, name, address, telephone) VALUES (?, ?, ?, ?)', (3, 'Animal Care Center', '789 Oak Dr', '555-9012'))
cursor.execute('INSERT INTO Clinic (clinicNo, name, address, telephone) VALUES (?, ?, ?, ?)', (4, 'VetCare Hospital', '101 Pine Ln', '555-3456'))
cursor.execute('INSERT INTO Clinic (clinicNo, name, address, telephone) VALUES (?, ?, ?, ?)', (5, 'Pet Wellness Center', '202 Cedar Dr', '555-7890'))

#RELATION 2
# Create table for Staff
cursor.execute('''CREATE TABLE IF NOT EXISTS Staff (
                    staffNo INTEGER PRIMARY KEY,
                    clinicNo INTEGER,
                    name TEXT,
                    address TEXT,
                    telephone TEXT,
                    DOB DATE,
                    position TEXT,
                    salary REAL,
                    FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo)
                )''')

# Insert data into Staff table
cursor.execute('INSERT INTO Staff (staffNo, clinicNo, name, address, telephone, DOB, position, salary) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (1, 1, 'John Doe', '123 Elm St', '555-1234', '1985-05-15', 'Veterinarian', 60000.0))
cursor.execute('INSERT INTO Staff (staffNo, clinicNo, name, address, telephone, DOB, position, salary) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (2, 2, 'Jane Smith', '456 Maple Ave', '555-5678', '1988-09-20', 'Veterinary Technician', 40000.0))
cursor.execute('INSERT INTO Staff (staffNo, clinicNo, name, address, telephone, DOB, position, salary) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (3, 1, 'Mark Johnson', '789 Oak Dr', '555-9012', '1979-03-10', 'Receptionist', 35000.0))
cursor.execute('INSERT INTO Staff (staffNo, clinicNo, name, address, telephone, DOB, position, salary) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (4, 3, 'Emily Brown', '101 Pine Ln', '555-3456', '1992-11-25', 'Veterinarian', 65000.0))
cursor.execute('INSERT INTO Staff (staffNo, clinicNo, name, address, telephone, DOB, position, salary) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (5, 2, 'Michael Rodriguez', '202 Cedar Dr', '555-7890', '1980-07-18', 'Veterinary Assistant', 30000.0))

#RELATION 3
# Create table for Owner
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Owner (
        ownerNo INTEGER PRIMARY KEY,
        name TEXT,
        address TEXT,
        telephone TEXT
    )
    ''')

#Insert data into Owner table
cursor.execute('INSERT INTO Owner (ownerNo, name, address, telephone) VALUES (?, ?, ?, ?)', (1, 'Alice Smith', '789 Oak St', '555-6789'))
cursor.execute('INSERT INTO Owner (ownerNo, name, address, telephone) VALUES (?, ?, ?, ?)', (2, 'Bob Johnson', '101 Pine St', '555-7890'))
cursor.execute('INSERT INTO Owner (ownerNo, name, address, telephone) VALUES (?, ?, ?, ?)', (3, 'Charlie Brown', '202 Maple St', '555-8901'))
cursor.execute('INSERT INTO Owner (ownerNo, name, address, telephone) VALUES (?, ?, ?, ?)', (4, 'Diana Rodriguez', '303 Cedar St', '555-9012'))
cursor.execute('INSERT INTO Owner (ownerNo, name, address, telephone) VALUES (?, ?, ?, ?)', (5, 'Elena Kim', '404 Walnut St', '555-0123'))

#RELATION 4
# Create table for Owner
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pet (
        petNo INTEGER PRIMARY KEY,
        name TEXT,
        DOB DATE,
        species TEXT,
        breed TEXT,
        color TEXT,
        ownerNo INTEGER,
        clinicNo INTEGER,
        FOREIGN KEY (ownerNo) REFERENCES Owner(ownerNo),
        FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo)
    )
    ''')

#Insert data into Pet table
cursor.execute('INSERT INTO Pet (petNo, name, DOB, species, breed, color, ownerNo, clinicNo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (1, 'Max', '2018-03-15', 'Dog', 'Golden Retriever', 'Golden', 1, 1))
cursor.execute('INSERT INTO Pet (petNo, name, DOB, species, breed, color, ownerNo, clinicNo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (2, 'Bella', '2019-05-20', 'Cat', 'Siamese', 'Cream', 2, 2))
cursor.execute('INSERT INTO Pet (petNo, name, DOB, species, breed, color, ownerNo, clinicNo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (3, 'Charlie', '2020-07-10', 'Dog', 'Poodle', 'White', 3, 1))
cursor.execute('INSERT INTO Pet (petNo, name, DOB, species, breed, color, ownerNo, clinicNo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (4, 'Luna', '2017-09-25', 'Cat', 'Maine Coon', 'Tortoiseshell', 4, 3))
cursor.execute('INSERT INTO Pet (petNo, name, DOB, species, breed, color, ownerNo, clinicNo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (5, 'Max', '2019-11-12', 'Dog', 'Labrador Retriever', 'Black', 5, 2))

#RELATION 5
# Create table for Examination
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Examination (
        examNo INTEGER PRIMARY KEY,
        chiefComplaint TEXT,
        description TEXT,
        dateSeen DATE,
        actionsTaken TEXT,
        clinicNo INTEGER,
        petNo INTEGER,
        FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo),
        FOREIGN KEY (petNo) REFERENCES Pet(petNo)
    )
    ''')

# Insert data into Examination table
cursor.execute('INSERT INTO Examination (examNo, chiefComplaint, description, dateSeen, actionsTaken, clinicNo, petNo) VALUES (?, ?, ?, ?, ?, ?, ?)', (1, 'Limping', 'Performed physical examination and X-ray.', '2023-01-05', 'Prescribed pain medication.', 1, 1))
cursor.execute('INSERT INTO Examination (examNo, chiefComplaint, description, dateSeen, actionsTaken, clinicNo, petNo) VALUES (?, ?, ?, ?, ?, ?, ?)', (2, 'Vomiting', 'Conducted blood tests and ultrasound.', '2023-02-10', 'Advised dietary changes.', 2, 2))
cursor.execute('INSERT INTO Examination (examNo, chiefComplaint, description, dateSeen, actionsTaken, clinicNo, petNo) VALUES (?, ?, ?, ?, ?, ?, ?)', (3, 'Coughing', 'Performed lung auscultation and prescribed antibiotics.', '2023-03-15', 'Scheduled follow-up appointment.', 1, 3))
cursor.execute('INSERT INTO Examination (examNo, chiefComplaint, description, dateSeen, actionsTaken, clinicNo, petNo) VALUES (?, ?, ?, ?, ?, ?, ?)', (4, 'Lethargy', 'Performed blood tests and physical examination.', '2023-04-20', 'Recommended additional diagnostic tests.', 3, 4))
cursor.execute('INSERT INTO Examination (examNo, chiefComplaint, description, dateSeen, actionsTaken, clinicNo, petNo) VALUES (?, ?, ?, ?, ?, ?, ?)', (5, 'Scratching', 'Conducted skin examination and allergy testing.', '2023-05-25', 'Prescribed antihistamines.', 2, 5))

# Get data and column names for each table and save them in array
cursor.execute('''
    SELECT name, address, telephone FROM Clinic;
    ''')
column_data['columns']['clinic'] = [row[0] for row in cursor.description]
column_data['data']['clinic'] = cursor.fetchall()

cursor.execute('''
        SELECT name, position, salary FROM Staff;
        ''')
column_data['columns']['staff'] = [row[0] for row in cursor.description]
column_data['data']['staff'] = cursor.fetchall()

cursor.execute('''
        SELECT name, address, telephone FROM Owner;
        ''')
column_data['columns']['owner'] = [row[0] for row in cursor.description]
column_data['data']['owner'] = cursor.fetchall()

cursor.execute('''
        SELECT name, species, breed, color FROM Pet;
        ''')
column_data['columns']['pet'] = [row[0] for row in cursor.description]
column_data['data']['pet'] = cursor.fetchall()

cursor.execute('''
        SELECT chiefComplaint, description, dateSeen FROM Examination;
        ''')
column_data['columns']['examination'] = [row[0] for row in cursor.description]
column_data['data']['examination'] = cursor.fetchall()

# Go through saved data to create an DataFrame and insert it in array
for column_name, column_values in column_data['columns'].items():
    data = column_data['data'][column_name]
    df = pd.DataFrame(data, columns=column_values)
    df.index = range(1, len(df) + 1)
    dataframes[column_name] = df

# Examination of DataFrame
for column_name, df in dataframes.items():
    print(df)
    print(df.columns)
    print('\n')

# Comit to save the changes on database
connection.commit()

# Close connection after we are done
connection.close()