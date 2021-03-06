from setuptools import setup

setup(
    name="vdk",
    version='1.0',
    py_modules=['cli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        vdk=cli:cli
    ''',
)
