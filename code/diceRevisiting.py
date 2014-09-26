from __future__ import print_function, division

import numpy
import thinkbayes2
import thinkplot

class Dice(thinkbayes2.Suite):

    def Likelihood(self, data, hypo):

        if hypo < data:
            return 0
        else:
            return 1.0/hypo

def main():
    hypos = [4,4,4,6,6,10,10,12,20,24]
    suite = Dice(hypos)

    thinkplot.Hist(suite, label='prior')

    suite.Update(6)

    thinkplot.Hist(suite, label='posterior1')

    suite.Update(10)

    thinkplot.Hist(suite, label='posterior2')
    thinkplot.Show()

    print (suite.Mean())
    print (suite.Std())

if __name__ == '__main__':
    main()
