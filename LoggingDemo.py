#program to create log file
import logging as lg
lg.basicConfig(filename="Logging10.txt",level=lg.DEBUG)
print("Python logging demo")
lg.warning("Warnings")
lg.debug("Debugging")
lg.error("Errors")
lg.info("Information")
lg.critical("Critical Situation")
