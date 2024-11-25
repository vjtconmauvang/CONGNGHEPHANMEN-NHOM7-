class Pet:
    def __init__(self, name, species, owner=None):
        self.name = name
        self.species = species
        self.owner = owner  
    
    def __str__(self):
        return f"{self.name} ({self.species}) - Owner: {self.owner.username if self.owner else 'No owner'}"

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.pets = []  
    
    def add_pet(self, pet):
        self.pets.append(pet)
        pet.owner = self  
    
    def remove_pet(self, pet):
        if pet in self.pets:
            self.pets.remove(pet)
            pet.owner = None  
        else:
            print(f"{self.username} không sở hữu thú cưng này.")
    
    def list_pets(self):
        if not self.pets:
            print(f"{self.username} không có thú cưng nào.")
        else:
            print(f"{self.username}'s Pets:")
            for pet in self.pets:
                print(f"  - {pet}")

class Manager:
    def __init__(self):
        self.users = []  
        self.pets = []  
        self.logged_in_user = None  
        self.admin_username = "admin"  
        self.admin_password = "123"   
        self.pet_fund_balance = 0  # Track the total pet fund balance
    
    def register_user(self):
        username = input("Nhập tên người dùng: ")
        password = input("Nhập mật khẩu: ")
        if self.find_user(username):
            print(f"Người dùng {username} đã tồn tại. Vui lòng chọn tên khác.")
            return None
        user = User(username, password)
        self.users.append(user)
        print(f"Đăng ký người dùng {username} thành công.")
        return user
    
    def login_user(self):
        username = input("Nhập tên người dùng: ")
        password = input("Nhập mật khẩu: ")
        user = self.find_user(username)
        if user and user.password == password:
            self.logged_in_user = user
            print(f"Đăng nhập thành công. Chào mừng {username}!")
            return user
        else:
            print("Tên người dùng hoặc mật khẩu không đúng.")
            return None
    
    def login_admin(self):
        username = input("Nhập tài khoản quản trị viên: ")
        password = input("Nhập mật khẩu quản trị viên: ")

        if username == self.admin_username and password == self.admin_password:
            print("Đăng nhập với tư cách quản trị viên thành công.")
            return True
        else:
            print("Tài khoản hoặc mật khẩu quản trị viên không đúng.")
            return False
    
    def find_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def adopt_pet(self, adopter_username, pet_name):
        adopter = self.find_user(adopter_username)
        if not adopter:
            print(f"Không tìm thấy người dùng {adopter_username}.")
            return

        pet = next((pet for pet in self.pets if pet.name == pet_name and pet.owner is None), None)
        if pet:
            adopter.add_pet(pet)
            print(f"{adopter.username} đã nhận {pet_name}!")
        else:
            print(f"Thú cưng {pet_name} không có sẵn để nhận hoặc đã có chủ sở hữu.")

    def give_away_pet(self, giver_username, pet_name):
        if not self.logged_in_user:
            print("Vui lòng đăng nhập trước khi cho đi thú cưng.")
            return

        giver = self.logged_in_user
        pet = next((pet for pet in giver.pets if pet.name == pet_name), None)
        if pet:
            giver.remove_pet(pet)
            self.pets.append(pet)  
            print(f"{giver.username} đã cho đi {pet_name}.")
        else:
            print(f"{giver.username} không sở hữu thú cưng {pet_name}.")

    def add_new_pet(self):
        if not self.logged_in_user:
            print("Vui lòng đăng nhập để thêm thú cưng.")
            return
        name = input("Nhập tên thú cưng: ")
        species = input("Nhập loài thú cưng: ")
        new_pet = Pet(name, species)
        self.logged_in_user.add_pet(new_pet)
        print(f"{self.logged_in_user.username} đã thêm thú cưng {new_pet} vào tài khoản.")

    def list_all_users(self):
        if not self.users:
            print("Không có người dùng nào trong hệ thống.")
        else:
            print("Danh sách người dùng:")
            for user in self.users:
                print(f"  - {user.username}")
    
    def donate_to_fund(self, amount):
        if not self.logged_in_user:
            print("Vui lòng đăng nhập trước khi đóng góp quỹ.")
            return
        if amount <= 0:
            print("Số tiền đóng góp phải lớn hơn 0.")
            return
        self.pet_fund_balance += amount
        print(f"{self.logged_in_user.username} đã đóng góp {amount} vào quỹ thú cưng.")

    def view_fund_balance(self):
        print(f"Quỹ thú cưng hiện tại có {self.pet_fund_balance} tiền.")
manager = Manager()
while True:
    choice = input("Chọn một hành động:\n1. Đăng ký\n2. Đăng nhập\n3. Đăng nhập với tư cách quản trị viên\n4. Thoát\nNhập lựa chọn: ")
    if choice == '1':
        manager.register_user()
    elif choice == '2':
        user = manager.login_user()
        if user:
            break
    elif choice == '3':
        if manager.login_admin():
            break
    elif choice == '4':
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if manager.logged_in_user:
    while True:
        action = input(f"\nChào mừng {manager.logged_in_user.username}!\nChọn hành động:\n1. Thêm thú cưng\n2. Xem thú cưng\n3. Cho đi thú cưng\n4. Đóng góp quỹ\n5. Xem số dư quỹ\n6. Thoát\nNhập lựa chọn: ")
        if action == '1':
            manager.add_new_pet()  # Thêm thú cưng mới
        elif action == '2':
            manager.logged_in_user.list_pets() 
        elif action == '3':
            pet_name = input("Nhập tên thú cưng bạn muốn cho đi: ")
            manager.give_away_pet(manager.logged_in_user.username, pet_name)  # Cho đi thú cưng
        elif action == '4':
            amount = float(input("Nhập số tiền bạn muốn đóng góp vào quỹ: "))
            manager.donate_to_fund(amount)  # Đóng góp vào quỹ
        elif action == '5':
            manager.view_fund_balance()  # Xem số dư quỹ
        elif action == '6':
            print("Cảm ơn bạn đã sử dụng hệ thống.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
elif manager.logged_in_user is None:
    if manager.login_admin():
        while True:
            admin_action = input("\nChọn hành động của quản trị viên:\n1. Xem danh sách người dùng\n2. Thoát\nNhập lựa chọn: ")
            if admin_action == '1':
                manager.list_all_users()  # Xem danh sách người dùng
            elif admin_action == '2':
                print("Đăng xuất quản trị viên.")
                break
            else:
                print("Lựa chọn không hợp lệ.")
