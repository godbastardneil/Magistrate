import numpy as np
import tensorflow
tf = tensorflow.compat.v1
tf.disable_eager_execution()

#Список наших бандитов. Бандит №4 наиболее оптимален для выбора.
bandits = [0.2, 0, -0.2, -5]
num_bandits = len(bandits)
def pullBandit(bandit):
    #Сгенерировать случайное число
    result = np.random.randn(1)
    if result > bandit:
        #Выигрыш
        return 1
    else:
        #Проигрыш
        return -1




tf.reset_default_graph()

#Эти 2 строчки создают feed-forward часть нейросети. Здесь и происходит выбор действия.
weights = tf.Variable(tf.ones([num_bandits]))
chosen_action = tf.argmax(weights,0)

#Следующие 6 строчек устанавливают процедуру обучения. Нейросеть принимает на вход действие и его результат, чтобы оценить функцию потерь и обновить веса сети.
reward_holder = tf.placeholder(shape=[1],dtype=tf.float32)
action_holder = tf.placeholder(shape=[1],dtype=tf.int32)
responsible_weight = tf.slice(weights,action_holder,[1])
loss = -(tf.log(responsible_weight)*reward_holder)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
update = optimizer.minimize(loss)





total_episodes = 1000 #Количество итераций обучения
total_reward = np.zeros(num_bandits) #Изначальный выигрыш всех бандитов равен 0
e = 0.1 #Вероятность случайного выбора
init = tf.global_variables_initializer()

#Запускаем граф tensorflow
with tf.Session() as sess:
    sess.run(init)
    i = 0
    while i < total_episodes:
        
        #Выбираем действие либо случайно либо на основе нейросети
        if np.random.rand(1) < e:
            action = np.random.randint(num_bandits)
        else:
            action = sess.run(chosen_action)
        #Получаем результат игры, выбрав одного из бандитов
        reward = pullBandit(bandits[action]) 
        
        #Обновляем веса
        _,resp,ww = sess.run([update,responsible_weight,weights], 
                      feed_dict={reward_holder:[reward],action_holder:[action]})
        
        #Обновляем общий выигрыш каждого бандита
        total_reward[action] += reward
        if i % 50 == 0:
            print("Общий выигрыш бандитов сейчас равен " + str(num_bandits) + 
            " bandits: " + str(total_reward))
        i+=1
print("Агент думает, что бандит №" + str(np.argmax(ww)+1) + " идеален...")
if np.argmax(ww) == np.argmax(-np.array(bandits)):
    print("...и он прав!")
else:
    print("...и он не прав!")