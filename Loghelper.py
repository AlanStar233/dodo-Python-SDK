import os
import logging

# log 输出
file_path = os.path.dirname(os.path.realpath(__file__)) + "/config/logging.ini"
if os.path.exists(file_path):
    import logging.config

    logging.config.fileConfig(file_path)
    log = logging.getLogger("bili_DODO_bot")
else:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%dT%H:%M:%S')
    log = logger = logging