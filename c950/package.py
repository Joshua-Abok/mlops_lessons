#Package class to define attribute for packages
class Package:
    def __init__(self, ID, address, city, state, zip, deadline, weight, notes, start, location, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.start = start
        self.location = location
        self.status = status
    
    #Return a string with specific package data
    #O(1)
    def __str__(self):  # overwite print(Package) otherwise it will print object reference 
        return f'ID: {self.ID}\n Address: {self.address},{self.city},{self.state},{self.zip}\n Delivery Time: {self.deadline}\n Weight: {self.weight}\n Start: {self.start}\n Status: {self.status}'