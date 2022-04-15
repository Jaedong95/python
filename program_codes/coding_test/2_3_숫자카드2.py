import sys 

m = input()
my_cards = sys.stdin.readline().replace('\n', '').split(' ')
n = input() 
answer_cards = sys.stdin.readline().replace('\n', '').split(' ')

card_list = dict()
for i in my_cards:
    card_list[i] = card_list.get(i, 0) + 1 

answer = [0] * len(answer_cards)

for key, val in card_list.items():
    if key in answer_cards:
        answer[answer_cards.index(key)] += val
        
sys.stdout.write(' '.join(map(str, answer)))