"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import numpy
import thinkbayes2
import thinkplot


class Hyrax(thinkbayes2.Suite):
    """Represents hypotheses about the state of the electorate."""

    def Likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.

        hypo: number of hyraxes
        data: the number already tagged the number caught, number tagged
        """
        (numberAlreadyTagged, numberCaught, numberTagged) = data
        #Assuming that for this case, the hypothesis is correct
        if (numberAlreadyTagged + (numberCaught - numberTagged))> hypo:
            like = 0
        else:
            like = thinkbayes2.EvalBinomialPmf(numberTagged,numberCaught,(numberAlreadyTagged/hypo))
        return like
    


def main():
    hypos = numpy.linspace(0, 500, 101)
    suite = Hyrax(hypos)

    thinkplot.Pdf(suite, label='prior')

    data = (10, 10, 2)
    suite.Update(data)

    thinkplot.Pdf(suite, label='posterior')
    thinkplot.Show()

    print (suite.Mean())
    print (suite.Std())

if __name__ == '__main__':
    main()
