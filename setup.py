from distutils.core import setup, Extension
import numpy

setup(
    name = "Bloch Simulator Library",
    version = "2.0",
    description = "Bloch Simulator and helper modules. Originally written by Brian Hargreaves and Mikki Lustig in Matlab.",
    author = "Niraj Amalkant",
    author_email = "namalkanti@gmail.com",
    url = "https://github.com/neji49/bloch-simulator-python",
    packages = ["bloch"],
    ext_modules=[Extension("bloch.bloch_simulator", ["bloch/bloch_simulator.c"])],
    include_dirs=[numpy.get_include()],
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
    ],
)
