import Papago

papago = Papago.Papago()

while True:
    code = int(input("""
파파고 월드~!
1. 번역하고 싶은 언어
2. 번역하고 싶은 말 넣기
3. 번역하기
4. 결과보기
5. 파파고 월드 종료하기
: """))
    if code == 1:
        papago.setting()
    if code == 2:
        papago.translate()
    if code == 3:
        papago.send()
    if code == 4:
        papago.getResult()
    if code == 5:
        break
print("파파고 월드를 이용해 주셔서 감사합니다~!")