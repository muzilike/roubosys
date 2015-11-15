# encoding: utf-8
import urllib2
import json

def now():
    res_text = ""
    url_weather = "http://apis.baidu.com/apistore/weatherservice/weather?citypinyin=shanghai"
    url_pm25 = "http://apis.baidu.com/apistore/aqiservice/aqi?city=%e4%b8%8a%e6%b5%b7"
    apikey = "f90d577c266f1869340ae74e1c409669"
    headers = { 'apikey' : apikey}
    req = urllib2.Request(url = url_weather, headers = headers)
    f = urllib2.urlopen(req)
    res = json.loads(f.read())
    if res["errMsg"] == "success":
        res_text = u"城市: " + res["retData"]["city"] + '\n'
        res_text = res_text + u"天气:" + res["retData"]["weather"] + "\n"
        res_text = res_text + u"温度: " + res["retData"]["temp"] + "\n"
        res_text = res_text + u"温度范围: " + res["retData"]["l_tmp"] + "~" + res["retData"]["h_tmp"] + "\n"
    else:
        res_text = "Get weather failed: " + res["errMsg"]

    req = urllib2.Request(url = url_pm25, headers = headers)
    f = urllib2.urlopen(req)
    res = json.loads(f.read())
    if res["retMsg"] == "success":
        res_text = res_text + u"空气指数:" + str(res["retData"]["aqi"]) + "\n"
        res_text = res_text + u"空气水平: " + res["retData"]["level"] + "\n"
        res_text = res_text + u"污染物类型: " + res["retData"]["core"] + "\n"
    else:
        res_text = res_text + "Get pm25 failed: " + res["errMsg"]

    return res_text
