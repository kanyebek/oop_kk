import lessons.lesson3 as ml

class RUSms (ml.OTPService):
    def sms_send(self):
        input("Номер телефона +7 xxx xx xx xx")

ru_sms = RUSms()
ru_sms.sms_send()

