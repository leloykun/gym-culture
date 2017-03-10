from setuptools import setup

setup(name='gym_culture',
      author='Franz Louis Cesista',
      packages=['gym_culture', 'gym_culture.envs'],
      package_data = {
          "gym_culture.envs": ["assets/*.txt"]
      },
      install_requires=['gym']  # dependencies
)
