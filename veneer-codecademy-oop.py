class Art:
    def __init__(self, artist, title, medium, year, owner):
        self.artist = artist
        self.title = title
        self.medium = medium
        self.year = year
        self.owner = owner

    def __repr__(self): # dunder
        return "{name}. \"{quote}\". {year}, {medium}. {owner_name}, {owner_loc}.".format(
            name=self.artist, quote=self.title, year=self.year, medium=self.medium, 
            owner_name=self.owner.name, owner_loc=self.owner.location
        )

class Markeplace:
    def __init__(self):
        self.listings = []

    def add_listing(self, new_listing):
        self.listings.append(new_listing)
    
    def remove_listing(self, expired_listing):
        self.listings.remove(expired_listing)

    def show_listing(self):
        for listing in self.listings:
            print(listing)

class Client:
    def __init__(self, name, location, is_museum):
        self.name = name
        self.is_museum = is_museum
        if is_museum:
            self.location = location
        else:
            self.location = "Private Collection"

    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            new_listing = Listing(artwork, price, self)
            veneer.add_listing(new_listing)

class Listing:
    def __init__(self, art, price, seller):
        self.art = art
        self.price = price
        self.seller = seller

    def __repr__(self):
        return '{art}, {price}'.format(
            art=self.art, price=self.price
        )

veneer = Markeplace()
#veneer.show_listing()

edytta = Client("Edytta Halpirt", None, is_museum=False)
moma = Client("The MOMA", "New York", is_museum=True)

girl_with_medium = Art(
    "Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas", edytta
    )
print(girl_with_medium)