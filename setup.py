from setuptools import setup

setup(name='gym_culture',
      version='0.0.2.5',
      url='https://github.com/LE-LOY/gym-culture',
      author='Franz Louis Cesista',
      license='MIT',
      packages=['gym_culture', 'gym_culture.envs'],
      package_data = {
          "gym_culture.envs": ["assets/*.txt", "widgets/*.py"]
      },
      install_requires=['gym', 'pygame', 'numpy', 'matplotlib']  # dependencies
)
