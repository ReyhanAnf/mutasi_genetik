from gen import *
from os import system
import numpy as np

jd = ['jodoh','tidak']
j = np.random.randint(0,2, size=(1,10))

# data dasar
target = jd[0]#input('target >> ')
bmutas = 0.8#(int(input('Mutasi (1-10)>> '))/10)
bplt = 10
populasi ={'gen':[],
		   'fit':[]}
		   
lop = True
banyak = 0

islop(target,bmutas,bplt,populasi,lop,banyak,system)