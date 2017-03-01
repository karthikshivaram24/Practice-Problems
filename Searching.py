"""
Implementation of Searching algorithms
1) Binary Search
2) Interpolation Search
"""
import unittest

class Search(object):
    """docstring for ."""
    def __init__(self, arg):
        self.arg = arg

    def binarySearch(k,linearStructure):
        """
        ** Important : The list/set has to be sorted for binary Search to work

        This method performs binary search on a linearStructure of elements

        params:   k               --> the element to Search
                  linearStructure --> list/set of elements

        result:  tuple(verdict,index)
        """

        def recurse(k,start,end,linearStructure):
            mid = int(start+(((end-start)+1) / 2))
            x=linearStructure
            if x[mid]==k:
                return (True,mid)
            elif x[mid] > k:
                return recurse(k,start,mid-1,linearStructure)
            else:
                return recurse(k,mid+1,end,linearStructure)

        return recurse(k=k,start=0,end=len(linearStructure)-1,linearStructure=linearStructure)

class TestSearch(unittest.TestCase):

    def testBinarySearch(self):
        x=[1,2,3,4,5,6,7]
        self.assertEqual(first=(True,5),second=Search.binarySearch(k=6,linearStructure=x))

if __name__ == '__main__':
    unittest.main()
