from setuptools import setup, version, find_packages 

setup (
    name='Second-Brain-Tools',
    version='0.0.1',
    packages=find_packages(),
    install_requires =[
        'click',
        'python-dotenv'
    ],
#sbt = second brain tools
    entry_points='''
    [console_scripts]
    sbt=main:home_screen
    second-brain-tools=main:home_screen
    '''
)
