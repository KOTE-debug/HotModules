from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="hotmodule",
    version="1.0",
    author="HotDrify",
    author_email="root76240@gmail.com",
    description="modules for your python project!",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/KOTE-debug/hotmodules/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
