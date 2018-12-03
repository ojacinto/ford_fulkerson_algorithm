#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright 2018(c). All rights reserved.
#
# This is free software; you can do what the LICENCE file allows you to.
# Author: Ing. Oraldo Jacinto Simon

from __future__ import (division as _py3_division,
                        print_function as _py3_print,
                        absolute_import as _py3_abs_import)

from texttable import Texttable
from ford_fulkerson import Flow

class Main(object):

    def __init__(self):
        '''A practical exercise for computing the maximum flow among a pair of nodes
        in a capacitated graph (ford_fulkerson)

        '''
        print ('''********************Ford Fulkerson Algorithm ************************
               Author: Oraldo Jacinto Simon
               Professor: M.I. Jesus Roberto López Santillán
               ''')

        flow_obj = Flow()
        edges = [
            ('s', 'o', 3),
            ('s', 'p', 3),
            ('o', 'p', 2),
            ('o', 'q', 3),
            ('p', 'r', 2),
            ('q', 'r', 4),
            ('r', 't', 3),
            ('q', 't', 2)
        ]
        # Add edges
        for edge in edges:
            source, sink, capacity = edge
            flow_obj.add_edge(source, sink, capacity)
        # Compute maximun flow
        res = flow_obj.maximum_flow('s', 't')
        table = Texttable()
        table.set_cols_align(["c", "c", "c"])
        table.set_cols_valign(["t", "m", "b"])
        table.set_cols_width([20,35,40])

        head = ["Method", "Add Edges", "Answer"]
        rows = []
        rows.append(head)
        str_edges ='Edges: %s' % str(edges)
        ford_fulkerson = [
            'Ford Fulkerson Algorithm',
            str_edges,
            res
        ]
        rows.append(ford_fulkerson)
        table.add_rows(rows)
        print(table.draw() + "\n")

Main()
