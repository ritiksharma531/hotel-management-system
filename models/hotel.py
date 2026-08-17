class Hotel:
    def __init__(self, hid, name, rating):
        self.hid = hid
        self.name = name
        self.rating = rating

    def __str__(self):
        return f'''{self.hid:<10}{self.name:<35}{self.rating:<20}'''