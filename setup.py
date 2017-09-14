from setuptools import setup, find_packages


setup(
    name='python-social-auth-steemconnect',
    version='0.1.0',
    packages=find_packages(),
    author='Krzysztof @noisy Szumny',
    author_email='noisy.pl@gmail.com',
    description='SteemConnect backend for python-social-auth.',
    long_description=open('README.md').read(),
    license='LICENSE',
    url='https://github.com/noisy/python-social-auth-steemconnect',
    keywords='django social auth oauth2 social-auth steem steemconnect steemit',
    classifiers=[
    ],
    install_requires=[
        'python-social-auth',
    ]
)
