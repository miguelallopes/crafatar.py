import requests, os, pathlib


# TODO Better Error Handling


# Response Class
class BaseResponse(object):
    def __init__(self, response: requests.Response):
        self.response = response

    @property
    def request_id(self):
        return self.response.headers["X-Request-ID"]

    @property
    def response_time(self):
        return self.response.headers["Response-Time"]

    @property
    def status_code(self):
        return self.response.status_code


class AvatarResponse(BaseResponse):
    @property
    def content(self):
        return self.response.content

    def save(self, filename="avatar", location=os.getcwd()):
        with open(pathlib.Path(location).joinpath(filename + ".png"), mode="wb+") as avatarfile:
            avatarfile.write(self.response.content)
            avatarfile.close()
        return True


class HeadRenderResponse(BaseResponse):
    @property
    def content(self):
        return self.response.content

    def save(self, filename="headrender", location=os.getcwd()):
        with open(pathlib.Path(location).joinpath(filename + ".png"), mode="wb+") as avatarfile:
            avatarfile.write(self.response.content)
            avatarfile.close()
        return True


class BodyRenderResponse(BaseResponse):
    @property
    def content(self):
        return self.response.content

    def save(self, filename="bodyrender", location=os.getcwd()):
        with open(pathlib.Path(location).joinpath(filename + ".png"), mode="wb+") as avatarfile:
            avatarfile.write(self.response.content)
            avatarfile.close()
        return True


class SkinResponse(BaseResponse):
    @property
    def content(self):
        return self.response.content

    def save(self, filename="skin", location=os.getcwd()):
        with open(pathlib.Path(location).joinpath(filename + ".png"), mode="wb+") as avatarfile:
            avatarfile.write(self.response.content)
            avatarfile.close()
        return True


class CapeResponse(BaseResponse):
    @property
    def content(self):
        return self.response.content

    def save(self, filename="cape", location=os.getcwd()):
        with open(pathlib.Path(location).joinpath(filename + ".png"), mode="wb+") as avatarfile:
            avatarfile.write(self.response.content)
            avatarfile.close()
        return True
