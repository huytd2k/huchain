import subprocess


def start():
    commands = ["uvicorn", "pychain.server.main:app", "--reload"]
    subprocess.run(commands)
