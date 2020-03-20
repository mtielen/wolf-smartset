import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='wolf_smartset',
    version='0.1.2',
    author="Adam Krol",
    author_email="adam.krol93@gmail.com",
    description="A package to comunicate with Wolf Smart Set Cloud",
    long_description=long_description,
    package_data={"wolf_smartset": ["py.typed"]},
    long_description_content_type="text/markdown",
    # url="https://github.com/javatechy/dokr",
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'httpx'
    ]
)
