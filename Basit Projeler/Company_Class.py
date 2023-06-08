"""
Aşağıdaki kod çalışan, yönetici, programcı ve alt dallarından oluşan classlar oluşturularak kişinin bilgilerini içeren bir projedir.
"""

class Worker():
    permission = 30
    def __init__(self, name, surname, company, salary, phone):
        self.name = name
        self.surname = surname
        self.company = company
        self.salary = salary
        self.phone = phone
        self.email = surname.lower()+name.lower()+"@"+company.lower()+".com"
        
    def view_info(self):
        print("-"*80)
        print(f"{self.name.title()} {self.surname.title()}, {self.company.upper()}, {self.phone}, {self.email}, {self.permission} ")
        print("-"*80)
        

class Programmer(Worker):
    permission = 20
    def __init__(self, name, surname, company, salary, phone, branch):
        super().__init__(name, surname, company, salary, phone)
        self.branch = branch
     
    def view_info(self):
        print(f"{self.name.title()} {self.surname.title()}, {self.company.upper()}, {self.phone}, {self.email}, {self.permission}, {self.branch.title()} \n")
    
        
        
class Management(Worker):
    def __init__(self, name, surname, company, salary, phone, team=None):
        super().__init__(name, surname, company, salary, phone)
        
        if(team==None):
            self.team = list()
        else:
            self.team = team
    def view_info(self):
        print("<>"*40)
        print("YÖNETİCİ\n")
        print(f"{self.name.title()} {self.surname.title()}, {self.company.upper()}, {self.phone}, {self.email}")
        
       
    def view_worker(self):
        print("|"*80)
        print("Takım Üyeleri:")
        for worker in self.team:
            worker.view_info()
            
        print("|"*80)
        
        
    def add_worker(self, worker):
        self.team.append(worker)
        

class BackendDeveloper(Programmer):
    permission = 15
    def __init__(self, name, surname, company, salary, phone, branch, SQL):
        super().__init__(name, surname, company, salary, phone, branch)    
            
        self.SQL = SQL
        
        
        
    def view_info(self):
        print("BackendDeveloper Çalışanı:") 
        print("-"*30)
        print(f"{self.name.title()} {self.surname.title()}, {self.company.upper()}, {self.phone}, {self.email}, {self.permission}, {self.branch.title()}, {self.SQL} \n")
        print("-"*30)   
         
worker1 = Worker("efnan", "kaya", "QWETR", 15000, "05847363349")
worker2 = Worker("erhan", "aslan", "erciyes", 10000, "05384356776")
worker1.view_info()
worker2.view_info()

programmer1 = Programmer("ali", "kara", "facebook", 17000, "05345768778", "software java")
programmer2 = Programmer("ahmet","ceylan","google",30000,"05465732883","software python")

management1 = Management("hasan", "deli", "HASTR", 11000, "05365477798")
management1.add_worker(programmer1)
management1.add_worker(programmer2)
management1.view_info()
management1.view_worker()

bd1 = BackendDeveloper("hasan", "yılmaz", "linkedin", 30000, "05355519449", "backend devoloper", "MSQL")
bd1.view_info()

