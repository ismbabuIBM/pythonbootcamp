veg_price_list = [('Tomato', 50.00), ('Carrot', 97.50), ('Beans', 34.25), ('Onion', 90)]

#find the lowest cost veggie of the day
def veggie_of_the_day(salePrice, veg_of_the_day):
    for veg, vegPrice in veg_price_list:
        if salePrice > vegPrice:
            salePrice = vegPrice
            veg_of_the_day = veg
        else:
            pass
    print('Veggie of the Day is :' + veg_of_the_day)

#function calling
veggie_of_the_day(100, "")
