# Always prefer setuptools over distutils
import re

from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# read the version from classla/_version.py
version_file_contents = open(path.join(here, 'classla/_version.py'), encoding='utf-8').read()
VERSION = re.compile('__version__ = \"(.*)\"').search(version_file_contents).group(1)

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

packages = find_packages(exclude=['data', 'docs', 'extern_data', 'figures', 'saved_models'])

setup(
    name='classla',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=VERSION,

    description='Adapted Stanford NLP Python Library with improvements for specific languages.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    # The project's main homepage.
    url='https://github.com/clarinsi/classla-stanfordnlp.git',

    # Author details
    author='CLARIN.SI',
    author_email='info@clarin.si',

    # Choose your license
    license='Apache License 2.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Information Technology',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],

    # What does your project relate to?
    keywords='natural-language-processing nlp natural-language-understanding stanford-nlp deep-learning clarinsi',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=packages,

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['numpy==1.23.0', 'protobuf>=4.21.2,<7.0.0', 'requests>=2.30.0,<3.0.0', 'torch>=1.13.0,<=2.7.0', 'tqdm>=4.66.1,<5', 'obeliks==1.1.6', 'reldi-tokeniser==1.0.3'],

    # List required Python versions
    python_requires='>=3.6',

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
    },
)
