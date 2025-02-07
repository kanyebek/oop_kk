from abc import ABC, abstractmethod


class OTPService(ABC):
    @abstractmethod
    def sms_send(self):
        pass


class NikitaOTP(OTPService):
    def sms_send(self):
        phone = input("Введите номер телефона в формате +996 xx xx xx")


class Twilio(OTPService):
    def sms_send(self):
        phone = input("Введите номер телефона в формате +7 xxx xx xx xx")


# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
#     @abstractmethod
#     def move(self):
#         pass