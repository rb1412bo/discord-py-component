from setuptools import setup, find_packages

setup(
    name="discord-py-components",
    version="0.1.0",
    author="Dein Name",
    author_email="deine@email.de",
    description="discord.py extension adding full Components V2 support",
    url="https://github.com/DEIN_USERNAME/discord-py-components",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Framework :: Discord :: discord.py",
        "License :: OSI Approved :: MIT License",
    ],
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=["discord.py>=2.0"],
    python_requires=">=3.8",
    include_package_data=True,
    zip_safe=False
)
