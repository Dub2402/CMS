from Source.Terminalyzer import Terminalyzer
from dublib.CLI.Templates import Clear

Clear()

try:
    Terminalyzer().Start()

except KeyboardInterrupt:
    Clear()
    exit(0)