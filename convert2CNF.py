#!usr/bin/python3
# the convert2CNF function is applied using Python
# this is for COMP4418 at UNSW
# written by Prophet 28/11/2017
# test enviornment:
# Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSCv.1900 32 bit (Intel)] on win32.
# the input format is
#        python convert2CNF.py '[p imp q, (neg r) imp (neg q)] seq [p imp r]'
#
#        imp means    ->
#        neg means    not
#        iff means    <->
#        and means    interception
#        or  means    Union

import argparse

def parserArgument():
    """
    acquire the system parameters
    """
    parser = argparse.ArgumentParser(description = 'Convert2CNF Project')
    parser.add_argument('proposition', type = str,\
        help = "the propsition you need to prove,the format is '[p imp q, (neg r) imp (neg q)] seq [p imp r]'",\
        action = 'store')

    return parser.parse_args()

class CNF(object):
    def __init__(self, proposition):
        self.prop = proposition

    def funcname(self, parameter_list):
        pass

    def is_CNF(self):
        pass

    def morgan_rules(self, mode):
        pass

    def gen_tries(self):
        pass

    def showCNF(self):
        pass





if __name__ == '__main__':
    argv = parserArgument()
    pro_after_CNF = CNF(argv.proposition)
    # print(argv.proposition)


