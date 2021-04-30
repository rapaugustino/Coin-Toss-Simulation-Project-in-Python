import random
import matplotlib.pyplot as plt


my_list = []
for idx in range(1000):
  
  num_flips_needed_counter = 0
  num_heads_counter = 0
  
  while num_heads_counter < 3:
    num_flips_needed_counter += 1
    
    #let head be 1 and tail be 0
    current_flip_result = random.randint(0,1)
    

    if current_flip_result == 1:
      num_heads_counter += 1
      
    else:
      num_heads_counter += 0 
  my_list.append(num_flips_needed_counter)
#print(my_list)


i = 1
avg_list = []
for toss in my_list:
  avg = sum(my_list[0:i])/len(my_list[0:i])
  avg_list.append(avg)
  i += 1
print(avg_list)
#print(sum(my_list)/len(my_list))


x = [i for i in range(1,1001)]
y = avg_list

plt.title('Simulation of Average Number of Coin Tosses Before Observing Three Heads')
plt.ylabel('Average Number of Tosses')
plt.xlabel('Number of Experiment/Toss')

plt.scatter(x,y)
plt.show()
