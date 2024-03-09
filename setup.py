from setuptools import find_packages, setup

HYPHEN_E_DOT = "-e ."


# functions to get required librearies names and version
def get_requirements(file_path:str)->list:
    """function to get all required libraries data from the given file"""
    required_libraries = []
    with open(file_path) as fh:
        required_libraries = [lib.replace("\n", "") for lib in fh.readlines()]

    if HYPHEN_E_DOT in required_libraries:
        required_libraries.remove(HYPHEN_E_DOT)

    return required_libraries


setup(
    name="mlproject",
    version="0.0.1",
    author="Mohit Raj Rathor",
    author_email="mohitrajrathor@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)