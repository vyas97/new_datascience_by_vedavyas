from sklearn import tree
x=[[181,80,44],[177,70,43],[160,60,38],[154,54,37],
   [166,65,40],[160,90,47],[175,64,39],[172,70,40],[159,55,37],
   [171,75,42],[181,85,43]]

y=['male','male','male','female','male','male',
   'female','male','female','male','male']

clf=tree.DecisionTreeClassifier()
clf=clf.fit(x,y)
prediction =clf.predict([[175,70,25.4]])
print (prediction)
