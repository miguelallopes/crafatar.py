# Server Errors
class ServerError(BaseException):
    pass


# User Errors
class UserError(BaseException):
    pass


class MalformedUUIDError(UserError):
    """
    This class are used to raise UUID errors
    """
    pass


class ArgumentError(UserError):
    """
    This class are used to raise errors when arguments are not correct
    """
    pass


class CapeNotFoundError(ServerError):
    """
    This class are used to raise errors when player has no cape
    """
    pass
