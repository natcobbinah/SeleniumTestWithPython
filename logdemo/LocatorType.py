from enum import Enum

class LocatorType(Enum):
    CLASS_NAME = "CLASS_NAME",
    CSS_SELECTOR = "CSS_SELECTOR",
    ID = "ID",
    NAME = "NAME",
    LINK_TEXT = "LINK_TEXT",
    PARTIAL_LINK_TEXT = "PARTIAL_LINK_TEXT",
    TAG_NAME = "TAG_NAME",
    XPATH = "XPATH"
