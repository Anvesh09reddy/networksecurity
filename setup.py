from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    requirement_lst=[]
    try:
        with open('requirements.txt', 'r') as f:
            lines=f.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!="-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the same directory as setup.py.")
    return requirement_lst

setup(
    name='NetworkSecurity',
    version='0.1.0',
    author='Anvesh Reddy',
    author_email='p.anveshreddy9@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)