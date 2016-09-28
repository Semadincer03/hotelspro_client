from setuptools import find_packages, setup

setup(
    name='hotelspro_client',
    version='1.1.0',
    packages=find_packages(),
    url='https://github.com/Semadincer03/hotelspro_client',
    license='GPL',
    author='Sema Dincer',
    author_email='dincersema@hotmail.com',
    description='Hotelspro.com api client',
    install_requires=['requests'],
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)