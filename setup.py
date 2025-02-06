from setuptools import setup, find_packages

setup(
    name="photo_analyzer",
    version="0.1.1",
    description="A tool for analyzing and organizing photos",
    author="RM Lombard",
    author_email="rmlombard@icloud.com",
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    python_requires=">=3.13",
    install_requires=[
    ],
    extras_require={
        "dev": [
            "pytest>=8.3.4",
            "pytest-cov",
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.13",
    ],
)

