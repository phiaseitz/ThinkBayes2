from __future__ import print_function, division
from thinkbayes2 import Pmf

'''Defines a class to do a bayseian update for a basket of eggs where the 
eggs are painted red and blue and some of them contain pearls.'''
class Egg(Pmf):

    '''Instantiates the egg class'''
    def __init__(self, hypos, priors):
        Pmf.__init__(self)
        '''Set the priors (for each H, the corrisponding p(H)'''
        for i in range(len(hypos)):
            self.Set(hypos[i],priors[i])
        self.Normalize()

    '''Perform an update based on the given data'''
    def Update(self, data):
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()

    '''The mix of eggs with pearls based on color'''
    mixes = {
        'Pearl':dict(red=0.7, blue=0.3),
        'No Pearl':dict(red=0.9, blue=0.1),
        }

    '''Return the likelihood of a pearl of a certain color having or not
    having a pearl'''
    def Likelihood(self, data, hypo):

        mix = self.mixes[hypo]
        like = mix[data]
        return like


'''Run when the python script is called from the command line'''
def main():
    '''Instantiate the hypotheses and the priors'''
    hypos = ['Pearl', 'No Pearl']
    priors = [0.4, 0.6]

    '''Create the pmf object'''
    pmf = Egg(hypos,priors)

    '''Assuming that we got a blue egg'''
    pmf.Update('blue')

    '''Print the results'''
    for hypo, prob in pmf.Items():
        print(hypo, prob)

'''If we're running from the command line, run the code defined by main()'''
if __name__ == '__main__':
    main()
