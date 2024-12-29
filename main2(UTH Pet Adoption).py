class Pet:
    def __init__(self, name, species, age=None, health_status=None, gender=None, image=None, video=None, owner=None):
        self.name = name
        self.species = species
        self.age = age
        self.health_status = health_status
        self.gender= gender
        self.image = image
        self.video = video
        self.owner = owner  
    
    def __str__(self):
        return f"{self.name} ({self.species}) - Age: {self.age}, Health: {self.health_status}, Gender: {self.gender}, Owner: {self.owner.username if self.owner else 'No owner'}"
    
    def display_details(self):
        return f"Name: {self.name}, Species: {self.species}, Age: {self.age}, Health Status: {self.health_status}, Gender: {self.gender}, Image: {self.image}, Video: {self.video}"
    
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

    def search_pet(self, species=None, health_status=None, gener=None): 
        matching_pets = [pet for pet in manager.pets if(not species or pet.species == species) and (not health_status or pet.health_status == health_status) and (not gener or pet.gender == gener)]
        if matching_pets:
           print("Thú cưng tìm thấy: ")
           for pet in matching_pets:
               print(f" -{pet}")
        else:
            print("Không tim thấy thú cưng phù hợp. ")

    def contract_center(self):
        print("Liên hệ với trung tâm cứu hộ thành công. Chúng tôi sẽ phản hồi sớm nhất. ")
        
