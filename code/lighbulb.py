from __future__ import print_function, division

import numpy
import thinkbayes2
import thinkplot


class Lightbulb(thinkbayes2.Suite):
    """Represents hypotheses about."""

    def Likelihood(self, data, hypo):
        """Computes the likelihood of the data under the hypothesis.

        hypo: The rate at which bulbs break per 2 months
        data: the number of broken bulbs
        """
        lam = hypo
        k = data

        like = thinkbayes2.EvalPoissonPmf(lam,k)
        return like


def main():
    hypos = numpy.linspace(0, 100, 101)
    suite = Lightbulb(hypos)

    thinkplot.PrePlot(2)

    thinkplot.Pdf(suite, label='prior')
    print('prior mean', suite.Mean())

    suite.Update(3)
    thinkplot.Pdf(suite, label='posterior')
    print('after 3 in Feb', suite.Mean())

    thinkplot.Show()



if __name__ == '__main__':
    main()