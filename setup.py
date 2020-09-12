from setuptools import setup, find_packages


def retrieve_required_dependencies():
    dependency_list = []
    for line in open("requirements.txt").read():
        dependency_list.append(line.replace("\n", ""))
    return dependency_list


setup(
    name='crafatar',
    version="1.0.0",

    install_requires=retrieve_required_dependencies(),
    packages=find_packages(),
    package_data={"": ["requirements.txt", "LICENSE", "README.md"]},

    author='PWRScript',
    author_email='powerofthescript@outlook.com',

    description='An unofficial API Wrapper for crafatar',
    license='MIT License',

    project_urls={
        "Bug Tracker": "https://github.com/PWRScript/crafatar.py/issues",
        # "Documentation": "https://docs.example.com/HelloWorld/", TODO Implement documentation
        "Source Code": "https://github.com/PWRScript/crafatar.py",
    },
    url='https://github.com/PWRScript/crafatar.py',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    keywords="crafatar api minecraft head face avatar body cape skin mojang",
)
