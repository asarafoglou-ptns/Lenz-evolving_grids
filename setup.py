import setuptools

setuptools.setup(
    name='evolving_grids',
    version='1.0',
    author='sarah_lenz',
    author_email='sarah.lenz@student.uva.nl',
    description='A Python package for playing Conway´s Game of Life',
    license='MIT',
    python_requires='>=3.8',
    install_requires=[
        'shiny==0.9.0',
        'htmltools==0.5.1',
        'uvicorn==0.29.0',
        'starlette==0.37.2'
    ],
    scripts=['app/run.py'],  # Include run.py as a script
    packages=setuptools.find_packages(),
    package_data={
        'app': ['static/*'],  # Include all files in the static folder
        '': ['requirements.txt']  # include requirements.txt at the root level
    },
    include_package_data=True,
)
