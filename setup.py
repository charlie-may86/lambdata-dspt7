import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata-dspt7", # Replace with your own username
    version="0.0.1",
    author="Charlie May",
    author_email="charles-may@lambdastudents.com",
    description="An attempt to publish packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/charlie-may86/lambdata-dspt7.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)