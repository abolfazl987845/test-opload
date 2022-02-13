import os
os.system('cls')

std_list = []
for i in range(1):
    print("student number %d " %(i+1))
    name = input("name: ")
    last_name = input('last name: ')

    score_list = []
    for x in range(1,10):
        print('Score...')
        Score = float(input('enter Score number %d \n' %(x+1)))
        score_list.append(Score)

        dic = {
            'name':name,
            'last name': last_name,
            "Score":score_list,
        }

        std_list.append(dic)

for i in range(1):
    std = std_list[i]
    score_sum = sum(std['Score'])
    score_len = len(std['Score'])
    averge = score_sum / score_len

    print('Student Number', i+1)
    print('Name: ', std['name'])
    print('Family:', std['last name'])
    print('Average:', averge)
    print('\n')






