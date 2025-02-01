class Notification:
    def send(self,mesg):
        self.mesg=mesg
        print(f"{self.mesg} notification has been sent")
class EmailNotification:
    def send(self,mesg):
        self.mesg=mesg
        print(f"{self.mesg} Email has been sent")
class SMSNotification:
    def send(self,mesg):
        self.mesg=mesg
        print(f"{self.mesg} SMS has been sent")
No=Notification()
No.send("Whatsapp new 3 messages")
e=EmailNotification()
e.send("Tommorrow is declared holiday")
n=SMSNotification()
n.send("Your data package is expiring soon")