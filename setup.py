import os

try:
    from setuptools import setup
    from pip.req import parse_requirements
    from pip.download import PipSession
except ImportError:
    raise ImportError(
        "Please upgrade `setuptools` to the newest version via: "
        "`pip install -U setuptools`"
    )

def read_requirements():
    '''parses requirements from requirements.txt'''
    reqs_path = os.path.join(__location__, 'requirements.txt')
    install_reqs = parse_requirements(reqs_path, session=PipSession())
    reqs = [str(ir.req) for ir in install_reqs]
    return reqs

def readme_handler(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as fh:
        readme = fh.read()
    return readme

if __name__ == '__main__':
      required = [str(ir.req) for ir in parse_requirements("requirements.txt")]

setup(name='lantern',
      version='1.0.0',
      description='A library for communicating with Yongnuo LED video lights.',
      url='https://github.com/kenkeiter/lantern',
      author='Ken Keiter',
      author_email='ken@kenkeiter.com',
      license='MIT',
      packages=['lantern'],
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose'],
      install_requires=required)