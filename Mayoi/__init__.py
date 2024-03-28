
__all__ = ['app']

from .config import Strings
from .Helpers.MongoDB import *
from .Helpers.TelegramTools import *

from os.path import dirname, basename, isfile, join
import glob
from importlib import import_module

from pyrogram import Client

app = Client(
    "mayoi",
    api_id = API_ID,
    api_hash = "API_HASH",
    bot_token="BOT_TOKEN"
)

files = glob.glob(join(join(dirname(__file__),'Handlers'),'*py'))
plugins = [basename(f)[:-3] for f in files if isfile(f) and not f.endswith('__init__.py')]

for plug in plugins:
    import_module('Mayoi.Handlers.'+plug)
