import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="terraobject",
    version="0.0.1",
    author="Joao Gilberto Magalhaes",
    author_email="joao@byjg.com.br",
    description="Terraobject package to share variables between terrascript components",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/byjg/terraobject",
    packages=setuptools.find_packages(exclude=['__pycache__']),
    package_dir={'terraobject': 'terraobject'},
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)