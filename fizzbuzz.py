# -*- coding: utf-8 -*-

import random

i = random.randint(1,101)

if i%15 == 0:
	print"FizzBuzz %d" % (i)
elif i%5 == 0:
	print "Buzz %d" % (i)
elif i%3 == 0:
	print"Fizz %d" % (i)
else:
	print i

print "hello python!"
			