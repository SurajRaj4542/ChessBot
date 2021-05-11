
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
    api_id = 1639263,
    api_hash = "bb491a5c6b6ab5cd510325d474908d49",
    bot_token="1652690019:AAHontptuFFuolfhNPO91H8hws1s2bWmaDg"
)

files = glob.glob(join(join(dirname(__file__),'Handlers'),'*py'))
plugins = [basename(f)[:-3] for f in files if isfile(f) and not f.endswith('__init__.py')]

for plug in plugins:
    import_module('Mayoi.Handlers.'+plug)
