class Card:
    price = 0
    def charge(self, p:int):
        self.price += p 
    
    def consume(self, p:int):
        self.price -= p 
    
    def print(self):
        print(f"잔액이 {self.price}원 입니다.")

card = Card()
user_answer = input('충전 / 소비 ? ')
if user_answer == '충전':
    price = int(input('충전할 금액을 입력하세요: '))
    card.charge(price)
elif user_answer == '소비':
    price = int(input('소비할 금액을 입력하세요: '))
    card.consume(price)

card.print()