#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 15:00:49 2017

@author: Sanjana
"""

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 15:10:06 2017

@author: Sanjana
"""

import numpy as np
from collections import defaultdict
from collections import deque
import time
import random
import math
import copy


class place:
    def __init__(self, x, y):
        self.r = x
        self.c = y

    def __eq__(self, O):

        if (self.r == O.r and self.c == O.c):
            return True
        else:
            return False


class node:
    pos = []

    def __init__(self):
        self.pos = []
        self.cur_row = -1
        self.num_liz = 0

    def nod(self, pos1, newpos, currow, numliz):
        self.pos = pos1[:]
        self.pos.append(newpos)
        self.cur_row = currow
        self.num_liz = numliz


class node1:
    pos = None

    def __init__(self):
        self.pos = np.array(a)
        self.cur_row = 0
        self.num_liz = 0

    def nod(self, mat, currow, numliz):
        self.pos = np.array(mat)
        self.cur_row = currow
        self.num_liz = numliz


class bfs:
    def expand(self, parent):

        state = {}
        row = (parent.cur_row) + 1
        o = parent.pos
        children = []
        if not o:
            for i in range(n):
                npos = place(row, i)
                nliz = (parent.num_liz) + 1
                b = node()
                b.nod(o, npos, row, nliz)
                children.append(b)

            return children

        for col in range(0, n):
            for t in range(0, len(o)):

                row1 = int(o[t].r)
                col1 = int(o[t].c)
                if ((row == row1) or (col == col1) or (row - col == row1 - col1) or (row1 + col1 == row + col)):

                    state[col] = True
                    break
                else:
                    state[col] = False

        for key in state:
            if (state[key] == False):
                npos = place(row, key)
                nliz = parent.num_liz + 1
                b = node()
                b.nod(o, npos, row, nliz)
                children.append(b)
            else:

                pass

        return children

    def result(self):
        initial = node()

        q = deque()
        q.append(initial)
        expand_nodes = []
        while (q):
            curnode = q.popleft()

            if (curnode.num_liz == p):
                return curnode
            expand_nodes = bfs.expand(self, curnode)
            for kid in expand_nodes:
                q.append(kid)

        return False

    def output(self):
        z = bfs.result(self)

        if (z == False):
            fo1 = open("output.txt", "w")
            fo1.write("FAIL")
        else:
            fo1 = open("output.txt", "w")
            fo1.write("OK\n")

            for i in range(0, n):
                ro = z.pos[i].r
                co = z.pos[i].c
                for j in range(0, n):
                    if (i == ro and j == co):
                        b[i][j] = 1

            for i in range(0, n):
                for j in range(0, n):
                    fo1.write(str(b[i][j]))
                fo1.write("\n")
            fo1.close()


class dfs:
    def expand(self, parent):

        state = {}
        row = (parent.cur_row) + 1
        o = parent.pos
        children = []
        if not o:
            for i in range(n):
                npos = place(row, i)
                nliz = (parent.num_liz) + 1
                b = node()
                b.nod(o, npos, row, nliz)
                children.append(b)
            return children

        for col in range(0, n):
            for t in range(0, len(o)):
                row1 = int(o[t].r)
                col1 = int(o[t].c)
                if ((row == row1) or (col == col1) or (row - col == row1 - col1) or (row1 + col1 == row + col)):

                    state[col] = True
                    break
                else:
                    state[col] = False

        for key in state:
            if (state[key] == False):
                npos = place(row, key)
                nliz = parent.num_liz + 1
                b = node()
                b.nod(o, npos, row, nliz)
                children.append(b)
            else:

                pass

        return children

    def result(self):
        initial = node()

        q = deque()
        q.append(initial)

        expand_nodes = []
        while (q):
            curnode = q.pop()

            if (curnode.num_liz == p):
                return curnode
            expand_nodes = bfs.expand(self, curnode)

            for kid in expand_nodes:
                q.append(kid)

        return False

    def output(self):
        z = dfs.result(self)

        if (z == False):
            fo1 = open("output.txt", "w")
            fo1.write("FAIL")
        else:
            fo1 = open("output.txt", "w")
            fo1.write("OK\n")

            for i in range(0, n):
                ro = z.pos[i].r
                co = z.pos[i].c
                for j in range(0, n):
                    if (i == ro and j == co):
                        b[i][j] = 1

            for i in range(0, n):
                for j in range(0, n):
                    fo1.write(str(b[i][j]))
                fo1.write("\n")
            fo1.close()


