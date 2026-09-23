# 상속: 부모클래스에서 만든 변수와 메서드를 물려 받아 사용할 수 있음
# 오버라이딩: 부모 클래스의 메서드를 상속 받아 재정의 하는 것

class ProtoTV:   # 상속을 주기 위한 부모 클래스
    # 전원, 채널, 볼륨을 매개변수로 하는 생성자 생성
    def __init__(self, on, channel, volume):
        self.is_on = on
        self.channel = channel
        self.volume = volume

    # 전원을 켜고 끄는 메서드
    def set_on(self, on):
        self.is_on = on

    # 채널 설정 메서드 (1 ~ 1000)
    def set_channel(self, cnl):
        if 0 < cnl <= 1000:
            self.channel = cnl
            print(f"채널을 {cnl}로 변경 하였습니다.")
        else:
            print(f"채널 설정 범위가 아닙니다.")

    # 볼륨 설정 메서드 (0 ~ 100)
    def set_volume(self, vol):
        if 0 <= vol <= 100:
            self.volume = vol
            print(f"볼륨을 {vol}로 변경 하였습니다.")
        else:
            print(f"볼륨 설정 범위가 아닙니다.")

# class ProductTV(ProtoTV):
#    def set_channel(self, cnl):  # 오버라이딩
#         if 0 < cnl <= 2000:
#             self.channel = cnl
#             print(f"채널을 {cnl}로 변경 하였습니다.")
#         else:
#             print(f"채널 설정 범위가 아닙니다.")

    # 정보를 출력하는 메서드 만들기
    def print_tv(self):
        print(f"전원: {'ON' if self.is_on else 'OFF'}")
        print(f"채널: {self.channel}")
        print(f"볼륨: {self.volume}")


productTV = ProductTV(False, 10, 10)
productTV.set_on(True)
productTV.set_volume(45)
productTV.set_channel(1200)
productTV.print_tv()