import setuptools


with open('Description.rst') as f:
    description = f.read()

setuptools.setup(
    author="Jash Shah",
    author_email="shahjash271@gmail.com",
    name='detect_mask',
    license="MIT",
    description='Python Package for detecting masks in the input Photos ,Pull out the camera for real time mask detection',
    version='v0.5.0',
    long_description=description,
    url='https://github.com/Jash271/Detect_Mask',
    packages=setuptools.find_packages(),
    
    python_requires=">=3.6.8",
    install_requires=['opencv-python'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        
        
        
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        
    ],
    include_package_data=True,
    
)
