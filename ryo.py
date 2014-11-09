#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# RollYourOwn
# author: Bart Grzybicki <bgrzybicki@gmail.com>

__version__ = '0.1'

class Cigarette(object):

    def __init__(self, cig_size='slim', rolled_or_filled='rolled'):
        self.rolled_or_filled = rolled_or_filled
        if cig_size != 'slim' and cig_size != 'regular':
            self.cig_size = 'slim'
        else:
            self.cig_size = cig_size

    def tobacco(self, pack_weight=40, price=18.0):
        if self.cig_size == 'slim':
            print(pack_weight)
            number_of_cigs = pack_weight / 0.5
        elif self.cig_size == 'regular':
            print('pack_weight=' + str(pack_weight)) # temporary
            number_of_cigs = pack_weight / 1.0
        self.tobacco_price = price / number_of_cigs
        return round(self.tobacco_price, 2)

    def filters(self, quantity=120, price=4.0):
        self.filter_price = price / quantity
        return round(self.filter_price, 2)

    def filter_tubes(self, quantity=200, price=4.0):
        self.tube_price = price / quantity
        return round(self.tube_price, 2)

    def paper_leaves(self, quantity=50, price=1.80):
        self.leaf_price = price / quantity
        return round(self.leaf_price, 2)

    def get_cig_price(self):
        if self.rolled_or_filled == 'rolled':
            self.cig_price = self.tobacco_price + self.filter_price + self.leaf_price
        elif self.rolled_or_filled == 'filled':
            self.cig_price = self.tobacco_price + self.tube_price
        return round(self.cig_price, 2)

    def get_pack_price(self):
        return round(self.cig_price * 20, 2)

def cig_config(size='slim', rof='rolled'):
    global cigs
    if rof == 'rolled':
        cigs = Cigarette(size, 'rolled')
        new_prices = get_or_set_prices()
        print(new_prices)
        prices_list = []
        for key, value in new_prices.iteritems():
            print key, value
            prices_list.append(key + '=' + str(value))
        prices_string = ''
        for element in prices_list:
            prices_string = prices_string + element
            if len(prices_list) > 1:
                prices_string = prices_string + ', '
        prices_string = prices_string[:-2]
        print(prices_string)
        code = 'cigs.tobacco({})'.format(prices_string)
        exec code

        print(cigs.filters())
        print(cigs.paper_leaves())
        print(cigs.get_cig_price())
        pack_price = cigs.get_pack_price()
        print(pack_price)
    elif rof == 'filled':
        cigs = Cigarette(size, 'filled')
        print get_or_set_prices()
        print(cigs.tobacco())
        print(cigs.filter_tubes())
        print(cigs.get_cig_price())
        pack_price = cigs.get_pack_price()
        print(pack_price)
    return pack_price

def get_or_set_prices():
    global cigs
    prices_dict = {}
    tobacco_params = cigs.tobacco.func_defaults
    tobacco_weight = raw_input('tobacco weight (' + str(tobacco_params[0]) + ') >')
    if tobacco_weight:
        prices_dict['pack_weight'] = float(tobacco_weight)
    else:
        pass
        #prices_dict['tobacco weight'] = ''
    tobacco_price = raw_input('tobacco price (' + str(tobacco_params[1]) + ') >')
    if tobacco_price:
        prices_dict['price'] = float(tobacco_price)
    else:
        pass
        #prices_dict['tobacco price'] = ''
    return prices_dict

def input_data():
    input_dict = {}
    rof = raw_input('(r)olled or (f)illed? >')
    if rof == 'r' or rof == 'R':
        rof = 'rolled'
    elif rof == 'f' or rof == 'F':
        rof = 'filled'
    size = raw_input('(s)lim or (r)egular? >')
    if size == 's' or size == 'S':
        size = 'slim'
    elif size == 'r' or size == 'R':
        size = 'regular'
    input_dict = {'size': size, 'rof': rof}
    return input_dict

def main():
    user_data = input_data()
    print user_data
    print(cig_config(user_data['size'], user_data['rof']))

if __name__ == '__main__':
    main()
