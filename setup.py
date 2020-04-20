from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='runelsewhere',
    version='0.0.1',
    description='Redefine the run line magic to change folders',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/aulemahal/RunElsewhere',
    author='Pascal Bourgault',
    author_email='pascal.bourgault@gmail.com',
    packages=find_packages(),
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Framework :: IPython',
        'Framework :: Jupyter',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='ipython magic remote spyder',
    install_requires=['ipython>=6.0'],
)
