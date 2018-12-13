
import setuptools

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setuptools.setup(
    name='flask-deploy',
    version='0.1',      
    description='A quick deploy script for productive flask app',
    url='https://github.com/Mon-ius/flask-deploy',
    author='Mon-ius',
    author_email='m1105930979@gmail.com',

    packages=setuptools.find_packages(),
    package_data={
        'flaskdeploy': ['data/*']
    },
    license='MIT',
    long_description=readme,
    long_description_content_type='text/markdown',
    entry_points={
    'console_scripts': [
        'flask-deploy = flaskdeploy.scripts.deploy:info',
        'fd gen = flaskdeploy.scripts.generation:cli',
        'fd deploy = flaskdeploy.scripts.deploy:cli',
    ],
    },
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Production/Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    platforms='linux',
)
