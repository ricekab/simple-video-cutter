from setuptools import setup, find_packages

__about__ = {}
with open("simplevideocutter/__about__.py") as fp:
    exec(fp.read(), __about__)

setup(
    name=__about__['__name__'],
    version=__about__['__version__'],
    description=__about__['__description__'],
    url='https://github.com/ricekab/simple-video-cutter',
    author='ricekab',
    author_email='contact@kevinchiytangtang.com',
    packages=find_packages(exclude=['tests']),
    license='MIT License',
    install_requires=['click>=8',
                      ],
    extras_require={
        'gui': ['PySide2'],
    },
    python_requires='>=3.8',
    entry_points='''
        [console_scripts]
        simplevideocut=simplevideocutter.cli:entry
    '''
)
