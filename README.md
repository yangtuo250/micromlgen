# Introducing MicroML

MicroML is an attempt to bring Machine Learning algorithms to microcontrollers.
Please refer to [this blog post](https://eloquentarduino.github.io/2019/11/you-can-run-machine-learning-on-arduino/)
to an introduction to the topic.

## Install

`pip install micromlgen`

## Support (and Relevant) Vector Machines

`micromlgen` can port to plain C SVM-based (SVC, LinearSVC, OneClassSVM)
and RVM-based (from `skbayes.rvm_ard_models` package) classifiers.

```python
from micromlgen import port
from sklearn.svm import SVC
from sklearn.datasets import load_iris


if __name__ == '__main__':
    iris = load_iris()
    X = iris.data
    y = iris.target
    clf = SVC(kernel='linear').fit(X, y)
    print(port(clf))
```

You may pass a classmap to get readable class names in the ported code

```python
from micromlgen import port
from sklearn.svm import SVC
from sklearn.datasets import load_iris


if __name__ == '__main__':
    iris = load_iris()
    X = iris.data
    y = iris.target
    clf = SVC(kernel='linear').fit(X, y)
    print(port(clf, classmap={
        0: 'setosa',
        1: 'virginica',
        2: 'versicolor'
    }))
```

## PCA

It can export a PCA transformer.

```python
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from micromlgen import port

if __name__ == '__main__':
    X = load_iris().data
    pca = PCA(n_components=2, whiten=False).fit(X)
    
    print(port(pca))
```

## SEFR

Read the post about [SEFR](https://eloquentarduino.github.io/2020/07/sefr-a-fast-linear-time-classifier-for-ultra-low-power-devices/).

```shell script
pip install sefr
```

```python
from sefr import SEFR
from micromlgen import port


clf = SEFR()
clf.fit(X, y)
print(port(clf))
```