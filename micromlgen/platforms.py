ARDUINO = 'arduino'
ATTINY = 'attiny'
STM32F4 = 'stm32f4'
ALL = [
    ARDUINO,
    ATTINY,
    STM32F4
]

ALLOWED_CLASSIFIERS = [
    'SVC',
    'OneClassSVC',
    'RVC',
    'SEFR',
    'DecisionTree',
    'RandomForest',
    'GaussianNB',
    'LogisticRegression',
    'PCA',
    'PrincipalFFT',
    'LinearRegression',
    'XGBClassifier'
]

ALLOWED_CLASSIFIERS_C = [
    'SVC',
    'OneClassSVC'
]