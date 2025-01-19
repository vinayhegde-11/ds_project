from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(filepath:str)->List[str]:
    '''
    This function will return list of requirements
    '''
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='ds_project',
    version='0.0.1',
    author='Vinay Hegde',
    author_email='learningwithvinay@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas', 'numpy', 'seaborn'] # for smal number of packages
    install_requires=get_requirements('requirements.txt')
)