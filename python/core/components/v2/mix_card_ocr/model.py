# Copyright (c) 2023 Baidu, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""身份证混贴数据类"""
import proto
from typing import List, Optional
from pydantic import BaseModel, Field


class MixCardOCRRequest(BaseModel):
    """ 身份证混贴识别
    属性:
        image (str):
            可选。图像内容的base64编码
        url (str):
            可选，图像的URL地址，经过base64编码
            图像大小必须小于4MB，图像的最短边长大于15像素，最长边长大于4096像素
        detect_risk（str）:
            是否检测风险（身份证复印件、临时身份证、身份证翻拍、修改过的身份证）类型，可选值是"true"或“false”
        detect_quality（str）:
            是否开启身份证质量类型(边框/四角不完整、头像或关键字段被遮挡/马赛克)检测功能,可选值是"true"或“false”
        detect_photo（str）:
            是否检测头像内容，默认不检测,可选值是"true"或“false”
        detect_card（str）:
            是否检测身份证并进行裁剪,"true"或“false”
    """
    image: str = Field(default="", description="图像内容的base64编码")
    url: str = Field(default="", description="图像的URL地址，经过base64编码")
    detect_risk: str = Field(
        default="", description="是否检测风险（身份证复印件、临时身份证、身份证翻拍、修改过的身份证）类型，可选值是\"true\"或“false\"")
    detect_quality: str = Field(default="", description="是否开启身份证质量类型(边框"
                                "四角不完整、头像或关键字段被遮挡/马赛克)检测功能,可选值是\"true\"或“false\"")
    detect_photo: str = Field(
        default="", description="是否检测头像内容，默认不检测,可选值是\"true\"或“false\"")
    detect_card: str = Field(
        default="", description="是否检测身份证并进行裁剪,\"true\"或“false\"")


class MixCardOCRLocation(BaseModel):
    """ 位置信息.

        属性:
            left (int): 表示定位位置的长方形左上顶点的水平坐标
            top (int): 表示定位位置的长方形左上顶点的垂直坐标
            width (int): 表示定位位置的长方形的宽度
            height (int): 表示定位位置的长方形的高度
         """
    left: int = Field(default=0, description="表示定位位置的长方形左上顶点的水平坐标")
    top: int = Field(default=0, description="表示定位位置的长方形左上顶点的垂直坐标")
    width: int = Field(default=0, description="表示定位位置的长方形的宽度")
    height: int = Field(default=0, description="表示定位位置的长方形的高度")


class MixCardOCRInfo(BaseModel):
    """ 身份证混贴手识别结果

        属性:
            card_location (MixCardLocation): 身份证的位置信息（坐标0点为左上角）
            card_type（str）: idcard_front(头像面)、idcard_back（国徽面）
            image_status (str): normal-识别正常、 non_idcard-上传的图片中不包含身份证 、blurred-身份证模糊
            other_type_card-其他类型证照 、over_exposure-身份证关键字段反光或过曝 、over_dark-身份证欠曝（亮度过低）
            unknown-未知状态
     """
    card_location: Optional[MixCardOCRLocation] = Field(
        default=None, description="身份证的位置信息（坐标0点为左上角）")
    card_type: str = Field(
        default="", description="idcard_front(头像面)、idcard_back（国徽面）")
    image_status: str = Field(
        default="", description="normal-识别正常、 non_idcard-上传的图片中不包含身份证 、blurred-身份证模糊")
    direction: int = Field(default=0, description="身份证正反面，0-正面，1-背面")
    idcard_number_type: int = Field(
        default=0, description="身份证号类型，0-普通身份证号码，1-港澳台身份证号码，2-护照号码")


class MixCardOCRResult(BaseModel):
    """身份证混贴别结果

        属性:
            words (str): 文本信息
            location（MixCardOCRLocation）: 位置信息
    """
    words: str = Field(default="", description="文本信息")
    location: Optional[MixCardOCRLocation] = Field(
        default=None, description="位置信息")


class MixOCRCardInfoResult(BaseModel):
    """身份证混贴信息

        属性:
            card_result (Map[str,MixCardOCRResult]): 身份证字段信息
            card_info（MixCardOCRInfo）: 身份证信息
    """
    card_result: Optional[dict[str, MixCardOCRResult]] = Field(
        default=None, description="身份证字段信息")
    card_info: Optional[MixCardOCRInfo] = Field(
        default=None, description="身份证信息")


class MixCardOCRResponse(BaseModel):
    """身份证混贴识别结果

        属性:
            request_id(str): 请求ID
            log_id (int): 用于问题跟踪的唯一日志ID
            words_result (List[MixOCRCardInfoResult]): 识别结果列表
            direction (int): 当detect_direction=true返回改字段，1（未定义）、
            0（正向）、1（逆时针90度）、2（逆时针180度）、3（逆时针270度）
            pdf_file_size (str): 输入PDF文件的总页数。当pdf_file参数有效时返回
    """
    request_id: str = Field(default="", description="请求ID")
    log_id: int = Field(default=0, description="用于问题跟踪的唯一日志ID")
    words_result: Optional[list[MixOCRCardInfoResult]
                           ] = Field(default=None, description="识别结果列表")
    direction: int = Field(
        default=0, description="当detect_direction=true返回改字段，1（未定义）、0（正向）、1（逆时针90度）、2（逆时针180度）、3（逆时针270度）")


class MixCardOCRInMsg(BaseModel):
    """ 手写体文字识别输入消息

        属性:
            raw_image(bytes): 图像原始内容
            url(str): 图像下载链接
    """
    raw_image: bytes = b''  # 原始图片byte数组
    url: str = ""  # 图片可下载链接


class MixCardPosition(BaseModel):
    """位置信息

       属性：
            left (int): 表示定位位置的长方形左上顶点的水平坐标
            top (int): 表示定位位置的长方形左上顶点的垂直坐标
            width (int): 表示定位位置的长方形的宽度
            height (int): 表示定位位置的长方形的高度
    """

    left: int
    top: int
    width: int
    height: int


class MixCardField(BaseModel):
    """ 字段信息

        属性：
            key（str): 字段名
            value (str): 字段值
            position(MixCardPosition): 字段位置信息
      """

    key: str
    value: str
    position: Optional[MixCardPosition] = None


class MixCardContent(BaseModel):
    """正/反识别结果

        属性：
            fields(List[MixCardField]):字段列表
            position(MixCardPosition): 正/反面在图像中的位置信息
    """
    fields: List[MixCardField] = list()
    position: MixCardPosition = None


class MixCardOCROutMsg(BaseModel):
    """身份证混贴识别结果

        属性：
            front（MixCardField）: 人像面信息
            back(MixCardField): 国徽面信息
            direction(int): 图像旋转角度，0（正向），- 1（逆时针90度），- 2（逆时针180度），- 3（逆时针270度）
    """
    front: MixCardContent = MixCardContent()
    back: MixCardContent = MixCardContent()
    direction: int = 0
