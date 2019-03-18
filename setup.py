
import setuptools

with open('README.md', 'r') as f:
    readme = f.read()

setuptools.setup(
    name='flask-deploy',
    version='0.4.0',      
    description='A quick deploy script for productive flask app',
    url='https://github.com/Mon-ius/flask-deploy',
    author='Mon-ius',
    author_email='m1105930979@gmail.com',

    packages=setuptools.find_packages(),
    package_data={
        'flaskdeploy': ['data/*']
    },
    install_requires=[
        'click',
    ],
    license='MIT',
    long_description=readme,
    long_description_content_type='text/markdown',
    entry_points={
    'console_scripts': [
        'flask-deploy =flaskdeploy.scripts.core:cli',
        'fd = flaskdeploy.scripts.core:cli',
    ],
    },
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
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
