from setuptools import setup, find_packages


setup(name='mrtrix3',
      version='1.0.0',
      description='Python package to interface with MRtrix3 file formats.',
      url='https://github.com/DoctorAnonymous/mrtrix3-pyio.git',
      author='zcmscy',
      author_email='zcmscy@icloud.com',
      license='MPL',
      packages=find_packages(),
      install_requires=['numpy'],
      zip_safe=False
      )
