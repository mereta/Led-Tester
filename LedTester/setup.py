from setuptools import setup

setup(name="ledTester",
      version="0.1",
      description="LED Testing for Assignment3 in COMP30670 2017",
      url="",
      author="Mereta Degutyte",
      author_email="mereta.degutyte@ucdconnect.ie",
      licence="GPL3",
      packages=['LedTester'],
      entry_points={
        'console_scripts':['led_tester=src.main:main']
        },
      install_requires=[
          'numpy',
      ],
      )