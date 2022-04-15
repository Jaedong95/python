class Gun:
    bullets = 0 
    def charge(self, num):
        print(f'{num}발의 총알을 충전합니다.')
        self.bullets += num 
    def shoot(self):
        print(f'탕 !')
        self.bullets -= 1 
    def check(self):
        print(f'현재 {self.bullets}발의 총알이 남아있습니다.')
    

gun = Gun()
bullets_n = int(input("몇 발의 총알을 충전하시겠습니까 ? "))
gun.charge(bullets_n)
gun.shoot()
gun.check()