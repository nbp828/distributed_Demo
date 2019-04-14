from setuptools import setup, find_packages

setup(
    name='pydist',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        pydist=pydist.scripts.pydist_command:pydist_command
        pdgrep=pydist.scripts.pydist_grep_command:pydist_grep_command
    ''',
)
