from setuptools import find_packages,setup
from typing import List
hypen = '-e .'

def get_requirements(file_path:str)->List[str]:
    
    
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if hypen in requirements:
            requirements.remove(hypen)
    return requirements

setup(
    name='mlpoject',
    version='0.0.1',
    author='navaneth',
    author_email='navaneethakrishnan.ravikumar@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    
)