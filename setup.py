from setuptools import setup, find_packages

project_url = 'https://github.com/LudwigCRON/sphinx-pywave'

requires = ['Sphinx>=1.8']

setup(
    name='sphinxcontrib-pywaveform',
    use_scm_version={
        "relative_to": __file__,
        "write_to": "sphinxcontrib/version.py",
    },
    url=project_url,
    license='MIT license',
    author='Ludwig CRON',
    author_email='ludwig.cron@gmail.com',
    description='A sphinx extension that allows generating pywave diagrams based on their textual representation',
    long_description=open("README.rst").read(),
    zip_safe=False,
    classifiers=[],
    platforms='any',
    packages=find_packages(exclude=['example']),
    include_package_data=True,
    install_requires=requires,
    py_modules=["pywaveform"],
    python_requires='>=3.5',
    setup_requires=[
        'setuptools_scm',
    ],
    namespace_packages=['sphinxcontrib'],
    keywords = ['sphinx', 'pywaveform', 'documentation'],
)
