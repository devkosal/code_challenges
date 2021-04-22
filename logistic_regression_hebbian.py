import numpy as np
import numpy as np
from sklearn.datasets import load_boston


X,y = load_boston(return_X_y=True)

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
scl = StandardScaler()
X_train = scl.fit_transform(X_train)
X_test = scl.transform(X_test)

num_feats = X.shape[1]

layer = np.random.uniform(-0.1,1,(num_feats, 1))

num_epcohs = 100
num_random_walks = 30

def sigmoid(x):
    return 1/(1+np.exp(-x))

def ce_loss(logits,y):
    eps = 1e-20
    return -sum(np.log(logits[range(len(logits)),y] + eps))

def accuracy(logits,y):
    return (logits.argmax(1) == y).mean()

def rmse(logits, y):
    return (np.mean((logits-y)**2))**.5

def softmax(x):
    exps = np.exp(x)
    return exps/sum(exps)

def normalize(x):
    (x - x.mean(0))/s.std(0)

coefs = np.random.uniform(0,1,5)
α = 0.2
σ = 0.1

n = X.shape[0]

for e in range(num_epcohs):
    new_coefs = np.empty((num_random_walks, 5))
    scores = np.empty((num_random_walks, 1))
    for rw in range(num_random_walks):
        new_coefs[rw] = coefs + (np.random.randn(5)*σ)
        η, A, B, C, D = list(new_coefs[-1])
        for i in range(len(X_train)):
            logits = X_train @ layer
            feats = X_train[i][...,None]
            acts = logits[i][None,...]
            diff = A*(feats @ acts) + B*feats + C*acts + D
            layer += η * diff
        logits = X_train @ layer
        scores[rw] = -rmse(logits,y_train)
    print(e, max(scores))
    weighted_scores =  softmax(scores) 
    print(e, max(weighted_scores))
    coefs = coefs + (α/σ)*(new_coefs * weighted_scores).sum(0)
    
    


        
        




