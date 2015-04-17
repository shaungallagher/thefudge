from setuptools import setup, find_packages


setup(name='thefudge',
      version=1.6,
      description="Magnificent app which corrects your previous console command",
      author='Vladimir Iakovlev',
      author_email='nvbn.rm@gmail.com',
      url='https://github.com/nvbn/thefudge',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['pathlib'],
      entry_points={'console_scripts': [
          'thefudge = thefudge.main:main']})
