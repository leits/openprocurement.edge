import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

requires = [
    'chaussette',
    'cornice',
    'gevent',
    'iso8601',
    'jsonpatch',
    'pbkdf2',
    'pyramid_exclog',
    'requests',
    'setuptools',
    'couchdb',
    'python-dateutil',
    'openprocurement_client',
    'openprocurement.api',
    'munch'
]
test_requires = requires + [
    'webtest',
    'python-coveralls',
    'nose'
]

entry_points = {
    'paste.app_factory': [
        'main = openprocurement.litepublic:main'
    ],
}

setup(name='openprocurement.litepublic',
      version='2.3.18',
      description='openprocurement.litepublic',
      long_description=README,
      classifiers=[
          "Framework :: Pylons",
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
      ],
      keywords="web services",
      author='Quintagroup, Ltd.',
      author_email='info@quintagroup.com',
      license='Apache License 2.0',
      url='https://github.com/openprocurement/openprocurement.litepublic',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['openprocurement'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=test_requires,
      extras_require={'test': test_requires},
      test_suite="openprocurement.litepublic.tests.main.suite",
      entry_points=entry_points)