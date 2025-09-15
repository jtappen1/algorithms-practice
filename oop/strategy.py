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


################################################################################################################################################
# Credit Card Payment Process

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class ApplePay(Payment):
    def pay(self, amount):
        return f"Payed using Apple Pay {amount}"

class Crypto(Payment):
    def pay(self, amount):
        return f"Payed using Crypto {amount}"

def checkout(method: str, amount: float):
    strategies = {
        "Crypto": Crypto(),
        "ApplePay": ApplePay()
    }
    strategy = strategies.get(method)
    if strategy is None:
        raise ValueError("Invalid payment type")
    print(strategy.pay(amount))

if __name__ == '__main__':
    service = ShippingCostService(FlatRateShipping(10))
    service.calculate_shipping_cost(10)

    checkout("Crypto", 10.0)
    checkout("ApplePay", 100.0)

    
################################################################################################################################################
'''
You’re creating a path cost engine. Depending on context, a vehicle might want to minimize distance, travel time, tolls, or fuel. 
The system should allow switching among these approaches at runtime while keeping the rest of the navigation pipeline the same.
'''


class PathCost(ABC):
    @abstractmethod
    def minimize_cost(self, cost):
        pass

class DistanceCost(PathCost):
    def minimize_cost(self, cost):
        return f"Minimizing distance cost: {cost}"
    
class FuelCost(PathCost):
    def minimize_cost(self, cost):
        return f"Minimizing fuel cost: {cost}"
    

class Engine:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PathCost):
        self.strategy = strategy
    
    def run_pipeline(self, cost):
       print(self.strategy.minimize_cost(cost))

if __name__ == "__main__":
    engine = Engine(FuelCost())
    engine.run_pipeline(10)   # Minimize fuel cost

    engine.set_strategy(DistanceCost())
    engine.run_pipeline(10)   # Minimize distance cost

        