from setuptools import setup

setup(
    name='Lunch',
    version='0.0.1',
    py_modules=['lunch'],
    install_requires=[
        'Click',
        'pyfiglet'
    ],
    entry_points='''
        [console_scripts]
        lunch=lunch:cli
    '''

)