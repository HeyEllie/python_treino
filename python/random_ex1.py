'''    random.randint(a, b): Returns a random integer N such that a <= N <= b. Both a and b are included in the possible range.
'''
import random
print(random.randint(1, 10))

'''    random.choice(sequence): Returns a random element from a non-empty sequence (e.g., a list, tuple, or string).
'''
print('-------------------------------------')
my_list = ['apple', 'banana', 'cherry']
print(random.choice(my_list))