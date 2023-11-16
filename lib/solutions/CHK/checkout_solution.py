
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # empty basket
    if len(skus) == 0: return 0

    # counter for skus
    basket = {item: 0 for item in "ABCD"}
    for item in skus:
        # illegal input
        if item not in basket:
            return -1
        else:
            basket[item] += 1

    # storage of items and prices/deals
    # deals ordered best to worst
    prices = {"A" : {"3A" : 130, "1A" : 50},
              "B" : {"2B" : 45,  "1B" : 30},
              "C" : {"1C" : 20},
              "D" : {"1D" : 15}}

    price = get_price_total(basket, prices)
    return price


def get_price_total(basket, prices):
    price = 0 
    for item in basket:
        for key, val in prices[item]:
            basket_quant = basket[item]
            deal_quant = int(key[0])
            price += (basket_quant // deal_quant) * val

            # update price in basket
            basket[item] = basket_quant % deal_quant

    return price
        

