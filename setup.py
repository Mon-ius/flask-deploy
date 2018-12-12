
import setuptools
setuptools.setup(
    name='flask-deploy',
    version='0.1',      
    description='A quick deploy script for flask app',
    url='https://github.com/Mon-ius/flask-deploy',
    author='Mon-ius',
    author_email='m1105930979@gmail.com',

    packages=setuptools.find_packages(),
    package_data={
        'flaskdeploy': ['utils/*']
    },
    license='MIT',
    long_description=open('README.md').read(),
    entry_points={
    'console_scripts': [
        'flask-gen = flaskdeploy.scripts.gen:cli',
        'flask-deploy = flaskdeploy.scripts.deploy:cli',
    ],
    },
    platforms='linux',
)
