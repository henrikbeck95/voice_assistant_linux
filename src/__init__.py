from pathlib import Path

CACHE_PATH = Path.home().joinpath('.cache', 'val')
CONFIG_PATH = Path.home().joinpath('.config', 'val','./src/settings.yml')

__version__ = '0.0.1'

if not CONFIG_PATH.exists():
    from shutil import copy
    import os

    dirname = Path(__file__).parent
    #src = dirname.joinpath('settings.yml')
    src = dirname.joinpath('./src/settings.yml')

    if not CONFIG_PATH.parent.exists():
        os.makedirs(CONFIG_PATH.parent)

    copy(src, CONFIG_PATH)