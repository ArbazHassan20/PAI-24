# -*- coding: utf-8 -*-
"""Lab 8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IAACge8yatdMQjkpPn-u__qGw_x7QnSK
"""

#Task 1
import numpy as np

a = np.arange(22, 50, 2)
print(a)

#Task 2
import numpy as np

a = np.arange(1, 19, 2).reshape(3, 3)
for b in a.flat:
    print(b)

#Task 3
import numpy as np

a = np.arange(2, 20, 2).reshape(3, 3)
b = a * 4
c = np.eye(3)
d = np.dot(b, c)
print(d)

#Task 4
import numpy as np

dt = np.dtype([('name', 'U10'), ('height', 'f4'), ('class', 'i4')])
a = np.array([('Alice', 5.5, 2), ('Bob', 6.0, 1), ('Charlie', 5.8, 2)], dtype=dt)
b = np.sort(a, order=['class', 'height'])
print(b)

#Task 5
import numpy as np

a = np.random.choice([2, 5, 9, 10], size=(4, 4))
b = np.eye(4)
c = np.dot(a, b)
d = np.arange(1, 32, 2).reshape(4, 4)
e = c + d
print(e)

#Task 6
import numpy as np

a = np.random.rand(5, 3)
b = np.random.rand(3, 2)
c = np.dot(a, b)
print(c)

#Task 7
import numpy as np

a = np.random.rand(1000)
m = np.mean(a)
v = np.var(a)
s = np.std(a)

with open('results.txt', 'w') as f:
    f.write(f'Average: {m}\nVariance: {v}\nStandard Deviation: {s}\n')