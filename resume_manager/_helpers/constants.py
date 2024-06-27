from enum import StrEnum


class Environments(StrEnum):
    """Project Running Environments

    This class provides an enumeration of environments that project will run in.
    """

    DEVELOPMENT = "development"
    TEST = "test"
    PRODUCTION = "production"
    STAGING = "staging"
