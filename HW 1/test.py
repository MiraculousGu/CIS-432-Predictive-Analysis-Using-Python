try:
	# test packages 	
	try: 
		import warnings
		with warnings.catch_warnings():
			warnings.filterwarnings("ignore", category=FutureWarning)
			import sklearn
			import pandas as pd
			import numpy as np
			import matplotlib.pyplot as plt
			import pydot_ng as pydot
			#import beakerx 
			#import folium
			import ipywidgets
			import lxml
			import requests
			import os
			import tensorflow
			import keras
			import networkx			
	except Exception as e: 
		raise Exception('A required package was not found (%s). Refer to the assignment for the installation instructions.'%str(e))
		
	# test shell commands and path variables in linux
	if os.name == 'posix':
		if os.system('command -v ls'): 
			raise Exception('ls command was not found')
		if os.system('command -v grep'): 
			raise Exception('grep command was not found')
		if os.system('command -v diff'): 
			raise Exception('diff command was not found')
		if os.system('command -v spyder'): 
			raise Exception('spyder command was not found')
		if os.system('command -v ipython'): 
			raise Exception('ipython command was not found')
		if os.system('command -v jupyter'): 
			raise Exception('jupyter command was not found')

	# test shell commands and path variables in windows		
	elif os.name == 'nt':
		if os.system('where ls'): 
			raise Exception('ls command was not found. Did you install coreutils and add its location to the Path variable? (see assignment details)')
		if os.system('where grep'): 
			raise Exception('grep command was not found. Did you install grep and add its location to the Path variable? (see assignment details)')
		if os.system('where diff'): 
			raise Exception('diff command was not found. Did you install grep and add its location to the Path variable? (see assignment details)')
		if os.system('where spyder'): 
			raise Exception('spyder command was not found. Did you install anaconda and add its location to the Path variable? (see assignment details)')
		if os.system('where ipython'): 
			raise Exception('ipython command was not found. Did you install anaconda and add its location to the Path variable? (see assignment details)')
		if os.system('where jupyter'): 
			raise Exception('jupyter command was not found. Did you install anaconda and add its location to the Path variable? (see assignment details)')	
	else:
		raise Exception('Unknown OS, please contact the instructor.')
	
	# test graphviz	
	try:
		graph = pydot.Dot(graph_type='graph')
		edge = pydot.Edge("Rochester", "Simon")
		graph.add_edge(edge)
		
		# generate 1st output file
		graph.write_png('test.png') 
		# generate 2nd output file
		pydot.graph_from_dot_file('test.dot').write_pdf('test.pdf') 
		
	except Exception as e:
		raise Exception('Encountered error while testing graphviz installation: %s'%str(e))

	# generate 3rd output file	
	with open('test.txt', 'w') as outfile:		
		outfile.write(str(os.environ)+'\n')
		outfile.write('uname:')
	os.system('uname -a >> test.txt' ) 
	if os.name == 'posix':	
		os.system('command -v ls >> test.txt' ) 
		os.system('command -v grep >> test.txt' ) 
		os.system('command -v diff >> test.txt' ) 
		os.system('command -v spyder >> test.txt' ) 
		os.system('command -v ipython >> test.txt' ) 
		os.system('command -v jupyter >> test.txt' ) 
	else:
		os.system('where ls >> test.txt' ) 
		os.system('where grep >> test.txt' ) 
		os.system('where diff >> test.txt' ) 
		os.system('where spyder >> test.txt' ) 
		os.system('where ipython >> test.txt' ) 
		os.system('where jupyter >> test.txt' ) 
	
				
	print('\nPassed installation tests!')
except Exception as e: 
	print('\nFailed installation tests:', e)