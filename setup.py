import os.path
import re

from setuptools import find_packages, setup

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))


def get_long_description():
    long_description = []
    with open(os.path.join("README.md")) as f:
        long_description.append(f.read())
    return "\n".join(long_description)

setup(
    name='py-solaredge',
    version='0.0.4.8',
    license='BSD',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    description='Python API wrapper for SolarEdge monitoring services',
    author='Yenthe Van Ginneken',
    author_email='yenthevg@gmail.com',
    maintainer='Yenthe Van Ginneken',
    maintainer_email='yenthevg@gmail.com',
    keywords=['SolarEdge', 'SolarEdge API', 'SolarEdge Monitoring', 'SolarEdge Monitoring API'],
    url='https://github.com/Yenthe666/pysolaredge',
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Scientific/Engineering',
    ],
)
