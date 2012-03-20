import sys, math

def getFile():
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
      
def discretizeData(data):
  """docstring for discretizeData"""
  out = open("discrete_data", "w")
  # Print keys
  for key in data[0]:
    # Remove Date
    if key != "Date":
      out.write(key + " ")
  # New Line
  out.write('\n')
  for datum in data:
    # Set classifier
    if int(datum["Time"]) < 0:
      datum["Time"] = "Early"
    else: datum["Time"] = "Late"
    
    # Segment Temp
    if int(datum["Temp"]) > 15:
      datum["Temp"] = "A" 
    elif int(datum["Temp"]) >= 10:
      datum["Temp"] = "B"
    elif int(datum["Temp"]) > 0:
      datum["Temp"] = "C"
    else:
      datum["Temp"] = "D"
    
    # Segment Humidity
    if int(datum["Hum"]) >= 95:
      datum["Hum"] = "A" 
    elif int(datum["Hum"]) >= 87:
      datum["Hum"] = "B"
    elif int(datum["Hum"]) >= 75:
      datum["Hum"] = "C"
    else:
      datum["Hum"] = "D"
    
    # Convert Light to integers
    datum["Light"] = int(math.floor(float(datum["Light"])))
    
    # Segment Light
    if int(datum["Light"]) > 10:
      datum["Light"] = "A" 
    elif int(datum["Light"]) > 8:
      datum["Light"] = "B"
    elif int(datum["Light"]) > 6:
      datum["Light"] = "C"
    else:
      datum["Light"] = "D"
    
    # Segment Cloud
    if int(datum["Cloud"]) == 100:
      datum["Cloud"] = "A" 
    elif int(datum["Cloud"]) >= 90:
      datum["Cloud"] = "B"
    elif int(datum["Cloud"]) > 20:
      datum["Cloud"] = "C"
    else:
      datum["Cloud"] = "D"
  
    # Write out the data set
    for item in datum:
      if item != "Date":
        out.write(str(datum[item]) + " ");
    
    # New Line
    out.write('\n')
    
  out.close() 
  
if __name__ == '__main__':
  fin = getFile()
  # Get the data into a dictionary
  tags = [line for line in fin.readline().split()];
  data = []
  for line in fin.readlines():
    data.append(dict(zip(tags,line.split())));
  
  discretizeData(data)