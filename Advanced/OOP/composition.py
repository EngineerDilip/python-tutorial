#Example: Composition
# Define the Component Classes (Engine and Wheel)
class Engine:
    def __init__(self, horsepower: int, type: str):
        self.horsepower = horsepower
        self.type = type

    def start(self):
        return f"Engine with {self.horsepower} HP ({self.type}) starts."

    def stop(self):
        return f"Engine with {self.horsepower} HP ({self.type}) stops."

class Wheel:
    def __init__(self, size: int):
        self.size = size

    def rotate(self):
        return f"Wheel of size {self.size} inches rotates."

    def stop_rotation(self):
        return f"Wheel of size {self.size} inches stops rotating."

# Contain class (Car), The Car class will contain an Engine object and a list of Wheel objects.

class Car:
    def __init__(self, make: str, model: str, engine: Engine, wheels: list[Wheel]):
        self.make = make
        self.model = model
        self.engine = engine  # Engine instance is a part of Car
        self.wheels = wheels  # List of Wheel instances is a part of Car

    def start(self):
        engine_status = self.engine.start()
        wheels_status = [wheel.rotate() for wheel in self.wheels]
        return f"{self.make} {self.model}:\n{engine_status}\n" + "\n".join(wheels_status)

    def stop(self):
        engine_status = self.engine.stop()
        wheels_status = [wheel.stop_rotation() for wheel in self.wheels]
        return f"{self.make} {self.model}:\n{engine_status}\n" + "\n".join(wheels_status)


# Create an Engine instance
engine = Engine(horsepower=300, type="V6")

# Create a list of Wheel instances
wheels = [Wheel(size=18) for _ in range(4)]  # Assuming a 4-wheeled car

# Create a Car instance
my_car = Car(make="Toyota", model="Camry", engine=engine, wheels=wheels)

# Test the Car's start and stop methods
print(my_car.start())
print(my_car.stop())

# Now even we can add more component class dynamically
class Sunroof:
    def open(self):
        return "Sunroof opens."

    def close(self):
        return "Sunroof closes."

# Adding Sunroof to Car dynamically
my_car.sunroof = Sunroof()
print(my_car.sunroof.open())  # Using the new component dynamically


# Example: Decorator Pattern with Composition
class GPS:
    def get_location(self):
        return "Current location: 123 Main St."

class HeatedSeats:
    def warm_up(self):
        return "Seats are now heated."

class SportCar:
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model
        self.features = []

    def add_feature(self, feature):
        self.features.append(feature)

    def describe_features(self):
        #ternary condition: expression if (condition) else expression
        descriptions = [feature.get_location() if hasattr(feature, "get_location") else feature.warm_up() 
                        for feature in self.features]
        return "\n".join(descriptions)

# Usage
my_car = SportCar("Toyota", "Camry")
my_car.add_feature(GPS())
my_car.add_feature(HeatedSeats())

print(my_car.describe_features())


#Example: Implementing Interfaces or Protocols 
# Payment process. checkout can be done with different payment type( PayPal, Credit Card,..etc)

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount:float) -> str:
        pass

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount:float) -> str:
        return f"Processed ${amount} with PayPal."

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount:float) -> str:
        return f"Processed ${amount} with Credit Card."

# Checkout class (container) contain payment type 
class Checkout:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor

    def pay(self, amount):
        return self.payment_processor.process_payment(amount)

# Usage
checkout_with_paypal = Checkout(PayPalProcessor())
print(checkout_with_paypal.pay(100))

checkout_with_cc = Checkout(CreditCardProcessor())
print(checkout_with_cc.pay(200))


# Example: Dependency Injection in a Notification System
# Imagine a notification system where you can switch between SMS and email notifications.

class SMSNotifier:
    def send(self, message):
        return f"Sending SMS: {message}"

class EmailNotifier:
    def send(self, message):
        return f"Sending Email: {message}"

class NotificationService:
    def __init__(self, notifier):
        self.notifier = notifier

    def notify(self, message):
        return self.notifier.send(message)

# Usage
sms_service = NotificationService(SMSNotifier())
print(sms_service.notify("Hello via SMS"))

email_service = NotificationService(EmailNotifier())
print(email_service.notify("Hello via Email"))


#Example: Order States
"""Imagine an Order class that changes behavior based on different states (e.g., Paid, Shipped, Delivered)."""

# OrderState Kind of abstract class
class OrderState:
    def next_state(self, order):
        raise NotImplementedError

# each derived class update the Order's next state.
class PaidState(OrderState):
    def next_state(self, order):
        order.state = ShippedState()
        return "Order is now shipped."

class ShippedState(OrderState):
    def next_state(self, order):
        order.state = DeliveredState()
        return "Order is now delivered."

class DeliveredState(OrderState):
    def next_state(self, order):
        order.state = OrderCompleteState()
        return "Order is already delivered."
    
class OrderCompleteState(OrderState):
    def next_state(self, order):
        return "Order is completed."

# Container class, Order has OrderState 
class Order:
    def __init__(self):
        self.state = PaidState()  # Start with the Paid state

    def next_state(self):
        return self.state.next_state(self)

# Usage
order = Order()
print(order.next_state())  # "Order is now shipped."
print(order.next_state())  # "Order is now delivered."
print(order.next_state())  # "Order is already delivered."
print(order.next_state())  # "Order is completed"

