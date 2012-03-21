from bayesToolkit import *

if __name__ == '__main__':
  # Get file
  fin = getFile()
  # Create Data
  data = createData(fin)
  # Get Optimal Bayes
  testPoint = {'Temp':'C','Hum':'D','Light':'C','Cloud':'C'}
  
  print optimalBayes(data, "Time", testPoint)
  print probOfClassesGivenAttribute(data, "Cloud", "D", "Time")
