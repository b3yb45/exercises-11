class AirConditioning:
    def __init__(self):
        self.__status = False
        self.__temperature = None

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, *args, **kwargs):
        self.__status = self.__status

    @status.getter
    def status(self):
        return self.__status

    @property
    def temperature(self):
        return self.__temperature
    
    @temperature.setter
    def temperature(self, *args, **kwargs):
        self.__temperature = self.__temperature

    @temperature.getter
    def temperature(self):
        return self.__temperature
    
    def switch_on(self):
        self.__status = True
        self.__temperature = 18

    def switch_off(self):
        self.__status = False
        self.__temperature = None

    def reset(self):
        self.switch_off

    def get_temperature(self):
        return self.__temperature
    
    def raise_temperature(self):
        if self.__status:
            self.__temperature += (1 if self.__temperature < 43 else 0)

    def lower_temperature(self):
        if self.__status:
            self.__temperature -= (1 if self.__temperature > 0 else 0)

    def __str__(self):
        if self.__status:
            return f'Кондиционер включен. Температурный режим: {self.__temperature} градусов.'

        return f'Кондиционер выключен.'
    
    def __repr__(self):
        return self.__str__()
    