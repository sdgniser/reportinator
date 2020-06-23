import atexit
from setuptools import setup
from setuptools.command.install import install

def _post_install():
    import reportinator.reconfig
    reportinator.reconfig.main(first_install=True)
    print('POST INSTALL')

class new_install(install):
    def __init__(self, *args, **kwargs):
        super(new_install, self).__init__(*args, **kwargs)
        atexit.register(_post_install)

setup(name='reportinator',
      version='1.0',
      description='Make LaTeX Reports from Markdown',
      url='http://github.com/sdgniser/reportinator',
      author='Spandan Anupam, Vishnu Namboodiri K S',
      author_email='spandan.anupam@niser.ac.in, vishnu.nks@niser.ac.in',
      license='GPL v3.0',
      packages=['reportinator'],
      cmdclass={
          'install': new_install,
          },
      package_data={
          "reportinator": ["layouts/*.cls"],
          "reportinator": ["scripts/make-my-report.py"],
          },
      entry_points={
          "console_scripts": [
              "reportinator = reportinator.main:main",
              ]
          },
      install_requires=[
          'matplotlib',
          'numpy',
          'ruamel.yaml',
          'doi2bib',
          'pandas',
          'pyyaml',
          'configurator',
          ],
      include_package_data=True,
      zip_safe=False)