class sa:
    random.seed(a=None, version=2)

    def yes(f):
        r = random.random()
        if (r < f):
            return True
        else:
            return False

    def conflict(bo):
        bc = 0

        for i in range(n - 1):
            j = i + 1
            while (j < n):
                row1 = bo[j].r
                col1 = bo[j].c
                row = bo[i].r
                col = bo[i].c
                if ((row == row1) or (col == col1) or (row - col == row1 - col1) or (row1 + col1 == row + col)):
                    bc += 1
                j += 1

        return bc

    # randomly place 4 objects(range from 0to n-1) in each row
    def sima(self):
        it = 2
        board = []
        u = True
        for i in range(n):
            x = i
            y = random.randint(0, n - 1)
            obj = place(x, y)
            board.append(obj)
        while (u):

            # T=(1/math.log10(it))
            T = 1 / it
            if (it == 2000000):
                break
            if (T < (0.00000000001)):
                break

            new = board[:]

            x = random.randint(0, n - 1)
            new[x].c = random.randint(0, n - 1)
            bc = sa.conflict(board)
            nc = sa.conflict(new)
            if (nc == 0):
                return new
                # nc-number of clash in new and bc in board
            deltae = nc - bc
            # deltae positive, move made is bad
            if (deltae > 0):
                x = deltae / T
                pr = math.exp(-x)
                if (sa.yes(pr)):
                    board = new[:]

                    # GOOD MOVE GETS ACCEPTED
            else:
                board = new[:]

            it += 1

        return board

    def output(self):
        z = sa.sima(self)

        if (z == False):
            fo1 = open("output.txt", "w")
            fo1.write("FAIL")
        else:
            fo1 = open("output.txt", "w")
            fo1.write("OK\n")

            for i in range(0, n):
                ro = z[i].r
                co = z[i].c
                for j in range(0, n):
                    if (i == ro and j == co):
                        b[i][j] = 1

            for i in range(0, n):
                for j in range(0, n):
                    fo1.write(str(b[i][j]))
                fo1.write("\n")
            fo1.close()


class bfstree:
    def safe(ro, co, l):

        row = ro
        col = co
        # upper left diagonal
        while (row >= 0 and col >= 0):
            if (l[row][col] == 2):
                # tree exist
                break
            else:
                if (l[row][col] == 1):
                    return False
            row -= 1
            col -= 1

            # up
        row = ro
        col = co
        while (row >= 0):

            if (l[row][col] == 2):
                break
            else:
                if (l[row][col] == 1):
                    return False
            row -= 1
            # right diagonal
        row = ro
        col = co
        while (row >= 0 and col < n):

            if (l[row][col] == 2):
                # tree exist
                break
            else:
                if (l[row][col] == 1):
                    return False
            row -= 1
            col += 1

            # right
        row = ro
        col = co
        while (col < n):

            if (l[row][col] == 2):
                break
            else:
                if (l[row][col] == 1):
                    return False
            col = col + 1
            # right down diagonal
        row = ro
        col = co
        while (row < n and col < n):

            if (l[row][col] == 2):
                # tree exist
                break
            else:
                if (l[row][col] == 1):
                    return False
            row += 1
            col += 1
            # down
        row = ro
        col = co
        while (row < n):

            if (l[row][col] == 2):

                # tree exist
                break
            else:
                if (l[row][col] == 1):
                    return False
            row += 1
            # left
        row = ro
        col = co
        while (col >= 0):

            if (l[row][col] == 2):
                break

            else:
                if (l[row][col] == 1):
                    return False
            col -= 1

            # left down diagonal
        row = ro
        col = co
        while (row < n and col >= 0):

            if (l[row][col] == 2):
                break

            else:
                if (l[row][col] == 1):
                    return False
            row += 1
            col -= 1

        return True

    def expand(self, parent):

        o = parent.pos

        children = []
        c = parent.num_liz
        d = parent.cur_row
        v = 0
        while (v < n and d < n):

            if (o[d][v] == 2 or o[d][v] == 1):
                pass
            else:
                if (bfstree.safe(d, v, o)):
                    h = np.array(o)
                    h[d][v] = 1
                    b = node1()
                    b.nod(h, d, c + 1)
                    children.append(b)

            v = v + 1

        d += 1
        childs = []
        while (len(childs) == 0 and d < n):
            for v in range(0, n):
                if (o[d][v] == 2 or o[d][v] == 1):
                    pass
                else:
                    if (bfstree.safe(d, v, o)):
                        h = np.array(o)
                        h[d][v] = 1
                        b = node1()
                        b.nod(h, d, c + 1)
                        childs.append(b)
            d += 1

        children = children + childs

        return children

    def result(self):
        initial = node1()
        q = deque()
        q.append(initial)
        expand_nodes = []
        while (q):
            curnode = q.popleft()
            if (curnode.num_liz == p):
                return curnode
            expand_nodes = bfstree.expand(self, curnode)
            for kid in expand_nodes:
                q.append(kid)
        return False

    def output(self):
        z = bfstree.result(self)

        if (z == False):

            fo1 = open("output.txt", "w")
            fo1.write("FAIL")
        else:
            fo1 = open("output.txt", "w")
            fo1.write("OK\n")
            y = z.pos
            for i in range(0, n):
                for j in range(0, n):
                    fo1.write(str(y[i][j]))
                fo1.write("\n")
            fo1.close()


