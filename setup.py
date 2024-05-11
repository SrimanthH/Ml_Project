from setuptools import find_packages,setup
from typing import List
def get_packages(file_path:str)->List[str]:
    '''
    This function will return a list of required packages present in the file path given to it

    '''
    HYPEN_E_DOT='-e .'
    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements
setup(
name='MLproject',
version='0.0.1',
author='Srimanth',
author_email='srimanth.nitk@gmail.com',
packages=find_packages(),
install_requires=get_packages('requirements.txt'),


)