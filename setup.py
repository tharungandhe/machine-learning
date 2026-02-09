from setuptools import setup, find_packages

def read_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()

setup(
    name="ml_project",
    version="0.1.0",
    author="Your Name",
    description="End-to-end Machine Learning project",
    packages=find_packages(),
    install_requires=read_requirements(),
)