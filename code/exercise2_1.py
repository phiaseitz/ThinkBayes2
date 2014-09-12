import code\thinkbayes2

class Cookie(thinkbayes2.Pmf):

	#Initialize the cookie method
	def __init__(self,hypos):
		thinkbayes2.Pmf.__init__(self)
		for hypo in hypos:
			self.Set(hypo,1)
		self.Normalize()
		#The mix of the cookies
		self.b1 = Bowl(30,10)
		self.b2 = Bowl(20,20)

	#Update the hypothesis
	def Update(self,data):
		#For each hypothesis
		for hypo in self.Values():
			#The likelihood of the data given the hypothesis
			like = self.Likelihood(data,hypo)
			#Multiplying the p(H) by p(D|H)
			self.Mult(hypo, like)
			#Normalizing
			self.Normalize()

	#Return p(D|H)
	def Likelihood(self,data,hypo):

		if hypo == 'Bowl 1':
			like = self.b1.getDist(data)
			self.b1.takeACookie(data)
		elif hypo == 'Bowl 2':
			like = self.b2.getDist(data)
			self.b2.takeACookie(data)

		return like

class Bowl:
	def __init__(self,vanillaCookies = 0,chocolateCookies = 0):
		self.vanilla = vanillaCookies
		self.chocolate = chocolateCookies
		self.vanillaDist = self.vanilla/(float(self.vanilla + self.chocolate))
		self.chocolateDist = self.chocolate/(float(self.vanilla + self.chocolate))
	def takeACookie(self, cookieType):
		if cookieType == 'vanilla':
			self.vanilla = self.vanilla - 1
		elif cookieType == 'chocolate':
			self.chocolate = self.chocolate - 1
		self.updateDist()

	def updateDist(self):
		self.vanillaDist = self.vanilla/(float(self.vanilla + self.chocolate))
		self.chocolateDist = self.chocolate/(float(self.vanilla + self.chocolate))

	def getDist(self,cookieType):
		if cookieType == 'vanilla':
			return self.vanillaDist
		elif cookieType == 'chocolate':
			return self.chocolateDist






#Define the hypothesis
hypos = ['Bowl 1', 'Bowl 2']
#Create the object
pmf   = Cookie(hypos)
#Say that I took a vanilla cookie
pmf.Update('vanilla')

for hypo, prob in pmf.Items():
	print hypo,prob

pmf.Update('chocolate')

for hypo, prob in pmf.Items():
	print hypo,prob