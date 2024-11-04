import logging

from command import Command

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    cmd = Command()
    cmd.handle()
