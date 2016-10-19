try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
    
def readme():
    with open('README.rst') as f:
        return f.read()
        
setup(name='PyGCMSE',
      version='1.0.0',
      description='Gradient Conduction Mean Square Error',
      classifiers=[
        'Development Status :: 1 - Alpha',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: MIT License'
        'Topic :: Scientific/Engineering'
      ],
      url='https://github.com/jlrandulfe/PyGCMSE',
      author='Javier Lopez Randulfe',
      author_email='javier.randulfe@uvigo.es',
      license='MIT',
      scripts=[''],
      packages=find_packages(exclude=['docs', 'tests*']),
      install_requires=[],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False
      )
