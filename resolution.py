#!usr/bin/python3
# the resolution function realized in Python
# this is for COMP4418 at UNSW
# written by YONGXI YANG 21/11/2017
# test enviornment:
# Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSCv.1900 32 bit (Intel)] on win32.
# the input format is
#        python resolution.py '[p imp q, (neg r) imp (neg q)] seq [p imp r]'
#
#        imp means ->
#        neg means not
#        iff means <->
#        and means interception
#        or  means Union


import argparse
import re

def parserArgument():

    parser = argparse.ArgumentParser(description = 'Resolution Project')
    parser.add_argument('proposition', type = str,\
        help = "the propsition you need to prove,the format is '[p imp q, (neg r) imp (neg q)] seq [p imp r]'",\
        action = 'store')

    return parser.parse_args()

class ResolutionError(object):
    def __init__(self, message):
        self.message = message

class ResolutionIOError(object):
    def __init__(self, message):
        self.message = message

class Resolution(object):
    def __init__(self, proposition):
        self.proposition = proposition

    def text_process(self):
        """
        this fucntion can cut the proposition string into atom.
        """
        pass

    def eliminate_atom(self):
        """
        this is the rule of resolution.
        """
        pass

    def convert2CNF(self):
        """
        this fucntion can convert the Proposition.
        """
        pass

    def resolution(self, porposition):
        """
        this fucntion is for calculating the truth of proposition using the resolution method.
        """
        pass

    def print_step(self):
        """
        this function print every step of proving.
        """
        pass

if __name__ == "__main__":
    argv = parserArgument()
    # print(argv.proposition)
    r = Resolution(argv.porposition)