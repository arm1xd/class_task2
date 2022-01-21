from user_module import *  
#c variant-1 такое себе
#class Admin(User):
#    def __init__(self, first_name, last_name, age, phone, work, login_attempts,privileges):
#        self.privileges = privileges
#        super().__init__(first_name, last_name, age, phone, work, login_attempts)

#    def show_privileges(self):
#        self.privileges = ["Allowed to add message","Allowed to delete users","Allowed to ban users"]
#        print(self.privileges)
#x = Admin(1, 1, 1, 1, 1, 1, 1)
#x.show_privileges()

        #c variant-2 тоже можно
#class Admin(User):
#    def __init__(self, first_name, last_name, age, phone, work, login_attempts):
#        self.privileges=[]
#        super().__init__(first_name, last_name, age, phone, work, login_attempts)
#    def show_privileges(self):
#        for i in self.privileges:
#            print(i)
#x = Admin(1, 1, 1, 1, 1, 1)
#x.privileges=["Allowed to add message","Allowed to delete users","Allowed to ban users"]
#x.show_privileges()
        #c variant-3 основной     
#class Admin(User):
#    def __init__(self, first_name, last_name, age, phone, work, login_attempts,privileges=[]):
#        self.privileges=privileges
#        super().__init__(first_name, last_name, age, phone, work, login_attempts)
#    def show_privileges(self):
#        for i in self.privileges:
#            print(i)
#x = Admin(1, 1, 1, 1, 1, 1,["Allowed to add message","Allowed to delete users","Allowed to ban users"])
#x.show_privileges()
        #c variant-4 тоже норм    
#class Admin(User):
#    def __init__(self, first_name, last_name, age, phone, work, login_attempts):
#        self.privileges = ["Allowed to add message","Allowed to delete users","Allowed to ban users"]
#        super().__init__(first_name, last_name, age, phone, work, login_attempts)
#    def show_privileges(self):
#        for i in self.privileges:
#             print(i)
#x = Admin(1, 1, 1, 1, 1, 1)
#x.show_privileges()

#d
class Privileges():
    def __init__(self):
        self.priv = ["Allowed to add message","Allowed to delete users","Allowed to ban users"]
    def show_privileges(self):
        for privilege in self.priv:
            print(privilege)
class Admin(User):
    def __init__(self, first_name, last_name, age, phone, work, login_attempts):       
        super().__init__(first_name, last_name, age, phone, work, login_attempts)
        self.priv=Privileges()
x=Admin(1,1,1,1,1,1)
x.priv.show_privileges()

