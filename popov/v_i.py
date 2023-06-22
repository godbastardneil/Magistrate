import numpy as np

'''==================================================
Initial set up
=================================================='''


SMALL_ENOUGH = 0.005 # порог схождения
GAMMA = 0.9         
NOISE = 0.10  

#Определить все состояния
all_states=[]
for i in range(3):
    for j in range(4):
            all_states.append((i,j))

#Определить награды для всех состояний
rewards = {}
for i in all_states:
        rewards[i] = 0
rewards[(1,2)] = -1
rewards[(2,2)] = -1
rewards[(2,3)] = 1
#Словарь возможных действий. У нас есть два «конечных» состояния (1,2 and 2,2)
actions = {
    (0,0):('D', 'R'), 
    (0,1):('D', 'R', 'L'),    
    (0,2):('D', 'L', 'R'),
    (0,3):('D', 'L'),
    (1,0):('D', 'U', 'R'),
    (1,1):('D', 'R', 'L', 'U'),
    (1,3):('D', 'L', 'U'),
    (2,0):('U', 'R'),
    (2,1):('U', 'L', 'R'),
}

#Определить начальную политику
policy={}
for s in actions.keys():
    policy[s] = np.random.choice(actions[s])

#Определить функцию начальной пользы
V={}
for s in actions.keys():
    V[s] = 0
V[(2,2)]=-1
V[(1,2)]=-1
V[(2,3)]=1
        
'''==================================================
Value Iteration
=================================================='''

# функия, возвращающая конечное состояние после совершения действия a в состоянии s
def step(a, s):
    if a == 'U':
        return (s[0]-1, s[1])
    if a == 'D':
        return (s[0]+1, s[1])
    if a == 'L':
        return (s[0], s[1]-1)
    if a == 'R':
        return (s[0], s[1]+1)


iteration = 0

while True:
    biggest_change = 0
    for s in all_states:            
        if s in policy:
            
            old_v = V[s]
            new_v = 0
            
            for a in actions[s]:
                nxt = step(a, s)

                #Выберите новое случайное действие (вероятность перехода)
                random_1=np.random.choice([i for i in actions[s] if i != a])
                
                act = step(random_1, s)

                #Рассчитать стоимость
                v = rewards[s] + (GAMMA * ((1-NOISE)* V[nxt] + NOISE * V[act])) 
                if v > new_v: #Это лучший поступок на данный момент? Если да, то делать
                    new_v = v
                    policy[s] = a

            #Сохраните лучшее из всех действий для состояния                                
            V[s] = new_v
            biggest_change = max(biggest_change, np.abs(old_v - V[s]))

            
   #See if the loop should stop now         
    if biggest_change < SMALL_ENOUGH:
        break
    iteration += 1

print(iteration)
print(policy)
print(V)
