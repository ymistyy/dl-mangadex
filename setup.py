from setuptools import setup, find_packages

setup(
    name="dl-mangadex",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "mangadex-downloader"
    ],
    entry_points={
        "console_scripts": [
            "dl-mangadex=dl_mangadex.cli:main"
        ]
    },
    author="YourName",
    description="Interactive CLI wrapper for mangadex-downloader",
    python_requires=">=3.8",
)