class dfstree:
    def safe(ro, co, l):

        row = ro
        col = co
        # upper left diagonal
        while (row >= 0 and col >= 0):
            if (l[row][col] == 2):
                # tree exist
                break
            else:
                if (l[row][col] == 1):
                    return False
            row -= 1
            col -= 1

            # up
        row = ro
        col = co
        while (row >= 0):

            if (l[row][col] == 2):
                break
            else:
                if (l[row][col] == 1):
                    return False
            row -= 1
            # right diagonal
        row = ro
        col = co
        while (row >= 0 and col < n):

            if (l[row][col] == 2):
                # tree exist
                break
            else:
                if (l[row][col] == 1):
                    return False
            row -= 1
            col += 1

            # right
        row = ro
        col = co
        while (col < n):

            # print(row,col)
            if (l[row][col] == 2):
                break
            else:
                if (l[row][col] == 1):
                    return False
            col = col + 1
            # right down diagonal
        row = ro
        col = co
        while (row < n and col < n):

            if (l[row][col] == 2):
                # tree exist
                break
            else:
                if (l[row][col] == 1):
                    return False
            row += 1
            col += 1
            # down
        row = ro
        col = co
        while (row < n):

            if (l[row][col] == 2):

                # tree exist
                break
            else:
                if (l[row][col] == 1):
                    return False
            row += 1
            # left
        row = ro
        col = co
        while (col >= 0):

            if (l[row][col] == 2):
                break

            else:
                if (l[row][col] == 1):
                    return False
            col -= 1

            # left down diagonal
        row = ro
        col = co
        while (row < n and col >= 0):

            if (l[row][col] == 2):
                break

            else:
                if (l[row][col] == 1):
                    return False
            row += 1
            col -= 1

        return True

    def expand(self, parent):

        o = parent.pos

        children = []
        c = parent.num_liz
        d = parent.cur_row
        v = 0
        while (v < n and d < n):

            if (o[d][v] == 2 or o[d][v] == 1):
                pass
            else:
                if (dfstree.safe(d, v, o)):
                    h = np.array(o)
                    h[d][v] = 1
                    b = node1()
                    b.nod(h, d, c + 1)
                    children.append(b)

            v = v + 1

        d += 1
        childs = []
        while (len(childs) == 0 and d < n):
            for v in range(0, n):
                if (o[d][v] == 2 or o[d][v] == 1):
                    pass
                else:
                    if (dfstree.safe(d, v, o)):
                        h = np.array(o)
                        h[d][v] = 1
                        b = node1()
                        b.nod(h, d, c + 1)
                        childs.append(b)
            d += 1

        children = children + childs

        return children

    def result(self):
        initial = node1()
        q = deque()
        q.append(initial)
        expand_nodes = []
        while (q):
            curnode = q.pop()

            if (curnode.num_liz == p):
                return curnode
            expand_nodes = bfstree.expand(self, curnode)
            for kid in expand_nodes:
                q.append(kid)
        return False

    def output(self):
        z = bfstree.result(self)

        if (z == False):

            fo1 = open("output.txt", "w")
            fo1.write("FAIL")
        else:

            fo1 = open("output.txt", "w")
            fo1.write("OK\n")
            y = z.pos
            for i in range(0, n):
                for j in range(0, n):
                    fo1.write(str(y[i][j]))
                fo1.write("\n")
            fo1.close()


