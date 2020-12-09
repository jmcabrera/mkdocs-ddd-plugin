import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mkdocs-ddd-plugin",
    version="0.0.1.b1",
    author="Juan Manuel CABRERA",
    author_email="juanma.cabrera@gmail.com",
    description="A plugin to link notions simply",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/slowcoding/mkdocs-ddd-plugin",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Environment :: Plugins",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    python_requires='>=3.6',
    entry_points={
        'mkdocs.plugins': ['ddd = slowcoding.ddd.plugin:DDDPlugin']
    }
)
