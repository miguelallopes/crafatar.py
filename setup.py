from setuptools import setup, find_packages

def retrieve_required_dependencies():
    dependency_list = []
    for line in open("requirements.txt").read():
        dependency_list.append(line)
    return dependency_list


setup(
    name='crafatar',
    version="1.0.0-alpha",

    install_requires=retrieve_required_dependencies(),
    packages=find_packages(),
    package_data={"": ["requirements.txt", "LICENSE","README.md"]},

    author='PWRScript',
    author_email='powerofthescript@outlook.com',

    description='An unofficial API Wrapper for crafatar',
    license='MIT License',

    project_urls={
        "Bug Tracker": "https://github.com/PWRScript/crafatar.py/issues",
        #"Documentation": "https://docs.example.com/HelloWorld/", TODO Implement documentation
        "Source Code": "https://github.com/PWRScript/crafatar.py",
    },
    url='https://github.com/PWRScript/crafatar.py',

    keywords="crafatar minecraft head face avatar body cape skin mojang",
)
