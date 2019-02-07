#!/usr/bin/env python3

# this file simulates a notebook

import ml

if __name__ == "__main__":

    class MyClass:
        def startup(self):
            from sklearn.datasets import load_iris
            from sklearn.linear_model import LogisticRegression
            X, y = load_iris(return_X_y=True)
            import pickle
            clf = LogisticRegression(random_state=0, solver='lbfgs',
                    multi_class='multinomial').fit(X, y)
            self.mycrazymodel = clf


        @ml.periodic(3)
        def trainAModel(self):
            print("training a new model...")
            print("pickle and store the model somewhere")

            from sklearn.datasets import load_iris
            from sklearn.linear_model import LogisticRegression
            X, y = load_iris(return_X_y=True)
            import pickle
            clf = LogisticRegression(random_state=0, solver='lbfgs',
                    multi_class='multinomial').fit(X, y)
            with open('skl_lr.pickle', 'wb') as outfile:
                pickle.dump(clf, outfile)

        @ml.callable
        def myCallableMethod(self, arg1, arg2):
            print("myCallableMethod: ", arg1, arg2)
            # load model if not yet loaded
            if not hasattr(self, 'mycrazymodel'):
                import pickle
                from sklearn.linear_model import LogisticRegression
                print("loading and unpickle the model...")
                self.mycrazymodel = "SKLearnModel"
                with open('skl_lr.pickle', 'rb') as modelfile:
                    self.mycrazymodel = pickle.load(modelfile)
            print("making a prediction using '{}' model".format(self.mycrazymodel))
            return 42
            
        def someOtherMethod(self, blah):
            print("do something else: ", blah)


    print("Writing out this class to file...")
    ml.storeClass(MyClass, 'storage.dill')
