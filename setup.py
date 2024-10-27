# setup.py

from setuptools import setup, find_packages

setup(
    name='shared_utils',
    version='0.1.9',
    packages=find_packages(),
    install_requires=[
        'python-dotenv',
        'SQLAlchemy>=2.0',
        'pyodbc',
        'pymysql',
        'psycopg2-binary',  # For PostgreSQL connections
    ],
    author='Will Palmer',
    author_email='willpalmer@alertacall.com',
    description='Shared utilities for database connections',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
