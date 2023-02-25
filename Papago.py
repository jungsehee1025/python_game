import os
import sys
import urllib.request
import json

class Papago:
    client_id = "rG8AkHHbVbLhFbVr1iYz"
    client_secret = ""
    url = "https://openapi.naver.com/v1/papago/n2mt"
    translatedText = ""
    data = ""
    targetLanguage = "en"
    def send(self):
        request = urllib.request.Request(self.url)
        request.add_header("X-Naver-Client-Id", self.client_id)
        request.add_header("X-Naver-Client-Secret", self.client_secret)
        response = urllib.request.urlopen(request, data=self.data.encode("utf-8"))
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            result = response_body.decode('utf-8')
            jsonRes = json.loads(result)
            self.translatedText = jsonRes["message"]["result"]["translatedText"]
            print("번역 되었습니다.")
        else:
            print("Error Code:" + rescode)
    def getResult(self):
        print(self.translatedText)
    def translate(self):
        text = input("번역하고 싶은 말을 넣어주세요: ")
        encText = urllib.parse.quote(text)
        self.data = f"source=ko&target={self.targetLanguage}&text=" + encText
    def setting(self):
        self.targetLanguage = input("바꾸고 싶은 언어를 입력해주세요: ")