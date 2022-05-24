from setuptools import setup, find_packages

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="verysimplemodule", 
        version= '0.0.1',
        author="Katie Brown",
        author_email="<kbrow327@uwo.ca>",
        description='Functions for analysis of MgII halos',
        packages=find_packages(),
        install_requires=['h5py', 'numpy', 'matplotlib', 'scipy', 'astropy'], 
        ]
)
