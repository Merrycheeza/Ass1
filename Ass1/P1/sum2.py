#!/usr/bin/env python3

print("Type integers, each followed by Enter; or ^D or ^Z to finish")

total = 0
count = 0

while True:
	try:
		line = input()
		if line:
			number = int(line)
			total += number
			count += 1
	except ValueError as err:
		print(err)
		continue
	except EOFError:
		break

if count:
	print("count =", count, "total =", total, "mean =", total / count)

#^D and ^Z are ctrl-D and ctrl-Z
#to run without python3 command, chmod a+x sum2.py
#to run in python3, exec(open('sum2.py).read())
