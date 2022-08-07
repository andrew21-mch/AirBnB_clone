from . import base_model
from .engine.file_storage import FileStorage

all = [base_model.BaseModel]

storage = FileStorage()
storage.reload()
