# 추상회 : 부모 클래스에서 선언한 메소드에 대해서 반드시 사옷ㄱ 받은 클래스에서 기능을 구현 해야 하는 특성
# - 추상 메서드가 포함된 부모 클래스는 객체로 만들 수 ㅇ벗고 단지 상속을 주기 위해서만 조냊
# - 아래의 예제는 사용자 또는 프로그램 개발자가 연결되는 네트워크에 대한 구조를 몰라도 추상화를 통해 연결 기능을 제공 할 수 있음을 보여주는 예쩨

from abc import *

class NetworkAdapter(metaclass=ABCMeta):
    @abstractmethod
    def connect(self):
        pass


class LAN(NetworkAdapter):
    def __init__(self, company):
        self.company = company
    def connect(self):
        print(f"{self.company} LAN 에 연결 했습니다.")

class WIFI(NetworkAdapter):
    def __init__(self, company):
        self.company = company
    def connect(self):
        print(f"{self.company}Wi_fi에 연결 했습니다.")

class LTE(NetworkAdapter):
    def __init__(self, company):
        self.company = company
    def connect(self):
        print(f"{self.company}LTE에 연결 헀습니다.")


net = input("연결할 네트워크를 선택 [1] LAN, [2] Wi-Fi, [3] LTE: ")
if net == "1":
    adapter = LAN("KT Megapass")
    adapter.connect()
elif net == "2":
    adapter = WIFI("SK Telecom")
    adapter.connect()
elif net == "3":
    adapter = LTE("LG U+")
    adapter.connect()
else: print("연결할 네트워크가 없습니다.")