#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# RollYourOwn
# author: Bart Grzybicki <bgrzybicki@gmail.com>

__version__ = '0.1'

import os
import platform
import re

class Cigarette(object):

    def __init__(self, cig_size='slim', rolled_or_filled='rolled'):
        self.rolled_or_filled = rolled_or_filled
        if cig_size != 'slim' and cig_size != 'regular':
            self.cig_size = 'slim'
        else:
            self.cig_size = cig_size

    def tobacco(self, tobacco_weight=40, tobacco_price=18.0):
        if self.cig_size == 'slim':
            #print(tobacco_weight)
            number_of_cigs = tobacco_weight / 0.5
        elif self.cig_size == 'regular':
            #print('pack_weight=' + str(tobacco_weight)) # temporary
            number_of_cigs = tobacco_weight / 1.0
        self.tobacco_price = tobacco_price / number_of_cigs
        return round(self.tobacco_price, 2)

    def filters(self, filters_quantity=120, filters_price=4.0):
        self.filter_price = filters_price / filters_quantity
        return round(self.filter_price, 2)

    def filter_tubes(self, filter_tubes_quantity=200, filter_tubes_price=4.0):
        self.tube_price = filter_tubes_price / filter_tubes_quantity
        return round(self.tube_price, 2)

    def paper_leaves(self, paper_leaves_quantity=50, paper_leaves_price=1.80):
        self.leaf_price = paper_leaves_price / paper_leaves_quantity
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
        new_prices_dict = get_or_set_prices(size, rof)
        #print(new_prices_dict)
        if 'tobacco_weight' or 'tobacco_price' in new_prices_dict:
            prices_list = []

            for key, value in new_prices_dict.iteritems():
                #print key, value
                if re.match('tobacco', key):
                    prices_list.append(key + '=' + str(value))
            prices_string = ''
            for element in prices_list:
                prices_string = prices_string + element
                if len(prices_list) > 1:
                    prices_string = prices_string + ', '
            prices_string = prices_string[:-2]
            #print(prices_string)
            code = 'cigs.tobacco({})'.format(prices_string)
            #print('code=' + code)
            exec code

        if 'filters_quantity' or 'filters_price' in new_prices_dict:
            prices_list = []

            for key, value in new_prices_dict.iteritems():
                #print key, value
                if re.match('filters', key):
                    prices_list.append(key + '=' + str(value))
            prices_string = ''
            for element in prices_list:
                prices_string = prices_string + element
                if len(prices_list) > 1:
                    prices_string = prices_string + ', '
            prices_string = prices_string[:-2]
            #print(prices_string)
            code = 'cigs.filters({})'.format(prices_string)
            #print('code=' + code)
            exec code

        if 'paper_leaves_quantity' or 'paper_leaves_price' in new_prices_dict:
            prices_list = []

            for key, value in new_prices_dict.iteritems():
                #print key, value
                if re.match('paper', key):
                    prices_list.append(key + '=' + str(value))
            prices_string = ''
            for element in prices_list:
                prices_string = prices_string + element
                if len(prices_list) > 1:
                    prices_string = prices_string + ', '
            prices_string = prices_string[:-2]
            #prices_dict['paper_leaves_price'] = float(paper_leaves_price)(prices_string)
            code = 'cigs.paper_leaves({})'.format(prices_string)
            #print('code=' + code)
            exec code

        #print(cigs.get_cig_price())
        cig_price = cigs.get_cig_price()
        pack_price = cigs.get_pack_price()
        #print(pack_price)#raw_input()
    elif rof == 'filled':
        cigs = Cigarette(size, 'filled')
        new_prices_dict = get_or_set_prices(size, rof)
        #print(new_prices_dict)

        if 'tobacco_weight' or 'tobacco_price' in new_prices_dict:
            prices_list = []

            for key, value in new_prices_dict.iteritems():
                #print key, value
                if re.match('tobacco', key):
                    prices_list.append(key + '=' + str(value))
            prices_string = ''
            for element in prices_list:
                prices_string = prices_string + element
                if len(prices_list) > 1:
                    prices_string = prices_string + ', '
            prices_string = prices_string[:-2]
            #print(prices_string)
            code = 'cigs.tobacco({})'.format(prices_string)
            #print('code=' + code)
            exec code

        if 'filter_tubes_quantity' or 'filter_tubes_price' in new_prices_dict:
            prices_list = []

            for key, value in new_prices_dict.iteritems():
                #print key, value
                if re.match('filter_tubes', key):
                    prices_list.append(key + '=' + str(value))
            prices_string = ''
            for element in prices_list:
                prices_string = prices_string + element
                if len(prices_list) > 1:
                    prices_string = prices_string + ', '
            prices_string = prices_string[:-2]
            #print(prices_string)
            code = 'cigs.filter_tubes({})'.format(prices_string)
            #print('code=' + code)
            exec code
        cig_price = cigs.get_cig_price()
        pack_price = cigs.get_pack_price()
        #print(pack_price)
    return cig_price, pack_price

