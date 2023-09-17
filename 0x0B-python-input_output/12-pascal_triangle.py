#!/usr/bin/python3
"""Moudule Implements PAscal's Triange using integers"""


def pascal_triangle(n):
    """Function implements PAscal's Triange using integers. Tri has n rows"""
    co = 1
    ce = 0
    count = 1
    st = 1
    stEv = 1
    endEv = 0
    end = 1
    ls = []

    while count <= n:
        row = []
        row.append(st)

        if count == 1:
            ls.append(row)
            count += 1
            continue

        if not count % 2 == 0:
            while co >= 1:
                st += co
                row.append(st)
                if not co == 1:
                    co -= 2
                else:
                    break

            while co <= end:
                st -= co
                row.append(st)

                if not co == end:
                    co += 2
                else:
                    break
            count += 1
            end += 2
            co += 2
        else:
            while ce >= 0:
                if ce != 0:
                    stEv += ce
                    row.append(stEv)

                if not ce == 0:
                    ce -= 2
                else:
                    break

            while ce <= endEv:
                if len(row) == n:
                    break
                stEv -= ce
                row.append(stEv)

                if not ce == endEv:
                    ce += 2
                else:
                    break
            count += 1
            endEv += 2
            ce += 2

        ls.append(row)
    return ls
