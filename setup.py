from setuptools import find_packages, setup

setup(
    name='cp2png',
    version="0.1",
    url='https://github.com/qurben/cp2png',
    license='MIT',
    author='Gerben Oolbekkink',
    author_email='g.j.w.oolbekkink@gmail.com',
    description='Convert .cp files to .png using Pillow',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Pillow >= 8.0'
    ],
    entry_points={},
)