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
import os
import unittest
import appbuilder


class TestGeneralOCR(unittest.TestCase):
    def setUp(self):
        """
        设置环境变量。

        Args:
            None

        Returns:
            None.
        """
        self.general_ocr = appbuilder.GeneralOCR()

    def test_run_with_raw_image(self):
        """
        测试只使用有效图片进行单测

        Args:
            None

        Returns:
            None

        """
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, 'general_ocr_test.png')
        with open(file_path, 'rb') as img_file:
            raw_image = img_file.read()

        # Create message with raw_image
        message = appbuilder.Message(content={"raw_image": raw_image})

        # Recognize landmark
        output = self.general_ocr.run(message)

        # Assert output is not None
        self.assertIsNotNone(output)

    def test_run_with_no_image(self):
        """
        测试run函数在传入无效图像的情况下的行为。

        Args:
            None

        Returns:
            None

        """
        # create empty message
        message = appbuilder.Message(content={})

        # Assert ValueError is raised
        with self.assertRaises(ValueError):
            self.general_ocr.run(message)

    def test_run_with_timeout_and_retry(self):
        """
         测试run函数在传入timeout、retry参数

        Args:
            None

        Returns:
            None

        """
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, 'general_ocr_test.png')
        with open(file_path, 'rb') as img_file:
            raw_image = img_file.read()

        # Create message with raw_image
        message = appbuilder.Message(content={"raw_image": raw_image})

        # Recognize general_ocr with timeout and retry parameters
        output = self.general_ocr.run(message, timeout=5.0, retry=3)

        # Assert output is not None
        self.assertIsNotNone(output)

    def test_run_with_invalid_url(self):
        """
        测试run函数在传入无效URL的情况下的行为。

        Args:
            None

        Returns:
            None

        """
        url = "http://example.com/invalid_url.jpg"
        message = appbuilder.Message({"url": url})
        with self.assertRaises(appbuilder.AppBuilderServerException):
            self.general_ocr.run(message=message)

    def test_run_without_image_and_url(self):
        """
        测试run 函数在没有传入图像和URL的情况下的行为。

        Args:
            None

        Returns:
            None

        """
        message = appbuilder.Message({})
        with self.assertRaises(ValueError):
            self.general_ocr.run(message=message)


if __name__ == '__main__':
    unittest.main()
