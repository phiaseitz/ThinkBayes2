import thinkbayes2
import thinkplot

class Euro(thinkbayes2.Suite):

	def Likelihood(self, data, hypo):
		x = hypo
		if data == 'H':
			return x/100.0
		else:
			return 1 - x/100.0

def main():
   
   suite = Euro(xrange(0,101))
   dataset = 'H' * 140 + 'T' * 120

   for data in dataset:
   	suite.Update(data)

   	thinkplot.Hist(suite)
   	thinkplot.Show(legend=False)

if __name__ == '__main__':
    main()