class Restaurant:
    def __init__(self, name):
        self.restaurant_name = name  
        self.reviews_data = []

    def name(self):  
        return self.restaurant_name

    def add_review_restaurant(self, review):
        self.reviews_data.append(review)

    def reviews(self):
        return self.reviews_data

    def customers(self):
        return list(set([review.customer() for review in self.reviews_data]))

    def average_star_rating(self):
        if not self.reviews_data:
            return 0
        total_ratings = sum([review.rating() for review in self.reviews_data])
        return total_ratings / len(self.reviews_data)

    def __str__(self):
        return f"Restaurant: {self.name}"