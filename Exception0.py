#Exception handeling
#scenario where finally won't execute
import os
try:
    print("Try")
    os._exit(0)
except ValueError:
    print("Except")
finally:
    print("Fianlly")
