class Time:
    def __init__(self, h=0, m=0, s=0):
        self.hour = h
        self.minute = m
        self.seccond = s
        self.fix()

    def show(self):
        print(self.hour, ":", self.minute, ":", self.seccond)

    def fix(self):
        if self.seccond >= 60:
            while self.seccond >= 60:
                self.seccond -= 60
                self.minute += 1
        if self.minute >= 60:
            while self.minute >= 60:
                self.minute -= 60
                self.hour += 1
        if self.seccond < 0:
            while self.seccond < 0:
                self.seccond += 60
                self.minute -= 1
        if self.minute < 0:
            while self.minute < 0:
                self.minute += 60
                self.hour -= 1


    def sum(self, other):
        result = Time()
        result.hour = self.hour + other.hour
        result.minute = self.minute + other.minute
        result.seccond = self.seccond + other.seccond
        result.fix()
        return result

    def sub(self, other):
        result = Time()
        result.hour = self.hour - other.hour
        result.minute = self.minute - other.minute
        result.seccond = self.seccond - other.seccond
        result.fix()
        return result

    def sec_to_hours(self, secconds):
        result = Time()
        result.hour = secconds // 3600
        result.minute = (secconds % 3600) // 60
        result.seccond = (secconds % 3600) % 60
        return result

    def hours_to_sec(self,):
        result = self.hour * 3600 + self.minute * 60 + self.seccond
        return result

