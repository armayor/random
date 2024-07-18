from setuptools import setup, find_packages

setup(
    name='random',  # Name of your package
    version='0.1',  # Version of your package
    packages=find_packages(),  # Automatically find packages in your project
    install_requires=[  # List of dependencies
        # 'dependency1',
        # 'dependency2',
    ],
    entry_points={  # Entry points for command-line scripts
        'console_scripts': [
            # 'my_command=my_project.module:function',
        ],
    },
    author='Your Name',  # Author's name
    author_email='your.email@example.com',  # Author's email
    description='A brief description of your project',  # Short description
    long_description=open('README.md').read(),  # Long description (usually from README file)
    long_description_content_type='text/markdown',  # Type of long description content
    url='https://github.com/yourusername/my_project',  # URL to the project's homepage
    classifiers=[  # List of classifiers (see https://pypi.org/classifiers/)
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Python version requirement
)
