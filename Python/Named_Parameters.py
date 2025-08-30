# This program displays the results of a series of coin flips.

import random
for i in range(100): # Perform 100 coin flips.
    if random.randint(0, 1) == 0:
        print('H', end=' ')
    else:
        print('T', end=' ')
    print()

# Replace the default separating string by passing the sep named parameter a different string.
print('cats','dogs','mice',sep=',')