class satree:
    random.seed(a=None, version=2)

    def yes(f):
        r = random.random()
        if (r < f):
            return True
        else:
            return False

    def conflict(l, bo):

        bc = 0
        for i in range(len(bo)):

            ro = bo[i].r
            co = bo[i].c
            row = ro
            col = co
            # ("Moving upper left diagonal")
            while (row >= 0 and col >= 0):
                if (l[row][col] == 2):
                    # tree exist
                    break
                else:
                    if (l[row][col] == 1 and row != ro and col != co):
                        bc = bc + 1

                row -= 1
                col -= 1
                # print("Moving up ")
            row = ro
            col = co
            while (row >= 0):

                if (l[row][col] == 2):
                    break
                else:
                    if (l[row][col] == 1 and row != ro):
                        bc = bc + 1

                row -= 1


                # right diagonal
            row = ro
            col = co
            while (row >= 0 and col < n):

                if (l[row][col] == 2):
                    # tree exist
                    break
                else:
                    if (l[row][col] == 1 and row != ro and col != co):
                        bc = bc + 1

                row -= 1
                col += 1

                # right
            row = ro
            col = co
            while (col < n):

                if (l[row][col] == 2):
                    break
                else:
                    if (l[row][col] == 1 and col != co):
                        bc = bc + 1

                col = col + 1

                # right down diagonal
            row = ro
            col = co
            while (row < n and col < n):

                if (l[row][col] == 2):
                    # tree exist
                    break
                else:
                    if (l[row][col] == 1 and row != ro and col != co):
                        bc = bc + 1

                row += 1
                col += 1
                # down
            row = ro
            col = co
            while (row < n):

                if (l[row][col] == 2):

                    # tree exist
                    break
                else:
                    if (l[row][col] == 1 and row != ro):
                        bc = bc + 1

                    row += 1


                    # left
            row = ro
            col = co
            while (col >= 0):

                if (l[row][col] == 2):
                    break

                else:
                    if (l[row][col] == 1 and col != co):
                        bc = bc + 1

                    col -= 1



                    # left down diagonal
            row = ro
            col = co
            while (row < n and col >= 0):

                if (l[row][col] == 2):
                    break

                else:
                    if (l[row][col] == 1 and row != ro and col != co):
                        bc = bc + 1

                row += 1
                col -= 1

        return bc

    def safe(l, x, y):

        bc = 0
        ro = x
        co = y
        row = ro
        col = co
        u = (time.time() - start_time)
        if (u > 240):
            fo1 = open("output.txt", "w")
            fo1.write("FAIL")
            exit()


            # print("Moving upper left diagonal")
        while (row >= 0 and col >= 0):
            if (l[row][col] == 2):
                # tree exist
                break
            else:
                if (l[row][col] == 1 and row != ro and col != co):
                    bc = bc + 1
            row -= 1
            col -= 1



            # print("Moving up ")
        row = ro
        col = co
        while (row >= 0):

            if (l[row][col] == 2):
                break
            else:
                if (l[row][col] == 1 and row != ro):
                    bc = bc + 1

            row -= 1


            # right diagonal
        row = ro
        col = co
        while (row >= 0 and col < n):

            if (l[row][col] == 2):
                # tree exist
                break
            else:
                if (l[row][col] == 1 and row != ro and col != co):
                    bc = bc + 1

            row -= 1
            col += 1

            # right
        row = ro
        col = co
        while (col < n):

            if (l[row][col] == 2):
                break
            else:
                if (l[row][col] == 1 and col != co):
                    bc = bc + 1

            col = col + 1

            # right down diagonal
        row = ro
        col = co
        while (row < n and col < n):

            if (l[row][col] == 2):
                # tree exist
                break
            else:
                if (l[row][col] == 1 and row != ro and col != co):
                    bc = bc + 1

            row += 1
            col += 1
            # down
        row = ro
        col = co
        while (row < n):

            if (l[row][col] == 2):

                # tree exist
                break
            else:
                if (l[row][col] == 1 and row != ro):
                    bc = bc + 1

            row += 1


            # left
        row = ro
        col = co
        while (col >= 0):
            if (l[row][col] == 2):
                break

            else:
                if (l[row][col] == 1 and col != co):
                    bc = bc + 1

            col -= 1



            # left down diagonal
        row = ro
        col = co
        while (row < n and col >= 0):

            if (l[row][col] == 2):
                break

            else:
                if (l[row][col] == 1 and row != ro and col != co):
                    bc = bc + 1

            row += 1
            col -= 1

        return bc

    def sima(self):
        T = 1000

        board = []
        global b
        global p

        re = True
        i = 0
        while (i < p):
            re = True
            while (re):
                x = random.randint(0, n - 1)
                y = random.randint(0, n - 1)
                if (b[x][y] != 2 and b[x][y] != 1):
                    obj = place(x, y)
                    board.append(obj)
                    b[x][y] = 1
                    re = False
            i = i + 1

        bc = satree.conflict(b, board)

        if (bc == 0):
            return b

        while (1):
            u = (time.time() - start_time)
            if (u > 240):
                fo1 = open("output.txt", "w")
                fo1.write("FAIL")
                exit()

                # T=(1/math.log10(it))
            T = 0.95*T
            # if(it==200):
            #   break
            new = copy.deepcopy(board)
            k = np.array(b)

            re = True
            i = random.randint(0, n - 1)
            ro = new[i].r
            co = new[i].c
            k[ro][co] = 0

            insert = 0
            for row_i in range(0,n):
                for col_j in range(0,n):
                    con = satree.safe(k, row_i, col_j)
                    if(con == 0 and k[row_i][col_j]!=1 and k[row_i][col_j]!=2):
                        k[row_i][col_j] = 1
                        new[i].r = row_i
                        new[i].c = col_j
                        insert = 1
                        break
                if(insert == 1):
                        break
            if(insert == 0):
                x = random.randint(0, n - 1)
                y = random.randint(0, n - 1)

                while(k[x][y] == 2 or k[x][y] == 1):
                    x = random.randint(0, n - 1)
                    y = random.randint(0, n - 1)
                k[x][y] = 1
                new[i].r = x
                new[i].c = y



            nc = satree.conflict(k, new)

            if (nc == 0):
                return k
                # nc-number of clash in new and bc in board
            deltae = nc - bc

            # deltae positive, move made is bad
            if (deltae > 0):
                x = deltae / T
                pr = math.exp(-x)

                if (sa.yes(pr)):
                    board.clear()
                    board = new[:]

                    b = np.array(k)
                    bc = nc
                    # GOOD MOVE GETS ACCEPTED
            else:
                board.clear()
                board = copy.deepcopy(new)
                b = np.array(k)
                bc= nc




        return False

    def output(self):
        z = satree.sima(self)
        fo1 = open("output.txt", "w")
        fo1.write("OK\n")
        for i in range(0, n):
            for j in range(0, n):
                fo1.write(str(z[i][j]))
            fo1.write("\n")
        fo1.close()




        # to read the input from the file


with open('input.txt') as f:
    words = [word.strip() for word in f]
sol = words.pop(0)
n = int(words.pop(0))
p = int(words.pop(0))
start_time = time.time()
tree = {}
tree = defaultdict(list)
t = False
a = np.full((n, n), 0)

for i in range(0, n):
    for j in range(0, n):

        if (words[i][j] == '2'):
            tree[i].append(j)
            a[i][j] = 2
            t = True
        else:
            a[i][j] = 0
b = np.array(a)

if (t == True):
    if (sol == "BFS"):

        u = bfstree()
        u.output()
    elif (sol == "DFS"):

        u = dfstree()
        u.output()
    elif (sol == "SA"):

        u = satree()
        u.output()


else:
    # no trees
    if (p <= n):
        # n queens
        if (sol == "BFS"):

            s = bfs()
            s.output()
        elif (sol == "DFS"):

            s = dfs()
            s.output()
        elif (sol == "SA"):

            s = sa()
            s.output()


    else:
        fo1 = open("output.txt", "w")
        fo1.write("FAIL")
        fo1.close()





       
                
        