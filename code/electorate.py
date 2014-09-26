"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import numpy
import thinkbayes2
import thinkplot


class Electorate(thinkbayes2.Suite):
    """Represents hypotheses about the state of the electorate."""

    def Likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.

        hypo: that  a certain percent of the voter population will vote 
        the candidate
        data: the poll data where 1.1 is the mean percentage point of error 
        in favor of the candidate, 3.7 is the standard deviaion, and 53percent
        of voters will vote
        """
        #Assuming that for this case, the hypothesis is correct
        a_hypo = hypo
        mean, std, measurement = data
        e_hypo = measurement - a_hypo
        like =  thinkbayes2.EvalNormalPdf(e_hypo, mean, std)
        return like
    def ProbLose(self):
        total = 0
        for value, prob in self.Items():
            if value < 50:
                total += prob

        return total


def main():
    hypos = numpy.linspace(0, 100, 101)
    suite = Electorate(hypos)

    thinkplot.Pdf(suite, label='prior')

    data = 1.1, 3.7, 53
    suite.Update(data)

    thinkplot.Pdf(suite, label='posterior')
    thinkplot.Show()

    print (suite.Mean())
    print (suite.Std())
    print (suite.ProbLose())

    thinkplot.Pdf(suite, label='prior')

    newData = -2.3, 4.1, 49

    suite.Update(newData)

    thinkplot.Pdf(suite, label='posterior')
    thinkplot.Show()

    print (suite.Mean())
    print (suite.Std())
    print (suite.ProbLose())

if __name__ == '__main__':
    main()
