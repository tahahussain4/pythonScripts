#!/usr/bin/python
# Goal 		: Calculate the comniation of steps if they can down by 1,2,3 
# Argument  : Nunber of steps to go

#TWO algorithms were used
#First Algorithm  : Uses recursion to go thorug possible combination ,printing the combination when it cant go donw any further
#Second Algorithm : Uses first approach but instead of passing a list to print it stores the stepCombinations at each level in the cache making it faster and more resuable

from sys import argv
import time
comboCache = []


########################### 
def generateStepCombinationsV1(steps):
	stepCombo(steps,[],0)

def addIntegerToArray(integer,listOfLists):
	for list in listOfLists:
		list.insert(0,integer)

def printCache():
	for cachedItem in comboCache:
		print cachedItem

def insertIntoArray(array,pos,element):
	if(len(array) < pos + 1):
		while(len(array) < pos + 1):
			array.append("dud")
	if(array[pos] == "dud"):
		array[pos] = element

def getAverageRunTime(function,testArgument,repeats):
	testArray = []
	for testNumber in range(0,repeats):
		timeStart = time.time()
		function(testArgument)
		timeEnd = time.time()
		testArray.append(timeEnd - timeStart)

	return sum(testArray)/float(len(testArray))
#############################

############# FIRST ALGORITHM (BAD ONE) ####################
def stepCombo(steps,previousSteps,level):
	possibleStepCombo = getPossibleStepOptions(steps)
	level = level + 1
	if(possibleStepCombo == []):
		print previousSteps
		return previousSteps

	for index, stepOption in enumerate(possibleStepCombo):
		# print "level"
		# print level
		# print "previousSteps"
		# print previousSteps
		# print "possible combo"
		# print possibleStepCombo

		copyList = previousSteps[:]
		copyList.append(stepOption)
		stepCombo(steps-stepOption,copyList,level)

def getPossibleStepOptions(stepsLeft):
	if(stepsLeft == 0):
		return []
	if(stepsLeft == 1):
		return [1]
	if(stepsLeft == 2):
		return [1,2]
	return [1,2,3]

############## SECOND ALGORITHM ######################
def generateStepCombinationsV2(step):
	#if step 1,0 rchck cahce and return
	try:

		if (isinstance(comboCache[step],str)):
			raise ValueError
		returnlist = [comboCache[step][:]]
		return returnlist

	except (IndexError,ValueError):
		if(step == 0):
			insertIntoArray(comboCache,step,[0])
			return [[0]];

		if(step == 1):
			insertIntoArray(comboCache,step,[1])
			return [[1]];

		megalist = []

		megalist = getStepList(step,1,megalist)

		if(step >= 2):
			megalist = getStepList(step,2,megalist)

		if(step >= 3):
			megalist = getStepList(step,3,megalist)

		insertIntoArray(comboCache,step, megalist)
		return megalist;

def getStepList(step,takenStep,megalist):
		returnList = generateStepCombinationsV2(step-takenStep)
		addIntegerToArray(takenStep,returnList)

		megalist = megalist + returnList
		return megalist


print "RunningScript ==========================" 	
timeArrayOld =[]

print ("timesSlower = " + str(getAverageRunTime(generateStepCombinationsV1,int(argv[1]),1000)/getAverageRunTime(generateStepCombinationsV2,int(argv[1]),1000)))
printCache()



