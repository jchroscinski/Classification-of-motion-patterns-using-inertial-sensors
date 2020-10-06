# load dataset
from os import listdir
from pandas import read_csv
import math

def calculate_features(folder_name):
	"""
	Uploading files and inserting data into function
	"""
	prefix = ''
	subjects = list()
	directory = prefix + 'HAR_1/' + folder_name + '/'
	for name in listdir(directory):
		filename = directory + '/' + name
		if not filename.endswith('.data'):
			continue
		df = read_csv(filename, header=None)
		values = df.values[:, 1:]
		subjects.append(values)
		run_functions(values, directory, name)
	return subjects

def calc_sum(sumaax,sumaay,sumaaz,sumagx,sumagy,sumagz,values):
	"""
	This function returns sum of all values with columns
	"""
	for j in range(len(values)):
		sumaax = sumaax + values[j][0]
		sumaay = sumaay + values[j][1]
		sumaaz = sumaaz + values[j][2]
		sumagx = sumagx + values[j][3]
		sumagy = sumagy + values[j][4]
		sumagz = sumagz + values[j][5]
	sumAX = sumaax
	sumAY = sumaay
	sumAZ = sumaaz
	sumGX = sumagx
	sumGY = sumagy
	sumGZ = sumagz
	return sumAX, sumAY, sumAZ, sumGX, sumGY, sumGZ

def calc_mean(sumaax,sumaay,sumaaz,sumagx,sumagy,sumagz,values):
	"""
	The function returns the average value calculated over each column
	"""
	sumAX, sumAY, sumAZ, sumGX, sumGY, sumGZ = calc_sum(sumaax,sumaay,sumaaz,sumagx,sumagy,sumagz,values)

	meanAcceelX = float(sumAX) / len(values)
	meanAcceelY = float(sumAY) / len(values)
	meanAcceelZ = float(sumAZ) / len(values)
	meanGyroX = float(sumGX) / len(values)
	meanGyroY = float(sumGY) / len(values)
	meanGyroZ = float(sumGZ) / len(values)
	meanList = [str(meanAcceelX), ",", str(meanAcceelY), ",", str(meanAcceelZ), ",", str(meanGyroX), ",",str(meanGyroY), ",", str(meanGyroZ),"\n"]
	return meanAcceelX, meanAcceelY, meanAcceelZ, meanGyroX, meanGyroY, meanGyroZ, meanList

def calc_rootMeanSquare(sumaax,sumaay,sumaaz,sumagx,sumagy,sumagz,values):
	"""
	The function returns the root mean square calculated over each column
	"""
	for j in range(len(values)):
		sumaax = sumaax + math.pow(values[j][0],2)
		sumaay = sumaay + math.pow(values[j][1],2)
		sumaaz = sumaaz + math.pow(values[j][2],2)
		sumagx = sumagx + math.pow(values[j][3],2)
		sumagy = sumagy + math.pow(values[j][4],2)
		sumagz = sumagz + math.pow(values[j][5],2)

	rootMeanSqareAcceelX = math.sqrt(sumaax / len(values))
	rootMeanSqareAcceelY = math.sqrt(sumaay / len(values))
	rootMeanSqareAcceelZ = math.sqrt(sumaaz / len(values))
	rootMeanSqareGyroX = math.sqrt(sumagx / len(values))
	rootMeanSqareGyroY = math.sqrt(sumagy / len(values))
	rootMeanSqareGyroZ = math.sqrt(sumagz / len(values))
	rootMeanSquareList = [str(rootMeanSqareAcceelX), ",", str(rootMeanSqareAcceelY), ",", str(rootMeanSqareAcceelZ), ",", str(rootMeanSqareGyroX), ",", str(rootMeanSqareGyroY), ",", str(rootMeanSqareGyroZ),"\n"]
	return rootMeanSquareList

