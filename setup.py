from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension('blubble_sort', ['Blubble-Sort/blubble_sort.cpp'], include_dirs=[pybind11.get_include()]),
    Extension('quick_sort', ['Quick-Sort-quick_sort.cpp'], include_dirs=[pybind11.get_include()])
]

setup(
    name='projeto_algoritmos',
    ext_modules=ext_modules
)