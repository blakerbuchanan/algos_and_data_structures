from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'A package containing data structures'
LONG_DESCRIPTION = 'A package containing data structures which can be used in implementations of algorithms'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="datastructures", 
        version=VERSION,
        author="Blake Buchanan",
        author_email="<blakerbuchanan@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'data structures'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)