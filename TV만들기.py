

class Television : # 클래스 이름은 대문자로 시작
    def __init__(self , name, on, channel, volume) :        #생성자
        self.name = name
        self.is_on = on
        self.channel = channel
        self.volume = volume


    def set_on(self, on):
        self.is_on = on


    def set_channel(self,cnl):
        self.channel = cnl


    def set_volume(self,vol):
        self.volume = vol


    def get_on(self):
        return self.is_on


    def get_channel(self):
        return self.channel


    def get_volume(self):
        return self.volume

    def view_tv(self):
        power = ("OFF", "ON")
        print(f"이름 : {self.name}")
        print(f"전원 : {power[self.is_on]}")
        print(f"채널 : {self.channel}")
        print(f"볼륨: {self.volume}")

lg_tv = Television("LG" , False , 10,10)        # 생성자 값
samsung_tv = Television("Samsung" , False , 10,10)
samsung_tv.view_tv()
lg_tv.view_tv()
