from setuptools import setup

setup(
    name='pytest_demo',
    version='0.0.1',
    description='Pytest demo tests',
    author='Sam',
    packages=['test'],  # Use the actual directory name containing your package
    install_requires=[
        'requests', 'responses',
        'jsonpath-rw', 'pytest', 'jsonpath-ng', 'jsonpath_rw_ext', 'requests-toolbelt', 'pytest-html', 'pytest-messenger', 'python-dateutil', 'Faker',
    ]
)