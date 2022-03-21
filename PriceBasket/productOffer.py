
class ProductOffer:
    
    def __init__(self, id, title, product, productPiece, discountedProduct, discountPercent):
        
        self.id = id
        self.title = title
        self.product = product.lower()
        self.productPiece = int(productPiece)
        if not self.productPiece:
            raise KeyError('Wrong productPiece value..!')
        self.discountedProduct = discountedProduct.lower()
        if not self.discountedProduct:
            raise KeyError('Wrong discountedProduct value..!')
        self.discountPercent = float(discountPercent)
        if not self.discountPercent:
            raise KeyError('Wrong discountPercent value..!')
