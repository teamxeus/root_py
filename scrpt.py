import math
import random
import time
'''
class root_finder():
	def __init__(self,)'''
def rooter():
	num = int(input("enter a number: "))
	options = [i for i in range(0,num-1)]
	random.shuffle(options)
	init_root = random.choice(options)
	print(init_root)
	func = pow(init_root,2) - num
	print(func)
	defunc = 2*init_root
	print(defunc)
	root = init_root - (func/defunc)
	print(root)

	for i in range(0,10):
		init_root = root
		func = pow(init_root,2) - num
		defunc = 2*init_root
		root = init_root - (func/defunc)
		time.sleep(1)
		init_root = root
		func = pow(init_root,2) - num
		defunc = 2*init_root
		root = init_root - (func/defunc)
		print(root)
	return root

rooter()