class Manager:
    def __init__(self):
        self.users = [] 
        self.pets = []  
        self.logged_in_user = None  
        self.admin_username = "admin"
        self.admin_password = "123"

    # Chức năng quản trị viên
    def admin_menu(self):
        while True:
            print("--- Menu Quản Trị Viên ---\n")
            print("1. Xem danh sách người dùng")
            print("2. Cập nhật thông tin người dùng")
            print("3. Xóa người dùng")
            print("4. Xem danh sách thú cưng")
            print("5. Cập nhật thông tin thú cưng")
            print("6. Xóa thú cưng")
            print("7. Đăng xuất")
            admin_action = input("Nhập lựa chọn của bạn: ")

            if admin_action == '1':
                self.list_users()
            elif admin_action == '2':
                self.update_user()
            elif admin_action == '3':
                self.delete_user()
            elif admin_action == '4':
                self.list_pets()
            elif admin_action == '5':
                self.update_pet()
            elif admin_action == '6':
                self.delete_pet()
            elif admin_action == '7':
                print("Đăng xuất quản trị viên.")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

    def login_admin(self):
        username = input("Nhập tài khoản quản trị viên: ")
        password = input("Nhập mật khẩu quản trị viên: ")

        if username == self.admin_username and password == self.admin_password:
            print("Đăng nhập với tư cách quản trị viên thành công.")
            self.admin_menu()
        else:
            print("Tài khoản hoặc mật khẩu quản trị viên không đúng.")

    def list_users(self):
        if not self.users:
            print("Không có người dùng nào trong hệ thống.")
        else:
            print("Danh sách người dùng:")
            for user in self.users:
                print(f"  - {user.username}")

    def update_user(self):
        username = input("Nhập tên người dùng cần cập nhật: ")
        user = self.find_user(username)
        if not user:
            print(f"Không tìm thấy người dùng {username}.")
            return

        new_username = input("Nhập tên người dùng mới (để trống để giữ nguyên): ") or user.username
        new_password = input("Nhập mật khẩu mới (để trống để giữ nguyên): ") or user.password
        user.username = new_username
        user.password = new_password
        print(f"Thông tin người dùng {username} đã được cập nhật.")

    def delete_user(self):
        username = input("Nhập tên người dùng cần xóa: ")
        user = self.find_user(username)
        if not user:
            print(f"Không tìm thấy người dùng {username}.")
            return
        self.users.remove(user)
        print(f"Đã xóa người dùng {username} khỏi hệ thống.")

    def list_pets(self):
        if not self.pets:
            print("Không có thú cưng nào trong hệ thống.")
        else:
            print("Danh sách thú cưng:")
            for pet in self.pets:
                owner = pet.owner.username if pet.owner else "Chưa có chủ"
                print(f"  - {pet.name} ({pet.species}) - Chủ: {owner}")

    def update_pet(self):
        pet_name = input("Nhập tên thú cưng cần cập nhật: ")
        pet = next((pet for pet in self.pets if pet.name == pet_name), None)
        if not pet:
            print(f"Không tìm thấy thú cưng {pet_name}.")
            return

        new_name = input(f"Nhập tên thú cưng mới (để trống để giữ nguyên): ") or pet.name
        new_species = input(f"Nhập loài thú cưng mới (để trống để giữ nguyên): ") or pet.species
        pet.name = new_name
        pet.species = new_species
        print(f"Thông tin thú cưng {pet_name} đã được cập nhật.")

    def delete_pet(self):
        pet_name = input("Nhập tên thú cưng cần xóa: ")
        pet = next((pet for pet in self.pets if pet.name == pet_name), None)
        if not pet:
            print(f"Không tìm thấy thú cưng {pet_name}.")
            return
        self.pets.remove(pet)
        print(f"Đã xóa thú cưng {pet_name} khỏi hệ thống.")

    # Chức năng người dùng chung
    def user_menu(self):
        while True:
            print("--- Menu Người Dùng ---\n")
            print("1. Đăng ký tài khoản")
            print("2. Đăng nhập")
            print("3. Thêm thú cưng (yêu cầu đăng nhập)")
            print("4. Xem danh sách thú cưng")
            print("5. Đăng xuất")
            print("6. Thoát")
            choice = input("Nhập lựa chọn của bạn: ")

            if choice == '1':
                self.register_user()
            elif choice == '2':
                self.login_user()
            elif choice == '3':
                if self.logged_in_user:
                    self.add_pet()
                else:
                    print("Bạn cần đăng nhập để thêm thú cưng.")
            elif choice == '4':
                self.list_pets()
            elif choice == '5':
                self.logout_user()
            elif choice == '6':
                print("Thoát menu người dùng.")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

    def register_user(self):
        username = input("Nhập tên người dùng mới: ")
        if self.find_user(username):
            print(f"Người dùng {username} đã tồn tại.")
            return

        password = input("Nhập mật khẩu: ")
        new_user = User(username, password)
        self.users.append(new_user)
        print(f"Đã đăng ký thành công người dùng {username}.")

    def login_user(self):
        if self.logged_in_user:
            print(f"Bạn đã đăng nhập với tài khoản {self.logged_in_user.username}.")
            return

        username = input("Nhập tên người dùng: ")
        password = input("Nhập mật khẩu: ")
        user = self.find_user(username)

        if user and user.password == password:
            self.logged_in_user = user
            print(f"Đăng nhập thành công! Chào mừng, {username}.")
        else:
            print("Tên người dùng hoặc mật khẩu không chính xác.")

    def logout_user(self):
        if self.logged_in_user:
            print(f"Đăng xuất thành công! Tạm biệt, {self.logged_in_user.username}.")
            self.logged_in_user = None
        else:
            print("Bạn chưa đăng nhập.")

    def add_pet(self):
        pet_name = input("Nhập tên thú cưng: ")
        species = input("Nhập loài thú cưng: ")
        new_pet = Pet(pet_name, species, self.logged_in_user)
        self.pets.append(new_pet)
        print(f"Thú cưng {pet_name} ({species}) đã được thêm vào hệ thống.")

    def find_user(self, username):
        return next((user for user in self.users if user.username == username), None)


# Chương trình chính
manager = Manager()

while True:
    print("\nChào mừng đến với hệ thống UTH Pet Adoption")
    print("1. Người dùng")
    print("2. Quản trị viên")
    print("3. Thoát")
    choice = input("Nhập lựa chọn của bạn: ")

    if choice == '1':
        manager.user_menu()
    elif choice == '2':
        manager.login_admin()
    elif choice == '3':
        print("Thoát chương trình. Tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")