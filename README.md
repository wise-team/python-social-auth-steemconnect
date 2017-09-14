python-social-auth-steemconnect
===========================

Pluggable authentication backend for python-social-auth, that allows authentication via SteemConnect (v2).


## Installation instructions

From pypi

    $ pip install python-social-auth-steemconnect

or clone from Github

    $ git clone git@github.com:noisy/python-social-auth-steemconnect.git
    $ cd python-social-auth-steemconnect && sudo python setup.py install

## Pre-requisites

`python-social-auth` must be installed and configured first. Please visit the
[python-social-auth documentation](http://psa.matiasaguirre.net/docs/) for instructions.


## Configuration instructions

1. Add Waveapps backend to AUTHENTICATION_BACKENDS:

        AUTHENTICATION_BACKENDS = (
            'steemconnect.backends.SteemConnectOAuth2',
            ...
            'django.contrib.auth.backends.ModelBackend',
        )

2. Add your Waveapps settings to your django `settings.py` file.

        SOCIAL_AUTH_STEEMCONNECT_KEY = "..."
        SOCIAL_AUTH_STEEMCONNECT_SECRET = "..."
        SOCIAL_AUTH_STEEMCONNECT_DEFAULT_SCOPE = ['vote', 'comment']


## Changelog

### 0.0.1
* Initial release

