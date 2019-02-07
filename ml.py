
#functions available for clients 

# --- annotations ---
def callable(func):
    print("marking {} as callable".format(func))
    func.callable = True
    return func 

def periodic(period_in_minutes):
    def wrapper(func):
        print("marking {} to run every {} minute".format(func, period_in_minutes))
        func.period_in_minutes = period_in_minutes
        return func
    return wrapper

# --- de/serialization functions ---
import dill

def storeClass(myClass, filename):
    with open('storage.dill', 'wb') as storage:
        dill.dump(myClass(), storage)

def loadInstance(filename):
    with open('storage.dill', 'rb') as storage:
        return dill.load(storage)

# --- a sketch of a class that holds and loaded instance ---
# this could be in a seprate library, as it is needed only on the server side

import inspect

class InstanceHolder():
    def __init__(self, filename):
        self.instance = loadInstance(filename)

        self.callables = {}
        self.periodics = {}

        for name, obj in inspect.getmembers(self.instance):
            if hasattr(obj,'callable') and obj.callable:
                print("callable: ", name)
                self.callables[name] = obj
            elif hasattr(obj, 'period_in_minutes'):
                print("periodic({}): {}".format(obj.period_in_minutes, name))
                self.periodics[obj.period_in_minutes] = obj 

        # run the startup method if there is one
        if hasattr(obj,'startup'):
            obj.startup()


    def runLoop(self):
        for t in range(20): # simulate 20 minutes
            print("time: ", t)
            for period, func in self.periodics.items():
                if t % period == 0:
                    func()

    def method(self, index):
        # this is kinda fake... but you get the idea
        return list(self.callables.values())[index]
