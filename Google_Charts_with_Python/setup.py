from setuptools import setup

setup(
    name="Google_Charts_with_Python",
    version="0.1",
    packages=["app"],
    entry_points={
        "console_scripts": [
            "my_script = Google_Charts_with_Python.__main__"
        ]
    },
)