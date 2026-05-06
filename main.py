# 4-m
class Phone:
    def __init__(self, model, battery, imei):
        self.model = model
        self._battery = battery
        self.__imei = imei  # private

    def call(self, minutes):
        self._battery -= minutes
        if self._battery < 0:
            self._battery = 0

    def charge(self, x):
        self._battery += x
        if self._battery > 100:
            self._battery = 100

    def info(self):
        print(f"Battery:{self._battery}")

phone = Phone("iPhone", 100, "999999")
phone.call(20)
phone.info()
phone.charge(30)
phone.info()
