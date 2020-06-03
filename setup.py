
import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="python-gsi",
    version="0.0.1",
    author="Alve Svarén",
    author_email="alve@hotmail.se",
    description="A simple web server for handling game state integrations in games like CSGO",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alvesvaren/spotify_python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    install_requires=[
        "Flask=>1.0.0"
    ],
    python_requires='>=3.5',
)