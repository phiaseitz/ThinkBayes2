"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import numpy
import thinkbayes2
import thinkplot


class Soccer(thinkbayes2.Suite):
    """Represents hypotheses about."""

    def Likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.

        hypo: The goal scoring rate (goals per game)
        data: the time of goals (minutes)
        """
        x = data
        lam = hypo/90.0

        like = thinkbayes2.EvalExponentialPdf(x,lam)
        return like

    def PredRemaining(self, rem_time, score):
        """Plots the predictive distribution for final number of goals.

        rem_time: remaining time in the game in minutes
        score: number of goals already scored
        """
        metapmf = thinkbayes2.Pmf()

        for lam,prob in self.Items():
            print (lam,prob)
            lt = lam * rem_time / 90
            pmf = thinkbayes2.MakePoissonPmf(lt,12)
            #thinkplot.Pdf(pmf, linewidth = 1, alpha = 0.2, color = 'purple')
            metapmf[pmf] = prob
        mix = thinkbayes2.MakeMixture(metapmf)
        mix += score
        thinkplot.Hist(mix)
        thinkplot.Show()


def main():
    hypos = numpy.linspace(0, 12, 101)
    suite = Soccer(hypos)

    thinkplot.PrePlot(4)

    thinkplot.Pdf(suite, label='prior')
    print('prior mean', suite.Mean())

#Prior using pseudo observation
    suite.Update(69)
    thinkplot.Pdf(suite, label='prior 2')
    print('Updating mean!', suite.Mean())

    suite.Update(11)
    thinkplot.Pdf(suite, label='posterior')
    print('after 1 goal', suite.Mean())

    suite.Update(12)
    thinkplot.Pdf(suite, label='posterior2')
    print('after 2 goals', suite.Mean())

    thinkplot.Show()

    suite.PredRemaining(67,2)



if __name__ == '__main__':
    main()
