import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQB36lj1WeG1yq6TLxqlkxEn7l6w64Q-boQdybe8oyB5sQO_1vDOE8neB_GkxFLmYHzQHpc8DFcclMOx6YSs5I_dmFGF5aFtPXGCgMU4ZsXNU9aLq2XOb8KnskpDcuNti_9r0RiGYt_oWS_qsDhKTBDNlJVHbv77eZbal5b-PZUm47S-oHXAfoSoQTgnL0-hUNbQkB5P-I6_IUFuzFVQLK59IV0H8nlfnOS1eypQzkLssPpZlsiMjeFkRkhhiEURbT4yqbPs2KsvrzWfwev2wGL_stM2aEZUyVbpULg4O5WgZBD_5ZkvB3DgIiYl-1QhJNN72UcIzdKJHlD08khHJLzDAAAAATs5VogA")
BOT_TOKEN = getenv("BOT_TOKEN", "5562051847:AAFqZo85Kovmx7L2oI9gOwJFcWVZCjP--dA")
BOT_NAME = getenv("BOT_NAME", "Luksmusicrobot")
API_ID = int(getenv("API_ID", 16715726 ))
API_HASH = getenv("API_HASH", "46b4f2199cdf4aa6c95e82aecc412837")
OWNER_NAME = getenv("OWNER_NAME", "ismayilzadevuqar")
ALIVE_NAME = getenv("ALIVE_NAME", "ismayilzadevuqar")
BOT_USERNAME = getenv("BOT_USERNAME", "LuksMusicRoBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "LuksMusicAsistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "NeonSUP")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "LuksProject")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5573868756").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/e184200a18fd3fcd015a2.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "540000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/XTQ067/musiqisnactus")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/e184200a18fd3fcd015a2.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/e184200a18fd3fcd015a2.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/e184200a18fd3fcd015a2.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/e184200a18fd3fcd015a2.jpg")
