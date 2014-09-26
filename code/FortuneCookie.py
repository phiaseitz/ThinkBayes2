from __future__ import print_function, division

import numpy
import thinkbayes2
import thinkplot

class FortuneCookie(thinkbayes2.Suite):
	def Likelihood(self, data, hypo):
		(numberOfCookies, inCommon) =  data
		if numberOfCookies > hypo:
			like = 0
		else:
			like = thinkbayes2.EvalBinomialPmf(inCommon,numberOfCookies,inCommon/hypo)

		return like

def main():
    hypos = numpy.linspace(0, 100, 101)
    suite = FortuneCookie(hypos)

    thinkplot.Pdf(suite, label='prior')

    data = (9,2)
    suite.Update(data)

    thinkplot.Pdf(suite, label='posterior')
    thinkplot.Show()


if __name__ == '__main__':
    main()