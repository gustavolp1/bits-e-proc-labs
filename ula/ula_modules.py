#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b
        carry.next = a & b

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    s = [Signal(bool(0)) for i in range(3)]
    haList = [None for i in range(2)]


    haList[0] = halfAdder(a, b, s[0], s[1]) 
    haList[1] = halfAdder(c, s[0], soma, s[2])

    @always_comb
    def comb():
        carry.next = s[1] | s[2]

    return instances()


@block
def adder2bits(x, y, soma, carry):

    temp = Signal(bool(0))
    full_1 = fullAdder(x[0], y[0], 0, soma[0], temp)
    full_2 = fullAdder(x[1], y[1], temp, soma[1], carry)
    
    return instances()


@block
def adder(x, y, soma, carry):

    n = len(x)
    faList = [None for i in range(n)]
    temp = [Signal(bool(0)) for i in range(n)]

    faList[0] = fullAdder(x[0], y[0], 0, soma[0], temp[0])
    for i in range(1, n):
        faList[i] = fullAdder(x[i], y[i], temp[i-1], soma[i], temp[i])

    @always_comb
    def comb():
        carry.next = temp[n-1]

    return instances()
