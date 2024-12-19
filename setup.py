from setuptools import setup
from pathlib import Path

VERSION = "2.0.0"
THIS_PATH = Path(__file__).parent
DESCRIPTION = "Python API for Banco Central de la República Argentina (BCRA)"
LONG_DESCRIPTION = (THIS_PATH / "README.md").read_text(encoding="utf-8")


setup(
    name="bcraapi",
    version=VERSION,
    url="https://github.com/Jaldekoa/BCRA-Wrapper",
    author="Jon Aldekoa",
    author_email="jaldekoa@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=["bcraapi"],
    test_suite='bcraapi.tests.test',
    platforms=["Any"],
    install_requires=["pandas", "requests"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ]
)
