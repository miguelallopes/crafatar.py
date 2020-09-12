import crafatar.error
import crafatar.objects
import crafatar.parameters

import requests

__author__ = "PWRScript"
__version__ = "1.0.0"


class CrafatarAPIWrapper(object):
    def __init__(self, base_api_url="https://crafatar.com"):
        self.__base_api_url = base_api_url

    def get_avatar(self, uuid: str, size=crafatar.parameters.size(160),
                   overlay=crafatar.parameters.Overlay.false, default=crafatar.parameters.Default.default):
        base_url = self.__base_api_url + f"/avatars/{uuid}"
        if size != crafatar.parameters.size(160):
            base_url = f"{base_url}?&size={size}"
        if overlay != crafatar.parameters.Overlay.false:
            base_url = f"{base_url}?&overlay={overlay}"
        if default != crafatar.parameters.Default.default:
            base_url = f"{base_url}?&default={default}"
        return crafatar.objects.AvatarResponse(requests.get(base_url))

    def get_head_render(self, uuid: str, scale=crafatar.parameters.scale(6),
                        overlay=crafatar.parameters.Overlay.false, default=crafatar.parameters.Default.default):
        base_url = self.__base_api_url + f"/renders/head/{uuid}"
        if scale != crafatar.parameters.scale(6):
            base_url = f"{base_url}?&size={scale}"
        if overlay != crafatar.parameters.Overlay.false:
            base_url = f"{base_url}?&overlay={overlay}"
        if default != crafatar.parameters.Default.default:
            base_url = f"{base_url}?&default={default}"
        return crafatar.objects.HeadRenderResponse(requests.get(base_url))

    def get_body_render(self, uuid: str, scale=crafatar.parameters.scale(6),
                        overlay=crafatar.parameters.Overlay.false, default=crafatar.parameters.Default.default):
        base_url = self.__base_api_url + f"/renders/body/{uuid}"
        if scale != crafatar.parameters.scale(6):
            base_url = f"{base_url}?&size={scale}"
        if overlay != crafatar.parameters.Overlay.false:
            base_url = f"{base_url}?&overlay={overlay}"
        if default != crafatar.parameters.Default.default:
            base_url = f"{base_url}?&default={default}"
        return crafatar.objects.BodyRenderResponse(requests.get(base_url))

    def get_skin(self, uuid: str, default=crafatar.parameters.Default.default):
        base_url = self.__base_api_url + f"/skins/{uuid}"
        if default != crafatar.parameters.Default.default:
            base_url = f"{base_url}?&default={default}"
        return crafatar.objects.SkinResponse(requests.get(base_url))

    def get_cape(self, uuid: str, default=crafatar.parameters.Default.default):
        base_url = self.__base_api_url + f"/capes/{uuid}"
        if default != crafatar.parameters.Default.default:
            base_url = f"{base_url}?&default={default}"
        return crafatar.objects.CapeResponse(requests.get(base_url))
