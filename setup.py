import setuptools


with open('Description.rst') as f:
    description = f.read()

setuptools.setup(
    author="Jash Shah",
    author_email="shahjash271@gmail.com",
    name='detect_mask',
    license="MIT",
    description='Python Package for detecting masks in the input Photos',
    version='v0.0.3',
    long_description=description,
    url='https://github.com/Jash271/Detect_Mask',
    packages=setuptools.find_packages(),
    
    python_requires=">=3.5",
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        
    ],
    include_package_data=True,
    
)
