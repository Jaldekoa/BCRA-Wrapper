from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "BCRA (Banco Central de la República Argentina) API wrapper in Python"
LONG_DESCRIPTION = "Python wrapper to interact with the official BCRA (Banco Central de la República Argentina) API. BCRA's API does not require tokens or registration, so feel free to use it."

setup(
    name="BCRA-Wrapper",
    version=VERSION,
    url="https://github.com/Jaldekoa/BCRA-Wrapper",
    author="Jon Aldekoa",
    author_email="jaldekoa@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=["BCRA_Wrapper"],
    test_suite='BCRA_Wrapper.tests.test',
    install_requires=["pandas", "requests"],
    keywords=['python', 'primer paquete'],
    classifiers=[
        "Development Status :: 3 - Alpha",
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
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ]
)
