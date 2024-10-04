"""
Script de Configuração do Pacote Image Processing

Este script configura o pacote 'image_processing' para distribuição.
Ele utiliza setuptools para definir os metadados do pacote e suas dependências.

Dependências:
    - setuptools

O script lê o arquivo README.md para a descrição longa do pacote e
o arquivo requirements.txt para as dependências do pacote.
"""

from setuptools import setup, find_packages


def read_file(filename: str) -> str:
    """
    Lê o conteúdo de um arquivo e retorna como uma string.

    Args:
        filename (str): O nome do arquivo a ser lido.

    Returns:
        str: O conteúdo do arquivo.

    Raises:
        FileNotFoundError: Se o arquivo especificado não for encontrado.
    """
    with open(filename, "r") as file:
        return file.read()


# Lê a descrição longa do README.md
page_description = read_file("README.md")

# Lê as dependências do requirements.txt
requirements = read_file("requirements.txt").splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Adriano Santos",
    author_email="adrianosantos.git@gmail.com",
    description="Image Processing Package using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Adriano1976/image-processing-package.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8'
)
