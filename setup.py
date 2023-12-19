from setuptools import find_packages,setup


setup(
    name = 'ML_Project',
    version='0.0.1'
    author='Ayush'
    author_email='jaiswalayush2708@gmail.com'
    packages= find_packages()
    install_requires = ['pandas','numpy','seaborn']
)