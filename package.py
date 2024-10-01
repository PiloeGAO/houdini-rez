name = "houdini"

version = "20.5.332"

authors = [
    "SifeFX"
]

description = \
    """
    Houdini is built from the ground up to be a procedural system that empowers artists to work freely, create multiple iterations and rapidly share workflows with colleagues.
    """

tools = [
    "houdini",
    "husk",
    "hython",
]

uuid = "sidefx.houdini"

build_command = ""

def commands():
    alias("houdini", '\"C:\\PROGRA~1\\Side Effects Software\\Houdini 20.5.332\\bin\\houdini.exe\"')
    alias("husk", '\"C:\\PROGRA~1\\Side Effects Software\\Houdini 20.5.332\\bin\\husk.exe\"')
    alias("hython", '\"C:\\PROGRA~1\\Side Effects Software\\Houdini 20.5.332\\bin\\hython.exe\"')