import pytest

from micromlgen import platforms

from . import port

platforms = [(True, 'arduino'), (True, 'attiny'), (False, 'arduino'), (False, 'stm32f4'), (False, 'attiny')]


@pytest.mark.parametrize(('isCplusplus', 'platform'), platforms)
@pytest.mark.parametrize('kernel', ['linear', 'rbf'])
@pytest.mark.parametrize('gamma', [0.01, 0.0001])
def test_SVC(iris, isCplusplus, platform, kernel, gamma):
    from sklearn.svm import SVC
    clf = SVC(kernel=kernel, gamma=gamma).fit(*iris)
    cfile = port(clf, cplusplus=isCplusplus, platform=platform)
    print(cfile)
    if 'stm32f4' == platform:
        assert 'uint' not in cfile


@pytest.mark.parametrize(('isCplusplus', 'platform'), platforms)
def test_decisiontree(iris, isCplusplus, platform):
    from sklearn.tree import DecisionTreeClassifier
    clf = DecisionTreeClassifier().fit(*iris)
    cfile = port(clf, cplusplus=isCplusplus, platform=platform)
    print(cfile)
    if 'stm32f4' == platform:
        assert 'uint' not in cfile


@pytest.mark.parametrize(('isCplusplus', 'platform'), platforms)
def test_xgboost(iris, isCplusplus, platform):
    from xgboost import XGBClassifier
    clf = XGBClassifier().fit(*iris)
    cfile = port(clf, cplusplus=isCplusplus, platform=platform)
    print(cfile)
    if 'stm32f4' == platform:
        assert 'uint' not in cfile


@pytest.mark.parametrize(('isCplusplus', 'platform'), platforms)
def test_linearregression(iris, isCplusplus, platform):
    from sklearn.linear_model import LinearRegression
    reg = LinearRegression().fit(*iris)
    cfile = port(reg, cplusplus=isCplusplus, platform=platform)
    print(cfile)
    if 'stm32f4' == platform:
        assert 'uint' not in cfile


@pytest.mark.parametrize(('isCplusplus', 'platform'), platforms)
def test_logisticregression(iris, isCplusplus, platform):
    from sklearn.linear_model import LogisticRegression
    clf = LogisticRegression().fit(*iris)
    cfile = port(clf, cplusplus=isCplusplus, platform=platform)
    print(cfile)
    if 'stm32f4' == platform:
        assert 'uint' not in cfile


if __name__ == '__main__':
    pytest.main()
