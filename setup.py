from setuptools import setup, find_packages
import os

version = '1.12.dev0'

setup(name='eappi.theme',
      version=version,
      description="EAPPI THeme",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone theme',
      author='Afterfive Technologies',
      author_email='inquiry@afterfivetech.com',
      url='http://github.com/afterfivetech',
      license='gpl',
      packages=find_packages(),
      namespace_packages=['eappi'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity [grok, relations]',
          'plone.namedfile [blobs]',
          'collective.grok',
          'plone.app.referenceablebehavior',
          'collective.dexteritytextindexer',
          'z3c.jbot'
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': [
              'plone.app.testing',
           ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # The next two lines may be deleted after you no longer need
      # addcontent support from paster and before you distribute
      # your package.
      # setup_requires=["PasteScript"],
      # paster_plugins=["templer.localcommands"],

      )
