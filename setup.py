import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="creasepattern",
    version="0.0.7",
    author="Gerben Oolbekkink",
    author_email="g.j.w.oolbekkink@gmail.com",
    description="Origami Crease Pattern tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qurben/creasepattern",
    project_urls={
        "Bug Tracker": "https://github.com/qurben/creasepattern/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'crease=creasepattern:main',
        ]
    },
    install_requires=[
        "Pillow",
        "defusedxml"
    ]
)
