class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.review_customer = customer
        self.review_restaurant = restaurant
        self.rating_score = rating
        Review.all_reviews.append(self)
        restaurant.add_review_restaurant(self)
        customer.add_review_customer(self)

    def rating(self):
        return self.rating_score

    def customer(self):
        return self.review_customer

    def restaurant(self):
        return self.review_restaurant

    @classmethod
    def all(cls):
        return cls.all_reviews

    def __str__(self):
        return f"Review by {self.review_customer.given_name()} for {self.review_restaurant.name()}: {self.rating_score}"