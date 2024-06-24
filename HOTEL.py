

from datetime import date


class Hotel:

    def __init__(self):
        self.rooms = {}
        self.available_rooms = {'Standard':[101,102,103,104],'Deluxe':[201,202,203,204],'Suite':[301,302,303,304],'Luxury':[401,402,403,404]}
        self.room_price = {1:800,2:1500,3:2500,4:5000}




    def check_in(self, Name, Address, Phono):
        global Room_no
        room_type = int(input('Room types: \n 1.Standard \n 2.Deluxe \n 3.Suite \n 4.Luxury \n Select room type: '))
        if room_type == 1:
            if self.available_rooms['Standard']:
                Room_no = self.available_rooms['Standard'].pop(0)
            else:
                print('sorry, Standard rooms are not available ☹ ')
                return

        elif room_type == 2:
            if self.available_rooms['Deluxe']:
                Room_no = self.available_rooms['Deluxe'].pop(0)
            else:
                print('sorry, Deluxe rooms are not available ☹ ')
                return

        elif room_type == 3:
           if self.available_rooms['Suite']:
                Room_no = self.available_rooms['Suite'].pop(0)
           else:
                print('sorry, Suite rooms are not available ☹ ')
                return

        elif room_type == 4:
            if self.available_rooms['Luxury']:
                Room_no = self.available_rooms['Luxury'].pop(0)
            else:
                print('sorry, Luxury rooms are not available ☹ ')
                return

        else:
            print("Choose valid room number")
        d,m,y = map(int,input("enter check in date ").split())
        check_in = date(y,m,d)
        self.rooms[Room_no] = {
            'Name' : Name,
            'Address' : Address,
            'Phono' : Phono,
            'check_in_date' : check_in,
            'room_type' : room_type,
            'roomservice' : 0
        }
        print(f"Checked in {Name} from {Address} to room: {Room_no} on {check_in}")




    def room_service(self, Room_no):
        if Room_no in self.rooms:
            print("^^^^^^^^^^^^^^^     VRINDHA HOTEL MENU ^^^^^^^^^^^^^^^^^^")
            print(" 1.Tea/Coffee: Rs-20/- \n 2.Tiffens: Rs-60/- \n 3.Lunch: Rs-100/- \n 4.Fastfood: Rs-120/- \n 5.Dinner: Rs:100/- \n 6.Exit")
            while 1:
                c = int(input("Select your choice: "))
                if c==1:
                    q=int(input("Enter Quantity: "))
                    self.rooms[Room_no]['roomservice'] += 20*q
                elif c==2:
                    q=int(input("Enter Quantity: "))
                    self.rooms[Room_no]['roomservice'] += 70*q
                elif c==3:
                    q=int(input("Enter Quantity: "))
                    self.rooms[Room_no]['roomservice'] += 150*q
                elif c==4:
                    q=int(input("Enter Quantity: "))
                    self.rooms[Room_no]['roomservice'] += 120*q
                elif c==5:
                    q=int(input("Enter Quantity: "))
                    self.rooms[Room_no]['roomservice'] += 100*q
                elif c==6:
                    break
                else:
                    print("invalid option")
            print("Room services Rs: ",self.rooms[Room_no]['roomservice'],"\n")
        else:
            print('invalid room number')




    def display_occupied(self):
        if not self.rooms:
            print("No rooms are Occupied")
        else:
            print('-----------Occupied Rooms: ---------------')
            print(" ")
            print("Room no   Name   Phono")
            print("  ")
            for Room_number, details in self.rooms.items():
                print(Room_number,'\t',details['Name'],'\t',details['Phono'])





    def check_out(self, Room_number):
        if Room_number in self.rooms:
            check_out_date = date.today()
            check_in_date = self.rooms[Room_number]['check_in_date']
            duration = (check_out_date - check_in_date).days
            roomtype = self.rooms[Room_number]['room_type']
            if roomtype == 1:
                self.available_rooms['Standard'].append(Room_number)
            elif roomtype == 2:
                self.available_rooms['Deluxe'].append(Room_number)
            elif roomtype == 3:
                self.available_rooms['Suite'].append(Room_number)
            elif roomtype ==4:
                self.available_rooms['Luxury'].append(Room_number)

            print("    ")
            print('    VRINDHA HOTEL RECEIPT     ')
            print(f"Name:{self.rooms[Room_number]['Name']}\nAddress:{self.rooms[Room_number]['Address']}")
            print(f"Phono:{self.rooms[Room_number]['Phono']}")
            print(f"Room Number:{Room_number}")
            print(f"Check in date:{check_in_date.strftime('%d %B %Y')}")
            print(f"Check out date:{check_out_date.strftime('%d %B %Y')}")
            print(f"No.of Days: {duration}\t Price per day:Rs.{self.room_price[roomtype]}")
            roombill = self.room_price[roomtype]*duration
            roomservice = self.rooms[Room_number]['roomservice']
            print('Room bill: Rs.',roombill)
            print('Room service: Rs.',roomservice)
            print('Total bill: Rs.',roombill+roomservice)
            del self.rooms[Room_number]
        else:
            print(f"Room {Room_number} is not occupied.")




    def start(self):
        while True:
            print("     ")
            print("              WELCOME TO VRINDHA HOTEL           ")
            print("1. Check-in")
            print("2. Room Service")
            print("3. Display occupied Rooms")
            print("4. Check-out")
            print("5. Exit")
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                Name = input("Enter Customer name: ")
                Address = input("Enter Customer address: ")
                Phono = input("Enter Customer Phono: ")
                while( len(Phono) < 10):
                    print("****************Enter 10 digit number**********************: ")
                    Phono = input("Enter Customer Phono: ")
                self.check_in(Name, Address, Phono)

            elif choice == 2:
                Room_no = int(input("Enter room number: "))
                self.room_service(Room_no)
            elif choice == 3:
                self.display_occupied()
            elif choice == 4:
                Room_number = int(input("Enter room number: "))
                self.check_out(Room_number)
            elif choice == 5:
                break
            else:
                print("Invalid choice !!!")
            print("--------------------------------------------------------------------------------------------------")



k = Hotel()
k.start()
