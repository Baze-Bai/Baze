from setuptools import setup, find_packages

setup(
    name='xlsx_processor',
    version='1.0',
    packages=find_packages(),
    py_modules=['xlsx_processor', 'main', 'test'],  
    install_requires=[
        'pandas',
        'setuptools',
        'chardet',
        'openpyxl',
        'xlrd',
    ],
    entry_points={
        'console_scripts': [
            'process_xlsx=main:main',
        ],
    },
    author='Zejun Bai',
    author_email='15583405928@163.com',
    description='A tool to process csv file, which can delete rows with missing values according to the column index you input.',
)
