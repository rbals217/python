# 에어컨 만들기
# 전원 ON/OFF
# 현재 온도 표시 기능 : 기본값은 20도로 설정
# 온도 조절 기능 (1도씩 조절 가능), 원하는 온도 설정
# 바람 세기 조절 기능 (1단계, 2단계, 3단계)
class AirCon:
    def __init__(self, power, temp, step):
        self.power = power
        self.temp = temp
        self.wind_step = step
        self.curr_temp = 5

    def set_power(self, is_on):
        self.power = is_on

    def set_temp(self, temp):
        self.temp = temp

    def set_wind_step(self, step):
        self.wind_step = step

    def view_info(self):
        wind_str = "", "1단계", "2단계", "3단계"
        print(f"전원 : {self.power and 'ON' or 'OFF'}")
        print(f"현재 온도 : {self.curr_temp}")
        print(f"설정 온도 : {self.temp}")
        print(f"바람 세기 : {wind_str[self.wind_step]}")


my_air_con = AirCon(False, 22, 1)
my_air_con.set_power(True)
my_air_con.set_wind_step(3)
my_air_con.set_temp(24)
my_air_con.view_info()