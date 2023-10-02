from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list pf requirements
    :param file_path:
    :return:
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
    name='miprojects',
    version='0.0.1',
    author='Saikrishna Vinjamuri',
    author_email='saikrishna.spark@gmail.com',
    packages=find_packages(),
    install_requirements=get_requirements('requirement.txt')

)
