from setuptools import setup, find_packages


setup(
    name='social-auth-steemconnect',
    version='0.0.1',
    packages=find_packages(),
    author='Krzysztof @noisy Szumny',
    author_email='noisy.pl@gmail.com',
    description='SteemConnect backend for python-social-auth.',
    long_description=open('README.md').read(),
    license='LICENSE',
    url='https://github.com/noisy/python-social-auth-steemconnect',
    keywords='django social auth oauth2 social-auth steem steemconnect steemit',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],
    install_requires=[
        'social-auth',
    ]
)
