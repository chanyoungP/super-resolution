from enum import Enum

class UpscaleErrorCode(Enum):
    NonTokenError = {
    "code": 401, # 아는 에러 
    "message": "Failed to connect. Contact service administrator.",
    "log": "Upscale API request error with non token. Please purchase token."
    }
    APIError = {
        "code": 500, #서버 에러 모르는 에러
        "message": "Failed to request. Contact service administrator.",
        "log": "API Error. Please check api."
    }
    FileNotFoundError = {
        "code": 404, #서버 에러 모르는 에러
        "message": "Failed to upload image. try again.",
        "log": "Wrong image path, Please check the input image path"
    }