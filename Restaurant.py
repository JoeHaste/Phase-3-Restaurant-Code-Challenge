class Restaurant:
    all_restaurants = []

    def __init__(self,name="",):
        self.name = name
        Restaurant.all_restaurants.append(self)

    @classmethod
    def all(cls):
        return cls.all_restaurants