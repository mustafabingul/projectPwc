class PriceBasket:

    def __init__(self, products, offers):
        
        self.products = products
        self.offers = offers
        self.discounts = []
        self.items = []
        

    def calculateDiscounts(self):

        for ofr in self.offers:
            #enough products for offer
            tmpProds = [p for p in self.items if p.name == ofr.product]
            tmpProdsCount = len(tmpProds)
            #offer count
            offerCount = tmpProdsCount // ofr.productPiece

            if not offerCount:
                continue

            # each discunt products
            discountProducts = [p for p in self.items if p.name == ofr.discountedProduct]
            for dProd in discountProducts:
                dProd.applyDiscount(ofr)
                offerCount -= 1
                if not offerCount:
                    break

    def add(self, item):
        self.items.append(self.products[item.lower()])        

    @property
    def total(self):
        return sum(product.discountedPrice for product in self.items)

    @property
    def subTotal(self):
        return sum(product.price for product in self.items)
    
    @property
    def discountedItems(self):
        return [p for p in self.items if p.hasDiscount]