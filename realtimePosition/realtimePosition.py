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

def apiKey():
    return "4943656c6779736f31303174776c5845"

def apiDefaultUri():
    return "http://swopenapi.seoul.go.kr/api/subway/{}/json/realtimePosition/{}/{}/{}"

def getApiUrlByParam(startNum=0,endNum=30,lineName="9호선"):
    return apiDefaultUri().format(apiKey(),startNum,endNum,urllib.parse.quote(lineName))

def apiCall(uri):
    req = urllib.request.Request(uri)
    res = urllib.request.urlopen(req)
    jsonObj = json.load(res)
    for row in jsonObj["realtimePositionList"]:
        print(row["statnNm"])

def main():
    print(getApiUrlByParam())
    print(apiCall(getApiUrlByParam()))



# python filename.py
if __name__ == "__main__":
    main()

