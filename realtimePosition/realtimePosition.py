#-*- coding: utf-8 -*-
#csv format
# realtimePosition { result, doce, developerMessage, link, message, status, total}
# [
#    rowNum, selectedCount, totalCount, subwayId, subwayNm, 
#    statnId, statnNm, trainNo, lastRecptnDt, recptnDt,  
#    updnLine, statnTid, statnTnm, trainSttus, directAt, 
#    lstcarAt
# ]
# api Key : 4943656c6779736f31303174776c5845
# url : http://swopenapi.seoul.go.kr/api/subway/4943656c6779736f31303174776c5845/xml/realtimePosition/0/23/9호선
#http://swopenapi.seoul.go.kr/api/subway/4943656c6779736f31303174776c5845/xml/realtimePosition/0/23/9%ED%98%B8%EC%84%A0
import urllib.request
import urllib.parse
import json
import pandas as pd
import os
import datetime
import logging

class ApiCaller():
  def __init__(self, logger):
    self.logger = logging.getLogger("my")
  def run():
    self.logger.info("run")

def apiKey():
    return "4943656c6779736f31303174776c5845"

def apiDefaultUri():
    return "http://swopenapi.seoul.go.kr/api/subway/{}/json/realtimePosition/{}/{}/{}"

def getApiUrlByParam(startNum=0,endNum=100,lineName="9호선"):
    return apiDefaultUri().format(apiKey(),startNum,endNum,urllib.parse.quote(lineName))
def resultStrFormatChange(jsonStr):
    return jsonStr.replace("\'","\"").replace("None","\"None\"")

def apiCall(uri,filePrefix):
    logger = logging.getLogger("my")
    try:
      logger.info("api call!")
      req = urllib.request.Request(uri)
      res = urllib.request.urlopen(req)
      jsonObj = json.load(res)
      pdataframe = pd.read_json(resultStrFormatChange(str(jsonObj["realtimePositionList"])))
      print(pdataframe)
      pdataframe.to_csv(filePrefix+"-"+str(datetime.datetime.now())+'.csv')
    except urllib.error.HTTPError:
      apiCall(uri,filePrefix)
    finally:
      pass
    
   
    #f = open("myjson.json", 'w')
    #f.write(str(jsonObj["realtimePositionList"]))
    #f.close
    #uploadToHDFS(open("myjson.json","rb"))
    #for row in jsonObj["realtimePositionList"]:
        #print(row["statnNm"])
def uploadToHDFS(file):
    headers = {
      'Content-Type': 'application/octet-stream'
    }
    req  = urllib.request.Request("http://172.20.10.5:50075/webhdfs/v1/user/myjson.json?op=CREATE&&user.name=jinhanchoi&namenoderpcaddress=localhost:9000&overwrite=false",headers=headers,data=file,method="PUT")

    urllib.request.urlopen(req).read()
def setLoggerInfo():
    mylogger = logging.getLogger("my")
    mylogger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    stream_hander = logging.StreamHandler()
    stream_hander.setFormatter(formatter)
    mylogger.addHandler(stream_hander)
    file_handler = logging.FileHandler(str(datetime.datetime.now())+'.log')
    mylogger.addHandler(file_handler)

def main():
    setLoggerInfo()
    logger = logging.getLogger("my")
    logger.info("############# Main Start ##############")
    apiCall(getApiUrlByParam(),"line9")
    apiCall(getApiUrlByParam(lineName="2호선"),"line2")


# python filename.py
if __name__ == "__main__":
    main()
    #uploadToHDFS()

