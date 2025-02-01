from abc import ABC,abstractmethod
class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass
    def logout(self):
        pass
class GoogleAuth(UserAuthentication):
    def login(self):
        print("Logging into google is successful")
    def logout(self):
        print("Logging out of the  google")
class FacebookAuth(UserAuthentication):
    def login(self):
        print("Logging into facebook is successful")
    def logout(self):
        print("Logging out of the facebook")
google = GoogleAuth()
facebook= FacebookAuth()
google.login()
google.logout()
facebook.login()
facebook.logout()