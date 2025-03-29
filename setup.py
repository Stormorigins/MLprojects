from setuptools import setup, find_packages
from typing import List

Hypen="-e ."#used to sync setup and req file
def get_requirement(file_path: str)-> List[str]:
    
    req=[]
    with open(file_path) as file:
        req=file.readlines()
        req=[i.replace("/n","") for i in req]

        if Hypen in req:
            req.remove(Hypen)
    return req
        


setup(
    name="MLprojects",
    version="0.0.1",
    author="Pushparaj",
    author_email= "Pushparaj29196@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt')

    
)