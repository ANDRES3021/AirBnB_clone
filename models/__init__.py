#!/usr/bin/python3
"""
Este es el módulo de inicio del modelo
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
