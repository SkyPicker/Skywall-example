import os
import shutil
from setuptools import setup, find_packages


root = os.path.dirname(__file__)

def requirements():
    with open(os.path.join(root, 'requirements.txt')) as f:
        return f.read().splitlines()

def readme():
    with open(os.path.join(root, 'README.md')) as f:
        return f.read()

def move(src, dest):
    src = os.path.join(root, src)
    dest = os.path.join(root, dest)
    if os.path.exists(src) and not os.path.exists(dest):
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.move(src, dest)


move('.babelrc', 'skywall_example/javascript/.babelrc')
move('package.json', 'skywall_example/javascript/package.json')
move('frontend', 'skywall_example/javascript/frontend-src')

setup(
    name='skywall-example',
    version='0.0.1',
    description='Skywall example module.',
    long_description=readme(),
    url='https://github.com/SkyPicker/skywall-example',
    author='',
    author_email='',
    license='GPL-3.0',
    install_requires=requirements(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    )
