"""
À CHANGER
"""
import pathlib
import smarthouse

from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

if __name__ == "__main__":
    setup(name='smarthouse',
          author='Francis M-G et Mohammed',
          author_email="alivecode.developers@gmail.com",
          version=smarthouse.__version__,
          description='The smarthouse project of ALIVEcode',
          long_description=README,
          long_description_content_type="text/markdown",
          classifiers=[
              "Programming Language :: Python :: 3",
              "Programming Language :: Python :: 3.10",
          ],
          url="https://github.com/ALIVEcode/SmartHouse",
          packages=find_packages(
              include=['smarthouse', 'smarthouse.*']),
          include_package_data=True,
          python_requires=">=3.10",
        #   install_requires=["alimata"],
          setup_requires="setuptools",
          )
