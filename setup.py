from setuptools import setup, find_packages


setup(
    name='bulkrecode',
    version='1.2',
    description='Bulk recode audio files',
    author='adisbladis',
    url='https://github.com/adisbladis/bulkrecode',
    license = "GNU GPLv3",
    packages=find_packages(),
    download_url='https://github.com/adisbladis/bulkrecode/tarball/1.2',
    scripts=[
        'bin/brc',
    ],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License (GPL)',
    ]
)
