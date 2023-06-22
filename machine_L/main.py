import random

# Переменные программы
MaxIter=10000

N = 4 # количество объектов
m = 6 # количество характеристик
k = 2 # количество наименований в рационе

min_d = 40
max_d = 80

norm = [random.randint(50,100) for i in range(m)] # норма
# Список Продуктоа
Object_list = [[random.randint(20,40) for i in range(m)] for i in range(N)]
for i in range(N):
	for j in range(m):
		if (random.random() > 0.5):
			Object_list[i][j] += random.randint(0,30)
#Начальные хромосомы
Hrom = []
for i in range(N):
    Hrom.append([0 for i in range(N)])
    for j in range(k):
        Hrom[i][random.randint(0, N-1)] = 1
### Финтнесс Функции
# Сумма отличия продуктов от нормы
def DiffSum():
	Sum = []
	for i in range(N):
		sum=0
		for j in range(m):
			sum += (norm[j]-Object_list[i][j])
		Sum.append(sum/10)
	return Sum
Sum = DiffSum()
# Сама фитнесс функция
def Fun():
	F = []
	for i in range(len(Hrom)):
		sum=0
		for j in range(N):
			sum += Hrom[i][j]*Sum[j]
		F.append(sum)
	return F
F = Fun()

# Вывод начальной информации
s = "Норма: "
for j in range(m):
	s += str(norm[j]) + ', '
print(s)
s = "Продукты:\n	"
for i in range(N):
	for j in range(m):
		s += str(Object_list[i][j]) + ', '
	s += '\n	'
print(s)
s = "Нач. хромосомы:\n	"
for i in range(len(Hrom)):
	for j in range(len(Hrom[i])):
		s += str(Hrom[i][j]) + " "
	s += "\n	"
print(s)

### Функции программы
def check():
	max = max_d
	for i in range(len(F)):
		if ((F[i] <= max) and (F[i]>0)): max = F[i]
	return not ((max >= min_d) and (max <= max_d))
# выбор особей для кроссовера
def Select():
	Sel = []
	Vert = []
	sum=0
	for j in range(N):
		sum += Sum[j]
	for i in range(len(F)):
		Vert.append(F[i]/sum)
	for t in range(len(F)):
		max = -1
		m = 0
		for i in range(len(F)):
			if (Vert[i]>max):
				max=Vert[i]
				m=i
		Vert[m]=-1
		Sel.append(m)
	return Sel
# Кроссовер
def krossover():
	Sel = Select()
	g = random.randint(0, N/2)
	l = len(Sel)
	t = 0
	while (t < l - 1):
		for i in range(g):
			tmp = Hrom[Sel[t]][i]
			Hrom[Sel[t]][i] = Hrom[Sel[t+1]][i]
			Hrom[Sel[t+1]][i] = tmp
		for i in range(g, N):
			tmp = Hrom[Sel[t]][i]
			Hrom[Sel[t]][i] = Hrom[Sel[t+1]][i]
			Hrom[Sel[t+1]][i] = tmp
		t += 2
# Мутация
def mutation():
	for i in range(len(Hrom)):
		for j in range(len(Hrom[i])):
			if (random.random()>0.5):
				Hrom[i][j] = 1 - Hrom[i][j]
		while (sum(Hrom[i]) != k):
			j = random.randint(0, N-1)
			Hrom[i][j] = 1 - Hrom[i][j]
### Основная программа
lg=True
step=0
while (lg):
	krossover()
	mutation()
	Sum = DiffSum()
	F = Fun()

	lg=check()
	step += 1
	if (step==MaxIter): lg=False
# Вывод результатов
s = "Кон. хромосомы:\n	"
for i in range(len(Hrom)):
	for j in range(len(Hrom[i])):
		s+=(str(Hrom[i][j]) + " ")
	s += "\n	"
print(s)

s = "Функция: "
for i in range(len(F)):
	s += (str(F[i]) + " ")
print(s)

j = 0
min = max_d
for i in range(len(F)):
	if (F[i] <= min):
		min = F[i]
		j = i
s = "Лучший рацион: " + str(j+1) + '\n	'
for i in range(len(Hrom[j])):
	if (Hrom[j][i] == 1):
		for l in range(len(Object_list[i])):
			s += str(Object_list[i][l]) + ' '
		s += '\n 	'
print(s)
