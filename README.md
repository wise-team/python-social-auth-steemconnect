python-social-auth-steemconnect
===========================

Pluggable authentication backend for python-social-auth, that allows authentication via SteemConnect (v2).


## Installation instructions

From pypi

    $ pip install social-auth-steemconnect

or clone from Github

    $ git clone git@github.com:wise-team/python-social-auth-steemconnect.git
    $ cd python-social-auth-steemconnect && sudo python setup.py install

## Pre-requisites

`python-social-auth` must be installed and configured first. Please visit the
[python-social-auth documentation](http://python-social-auth-docs.readthedocs.io/) for instructions.


## Configuration instructions

1. Add Waveapps backend to AUTHENTICATION_BACKENDS:

        AUTHENTICATION_BACKENDS = (
            'steemconnect.backends.SteemConnectOAuth2',
            ...
            'django.contrib.auth.backends.ModelBackend',
        )

2. Add your Waveapps settings to your django `settings.py` file.

        SOCIAL_AUTH_STEEMCONNECT_KEY = '<your-steemconnect-app-acccount>' # ex. 'myproject.app'
        SOCIAL_AUTH_STEEMCONNECT_DEFAULT_SCOPE = ['vote', 'comment']

## Examples

Ready to use examples of projects in Django, Flask and Tornado frameworks are prepared here:

https://github.com/wise-team/python-social-auth-steemconnect-examples

## Changelog

### 0.0.3
* SteemConnect endpoint changed from `https://v2.steemconnect.com` to `https://steemconnect.com`

### 0.0.2
* package rename

### 0.0.1
* Initial release

