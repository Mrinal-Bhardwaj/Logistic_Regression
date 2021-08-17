from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt

iris = datasets.load_iris()

x= iris["data"][:,3:]
y = (iris["target"] == 2).astype(np.int)

clf = LogisticRegression()
clf.fit(x, y)
example = clf.predict(([[1.6]]))

print(example)

x_new = np.linspace(0,3,1000).reshape(-1,1)
y_prob = clf.predict_proba(x_new)

plt.plot(x_new,y_prob[:,-1],"g-", Label="Verginica")
plt.show()
print(x_new)

print(y)
print(x)
