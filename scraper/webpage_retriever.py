import requests
import json
from lxml import html
import unicodedata
import re

BASE_URL = "https://www.reg.uci.edu/perl/WebSoc"

'''
def getResultByDept(dept: str, courseNum: str) -> ():
    data = {
        "Submit" : "Display Web Results",
        "YearTerm" : "2019-92",
        "ShowComments" : "on",
        "ShowFinals" : "on",
        "Breadth" : "ANY",
        "Dept" : dept,
        "CourseNum" : courseNum,
        "Division" : "ANY",
        "ClassType" : "ALL"
    }
    try:
        request = requests.post(BASE_URL, data = data)
    except:
        print("Connection Failed")
        return None
    return _getCourseDict(request.text)
'''

def getResultByCode(courseCode: str):
    data = {
        "Submit" : "Display Web Results",
        "YearTerm" : "2019-92",
        "ShowComments" : "on",
        "ShowFinals" : "on",
        "Breadth" : "ANY",
        "Dept" : "ALL",
        "Division" : "ANY",
        "CourseCodes" : courseCode,
        "ClassType" : "ALL"
    }
    try:
        request = requests.post(BASE_URL, data = data)
    except:
        print("Connection Failed")
        return None
    return _getCourseInfo(request.text)


def _getCourseInfo(webpage: str) -> list:
    res = list()
    title = ''
    doc = html.document_fromstring(webpage)
    courseInfo = doc.xpath("//tr[@valign='top']")
    if not courseInfo or courseInfo == []:
        return [None]
    i = 0
    while i < len(courseInfo):
        details = dict()
        ci = courseInfo[i]
        if ci.get('bgcolor') == '#fff0ff':  # Couese Title
            title = _parseTitle(ci.text_content())
            res.append(title)
            i += 1
        else:   # Course Details
            while ci.get('bgcolor') != '#fff0ff' and i < len(courseInfo):
                code = ci.xpath("./td[1]")[0].text_content()
                _type = ci.xpath("./td[2]")[0].text_content()
                instructor = ci.xpath("./td[5]")[0].text_content()
                status = ci.xpath("./td[17]")[0].text_content()
                
                res.append(code)
                res.append(_type)
                res.append(instructor)
                res.append(status)
                
                i += 1
                if i < len(courseInfo):
                    ci = courseInfo[i]
    return res
            

def _parseTitle(text: str) -> str:
    if not text:
        return "Course Title Not Found"
    text = re.sub(r'\s+', ' ', unicodedata.normalize("NFKD", text.strip()))
    return text if text.find('(') == -1 else text[:text.find('(') - 1]


if __name__ == "__main__":
    print(getResultByCode("20240"))