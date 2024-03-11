from enum import Enum

class LoadStatus(Enum):
    PENDING = 'PENDING'
    ERROR  = 'ERROR'
    CURRENT = 'CURRENT'
    OUTDATED = 'OUTDATED'
