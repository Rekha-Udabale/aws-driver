import json
from setuptools import setup, find_namespace_packages

with open('awsdriver/pkg_info.json') as fp:
    _pkg_info = json.load(fp)

with open("DESCRIPTION.md", "r") as description_file:
    long_description = description_file.read()

setup(
    name='awsdriver',
    version=_pkg_info['version'],
    description='None',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_namespace_packages(include=['awsdriver*']),
    include_package_data=True,
    install_requires=[
        'werkzeug==0.14',
        'itsdangerous==2.0.1',
        'ignition-framework==3.0.1',
        'uwsgi>=2.0.18,<3.0',
        'gunicorn>=19.9.0,<20.0',
        'boto3==1.18.4',
        'cfn-flip==1.2.3'
    ],
    entry_points='''
        [console_scripts]
        awsdriver-dev=awsdriver.__main__:main
    ''',
    scripts=['awsdriver/bin/awsdriver-uwsgi', 'awsdriver/bin/awsdriver-gunicorn', 'awsdriver/bin/awsdriver']
)