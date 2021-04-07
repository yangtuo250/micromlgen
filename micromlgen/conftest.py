import pytest
from sklearn.datasets import load_iris


@pytest.fixture(scope='module')
def iris():
    iris = load_iris()
    print("iris dataset loaded!")

    return iris.data, iris.target
