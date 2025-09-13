# Item
# Name: str
# Price: float
# id: int

# Enum Coin
# Penny = 0.01
# Nickel = 0.05 
# Dime = 0.1
# Quarter = 0.25

# Enum Cash
# Dollar = 1 
# fiver
# tenner 
# twenty

# inventory:
# Products: dict[str, Product]
# quantities:  dict[str, int]
# addItem
# getItemAvailability
# reduceStock
# getItem


# VendingMachine:
#- Inventory
# current_state: VendingMachineState
# balance
# selectedItem
# getInstance(): VendingMachine
# insertCoin(coin: Coin) -> None
# insertCash(cash: Cash) -> None
# dispense() -> Item

# VendingMachineState
# selectItem()
# dispense()
# refund()
# insertMoney





# Singleton Class

# Exception

from enum import Enum
from abc import ABC , abstractmethod

class Item:
    def __init__(self, name: str, price: float, id: str):
        self.name = name
        self.price = price 
        self.id = id
    
class Coin(Enum):
    PENNY = 0.01
    NICKEL = 0.05
    DIME = 0.1
    QUARTER = 0.25

class Cash(Enum):
    ONE = 1
    FIVE = 5
    TEN = 10
    TWENTY = 20

class Inventory:

    def __init__(self):
        self.products : dict[str, Item]
        self.quanitites : dict[str, int]
    
    def add_item(item: Item, quanitity: int) -> None:
        pass

    def reduce_stock(item: Item) -> None:
        pass
    
    def availability(id: str) -> bool:
        pass

    def get_item(id: str) -> Item:
        pass

class VendingMachine:
    pass

class VendingMachineState(ABC):

    def __init__(self, machine: 'VendingMachine'):
        self.machine = machine
    
    @abstractmethod
    def select_item(self, id: str):
        pass

    @abstractmethod
    def insert_money(self, amount: float):
        pass

    @abstractmethod
    def refund(self):
        pass

    @abstractmethod
    def dispense(self):
        pass

class IdleState(VendingMachineState):
    """State when machine is waiting for user interaction."""
    
    def insert_coin(self, coin: Coin):
        print("Please select an item before inserting money.")
    
    def select_item(self, code: str):
        if not self.machine.get_inventory().is_available(code):
            print("Item not available.")
            return
        
        self.machine.set_selected_item_code(code)
        # Import here to avoid circular dependency
        self.machine.set_state(ItemSelectedState(self.machine))
        print(f"Item selected: {code}")
    
    def dispense(self):
        print("No item selected.")
    
    def refund(self):
        print("No money to refund.")


class ItemSelectedState(VendingMachineState):
    """State when an item has been selected but insufficient money inserted."""
    
    def insert_coin(self, coin: Coin):
        self.machine.add_balance(coin.get_value())
        print(f"Coin inserted: {coin.get_value()}¢ ({coin.name})")
        
        selected_item = self.machine.get_selected_item()
        if selected_item and self.machine.get_balance() >= selected_item.get_price():
            print("Sufficient money received.")
            # Import here to avoid circular dependency
            self.machine.set_state(HasMoneyState(self.machine))
    
    def select_item(self, code: str):
        print("Item already selected. Please insert money or request refund to select a different item.")
    
    def dispense(self):
        print("Please insert sufficient money.")
    
    def refund(self):
        self.machine.refund_balance()
        self.machine.reset()
        # Import here to avoid circular dependency
        self.machine.set_state(IdleState(self.machine))


class HasMoneyState(VendingMachineState):
    """State when sufficient money has been inserted."""
    
    def insert_coin(self, coin: Coin):
        # Allow more coins (will be returned as change)
        self.machine.add_balance(coin.get_value())
        print(f"Additional coin inserted: {coin.get_value()}¢ ({coin.name}) - will be returned as change.")
    
    def select_item(self, code: str):
        print("Item already selected. Please dispense or request refund to select a different item.")
    
    def dispense(self):
        # Import here to avoid circular dependency
        self.machine.set_state(DispensingState(self.machine))
        self.machine.dispense_item()
    
    def refund(self):
        self.machine.refund_balance()
        self.machine.reset()
        # Import here to avoid circular dependency
        self.machine.set_state(IdleState(self.machine))


class DispensingState(VendingMachineState):
    """State when item is being dispensed - blocks all user input."""
    
    def insert_coin(self, coin: Coin):
        print("Currently dispensing. Please wait.")
    
    def select_item(self, code: str):
        print("Currently dispensing. Please wait.")
    
    def dispense(self):
        # Already triggered by HasMoneyState
        print("Dispensing in progress...")
    
    def refund(self):
        print("Dispensing in progress. Refund not allowed.")