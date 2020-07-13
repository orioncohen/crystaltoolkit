# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ""

setup(
    long_description=readme,
    name="crystal_toolkit",
    version="2020.06.04",
    python_requires="==3.*,>=3.7.0",
    author="Matthew Horton",
    author_email="mkhorton@lbl.gov",
    packages=[
        "crystal_toolkit",
        "crystal_toolkit.apps",
        "crystal_toolkit.apps.examples",
        "crystal_toolkit.apps.examples.tests",
        "crystal_toolkit.apps.tests",
        "crystal_toolkit.components",
        "crystal_toolkit.components.transformations",
        "crystal_toolkit.core",
        "crystal_toolkit.core.tests",
        "crystal_toolkit.helpers",
        "crystal_toolkit.renderables",
    ],
    package_data={
        "crystal_toolkit": ["*.json"],
        "crystal_toolkit.apps": ["assets/*.ico", "assets/*.json", "assets/*.png"],
        "crystal_toolkit.apps.examples": ["*.json"],
        "crystal_toolkit.core": ["*.yaml"],
    },
    install_requires=[
        "dash[testing]==1.*,>=1.9.1",
        "dash-daq==0.*,>=0.4.0",
        "dash-mp-components==0.*,>=0.0.8",
        "dash-table==4.*,>=4.6.1",
        "flask-caching==1.*,>=1.8.0",
        "gevent==1.*,>=1.4.0",
        "gunicorn==20.*,>=20.0.4",
        "plotly==4.*,>=4.5.4",
        "pydantic==1.*,>=1.4.0",
        "pymatgen==2020.*,>=2020.3.13",
        "redis==3.*,>=3.4.1",
        "scikit-learn==0.*,>=0.22.2",
        "webcolors==1.*,>=1.11.1",
    ],
    extras_require={
        "dev": [
            "black==19.*,>=19.10.0",
            "dephell==0.*,>=0.8.2",
            "pre-commit==2.*,>=2.2.0",
            "pytest==5.*,>=5.4.1",
            "recommonmark==0.*,>=0.6.0",
            "sphinx==2.*,>=2.4.4",
            "sphinx-rtd-theme==0.*,>=0.4.3",
        ]
    },
)
