print(f'\n*** ENTER SCORE OF PLAYER ***')
score=list(map(int,input().split()))
print(f'You have entered {len(score)} Players Score:')
print(score)
mini=score[0]
maxi=score[0]
total=0
for value in score:
    if value>maxi:
        maxi=value
    if value<mini:
        mini=value
    total+=value
print(f'\nTotal Score of Playes are: {total}')
print(f'Maximum score of player: {maxi}')
print(f'Minimum score of player: {mini}')
