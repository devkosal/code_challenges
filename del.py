import numpy as np
import pandas as pd
df = pd.read_csv('../data/USA_Housing.csv')
X_all = np.array(df.iloc[:,0:-2])
y_all = np.array(df.iloc[:,-2]).reshape((len(df), 1))

class Linear():
	def __init__(self, X, y, iters = 10000 ):
    	self.X = np.concatenate((np.ones(y.shape), X),axis =1)
    	self.y = y
    	self.preds = np.zeros(y.shape)
    	self.n = y.shape[0]
    	self.loss = None
    	self.lr = 0.0000000001 # funny, it the lr is too big I don't get convergence
    	self.beta = np.random.uniform(low=-1.0, high=1.0, size= (1, self.X.shape[1]) )
    	self.grad = np.random.uniform(low=-1.0, high=1.0, size= self.beta.shape )
    	self.iters = iters

	def forward(self):
    	self.preds = np.sum(self.X *self.beta, axis =1, keepdims=True)

	def backward(self):
    	self.grad =2*  np.mean((self.preds - self.y)* self.X, axis=0, keepdims=True )
    	self.beta = self.beta -  self.lr * self.grad

	def calculate_loss(self):
    	self.loss = np.mean( (self.y - self.preds)**2 )

	def fit(self):
    	for _ in range(self.iters):
        	self.forward()
        	self.backward()
        	self.calculate_loss()
        	#print(self.loss)

linear= Linear(X_all, y_all)
linear.fit()
Linear.beta
