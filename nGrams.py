"""
This class shall compute Ngrams from a given string. And contains a method for identifying the frequency of the Ngrams.
And also a method to calculate the ngram probabilities.
"""
from collections import Counter
from collections import defaultdict
import unittest

class NGrams(object):
    """Class containing methods for nGram calculation and count."""
    def __init__(self, arg):
        self.arg = arg

    def nGram_String(n,sentence):
        """
        This method basically calculates all the ngrams available in the given sentence.

        params:  n        -> the size of grams(tokens)
                 sentence -> the sentence to extract ngrams from.

        returns: nGrams -> List containing all the ngrams from given text
        """
        # Method 1:
        tokens = sentence.split()
        nGrams = []
        for i in range(len(tokens)-n+1):
            ngram = "_"
            for x in range(i,i+n,1):
                ngram+= tokens[x]
            nGrams.append(ngram[1:])

        return nGrams

    def countNgrams(nGrams_list):
        """
        This method calculates the frequency of the every Ngram from a list of list of Ngrams

        params:  nGrams_list -> the list of list of ngrams where each list represents a sentence

        returns: result      -> Counter object containing the ngrams and there respective frequencies
        """
        result = Counter()
        for i in range(len(nGrams_list)):
            result.update(nGrams_list[i])

        return result

    def nGram_tuple(n,sentence):
        """
        This also calculates the ngrams of a sentence but each gram is represented as form of a tuple

        params: n        -> size of nGram
                sentence -> the string to retrieve nGrams from

        result: NGRAM -> List of tuples where each tuple correspondts to an nGram
        """
        tokens = sentence.split()
        # zip(iter1=tokens,iter2=tokens[1:])
        # * is splat operator converts a list into elements for a function argument,
        # zip iterates through n iterables simultaneosly so for bigram (list1,list2), trigram(list1,list2,list3), etc...
        return zip(*[tokens[i:] for i in range(n)])

    def ngramProb(ngramList,n,verbose=True):
        """
        This method calculates the ngram probabilities from a list of Ngram . And returns them in the form
        eg: for 3-gram model

        p(w_i|w_i-2,w_i-1) = c(w_i-2,w_i-1,w_i) /c(w_i-2,w_i-1)

        params:  ngramList --> list containing tuples where each tuple represents an N_gram
                 n         --> ngram size
                 verbose   --> Flag used to indicate wether results are to be printed or not

        returns: dict of counter objects in the form {(w_i-2,w_i-1):{\w_i:p(w_i|w_i-2,w_i-1)}}
        """
        ngram_distribution = defaultdict(Counter)
        for i in range(len(ngramList)):
            ngram_distribution[ngramList[i][:-1]].update(ngramList[i][-1])

        # Now we normalize (dive numberator by denominator) to get our probability distribution over ngram

        for ngram in ngram_distribution:
            denom = sum([temp_dic[y] for temp_dic in ngram_distribution[ngram] for y in temp_dic])
            for word in ngram_distribution[ngram]:
                ngram_distribution[ngram][word] = ngram_distribution[ngram][word] / denom

        if verbose == True:
            for ngram in ngram_distribution:
                print(ngram  + " --> " + str(ngram_distribution[ngram]))
        return ngram_distribution


class TestNGram(unittest.TestCase):

    input_list = ['all', 'this', 'happened', 'more', 'or', 'less']

    def testNgram_String(self):
        self.assertTrue()
        self.assertFalse()
        self.assertTrue()

    def testNgram_count(self):
        self.assertEqual()
        self.assertEqual()

    def testNgram_tuple(self):
        self.assertTrue()
        self.assertTrue()
        self.assertTrue()

if __name__ == '__main__':
    unittest.main()
