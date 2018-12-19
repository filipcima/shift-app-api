import os

MONGO_URI = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/shiftapp')
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']
DATE_FORMAT = '%d/%m/%y %H:%M:%S'
people = {
    'item_title': 'person',

    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'lastname'
    },
    'schema': {
        'firstname': {
            'type': 'string'
        },
        'lastname': {
            'type': 'string'
        },
        'role': {
            'type': 'string',
            'allowed': ['superior_user', 'basic_user']
        },
        'mail': {
            'type': 'string'
        },
        'password_hash': {
            'type': 'string'
        },
        'superior': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'people',
                'embeddable': True
            }
        }
    }
}

shifts = {
    'item_title': 'shift',
    'schema': {
        'date_from': {
            'type': 'datetime'
        },
        'date_to': {
            'type': 'datetime'
        },
        'number_of_workers': {
            'type': 'integer'
        },
        'superior_plan': {
            'type': 'objectid',
            'required': False,
            'data_relation': {
                'resource': 'superior_plans',
                'embeddable': True
            }
        },
        'workers': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'people',
                    'embeddable': True
                }
            }
        }

    }
}

superior_plans = {
    'item_title': 'superior_plan',
    'schema': {
        'owner': {
            'type': 'objectid',
            'required': True,
            'data_relation': {
                'resource': 'people',
                'field': '_id',
                'embeddable': True
            }
        },
        'status': {
            'type': 'string'
        },
        'shifts': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'shift',
                    'embeddable': True
                }
            }
        },
        'created': {
            'type': 'datetime'
        }
    }
}

request = {
    'schema': {
        'created_by': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'people',
                'embeddable': True
            }
        },
        'for_shift': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'shifts',
                'embeddable': True
            }
        },
        'request_type': {
            'type': 'string',
            'allowed': ['cancel', 'change']
        },
        'accepted': {
            'type': 'boolean'
        },
        'resolved': {
            'type': 'boolean'
        }
    }
}


notification = {
    'schema': {
        'for_users': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'people',
                    'embeddable': True
                }
            }
        },
        'from_user': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'people',
                'embeddable': True
            }
        },
        'message': {
            'type': 'string'
        },
        'notification_type': {
            'type': 'string',
            'allowed': ['informational', 'change_request', 'cancel_request'],
            'required': True
        },
        'show': {
            'type': 'boolean',
            'required': True
        },
        'shift': {
            'type': 'objectid',
            'required': False,
            'data_relation': {
                'resource': 'shifts',
                'embeddable': True
            }
        }

    }
}

DOMAIN = {
    'people': people,
    'shifts': shifts,
    'superior_plans': superior_plans,
    'requests': request,
    'notifications': notification
}
