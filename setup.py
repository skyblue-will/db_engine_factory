from setuptools import setup, find_packages

setup(
    name='db_engine_factory',  # Updated name
    version='0.1.0',
    packages=find_packages(),  # This will now find 'db_engine_factory' and 'tests'
    include_package_data=True,
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
    description='Library for managing multiple database connections via configuration',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'test_db_engine_factory=tests.test:test_connections'  # Updated command name
        ]
    },
)
