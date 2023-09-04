class Customer:
    all_customers = []

    def __init__(self,given_name,family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self)

    def full_name(self):
        return (f"Full name: {self.given_name} {self.family_name}")
    
    @classmethod
    def all(cls):
        return cls.all_customers