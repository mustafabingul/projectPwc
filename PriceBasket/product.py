
class Product:

    def __init__(self, name, price, unit):
        self.name = name.lower()
        self.price = int(price)
        self.unit = unit.lower()
        self.discount = None

    def applyDiscount(self, discount):
        self.discount = discount

    @property
    def hasDiscount(self):
        return self.discount is not None

    @property
    def discountedPrice(self):
        if self.discount:
            return int(self.price - self.discountAmount)
        return self.price

    @property
    def discountAmount(self):        
        if self.discount:
            return int(self.price * self.discount.discountPercent / 100.0)
        return 0

    @property
    def discountMessage(self):
        discount_amount_str = '-£{:.2f}'.format(self.discountAmount/100)
        if self.discountAmount < 100:
            discount_amount_str = '-{}p'.format(self.discountAmount)
        if self.discount:
            return '{}: {}'.format(
                self.discount.title, discount_amount_str)
        return None
