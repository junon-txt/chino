from setuptools import setup

setup(
    name='path_rewriter',
    version='0.1',
    py_modules=['plugin'],
    install_requires=[
        'mkdocs',
    ],
    entry_points={
        'mkdocs.plugins': [
            'path_rewriter = plugin:PathRewriterPlugin',
        ],
    },
)
