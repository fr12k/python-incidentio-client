from enum import Enum


class CustomFieldV1ResponseBodyRequiredV2(str, Enum):
    NEVER = "never"
    BEFORE_RESOLUTION = "before_resolution"
    ALWAYS = "always"

    def __str__(self) -> str:
        return str(self.value)