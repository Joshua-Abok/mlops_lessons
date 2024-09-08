import datetime

#Return information for all of the packages that match a given time
#O(n)
# def get_all_packages(hm, time):
#     try:
#         (h, m, s) = time.split(':')
#         time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
#         for i in range(1, 41):
            
#             try:
#                 start = hm.search(i).start
#                 status = hm.search(i).status
#                 (h,m,s) = start[0].split(':')
#                 start = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
#                 (h,m,s) = status.split(':')
#                 status = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
#             except ValueError:
#                 pass
            
#             if start >= time:
#                 hm.search(i).status = 'At Hub'
#                 hm.search(i).start = 'Departing at ' + str(start)
#                 print(hm.search(i).__str__()) 

#             elif start <= time:
#                 if status > time:
#                     hm.search(i).status = 'In Route'
#                     hm.search(i).start = 'Departed at ' + str(start)
#                     print(hm.search(i).__str__())  
#                 else:
#                     hm.search(i).status = 'Delivered at ' + str(status)
#                     hm.search(i).start = 'Departed at ' + str(start)
#                     print(hm.search(i).__str__()) 
                    

#     except:
#         print('Invalid input, try again.')

# #Return a single package that matches a given id and time
# #O(1)
# def get_single_package(hm, id, time):
#     try:
#         start = hm.search(id).start
#         status = hm.search(id).status
#         (h,m,s) = start[0].split(':')
#         start = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
#         (h,m,s) = status.split(':')
#         status = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
#         (h,m,s) = time.split(':')
#         time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

#         if start >= time:
#             hm.search(id).status = 'At Hub'
#             hm.search(id).start = 'Departing at ' + str(start)
#             print('Package ID: ' + str(hm.search(id).ID))
#             print('Status of Delivery: ' + str(hm.search(id).status))

#         elif start <= time:
#             if time < status:
#                 hm.search(id).status = 'In Route'
#                 hm.search(id).start = 'Departed at ' + str(start)
#                 print(hm.search(id).__str__())  
#             else:
#                 hm.search(id).status = 'Delivered at ' + str(status)
#                 hm.search(id).start = 'Departed at ' + str(start)
#                 print(hm.search(id).__str__())  

#     except:
#         print('Invalid input, try again.')



####################################################################################


####################################################################################

import datetime
from load_trucks import *

class PackageHandler:
    def __init__(self, hashtable):
        self.hm = hashtable

    # Return information for all of the packages that match a given time
    # O(n)
    def get_all_packages(self, time):
        try:
            (h, m, s) = time.split(':')
            time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            for i in range(1, 41):  # Assuming there are 40 packages
                
                try:
                    package = self.hm.search(i)
                    start = package.start
                    status = package.status
                    (h, m, s) = start[0].split(':')
                    start = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    (h, m, s) = status.split(':')
                    status = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                except ValueError:
                    pass

                if start >= time:
                    package.status = 'At Hub'
                    package.start = 'Departing at ' + str(start)
                    print(package)

                elif start <= time:
                    if status > time:
                        package.status = 'In Route'
                        package.start = 'Departed at ' + str(start)
                        print(package)
                    else:
                        package.status = 'Delivered at ' + str(status)
                        package.start = 'Departed at ' + str(start)
                        print(package)

        except:
            print('Invalid input, try again.')

    # Return a single package that matches a given id and time
    # O(1)
    def get_single_package(self, id, time):
        try:
            package = self.hm.search(id)
            start = package.start
            status = package.status
            (h, m, s) = start[0].split(':')
            start = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            (h, m, s) = status.split(':')
            status = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            (h, m, s) = time.split(':')
            time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

            if start >= time:
                package.status = 'At Hub'
                package.start = 'Departing at ' + str(start)
                print('Package ID:', package.ID)
                print('Status of Delivery:', package.status)

            elif start <= time:
                if time < status:
                    package.status = 'In Route'
                    package.start = 'Departed at ' + str(start)
                    print(package)
                else:
                    package.status = 'Delivered at ' + str(status)
                    package.start = 'Departed at ' + str(start)
                    print(package)

        except:
            print('Invalid input, try again.')


options = PackageHandler(lt.hm)