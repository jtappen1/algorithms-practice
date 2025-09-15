'''
Practicing the Singleton Pattern for Design and OOP Interviews
'''
from threading import Lock

class ThreadsafeSingleton:
    _instance = None
    _lock = Lock()

    def __init__(self):
        if ThreadsafeSingleton._instance is not None:
            raise Exception("Use get_instance instead")

    @staticmethod
    def get_instance():
        with ThreadsafeSingleton._lock:
            if ThreadsafeSingleton._instance is None:
                ThreadsafeSingleton._instance = ThreadsafeSingleton()
        
        return ThreadsafeSingleton._instance

# So there is a static method on the class, so to get the singleton ThreadSafeSingleton is called with the get_instance method. 
# That uses the _lock attribute which is defined as a class variable and is available globally, so there is only one per instance globally. 
# That is what makes it threadsafe, and then from there if there is not a instance created we initialize it and set it, otherwise we just return it. 
# And so that single instance that is available globally and can't be replicated.


####################################################################################################################################################
# Singleton Practice

from threading import Lock
class Logger:
    _instance = None
    _lock = Lock()
    def __init__(self):
        if Logger._instance is not None:
            raise Exception("Use get_instance instead")
        
    @staticmethod
    def get_instance():
        with Logger._lock:
            if Logger._instance is None:
                Logger._instance = Logger()
        return Logger._instance

    def log(self, message: str):
        with open(self._log_file, "a") as f:
            f.write(message + "\n")



####################################################################################################################################################################################################################################


class LocalizationService:
    _instance = None
    def __init__(self):
        if LocalizationService._instance is not None:
            raise Exception("Use get_instance instead")
        
    @staticmethod
    def get_instance():
        if LocalizationService._instance is None:
            LocalizationService._instance = LocalizationService()
        return LocalizationService._instance
    
    def access(self):
        print("Accessing Service.....")


if __name__ == "__main__":
    service = LocalizationService.get_instance()
    service.access()



