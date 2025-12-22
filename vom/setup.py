from setuptools import setup, find_packages

setup(
    name='vom-standard',
    version='0.5',
    description='team-based version control integrating git and github for maximum team potential',
    author='semicolon studios',
    author_email='pixilreal@example.com',
    packages=find_packages(),
    install_requires=[
        "cryptography"
    ],
    entry_points={
        'console_scripts': [
            'vom=vom:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.13',
)