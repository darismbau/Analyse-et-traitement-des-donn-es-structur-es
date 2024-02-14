import os
from setuptools import setup as st



dir = os.getcwd()




st(
    name='my_package_YB',
    version="1",
    description="un paquer pour gerer des biblio",
    packages=[],
    scripts=[dir + '\\my_package_YB\\find3.py'],
)
