#!/usr/bin/env python3

# this file simulates a notebook

import ml

if __name__ == "__main__":

    class MyClass:
        # Uncommenting the following should break things, as we'll be trying to 'dill'
        # self.model, which is a RandomForestClassifier
        #def __init__(self):
        #    self.mycrazymodel = self.trainModel()

        def trainModel(self):
            from sklearn.ensemble import RandomForestClassifier
            from sklearn.datasets import make_classification

            X, y = make_classification(n_samples=1000, n_features=4,
                    n_informative=2, n_redundant=0, random_state=0, shuffle=False)
            clf = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
            clf.fit(X, y)
            return clf

        def startup(self):
            self.mycrazymodel = self.trainModel()

        @ml.periodic(3)
        def trainAModel(self):
            print("training a new model...")
            print("pickle and store the model somewhere")
            clf = self.trainModel() # this could be loading new data...

            import pickle
            with open('skl.pickle', 'wb') as outfile:
                pickle.dump(clf, outfile)

        @ml.callable
        def myCallableMethod(self, arg1, arg2):
            print("myCallableMethod: ", arg1, arg2)
            # load model if not yet loaded
            if not hasattr(self, 'mycrazymodel'):
                import pickle
                print("loading and unpickle the model...")
                with open('skl.pickle', 'rb') as modelfile:
                    self.mycrazymodel = pickle.load(modelfile)

            # make a prediction
            pred = self.mycrazymodel.predict([[0, 0, 0, 0]])
            print("making a prediction using '{}' model: {}".format(
                self.mycrazymodel, pred))
            return pred
            

    print("Writing out this class to file...")
    ml.storeClass(MyClass, 'storage.dill')
