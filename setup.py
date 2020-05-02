from setuptools import setup


setup(
    name='textbot',
    version='0.1.0',  # TODO: Read it from __init__.py without loading.
    url='https://github.com/pylover/textbot',
    description='Simple text assistant using Python',
    packages=['textbot'],
    install_requires=[
        'easycli'
    ],
    license='MIT',
    entry_points={
        'console_scripts': [
            'textbot = textbot.cli:TextBot.quickstart',
        ]
    }

)
