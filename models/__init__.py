#!/usr/bin/python3
"""this will initialise the package"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
