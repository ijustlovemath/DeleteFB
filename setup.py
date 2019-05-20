import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="delete-facebook-posts",
    version="1.0.0",
    author="Wesley Kerfoot",
    author_email="wes@wesk.tech",
    description="A Selenium Script to Delete Facebook Posts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/weskerfoot/DeleteFB",
    packages=setuptools.find_packages(),
    install_requires = [
        "selenium>=3.141.0",
        "selenium-requests>=1.3",
        "requests>=2.21.0"
    ],
    classifiers= [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        "console_scripts" : [
            "deletefb = deletefb:run_delete"
        ]
    }
)
