# load dataset
from os import listdir
from pandas import read_csv
from shutil import copyfile
import os.path
import math

def append_0(name):
	""""
	Old worse method which simply appends the whole list by 0 to the constant dimension
	"""
	prefix = ''
	subjects = list()
	directory = prefix + 'HAR_zeros/' + folder_name + '/'
	for name in listdir(directory):
		filename = directory + '/' + name
		if not filename.endswith('.csv'):
			continue
		df = read_csv(filename, header=None)
		values = df.values[:, 1:]
		subjects.append(values)

		for j in range(len(values)):
			#lista = ['0', ",", '0', ",", '0', ",", '0', ",", '0', ",", '0', "\n"]
			lista = [str(values[j, 0]), ",", str(values[j, 1]), ",", str(values[j, 2]), ",", str(values[j, 3]), ",",
					 str(values[j, 4]), ",", str(values[j, 5]), "\n"]
			plik = open(directory + 'a' + name, 'a')
			plik.writelines(lista)
			plik.close()

		for j in range((len(values) + 1), 401):
			lista = ['0', ",", '0', ",", '0', ",", '0', ",", '0', ",", '0', "\n"]
			plik = open(directory + 'a' + name, 'a')
			plik.writelines(lista)
			plik.close()
	return subjects



def calculate(name, pr_p):
	"""
	Proper trapezoidal sampling function
	"""
	prefix = ''
	subjects = list()
	directory = prefix + 'HAR_extend/' + folder_name + '/'    #path to directory
	for name in listdir(directory):
		filename = directory + '/' + name
		if not filename.endswith('.data'):
			continue
		df = read_csv(filename, header=None)
		values = df.values[:, 1:]
		subjects.append(values)
		pr_n = (400 * 50) / (len(values) - 1)
		liczba = math.floor((len(values)-1)/pr_p*pr_n+1)

		for i in range(liczba):
			poz = (i - 1) / pr_n * pr_p + 1
			accelX =values[math.ceil(poz)-1][0]-(values[math.ceil(poz)-1][0]-values[math.floor(poz)-1][0])*(math.ceil(poz)-poz)
			accelY =values[math.ceil(poz)-1][1]-(values[math.ceil(poz)-1][1]-values[math.floor(poz)-1][1])*(math.ceil(poz)-poz)
			accelZ =values[math.ceil(poz)-1][2]-(values[math.ceil(poz)-1][2]-values[math.floor(poz)-1][2])*(math.ceil(poz)-poz)
			gyroX =values[math.ceil(poz)-1][3]-(values[math.ceil(poz)-1][3]-values[math.floor(poz)-1][3])*(math.ceil(poz)-poz)
			gyroY =values[math.ceil(poz)-1][4]-(values[math.ceil(poz)-1][4]-values[math.floor(poz)-1][4])*(math.ceil(poz)-poz)
			gyroZ =values[math.ceil(poz)-1][5]-(values[math.ceil(poz)-1][5]-values[math.floor(poz)-1][5])*(math.ceil(poz)-poz)
			lista = [str(accelX), ",", str(accelY), ",", str(accelZ), ",", str(gyroX), ",", str(gyroY), ",", str(gyroZ), "\n"]
			listaAcc = [str(accelX), ",", str(accelY), ",", str(accelZ), "\n"]
			listaGyro = [str(gyroX), ",", str(gyroY), ",", str(gyroZ), "\n"]
			if i < 400 :
				plik = open(directory + 'b' + name, 'a')		#open/create file with b before its name
				plik.writelines(lista)
				plik.close()
	return


for folder_name in listdir('HAR_extend/'):
	calculate(folder_name,50)

#for folder_name in listdir('HAR_zeros/'):
#	subjects = append_0(folder_name)

