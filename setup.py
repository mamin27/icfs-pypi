from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 3',
]

setup(
    name = 'icfs',
    version = '0.0.2',
    author = 'Marian Minar',
    author_email = 'mminar7@gmail.com',
    platform = 'armv7l',
    description = 'Library create and manage file system at I2C EEPROM ICs.',
    long_description = open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url = 'https://github.com/mamin27/icfs',
    license='GPLv3',
    classifiers=classifiers,
    keywords=['raspberry','I2C','filesystem','ecomet'],
    packages=find_packages(),
    install_requires=[
    'Adafruit_PureIO >= 1.1.8',
    'RPI.GPIO >= 0.7.1',
    'smbus2 >= 0.4.2',
    'ecomet-i2c-sensors >= 0.1.6',
    'pyyaml >= 6.0',
    'crc >= 4.1.0',
    ]
)
