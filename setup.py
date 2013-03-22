from setuptools import setup, find_packages

setup(
    name = "freeze",
    version = "0.1",
    packages = find_packages(),

    install_requires = ['six'],

    author = "Jean-Louis Fuchs",
    author_email = "ganwell@fangorn.ch",
    description = "Freeze - hash / sort / compare / diff anything\n\n"
                  "Freeze the state of data-structures and objects for "
                  "data-analysis or testing (diffing data-structures).",
    license = "Modified BSD",
    keywords = "freeze state hash sort compare unittest",
    url = "https://github.com/adfinis-sygroup/freeze",
)
