
import argparse
import sys
from PriceBasket import product
from PriceBasket import priceBasket
from PriceBasket import productOffer
from PriceBasket import logger

logger = logger.Logger()

def myArgs(argv=None):    
    parser = argparse.ArgumentParser(prog='PriceBasket')    
    parser.add_argument(
        'items',
        metavar='item',
        type=str,
        nargs='+',
        help='Plese add item to basket.')
    return parser.parse_args(argv)

def main(argv=None):
    
    #arguments
    args = myArgs(argv)
    #print(args)
    p1 = product.Product('Soup', 65, 'tin')
    p2 = product.Product('Bread', 80, 'loaf')
    p3 = product.Product('Apples',100, 'bag')
    p4 = product.Product('Milk', 130, 'bottle')    
    items = {}
    items[p1.name]=p1
    items[p2.name]=p2
    items[p3.name]=p3
    items[p4.name]=p4
    d1 = productOffer.ProductOffer(1,'Apples 10% off','Apples',1,'Apples',10)
    d2 = productOffer.ProductOffer(2,'Buy 2 tins soup get you a half price loaf','Soup', 2,'Bread',50)
    offers = []
    offers.append(d1)
    offers.append(d2)    

    myBasket = priceBasket.PriceBasket(items, offers)
    for item in args.items:
        myBasket.add(item)

    # calculation results
    print(f'Subtotal: £{myBasket.subTotal/100:.2f}')
    myBasket.calculateDiscounts()
    if myBasket.discountedItems:
        for item in myBasket.discountedItems:
            print(item.discountMessage)
    else:
        print('(No offers available)')
    print(f'Total: £{myBasket.total/100:.2f}')

if __name__ == '__main__':
    sys.exit(main())
