from abc import ABC,abstractmethod

class OrderProcess(ABC):

    def select_item(self):
        print('Selecting Item...') 
    
    @abstractmethod
    def make_payment(self):
        pass

    @abstractmethod
    def deliver_item(self):
        pass

    @abstractmethod
    def process_order(self):
        self.select_item()
        self.make_payment()
        self.deliver_item()

class DigitalOrder(OrderProcess):
    def make_payment(self):
        print('Processing online payment')
    
    def deliver_item(self):
        print('Sending download link via email')


class PhysicalOrder(OrderProcess):

    def make_payment(self):
        print("Processing payment at checkout...")

    def deliver_item(self):
        print("Arranging shipping for physical delivery.")

# Client code
def client_code(order: OrderProcess):
    order.process_order()
    
if __name__ == "__main__":
    print("Digital Order:")
    client_code(DigitalOrder())
    
    print("\nPhysical Order:")
    client_code(PhysicalOrder())
    