LOG_CONFIG = {
    'version': 1,
    'loggers': {
        "example_app": {
            'handlers': ['console', 'file'],
            'level': 'DEBUG'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'level': 'DEBUG'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'data.log',
            'formatter': 'detailed'
        },
    },
    'formatters': {
        'detailed': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(name)-15s %(levelname)-8s %(filename)-10s %(lineno)-6s %(message)s'
        },
        'simple': {
            'class': 'logging.Formatter',
            'format': '%(name)-15s %(levelname)-8s %(pathname)-10s %(message)s'
        }
    },


}
