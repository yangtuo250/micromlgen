from micromlgen import platforms
from micromlgen.svm import is_svm, port_svm
from micromlgen.rvm import is_rvm, port_rvm
from micromlgen.sefr import is_sefr, port_sefr
from micromlgen.decisiontree import is_decisiontree, port_decisiontree
from micromlgen.randomforest import is_randomforest, port_randomforest
from micromlgen.logisticregression import is_logisticregression, port_logisticregression
from micromlgen.gaussiannb import is_gaussiannb, port_gaussiannb
from micromlgen.pca import is_pca, port_pca
from micromlgen.principalfft import is_principalfft, port_principalfft
from micromlgen.linearregression import is_linear_regression, port_linear_regression
from micromlgen.xgboost import is_xgboost, port_xgboost


def port(clf, classname=None, classmap=None, platform=platforms.ARDUINO, precision=None, cplusplus=True, **kwargs):
    """Port a classifier to plain C++ or C"""
    assert platform in platforms.ALL, 'Unknown platform %s. Use one of %s' % (platform, ', '.join(platforms.ALL))
    if is_svm(clf):
        return port_svm(**locals())
    elif cplusplus and is_rvm(clf):
        return port_rvm(**locals())
    elif cplusplus and is_sefr(clf):
        return port_sefr(**locals())
    elif is_decisiontree(clf):
        return port_decisiontree(**locals())
    elif cplusplus and is_randomforest(clf):
        return port_randomforest(**locals())
    elif is_logisticregression(clf):
        return port_logisticregression(**locals())
    elif cplusplus and is_gaussiannb(clf):
        return port_gaussiannb(**locals())
    elif cplusplus and is_pca(clf):
        return port_pca(**locals())
    elif cplusplus and is_principalfft(clf):
        return port_principalfft(**locals(), **kwargs)
    elif is_linear_regression(clf):
        return port_linear_regression(**locals(), **kwargs)
    elif is_xgboost(clf):
        return port_xgboost(**locals(), **kwargs)
    raise TypeError('clf MUST be one of %s' %
                    ', '.join(platforms.ALLOWED_CLASSIFIERS if cplusplus else platforms.ALLOWED_CLASSIFIERS_C))
