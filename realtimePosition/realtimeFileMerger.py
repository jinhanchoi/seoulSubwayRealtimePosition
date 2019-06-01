import os

def getFileListFromDirPath(filePath):
  resultFiles = []
  for root,dir,files in os.walk(filePath):
    for file in files:
      if '.csv' in file:
        resultFiles.append(os.path.join(root,file))  
  return resultFiles

def readCsvFile(fileName,readHeader=False):
  with open(fileName,'r') as f:
    if readHeader == True:
      return f.readlines()
    else:
      return f.readlines()[1:]

def main():
  list = getFileListFromDirPath("./results_pos/line9")
  with open("realtimePosition_line9.csv",'w') as output:
    for (idx,f) in enumerate(list):
      if idx == 0:
        content = readCsvFile(f,True)
      else:
        content = readCsvFile(f,False)
      for line in content:
        output.write(line)
      
# python filename.py
if __name__ == "__main__":
    main()