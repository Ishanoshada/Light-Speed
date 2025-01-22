from setuptools import setup, find_packages

setup(
    name="light_speed",
    version="0.1.3",
    description="A comprehensive physics package for light speed and real-world calculations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ishan Oshada",
    author_email="ishan.kodithuwakku.offical@gmail.com",
    url="https://github.com/ishanoshada/light-speed",
    packages=find_packages(),
    
    install_requires=[
        "numpy",
    ],
    keywords="relativity physics light-speed optics",
    project_urls={
        "Bug Tracker": "https://github.com/ishanoshada/light-speed/issues",
        "Source Code": "https://github.com/ishanoshada/light-speed",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
    ]
)
