from setuptools import setup
REQUIRES = [
    'records',
    'allure',
    'sqlalchemy',
    'structlog'
]

setup(
    name='orm_client',
    version='0.0.1',
    packages=['ormclient'],
    url='https://github.com/widowblack11/orm_client.git',
    license='MIT',
    author='oksanaprokopenko',
    author_email='-',
    istall_requires=REQUIRES,
    description='orm client with sqlalchemy'
)
