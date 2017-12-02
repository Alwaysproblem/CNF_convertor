#!usr/bin/python3
# the convert2CNF function is applied using Python
# this is for COMP4418 at UNSW
# written by Prophet 28/11/2017 and Thanks to Eric Martin who is Dr Eric Matin of COMP9021.
#
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
from binarytree import *
from stack import *

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


    def is_CNF(self):
        """
        check if it satisfy CNF rules.
        """
        pass

    # the De Morgan law:

    def neg_neg(self,BT):
        """
        the neg-neg rules.

        >>> from binarytree import BinaryTree 
        >>> t = BinaryTree("neg")
        >>> t.left_node = BinaryTree("neg")
        >>> t.left_node.left_node = BinaryTree("p")
        >>> t.print_binary_tree()
                    p
              neg
        <BLANKLINE>
        neg
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        >>> a = CNF("")
        >>> x = a.neg_neg(t)
        >>> x.print_binary_tree()
        p
        >>> c = BinaryTree("neg")
        >>> c.left_node = BinaryTree("neg")
        >>> c.left_node.left_node = BinaryTree("neg")
        >>> c.left_node.left_node.left_node = BinaryTree("p")
        >>> c.print_binary_tree()
                          p
                    neg
        <BLANKLINE>
              neg
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        neg
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        >>> x = a.neg_neg(c)
        >>> x.print_binary_tree()
              p
        neg
        <BLANKLINE>
        >>> d = BinaryTree("neg")
        >>> d.left_node = BinaryTree("p")
        >>> x = a.neg_neg(d)
        >>> x.print_binary_tree()
              p
        neg
        <BLANKLINE>
        >>> e = BinaryTree("p")
        >>> x = a.neg_neg(e)
        >>> x.print_binary_tree()
        p
        """
        if BT.value == "neg" and BT.left_node.value == "neg":
            return BT.left_node.left_node
        else:
            return BT

    def neg_and_or(self, BT, mode):
        """
        !(p or q) == !p and !q
        !(p and q) == !p or !q

        >>> from binarytree import BinaryTree 
        >>> t = BinaryTree("neg")
        >>> t.left_node = BinaryTree("neg")
        >>> t.left_node.left_node = BinaryTree("p")
        >>> t.print_binary_tree()
                    p
              neg
        <BLANKLINE>
        neg
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        >>> a = CNF("")
        >>> x = a.neg_and_or(t,'neg-or')
        >>> x.print_binary_tree()
                    p
              neg
        <BLANKLINE>
        neg
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        >>> r = BinaryTree("neg")
        >>> r.left_node = BinaryTree("or")
        >>> r.left_node.left_node = BinaryTree("p")
        >>> r.left_node.right_node = BinaryTree("q")
        >>> r.print_binary_tree()
                    p
              or
                    q
        neg
        <BLANKLINE>
        <BLANKLINE>
        <BLANKLINE>
        >>> x = a.neg_and_or(r,'neg-or')
        >>> x.print_binary_tree()
        """
        if BT.value == 'neg' and BT.left_node.value in ['and', 'or']:
            BT.left_node.value = 'neg'
            BT.right_node = BinaryTree("neg")
            if mode == 'neg-or':
                BT.value = 'and'
            elif mode == 'neg-and':
                BT.value = 'or'
            BT.right_node.left_node = BT.left_node.right_node
            BT.left_node.right_node = BinaryTree()
            BT.right_node.right_node = BinaryTree()
        else:
            pass
        return BT

    def morgan_rules(self, mode):
        """
        the converting rules --- De Morgan law.
        """
        pass

    def gen_tries(self):
        """
        generate the binary tries for input proposition.
        """
        pass

    def CNF_simplifier(self):
        """
        simplify the non-CNF proposition. 
        """
        pass

    def showCNF(self):
        """
        showing the CNF result.
        """
        pass





if __name__ == '__main__':
    # import doctest
    # doctest.testmod()

    r = BinaryTree("neg")
    r.left_node = BinaryTree("or")
    r.left_node.left_node = BinaryTree("p")
    r.left_node.right_node = BinaryTree("q")
    r.print_binary_tree()
    t = BinaryTree("and")
    t.left_node = BinaryTree("neg")
    t.left_node.left_node = BinaryTree("p")
    t.right_node = BinaryTree("neg")
    t.right_node.right_node = BinaryTree("p")
    t.print_binary_tree()


    a = CNF("")
    x = a.neg_and_or(r,'neg-or')
    x.print_binary_tree()

    # argv = parserArgument()
    # a = BinaryTree()
    # b = Stack()
    # print(b)
    # print(a)
    # pro_after_CNF = CNF(argv.proposition)
    # print(argv.proposition)


 