def calc_variance(sumaax,sumaay,sumaaz,sumagx,sumagy,sumagz,values):
	"""
	The function returns the variance calculated over each column
	"""
	meanAcceelX, meanAcceelY, meanAcceelZ, meanGyroX, meanGyroY, meanGyroZ, meanList = calc_mean(sumaax,sumaay,sumaaz,sumagx,sumagy,sumagz,values)

	sumVAX = 0.0
	sumVAY = 0.0
	sumVAZ = 0.0
	sumVGX = 0.0
	sumVGY = 0.0
	sumVGZ = 0.0
	for j in range(len(values)):
		sumVAX = sumVAX + math.pow(float(values[j][0]-meanAcceelX),2)
		sumVAY = sumVAY + math.pow((values[j][1]-meanAcceelY),2)
		sumVAZ = sumVAZ + math.pow((values[j][2]-meanAcceelZ),2)
		sumVGX = sumVGX + math.pow((values[j][3]-meanGyroX),2)
		sumVGY = sumVGY + math.pow((values[j][4]-meanGyroY),2)
		sumVGZ = sumVGZ + math.pow((values[j][5]-meanGyroZ),2)
	vaianceAccelX = sumVAX / len(values)
	vaianceAccelY = sumVAY / len(values)
	vaianceAccelZ = sumVAZ / len(values)
	vaianceGyroX = sumVGX / len(values)
	vaianceGyroY = sumVGY / len(values)
	vaianceGyroZ = sumVGZ / len(values)
	varianceList = [str(vaianceAccelX), ",", str(vaianceAccelY), ",", str(vaianceAccelZ), ",", str(vaianceGyroX), ",", str(vaianceGyroY), ",", str(vaianceGyroZ),"\n"]
	return vaianceAccelX, vaianceAccelY, vaianceAccelZ, vaianceGyroX, vaianceGyroY, vaianceGyroZ, varianceList

def calc_meanAbsDeviation(sumaax,sumaay,sumaaz,sumagx,sumagy,sumagz,values):
	"""
	The function returns the mean absolute deviation over each column
	"""
	meanAcceelX, meanAcceelY, meanAcceelZ, meanGyroX, meanGyroY, meanGyroZ, meanList = calc_mean(sumaax,sumaay,sumaaz,sumagx,sumagy,sumagz,values)
	devAX = 0.0
	devAY = 0.0
	devAZ = 0.0
	devGX = 0.0
	devGY = 0.0
	devGZ = 0.0
	for j in range(len(values)):
		devAX = devAX + math.fabs(values[j][0]-meanAcceelX)
		devAY = devAY + math.fabs(values[j][1]-meanAcceelY)
		devAZ = devAZ + math.fabs(values[j][2]-meanAcceelZ)
		devGX = devGX + math.fabs(values[j][3]-meanGyroX)
		devGY = devGY + math.fabs(values[j][4]-meanGyroY)
		devGZ = devGZ + math.fabs(values[j][5]-meanGyroZ)
	meanDevX = devAX / len(values)
	meanDevY = devAY / len(values)
	meanDevZ = devAZ / len(values)
	meanDevAX = devGX / len(values)
	meanDevAY = devGY / len(values)
	meanDevAZ = devGZ / len(values)
	meanDeviationList = [str(meanDevX), ",", str(meanDevY), ",", str(meanDevZ), ",", str(meanDevAX),  ",", str(meanDevAY), ",", str(meanDevAZ),"\n"]
	return meanDeviationList, meanList


def calc_deviation(sumaax,sumaay,sumaaz,sumagx,sumagy,sumagz,values):
	"""
	The function returns the deviation calculated over each column
	"""
	varianceAccelX, varianceAccelY, varianceAccelZ, varianceGyroX, varianceGyroY, varianceGyroZ, varianceList = calc_variance(sumaax,sumaay,sumaaz,sumagx,sumagy,sumagz,values)

	devAX = math.sqrt(varianceAccelX)
	devAY = math.sqrt(varianceAccelY)
	devAZ = math.sqrt(varianceAccelZ)
	devGX = math.sqrt(varianceGyroX)
	devGY = math.sqrt(varianceGyroY)
	devGZ = math.sqrt(varianceGyroZ)

	deviationList = [str(devAX), ",", str(devAY), ",", str(devAZ), ",", str(devGX), ",", str(devGY), ",", str(devGZ),"\n"]
	return deviationList, varianceList

def run_functions(values, directory, name):
	"""
	Feature functions call and writing data to file
	"""
	rootMeanSquareList = calc_rootMeanSquare(sumaax,sumaay,sumaaz,sumagx,sumagy,sumagz,values)
	meanDeviationList, meanList = calc_meanAbsDeviation(sumaax,sumaay,sumaaz,sumagx,sumagy,sumagz,values)
	deviationList, varianceList = calc_deviation(sumaax,sumaay,sumaaz,sumagx,sumagy,sumagz,values)
	plik = open(directory + 'g' + name, 'a')		# you can manipulate g prefix to mark different used methods
	# to save the results with the selected feature extraction method, comment out the others
	plik.writelines(meanList)
	plik.writelines(rootMeanSquareList)
	plik.writelines(meanDeviationList)
	plik.writelines(varianceList)
	plik.writelines(deviationList)
	plik.close()
	return

# resetting variables
sumaax=0.0
sumaay=0.0
sumaaz=0.0
sumagx = 0.0
sumagy = 0.0
sumagz = 0.0

for folder_name in listdir('HAR_1/'):
	calculate_features(folder_name)
