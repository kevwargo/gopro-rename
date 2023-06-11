from setuptools import find_packages, setup

setup(
    name="gopro_rename",
    packages=find_packages(),
    python_requires=">=3",
    entry_points={
        "console_scripts": [
            "gopro-rename = gopro_rename:run",
        ],
    },
)
