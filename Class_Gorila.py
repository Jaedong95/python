class Gorila:
    banana = 10 
    cur_x = 0 
    cur_y = 0 
    def eat(self, num):
        if num > self.banana:
            print(f"가지고 있는 바나나보다 더 많이 먹을 수 없다 우우 (현재 바나나 수: {self.banana})")
        else: 
            self.banana -= num
    def check(self):
        print(f'내 뱃속엔 지금 {self.banana}개의 바나나가 있다 우우')
    def shout(self, string):
        print(f'{string} 우우')
    def walk(self, x, y):
        self.cur_x += x 
        self.cur_y += y 
        print(f'나는 지금 ({self.cur_x}, {self.cur_y}에 있다 우우')

gor = Gorila()
eat_n = int(input("몇 개의 바나나를 먹을건가요 ? "))
gor.eat(eat_n)
gor.check()
shout_text = input("뭐라고 소리칠건가요 ? ")
gor.shout(shout_text)
x, y = map(int, input('x, y 좌표로 얼만큼 이동할건가요 ? ').split(' '))
gor.walk(x, y)