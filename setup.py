from setuptools import setup, find_packages

setup(
    name='shared_utils',
    version='0.2.3',
    packages=find_packages(),  # Automatically finds and includes sub-packages like 'tests'
    include_package_data=True,  # Include all package data files specified
    package_data={
        'tests': ['*.py'],  # Include all Python files in the 'tests' package
    },
    install_requires=[
        'python-dotenv',
        'SQLAlchemy>=2.0',
        'pyodbc',
        'pymysql',
        'psycopg2-binary',
    ],
    author='Will Palmer',
    author_email='willpalmer@alertacall.com',
    description='Shared utilities for database connections',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'test_shared_utils=tests.test:test_connections'  # Entry point for running the test script
        ]
    },
)
