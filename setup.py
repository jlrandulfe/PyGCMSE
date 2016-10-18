try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
    
def readme():
    with open('README.rst') as f:
        return f.read()
        
setup(name='UviSpace',
      version='3.0',
      description='UVigo iSpace project python packages',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Framework :: Robot Framework',
        'Topic :: Scientific/Engineering'
      ],
      url='',
      author='Javier Lopez Randulfe',
      author_email='javier.randulfe@uvigo.es',
      license='https://github.com/jlrandulfe/UviSpace',
      scripts=['bin/first-script'],
      packages=find_packages(exclude=['docs', 'tests*']),
      install_requires=[],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False
      )
