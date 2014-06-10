from distutils.core import setup

setup(
    name='Gnosis',
    version='0.1.0',
    author='David Mertz, Mark Wallsgrove',
    author_email='mark.wallsgrove@gmail.com',
    packages=[
        'gnosis',
        'gnosis.util',
        'gnosis.util.convert',
        'gnosis.util.test',
        'gnosis.anon',
        'gnosis.xml',
        'gnosis.xml.relax',
        'gnosis.xml.objectify',
        'gnosis.xml.objectify.doc',
        'gnosis.xml.objectify.test',
        'gnosis.xml.validity',
        'gnosis.xml.pickle',
        'gnosis.xml.pickle.util',
        'gnosis.xml.pickle.doc',
        'gnosis.xml.pickle.parsers',
        'gnosis.xml.pickle.ext',
        'gnosis.xml.pickle.test',
        'gnosis.magic'
    ],
    url='http://github.com/smokedice/Gnosis',
    
    # Old version stated:
    # license='Creative Commons Attribution 3.0 Unported',
    # The issue with that is that CC-BY is 
    # a) not a software license;
    # b) not compatible with GPL, so you can't mix them in one project; and
    # c) is not what David specified in his code on gnosis.cx :)
    # I suggest going with CC0 as per David's recommendation.
    # See also http://wiki.creativecommons.org/CC0_FAQ#May_I_apply_CC0_to_computer_software.3F_If_so.2C_is_there_a_recommended_implementation.3F
    license='CC0 1.0 Universal',
    
    
    description='Parses XML into Python object representation',
    long_description=open('README.rst').read(),

    keywords = 'XML indexing multimethods metaclass pickle validity HOF RNC RNG',

 # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',

        # Pick your license as you wish (should match "license" above)
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',

        # Other stuff as in original PyPI page
        'Environment :: Console',
        'Natural Language :: English',
        'Operating System :: OS/2',
        'Operating System :: OS Independent',
        'Operating System :: Unix',
        'Programming Language :: C',
        'Programming Language :: Python',
        'Programming Language :: Rexx',
        'Programming Language :: SQL',
        'Programming Language :: Unix Shell',
        'Topic :: Communications :: Email',
        'Topic :: Communications :: Email :: Filters',
        'Topic :: Communications :: Email :: Mail Transport Agents',
        'Topic :: Communications :: Email :: Post-Office :: POP3',
        'Topic :: Documentation',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Object Brokering',
        'Topic :: System :: Archiving :: Compression',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Markup :: XML',
        
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

)
