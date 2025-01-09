from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self, balance: float):
        self.balance = balance

    def pay(self, amount: float):
        if amount > self.balance:
            raise ValueError("Not enough balance.")
        self.balance -= amount
        print(f"[PaymentMethod] Paid {amount}. New balance: {self.balance}")

    @abstractmethod
    def refund(self, amount: float):
        pass

class NonRefundablePaymentMethod(PaymentMethod):
    def refund(self, amount: float):
        raise ValueError("This payment method does not support refunds.")

class NonRefundableGiftCard(NonRefundablePaymentMethod):
    pass

class RefundableGiftCard(PaymentMethod):
    def refund(self, amount: float):
        self.balance += amount
        print(f"[RefundableGiftCard] Refunded {amount}. New balance: {self.balance}")
