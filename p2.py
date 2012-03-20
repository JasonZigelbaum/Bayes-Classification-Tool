import sys

def getFile():
  """ Get file from stdin, ask for it if it's not there"""
  # If input, use as stdin
  if len(sys.argv) < 2:
    # Ask the user for the name of the file
    print "Filename: ", 
    filename = sys.stdin.readline().strip()
  # Else use file input.
  else:
    filename = sys.argv[1]

  try:
    fin = open(filename, "r")
  except IOError:
    print "Error: The file '%s' was not found on this system." % filename
    sys.exit(0)
    
  return fin

def createData(fin):
  """ Create an array of dictionaries and return as the data"""
  # Get tags
  tags = [line for line in fin.readline().split()];
  data = []
  # Zip data into a dictionary
  for line in fin.readlines():
    data.append(dict(zip(tags,line.split())));
  return data

def optimalBayes(data, classifier, dataPoint):
  """ Calculate the optimal bayes given a dataset, data point and classifier attribute. NOTE: data point must have all attributes except the classifier. If the test data point is never found within the data set and therefore may as well be random I return nothing."""

  maxVal = 0
  classes = getClasses(data, classifier)
  # Get max for all each class
  for classVal in classes:
    # Probability of the class within the whole data set
    c = probOfClass(data, classifier, classVal)
    # Probability of the data point ex. A C D A within the matching class set of the data
    a = probOfDataPointGivenClass(data, dataPoint, classifier, classVal)
    val = c*a
    if val > maxVal:
      maxClass = classVal
      maxVal = val
  
  if maxVal == 0: return "Test data not seen before. Calculation is irrelevant."
  
  return (maxVal, maxClass)
    
def getClasses(data, classifier):
  """ Returns an array of the possible classes for a classifier in a given dataset"""
  classes = []
  for datum in data:
    if datum[classifier] not in classes:
      classes.append(datum[classifier])
  return classes
  
def probOfAttribute(data, attribute, value):
  """ Gets the probability of a given attribute/value pair within a dataset """
  total = 0
  inst = 0
  for datum in data:
    total+=1
    if datum[attribute] == value:
      inst+=1

  return (float(inst)/total)
  
def probOfClassesGivenAttribute(data, attribute, value, classifier):
  """ Gets the probabilty distro of possible classes given an attribute/value pair """
  classes = getClasses(data, classifier)
  initVals = [0 for classification in classes]
  result = dict(zip(classes,initVals))

  for datum in data:
    if datum[attribute] == value:
      result[datum[classifier]] += 1

  # Return (early %, late %)
  return result
  
def probOfClass(data, classifier, class_value):
  """docstring for probOfClass"""
  result = 0
  for datum in data:
    if (str(datum[classifier]) == class_value):
      result+=1

  return float(result)/len(data)

def probOfDataPointGivenClass(data, data_point, classifier, class_value):
  """docstring for probOfDataPoint"""
  result = 0

  for datum in data:
    # if of the same class
    if (datum[classifier] == class_value):
      shared_item = set(datum.items()) & set(data_point.items())
      if len(shared_item) == len(datum.items()) - 1:
        result += 1

  return float(result)/len(data)

def attributeDistro(data):
  """Prints the probabilty distribution for each attribute in the data """
  for attribute in data[0]:
    types = getClasses(data, attribute)
    for value in types:
      print (attribute, value, probOfAttribute(data, attribute, value))

if __name__ == '__main__':
  # Get file
  fin = getFile()
  # Create Data
  data = createData(fin)
  # Get Optimal Bayes
  testPoint = {'Temp':'C','Hum':'D','Light':'C','Cloud':'C'}

  classes = ["Early", "Late"]
  print(optimalBayes(data, "Time", testPoint))
  print probOfClassesGivenAttribute(data, "Cloud", "D", "Time")
