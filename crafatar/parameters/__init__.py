import crafatar.error


class Default:
    """
    Class used to select which model show if player has no skin
    """

    @property
    def default(self):
        """
        Returns the argument representing a url containing a image to be used as a model
        :return: "default"
        """
        return "default"

    @property
    def steve(self):
        """
        Returns the argument representing the Steve model
        :return: "MHF_Steve"
        """
        return "MHF_Steve"

    @property
    def alex(self):
        """
        Returns the argument representing the Alex model
        :return: "MHF_Alex"
        """
        return "MHF_Alex"

    @staticmethod
    def uuid(uuid: str):
        """
        Returns the argument representing a custom minecraft user model
        :param uuid: The uuid of the minecraft player to retrieve the model
        :return: uuid
        """
        return uuid

    @staticmethod
    def custom(url: str):
        """
        Returns the argument representing a url containing a image to be used as a model
        :param url: The url of a picture to retrieve the model
        :return: url
        """
        return url


class Overlay:
    """
    Class used to define if multi-layered skins should be rendered as multi-layered or single-layered
    """

    @property
    def false(self):
        return "false"

    @property
    def true(self):
        return "true"


def scale(scalenum: int):
    """
    Function used to define the scale factor for renders
    :param scalenum: An integer between 1 and 512
    """
    if scalenum < 0 or scalenum > 512:
        raise crafatar.error.ArgumentError("«scale» argument only accepts integers between 1 and 512")
    return scalenum


def size(sizenum: int):
    """
    Function used to define the size for avatars in pixels
    :param sizenum: An integer between 1 and 10
    """
    if sizenum < 0 or sizenum > 512:
        raise crafatar.error.ArgumentError("«size» argument only accepts integers between 1 and 512")
    return sizenum
