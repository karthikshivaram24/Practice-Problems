import unittest

class Sorting(object):

    """This class is used for Insertion Sort, Bubble Sort, Selection Sort"""
    def __init__(self, arg):
        self.__init__

    def insertionSort(LinearStructure):
        """
        This is how you sort cards in your hand.
        --> Everything will be sorted till j-1 index

        if X = [23,42,12,15,20]

        1--> 23 42 12 15 20
        2--> 12 23 42 15 20
        3--> 12 15 23 42 20
        4--> 12 15 23 20 42

        This is a implementation of Insertion Sort
        Best-Case : O(1) - Already Sorted
        Worst-Case: O(n^2) - Sorted in Opposite way
        Avg-Case: O(n^2)

        Params   : LinearStructure - Any type of linear datastructure - Lists,Sets
        Returns  : The sorted structure
        """
        # print("\t\t************** INSERTION SORT **************")

        for j in range(1,len(LinearStructure)):
            key = LinearStructure[j]
            for i in range(j-1,-1,-1):
                if LinearStructure[i] > key :
                    LinearStructure[i+1] = LinearStructure[i]
                    j=i
                    if(i==0):
                        LinearStructure[0] = key
                else:
                    LinearStructure[j] = key
    
        return LinearStructure


    def selectionSort(LinearStructure):
        """
        Keep finding the mininmum value in array and move it to the front:

        Worst-Case : O(n^2)

        if X = [23,42,12,15,20]

        1 --> 12 42 23 15 20
        2 --> 12 15 23 42 20
        3 --> 12 15 20 42 23
        4 --> 12 15 20 23 42

        Params : LinearStructure --> List/Set to be sorted

        Result : Sorted LinearStructure
        """
        # print("\t\t************** SELECTION SORT **************")
        for i in range(len(LinearStructure)):
            min_element = LinearStructure[i]
            min_index = i
            for j in range(i,len(LinearStructure)):
                if LinearStructure[j] < min_element:
                    min_element = LinearStructure[j]
                    min_index = j
            temp = LinearStructure[i]
            LinearStructure[i] = min_element
            LinearStructure[min_index] = temp

        return LinearStructure

    def bubbleSort(LinearStructure):
        """
        This sorting technique O(n2) Worst-Case

        if X = [23,42,12,15,20]

        1--> 23 42 12 15 20
        2--> 12 42 23 15 20
        3--> 12 42 15 23 20
        4--> 12 42 15 20 23
        5--> 12 15 42 20 23
        6--> 12 15 20 42 23
        7--> 12 15 20 23 42

        params : LinearStructure
        return : Sorted Structure

        """
        # print("\t\t************** BUBBLE SORT **************")
        for i in range(len(LinearStructure)):
            for j in range(i+1,len(LinearStructure)):
                if LinearStructure[i] > LinearStructure[j]:
                    temp = LinearStructure[i]
                    LinearStructure[i] = LinearStructure[j]
                    LinearStructure[j] = temp

        return LinearStructure

class TestSorting(unittest.TestCase):
    def testSorting(self):
        self.assertEqual(Sorting.insertionSort([3,8,2,59,23,20,34,52]),sorted([3,8,2,59,23,20,34,52]))
        self.assertEqual(Sorting.selectionSort([3,8,2,59,23,20,34,52]),sorted([3,8,2,59,23,20,34,52]))
        self.assertEqual(Sorting.bubbleSort([3,8,2,59,23,20,34,52]),sorted([3,8,2,59,23,20,34,52]))

if __name__ == '__main__':
    unittest.main()