def get_or_set_prices(size='slim', rof='rolled'):
    global cigs
    prices_dict = {}
    tobacco_params = cigs.tobacco.func_defaults
    filters_params = cigs.filters.func_defaults
    filter_tubes_params = cigs.filter_tubes.func_defaults
    paper_leaves_params = cigs.paper_leaves.func_defaults

    tobacco_weight = raw_input('tobacco weight (' + str(tobacco_params[0]) + ') >')
    if tobacco_weight:
        prices_dict['tobacco_weight'] = float(tobacco_weight)
    else:
        pass

    tobacco_price = raw_input('tobacco price (' + str(tobacco_params[1]) + ') >')
    if tobacco_price:
        prices_dict['tobacco_price'] = float(tobacco_price)
    else:
        pass

    if rof == 'rolled':
        filters_quantity = raw_input('filters quantity (' + str(filters_params[0]) + ') >')
        if filters_quantity:
            prices_dict['filters_quantity'] = int(filters_quantity)
        else:
            pass

        filters_price = raw_input('filters price (' + str(filters_params[1]) + ') >')
        if filters_price:
            prices_dict['filters_price'] = float(filters_price)
        else:
            pass

    if rof == 'filled':
        filter_tubes_quantity = raw_input('filter tubes quantity (' + str(filter_tubes_params[0]) + ') >')
        if filter_tubes_quantity:
            prices_dict['filter_tubes_quantity'] = int(filter_tubes_quantity)
        else:
            pass

        filter_tubes_price = raw_input('filter tubes price (' + str(filter_tubes_params[1]) + ') >')
        if filter_tubes_price:
            prices_dict['filter_tubes_price'] = float(filter_tubes_price)
        else:
            pass

    if rof == 'rolled':
        paper_leaves_quantity = raw_input('paper leaves quantity (' + str(paper_leaves_params[0]) + ') >')
        if paper_leaves_quantity:
            prices_dict['paper_leaves_quantity'] = int(paper_leaves_quantity)
        else:
            pass

        paper_leaves_price = raw_input('paper leaves price (' + str(paper_leaves_params[1]) + ') >')
        if paper_leaves_price:
            prices_dict['paper_leaves_price'] = float(paper_leaves_price)
        else:
            pass

    #print('prices_dict=' + str(prices_dict))
    return prices_dict

def input_data():
    input_dict = {}
    running = True
    while running:
        cigs_daily = raw_input('how many cigs you smoke daily? >')
        if cigs_daily.isdigit():
            running = False

    running = True
    while running:
        rof = raw_input('(r)olled or (f)illed? >')
        if rof == 'r' or rof == 'R':
            rof = 'rolled'
            running = False
        elif rof == 'f' or rof == 'F':
            rof = 'filled'
            running = False

    running = True
    while running:
        size = raw_input('(s)lim or (r)egular? >')
        if size == 's' or size == 'S':
            size = 'slim'
            running = False
        elif size == 'r' or size == 'R':
            size = 'regular'
            running = False
    input_dict = {'size': size, 'rof': rof, 'cigs_daily': int(cigs_daily)}
    return input_dict

def clear_screen():
    ''' Clears the screen.

    usage: clearscreen()
    '''
    os_platform = platform.system()
    if os_platform == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def print_header():
    print('RollYourOwn ' + __version__ )

