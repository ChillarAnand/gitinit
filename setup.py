from distutils.core import setup

files = [
    'gitinit/gitignores/*'
]
setup(
    name='gitinit',
    packages=['gitinit'],
    version='1.0.0',
    description='Initiates git with gitignore for provided language',
    author='Bibhas C Debnath',
    author_email="me@bibhas.in",
    url="https://github.com/iambibhas/gitinit",
    package_data={'gitinit': files},
    scripts=["gitinit", ],
)
