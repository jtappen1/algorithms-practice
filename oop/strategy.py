'''
Strategy Pattern.  
Useful if you have multiple ways to perform a task or calculation.
The behavior of the class changes at runtime.
Essentially define a family of algorithms that are interchangeable and can be set at runtime.
'''
from abc import ABC, abstractmethod

class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, order):
        pass

class FlatRateShipping(ShippingStrategy):
    def __init__(self,rate):
        self.rate = rate
    
    def calculate_cost(self, order):
        print(f"Calculating with Flat Rate strategy (${self.rate})")
        return self.rate 

class WeightBasedShipping(ShippingStrategy):
    def __init__(self, rate_per_kg):
        self.rate_per_kg = rate_per_kg
    
    def calculate_cost(self, order):
        print(f"Calculating with Weight-Based strategy (${self.rate_per_kg}/kg)")
        return order.get_total_weight() * self.rate_per_kg
    
class ShippingCostService:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        print(f"ShippingCostService: Strategy changed to {strategy.__class__.__name__}")
        self.strategy = strategy
    
    def calculate_shipping_cost(self, order):
        return self.strategy.calculate_cost(order) 

if __name__ == '__main__':
    service = ShippingCostService(FlatRateShipping(10))
    service.calculate_shipping_cost(10)

    
