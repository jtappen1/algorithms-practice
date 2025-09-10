'''
Factory Method implementation in Python
'''
from abc import ABC, abstractmethod

# Simple Factory:
class EmailNotification1:
    def send(self, send_message):
        print(f'Sending email message: {send_message}')

class TextNotification1:
    def send(self, send_message):
        print(f'Sending text message: {send_message}')

class WhatsappNotification1:
    def send(self, send_message):
        print(f'Sending Whatsapp message: {send_message}')

class NotificationFactory:
    @staticmethod
    def send_notification(msg_type: str):
        match msg_type:
            case 'EMAIL':
                return EmailNotification1()
            case 'TEXT':
                return TextNotification1()
            case 'WHATSAPP':
                return WhatsappNotification1()
            case _:
                return ValueError("Unknown Type")

class NotificationService:
    def send_notification(msg_type, msg) -> None:
        notification = NotificationFactory.send_notification(msg_type)
        notification.send(msg)


#########################################################################


# Factory Design Method
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
       print(f"Sending Message {message}")
    
class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"Sending push notification: {message}")


class NotificationCreator(ABC):
    @abstractmethod
    def create_notification(self):
        pass

    def send(self, message):
        notification = self.create_notification()
        notification.send(message)
class ConcreteEmailCreator(NotificationCreator):
    def create_notification(self):
       return EmailNotification()

class ConcreteSMSCreator(NotificationCreator):
    def create_notification(self):
        return SMSNotification()

class ConcretePushNotificationCreator(NotificationCreator):
    def create_notification(self):
        return PushNotification()



if __name__ == "__main__":
    NotificationService.send_notification('EMAIL', 'hello world')

    creator = ConcreteEmailCreator()
    creator.send("hello world")


    