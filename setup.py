from setuptools import setup, find_packages

setup(
    name='shared_utils',
    version='0.2.1',
    packages=find_packages(),
    include_package_data=True,  # Ensures non-code files like test scripts are included
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
            'test_shared_utils=tests.test:test_connections'  # Command to run test
        ]
    },
)