def get_savings(cigs_daily, ryo_cig_price, ord_cig_price):
    savings_dict = {}
    cigs_monthly = cigs_daily * 30
    cigs_yearly = cigs_monthly * 12

    cigs_daily_price = cigs_daily * ryo_cig_price
    cigs_monthly_price = cigs_daily_price * 30
    cigs_yearly_price = cigs_monthly_price * 12

    ord_cigs_daily_price = cigs_daily * ord_cig_price
    ord_cigs_monthly_price = ord_cigs_daily_price * 30
    ord_cigs_yearly_price = ord_cigs_monthly_price * 12

    savings_daily = ord_cigs_daily_price - cigs_daily_price
    savings_monthly = ord_cigs_monthly_price - cigs_monthly_price
    savings_yearly = ord_cigs_yearly_price - cigs_yearly_price

    savings_dict['cigs_daily'] = cigs_daily
    savings_dict['cigs_monthly'] = cigs_monthly
    savings_dict['cigs_yearly'] = cigs_yearly

    savings_dict['cigs_daily_price'] = cigs_daily_price
    savings_dict['cigs_monthly_price'] = cigs_monthly_price
    savings_dict['cigs_yearly_price'] = cigs_yearly_price

    savings_dict['ord_cigs_daily_price'] = ord_cigs_daily_price
    savings_dict['ord_cigs_monthly_price'] = ord_cigs_monthly_price
    savings_dict['ord_cigs_yearly_price'] = ord_cigs_yearly_price

    savings_dict['savings_daily'] = savings_daily
    savings_dict['savings_monthly'] = savings_monthly
    savings_dict['savings_yearly'] = savings_yearly

    savings_dict['ordinary_cig_price'] = ord_cig_price

    return savings_dict

def ordinary_cig_price():
    ord_cigpack_price = 14
    ord_cig_price = ord_cigpack_price / 20.0
    ord_cig_price = round(ord_cig_price, 2)
    print('fuct returns: ' + str(ord_cig_price))
    return  ord_cig_price

def print_savings(ryo_savings_dict):
    print('Ordinary cig pack price: ' + str(ryo_savings_dict['ordinary_cig_price'] * 20))
    print('Ordinary cig price: ' + str(ryo_savings_dict['ordinary_cig_price']))
    print('Cigs smoked per day: ' + str(ryo_savings_dict['cigs_daily']))
    print('Daily price of ordinary cigs: ' + str(ryo_savings_dict['cigs_daily_price']))
    print('Cigs smoked per month: ' + str(ryo_savings_dict['cigs_monthly']))
    print('Monthly price of ordinary cigs: ' + str(ryo_savings_dict['cigs_monthly_price']))

    #savings_dict = {}
    #savings_dict['cigs_monthly'] = cigs_monthly
    #savings_dict['cigs_yearly'] = cigs_yearly
    #savings_dict['cigs_daily_price'] = cigs_daily_price
    #savings_dict['cigs_monthly_price'] = cigs_monthly_price
    #savings_dict['cigs_yearly_price'] = cigs_yearly_price
    # savings_dict['ord_cigs_daily_price'] = ord_cigs_daily_price
    # savings_dict['ord_cigs_monthly_price'] = ord_cigs_monthly_price
    # savings_dict['ord_cigs_yearly_price'] = ord_cigs_yearly_price
    # savings_dict['savings_daily'] = savings_daily
    # savings_dict['savings_monthly'] = savings_monthly
    # savings_dict['savings_yearly'] = savings_yearly
    # #savings_dict['ordinary_cig_price'] = ord_cig_price
    # #return savings_dict

def main():
    clear_screen()
    print_header()
    user_data = input_data()
    print('user_data=' + str(user_data))
    #print(cig_config(user_data['size'], user_data['rof']))
    ryo_costs_list = cig_config(user_data['size'], user_data['rof'])
    print(ryo_costs_list)
    ord_cig_price = ordinary_cig_price()
    print('ord_cig_price=' + str(ord_cig_price))
    smoker_savings_dict = get_savings(user_data['cigs_daily'], ryo_costs_list[0], ord_cig_price)
    print(smoker_savings_dict)
    print_savings(smoker_savings_dict)

if __name__ == '__main__':
    main()
