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