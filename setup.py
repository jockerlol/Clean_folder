from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0',
    description='this script sorts your files in the folder',
    classifiers=[
        "License :: OSI Approved :: Apache",
        "Operating System :: OS Independent",
        'Programing language :: Python :: 3.11'
    ],
    author='Oleksandr',
    author_email='jockerlol1@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    python_requires='>=3.8',
    include_package_data=True,
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)