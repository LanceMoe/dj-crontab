#!/usr/bin/env python
from setuptools import setup


setup(
    name='dj-crontab',
    description='dead simple crontab powered job scheduling for django',
    version='0.8.0',
    author='Lance.Moe',
    author_email='admin@lance.moe',
    license='MIT',
    url='https://github.com/LanceMoe/dj-crontab',
    long_description=open('README.rst').read(),
    packages=[
        'django_crontab',
        'django_crontab.management',
        'django_crontab.management.commands'],
    install_requires=[
        'Django>=1.8'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: System :: Installation/Setup'
    ]
)
