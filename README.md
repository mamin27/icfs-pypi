# ecomet_i2c_sensors-pypi
**Last modification:** 3.03.2023

**Contributor:** Marian Minar, Juraj Cekan

```python
$ pip3 install setuptools
$ pip3 install wheel
$ sudo apt-get install python3-venv -y
$ python3 -m venv ~/my_venv
$ source ~/my_venv/bin/activate
$ git clone git@github.com:mamin27/icfs-pypi.git
$ cd ~/icfs-pypi
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
icfs

**Dependency:**
* Adafruit_PureIO 1.1.9

**Download commands:**
```sh
vi CHANGELOG.txt
vi setpu.py

pip3 install -i https://test.pypi.org/simple/ icfs
pip3 install -i https://pypi.org/simple/ icfs

pip install icfs
```
