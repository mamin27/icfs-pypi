# ecomet_i2c_sensors-pypi
**Last modification:** 25.01.2022

**Contributor:** Marian Minar, Juraj Cekan

```python
$ pip3 install setuptools
$ pip3 install wheel
$ sudo apt-get install python3-venv -y
$ python3 -m venv ~/my_venv
$ source ~/my_venv/bin/activate
$ git clone git@github.com:JurajCekan/ecomet_i2c_sensors-pypi.git
$ cd ~/ecomet_i2c_sensors-pypi
$ python3 setup.py bdist_wheel
$ pip3 install -e .


$ pip3 install setuptools wheel
$ pip3 install twine
$ twine upload --verbose --repository testpypi dist/*

$ twine upload --verbose --repository pypi dist/*
```

**Links:**

* [TestPyPi](https://test.pypi.org/)
* [PyPi](https://pypi.org/)

**Library Name:**
ecomet-i2c-sensors

**Dependency:**
* Adafruit_PureIO 1.1.9
* pickle5 0.0.11
* json5 0.9.6

**Download commands:**
```sh
vi CHANGELOG.txt
vi setpu.py

pip3 install -i https://test.pypi.org/simple/ ecomet-i2c-sensors
pip3 install -i https://pypi.org/simple/ ecomet-i2c-sensors

pip install ecomet-i2c-sensors
```
