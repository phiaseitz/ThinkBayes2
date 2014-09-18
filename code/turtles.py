"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

import thinkbayes2


class Turtle(thinkbayes2.Suite):
    """A map from string turtle ID to probablity."""

    def Likelihood(self, data, hypo):
        """The likelihood of the data under the hypothesis.

        data: string cookie type
        hypo: string bowl ID
        """
        like = hypo[data] / hypo.Total()
        
        return like


def main():
    turt0 = thinkbayes2.Hist(dict(blue=1, green=0))
    turt1 = thinkbayes2.Hist(dict(blue=2/3, green=1/3))
    turt2 = thinkbayes2.Hist(dict(blue=1/3, green=2/3))
    turt3 = thinkbayes2.Hist(dict(blue=0, green=1))
    pmf = Turtle([turt0, turt1, turt2, turt3])

    print('After 1 green')
    pmf.Update('green')
    for hypo, prob in pmf.Items():
        print(hypo, prob)



if __name__ == '__main__':
    main()