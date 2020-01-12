#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019

@author: swilson5
"""
import math


class Calculator:
    def __init__(self, nums):
        self.data = nums
        self.calc_stats()
    def get_median(self):
        n = len(self.sorted_data)
        if (n%2 == 0):
            return (((self.sorted_data[n//2]) + (self.sorted_data[n//2 - 1]))/2)
        else:
            return self.sorted_data[len(self.sorted_data)//2]
    def get_variance(self):
        list_of_diffs = [(x - self.mean)**2 for x in self.data]
        return sum(list_of_diffs)/(len(self.data) - 1)
    def get_stand_dev(self):
        self.variance = self.get_variance()
        std_dev = ((self.variance)**(.5))
        return std_dev
    def calc_stats(self):
        self.length = len(self.data)
        self.mean = sum(self.data)/len(self.data)
        self.sorted_data = sorted(self.data)
        self.median = self.get_median()
        self.variance = self.get_variance()
        self.stand_dev = self.get_stand_dev()
    def add_data(self, new_nums):
        self.data.extend(new_nums)
        self.calc_stats()
    def remove_data(self, new_nums):
        for item in new_nums:
            if item in self.data:
                self.data.remove(item)
        self.calc_stats()
