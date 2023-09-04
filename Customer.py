from Review import Review

class Customer:
    all_customers = []

    def __init__(self,given_name,family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        self.fullName = given_name + " " + family_name
        Customer.all_customers.append(self)

    def full_name(self):
        return (f"Full name: {self.given_name} {self.family_name}")
    
    @classmethod
    def all(cls):
        return cls.all_customers

    def add_review(self, restaurant, rating):
        review_by_customer = Review(self, restaurant, rating)
        return review_by_customer

    def add_review_customer(self,review):
        self.reviews.append(review)

    def restaurants(self):
        return list(set([review.restaurant() for review in self.reviews]))

    def num_reviews(self):
        return len(self.reviews)

    @classmethod
    def find_by_name(cls, name):
        for customerObj in cls.all_customers:
            if customerObj.full_name() == name:
                return customerObj
            else:        
                print("There is no customer with that full name.")

    @classmethod
    def find_all_by_given_name(cls, name):
        customer_match_list = []
        for customerObj in cls.all_customers:
            if customerObj.given_name() == name:
                customer_match_list.append(customerObj)
                return customer_match_list
            else:
                print("There is no customer with that given name.")
             