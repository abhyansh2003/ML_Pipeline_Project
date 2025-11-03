from setuptools import find_packages, setup
from typing import List

HYPHON_E_DOT = "-e ."

def get_requirements(filepath: str) -> List[str]:
    requirements = []
    
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        # there is hidden '/n for the next line in requirements.txt so
        # we are going to replace it.'
        requirements = [i.replace("\n", "") for i in requirements]
        
        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)
        
setup(
    name='ML_Python_Project',
    version='0.0.1',
    description='It is a ML proejct in which ML Pipeline will be used.',
    # long_description=open('README.md').read(),
    # long_description_content_type='text/markdown',
    author='abhyansh2003',
    author_email='shrivastavaabhyansh91@gmail.com',
    url='https://github.com/abhyansh2003/ML_Pipeline_Project',
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
    )