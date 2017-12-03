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
import copy

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


    def or_and(self, BT):
        """
        (p and q) or c = (p or c) and (q or c)

        """ 
        if BT.value == 'or':
            if BT.left_node.value == 'and' and BT.right_node.value != 'and':
                BT.value = "and"
                BT.left_node.value = 'or'
                right_copy_tree = copy.deepcopy(BT.right_node)
                new_tree = BinaryTree("or")
                BT.right_node, new_tree.right_node = new_tree, BT.right_node
                BT.right_node.left_node = BT.left_node.right_node
                BT.left_node.right_node = right_copy_tree

            elif BT.right_node.value == 'and' and BT.left_node.value != 'and':
                BT.value = "and"
                BT.right_node.value = 'or'
                right_copy_tree = copy.deepcopy(BT.left_node)
                new_tree = BinaryTree("or")

                BT.left_node, new_tree.left_node = new_tree, BT.left_node
                BT.left_node.right_node = BT.right_node.left_node
                BT.right_node.left_node = right_copy_tree

            else:
                pass
        else:
            pass

        return BT

    def and_or_and(self, BT):
        """
        (p and q) or (r and t) = (p or r) and (p or t) and (q or r) and (q or t).
        """
        if BT.value == 'or':
            if BT.left_node.value == 'and' and BT.right_node.value == 'and':
                BT.value = 'and'
                new_tree_list = [BinaryTree("or") for _ in range(0,4)]
                new_tree_list[0].left_node = copy.deepcopy(BT.left_node.left_node)
                new_tree_list[0].right_node = copy.deepcopy(BT.right_node.left_node)
                new_tree_list[1].left_node = copy.deepcopy(BT.left_node.left_node)
                new_tree_list[1].right_node = copy.deepcopy(BT.right_node.right_node)
                new_tree_list[2].left_node = copy.deepcopy(BT.left_node.right_node)
                new_tree_list[2].right_node = copy.deepcopy(BT.right_node.left_node)
                new_tree_list[3].left_node = copy.deepcopy(BT.left_node.right_node)
                new_tree_list[3].right_node = copy.deepcopy(BT.right_node.right_node)
    
                BT.left_node.left_node = new_tree_list[0]
                BT.left_node.right_node = new_tree_list[1]
                BT.right_node.left_node = new_tree_list[2]
                BT.right_node.right_node = new_tree_list[3]
            else:
                pass
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

    # r = BinaryTree("neg")
    # r.left_node = BinaryTree("and")
    # r.left_node.left_node = BinaryTree("p")
    # r.left_node.right_node = BinaryTree("q")
    # r.print_binary_tree()

    # t = BinaryTree("and")
    # t.left_node = BinaryTree("neg")
    # t.left_node.left_node = BinaryTree("p")
    # t.right_node = BinaryTree("neg")
    # t.right_node.left_node = BinaryTree("q")
    # t.print_binary_tree()

    ### the test for or-and law!!
    # r = BinaryTree("or")
    # r.left_node = BinaryTree("and")
    # r.left_node.left_node = BinaryTree("p")
    # r.left_node.right_node = BinaryTree("q")
    # r.right_node = BinaryTree("c")
    # print("\nthe or_left_and tree:")
    # r.print_binary_tree()

    # r = BinaryTree("or")
    # r.right_node = BinaryTree("and")
    # r.right_node.left_node = BinaryTree("p")
    # r.right_node.right_node = BinaryTree("q")
    # r.left_node = BinaryTree("c")

    # print("\nthe or_right_and tree:")
    # r.print_binary_tree()

    # the test for and-or-and law
    r = BinaryTree("or")
    r.right_node = BinaryTree("and")
    r.left_node = BinaryTree("and")
    r.right_node.left_node = BinaryTree("r")
    r.right_node.right_node = BinaryTree("t")
    r.left_node.left_node = BinaryTree("p")
    r.left_node.right_node = BinaryTree("q")
    print("\nthe and-or-and tree:")
    r.print_binary_tree()


    a = CNF("")
    # x = a.or_and(r)
    x = a.and_or_and(r)
    print("after converting:")
    x.print_binary_tree()

    # argv = parserArgument()
    # a = BinaryTree()
    # b = Stack()
    # print(b)
    # print(a)
    # pro_after_CNF = CNF(argv.proposition)
    # print(argv.proposition)


 