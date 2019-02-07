#!/usr/bin/env python3

import ml

def main():

    ih = ml.InstanceHolder('storage.dill')
    ih.runLoop()
    ih.method(0)(1,2)

if __name__ == "__main__":
    main()
