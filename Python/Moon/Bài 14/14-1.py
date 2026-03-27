class Dog:
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
    def run(self):
        print(f"{self.breed} đang chạy...")
    def eat(self):
        print(f"{self.breed} đang ăn...")
#Tạo 3 đối tượng chó:
dog1 = Dog("Chó Phú Quốc", "Vàng")
dog2 = Dog("Chó Pitbull", "Đen")
dog3 = Dog("Chó Golden", "Vàng")
#Gọi phương thức chạy và ăn của các đối tượng chó:
dog1.run()
dog2.eat()
dog3.run()