# Observer Interface 
# - Has an update method, all concrete modules will implement the interface

# Subject Interface
# - We have this so that the 

from abc import ABC, abstractmethod
# Abstract Observer class
class FitnessDataObserver(ABC):
    @abstractmethod
    def update(self, data):
        pass

# Abstract Subject Class
class FitnessDataSubject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass
    
    @abstractmethod
    def remove_observer(self, observer):
        pass
    
    @abstractmethod
    def notify_observers(self):
        pass

class FitnessData(FitnessDataSubject):
    
    def __init__(self):
        self.steps = 0
        self.active_minutes = 0
        self.calories = 0
        self.observers = []
    
    def register_observer(self, observer):
        self.observers.append(observer)
    
    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)
    
    def new_fitness_data_pushed(self, steps, active_minutes, calories):
        self.steps = steps
        self.active_minutes = active_minutes
        self.calories = calories

        print(f"\nFitnessData: New data received – Steps: {steps}, "
              f"Active Minutes: {active_minutes}, Calories: {calories}")
        
        self.notify_observers()

    def daily_reset(self):
        self.steps = 0
        self.active_minutes = 0
        self.calories = 0
        
        print("\nFitnessData: Daily reset performed.")
        self.notify_observers()
    
    # Getters
    def get_steps(self):
        return self.steps
    
    def get_active_minutes(self):
        return self.active_minutes
    
    def get_calories(self):
        return self.calories

class LiveActivityDisplay(FitnessDataObserver):
    def update(self, data):
        print(f"Live Display → Steps: {data.get_steps()} "
              f"| Active Minutes: {data.get_active_minutes()} "
              f"| Calories: {data.get_calories()}")
        
class ProgressLogger(FitnessDataObserver):
    def update(self, data):
        print(f"Logger → Saving to DB: Steps={data.get_steps()}, "
              f"ActiveMinutes={data.get_active_minutes()}, "
              f"Calories={data.get_calories()}")
        
class GoalNotifier(FitnessDataObserver):
    def __init__(self):
        self.step_goal = 10000
        self.goal_reached = False
    
    def update(self, data):
        if data.get_steps() >= self.step_goal and not self.goal_reached:
            print(f"Notifier → 🎉 Goal Reached! You've hit {self.step_goal} steps!")
            self.goal_reached = True
    
    def reset(self):
        self.goal_reached = False

def fitness_app_observer_demo():
    fitness_data = FitnessData()
    
    display = LiveActivityDisplay()
    logger = ProgressLogger()
    notifier = GoalNotifier()
    
    # Register observers
    fitness_data.register_observer(display)
    fitness_data.register_observer(logger)
    fitness_data.register_observer(notifier)
    
    # Simulate updates
    fitness_data.new_fitness_data_pushed(500, 5, 20)
    fitness_data.new_fitness_data_pushed(9800, 85, 350)
    fitness_data.new_fitness_data_pushed(10100, 90, 380)  # Goal should trigger
    
    # Daily reset
    notifier.reset()
    fitness_data.daily_reset()


#########################################################################################################################################################
# 1.  Make the subject: This is the object that maintains the statem and notifies the observers how it changes.
class Stock:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        self._observers = []
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

# Make the Observer Base class, this will have the update method that will be called 
class Observer(ABC):
    @abstractmethod
    def update(self, stock):
        pass

class PriceAlert(Observer):
    def __init__(self, threshold: int):
        self.threshold =threshold

    def adjust_threshold(self, threshold):
        self.threshold = threshold

    def update(self, stock):
        if self.threshold < stock.price:
            print(f"Alert! {stock.name} price is above {self.threshold}: {stock.price}")

def market():
    apple_stock = Stock("APPL", 10)
    alert1 = PriceAlert(15)
    alert2 = PriceAlert(20)

    apple_stock.attach(alert1)
    apple_stock.attach(alert2)

    apple_stock.price = 25
    apple_stock.notify()

#########################################################################################################################################################
# Scenario – Weather Station / Display System

# You are building a weather monitoring system. The system tracks weather data (temperature, humidity, pressure) and notifies multiple display units whenever data changes.
# Requirements:
# The WeatherStation is the subject — it stores the current weather readings.

# Multiple displays can subscribe to updates:
# CurrentConditionsDisplay → shows the current temperature and humidity.
# StatisticsDisplay → shows average, min, and max temperature over time.
# ForecastDisplay → shows a simple forecast based on pressure trends.
# Displays should update automatically whenever the weather changes.

# You should be able to add or remove displays at runtime.

import numpy as np
class WeatherStation:
    def __init__(self,  temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
        self._observers = {}
    
    def attach(self, observer):
        if observer.name in self._observers:
            raise Exception("Display Already Exists")
        self._observers[observer.name] = observer
    
    def detach(self, observer):
        if observer.name not in self._observers:
            raise Exception("Display not found in Observers")
    
    def notify(self):
        for observer in self._observers.values():
            observer.update(self)

class Observer(ABC):
    def __init__(self, name):
        self.name = name
        
    @abstractmethod
    def update(self, weather_station):
        pass

class CurrentConditionsDisplay(Observer):
    def __init__(self, name):
        super().__init__(name)

    def update(self, weather_station):
        print(f"Current Temp: {weather_station.temperature} Current Humidity: {weather_station.humidity}")
    
class StatisticsDisplay(Observer):
    def __init__(self, name):
        super().__init__(name)
        self._temperatures = []
        self._humidity = []
    
    def clear(self):
        self._temperatures.clear()
        self._humidity.clear() 

    def update(self, weather_station):
        self._temperatures.append(weather_station.temperature)
        self._humidity.append(weather_station.humidity)
        print(f"Mean temp: {np.mean(self._temperatures)} Mean Humidity {np.mean(self._humidity)}")

def demo_station():
    ws = WeatherStation(100, 0.5)
    ws.attach(StatisticsDisplay("StatsDisplay"))
    ws.attach(CurrentConditionsDisplay("CurrConditionsDisplay"))

    ws.temperature = 40
    ws.notify()

    ws.humidity = 0.8
    ws.notify()

if __name__ == "__main__":

    # print("\n\n=== Observer Pattern Approach ===")
    # fitness_app_observer_demo()

    # market()

    demo_station()
