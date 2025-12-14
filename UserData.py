import csv

class UserDetail:
    
    def setUserName(userName,mail):   
        data=[]
        data.append(userName) 
        data.append(mail)    
        # File path for the CSV file
        file_path = "user.csv"

        # Write the data to the CSV file
        with open(file_path, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(data)
    
    def getUserName():
        file_path = "user.csv"
        with open(file_path, 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                return row[0]
            
    def getMail():
        file_path = "user.csv"
        with open(file_path, 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                return row[1]
    
            
