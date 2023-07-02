import os

from dotenv import load_dotenv

if os.environ.get('DEBUG') == "True":
    print("logging test environment")
    load_dotenv(".env.test")
else:
    print("logging general environment")
    load_dotenv(".env")
