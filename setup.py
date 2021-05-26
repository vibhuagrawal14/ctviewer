from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.txt'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ctviewer',
    version='1.0.0',    
    description='Interactive utility to view 3D CT images in ipython notebooks',
    url='https://github.com/vibhuagrawal14/ctviewer',
    author='Vibhu Agrawal',
    author_email='vibhu.agrawal14@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    packages=['ctviewer'],
    install_requires=['numpy',
                      'matplotlib',                     
                      ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
