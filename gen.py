import numpy as np


def rgen(target):
	global asc
	asc = ''
	rmgen = np.random.randint(32,128, size=(1,len(target)))
	for i in range(0,len(target)):
		asc += chr(rmgen[0][i])
	return asc
	




def hit_fit(acak,target):
	ascar = []
	for i in range(0,len(acak)):
		if acak[i] == target[i]:
			ascar.append(1)
		else:
			ascar.append(0)
	sascar = np.sum(ascar)
	final = 100 / len(target) * sascar							
	return final
	


	
def populat(bplt,populasi,target):
	for i in range(0,bplt):
		populasi['gen'].append(rgen(target))
		
	for i in range(0,bplt):
		ab = populasi['gen']
		populasi['fit'].append(hit_fit(ab[i],target))
	return populasi



def maxim(populasi):
	nmx1 = np.max(populasi['fit'])
	imx1 = populasi['fit'].index(nmx1)
	parent1 = [populasi['gen'][imx1],populasi['fit'][imx1]]
	nmx2 = np.max(populasi['fit'])
	imx2 = populasi['fit'].index(nmx2)
	parent2 = [populasi['gen'][imx2],populasi['fit'][imx2]]
	return parent1 , parent2
	
	




def cross(parent1,parent2,target):
	b1 = len(parent1[0])
	c1 = int(np.round(b1/2))
	a1 = parent1[0][c1:]
	a11 = parent1[0][:c1]
	
	b2 = len(parent2[0])
	c2 = int(np.round(b2/2))
	a2 = parent2[0][:c2]
	a22 = parent2[0][c2:]
	
	gchild1 = a11 + a22
	gchild2 = a1 + a2
	fchild1 = hit_fit(gchild1,target)
	fchild2 = hit_fit(gchild2,target)
	
	child1 = {'gen':gchild1,'fit':fchild1}
	child2 = {'gen':gchild2,'fit':fchild2}

	return child1, child2
	
	
	

def mutasi(bmutas,child,target):
	mutan = child
	rand = np.random.rand(len(mutan['gen']))
	for i in range(0,len(mutan['gen'])):
		a = np.random.randint(32,128,size=(1,1))
		if rand[i] < bmutas:
			if target[i] == mutan['gen'][i]:
				mutan['gen'] = mutan['gen']
				mutan['fit'] = mutan['fit']
			else:
				mutan['gen'] = mutan['gen'].replace(mutan['gen'][i],chr(a[0][0]))
				mutan['fit'] = hit_fit(mutan['gen'],target)
		else:
			mutan['gen'] = mutan['gen']
			mutan['fit'] = mutan['fit']
	return mutan['gen'], mutan['fit']



def regen(childern,populasi,bplt):
	fitness = []
	for i in range(0,bplt):
		fitness.append(0)
	
	for i in range(0,len(fitness)):
		fitness[i] = populasi['fit'][i]
	
	for i in range(0,len(childern)):
		imf = fitness.index(min(fitness))
		#fitness.remove(imf)
		populasi['fit'].remove(populasi['fit'][imf])
		populasi['gen'].remove(populasi['gen'][imf])
		
	for i in range(0,len(childern)):
		fitness.append(childern[i]['fit'])
		populasi['gen'].append(childern[i]['gen'])
		populasi['fit'].append(childern[i]['fit'])
	return populasi



def log(mutant1,mutant2,system,banyak):
	print(f'banyak = {banyak}')
	print(f"gen baru = {mutant1['gen']} , fitness = {mutant1['fit']} %\n")
	print(f"gen baru = {mutant2['gen']} , fitness = {mutant2['fit']} %\n")
	system('clear')




def kondisi(mutant1,mutant2,target,lop):
	if mutant1['gen'] == target:
		lop = False
		print(f"gen baru = {mutant1['gen']} , fitness = {mutant1['fit']} %\n")
		print(f"gen baru = {mutant2['gen']} , fitness = {mutant2['fit']} %\n")	
	elif mutant2['gen'] == target:
		lop = False
		print(f"gen baru = {mutant1['gen']} , fitness = {mutant1['fit']} %\n")
		print(f"gen baru = {mutant2['gen']} , fitness = {mutant2['fit']} %\n")
	else:
		lop = True
	return lop
	



def islop(target,bmutas,bplt,populasi,lop,banyak,system):
	while lop:
		
		#buat populasi
		populat(bplt,populasi,target)
		
		
			
		#mencari populasi terbaik
		mxm = maxim(populasi)
				
		#cross populasi
		parent1 = mxm[0]	
		parent2 = mxm[1]
		[child1,child2] = cross(parent1,parent2,target)
			
		#mutasi
		mutant1 = dict()
		mutant2 = dict()
			
		[mutant1['gen'],mutant1['fit']] = mutasi(bmutas,child1,target)
		[mutant2['gen'],mutant2['fit']] = mutasi(bmutas,child2,target)
		
		
		
		#regen
		childern = [mutant1,mutant2]
		
		populasi = regen(childern,populasi,bplt)
		
		banyak += 1
		
		log(mutant1,mutant2,system,banyak)
		
			
		lop = kondisi(mutant1,mutant2,target,lop)				