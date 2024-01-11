import os
import unittest
import appbuilder
import json


class TestRagBaiduSearch(unittest.TestCase):

    def setUp(self):
        """
        return rag_with_baidu_search class
        """
        # 设置环境变量和初始化TestMRCComponent实例
        self.model_name = "eb-turbo-appbuilder"
        self.rag_with_baidu_search = appbuilder.RAGWithBaiduSearch(model=self.model_name)

    def test_rag_with_baidu_search(self):
        msg = "残疾人怎么办相关证件"
        msg = appbuilder.Message(msg)
        is_stream = False
        instruction = "你是问答助手，在回答问题前需要加上“很高兴为您解答："
        instruction = appbuilder.Message(instruction)
        answer = self.rag_with_baidu_search(msg, reject=True, clarify=True, highlight=True,
                                            friendly=True, cite=True, temperature=0.5, stream=is_stream,
                                            instruction=instruction)
        self.assertIsNotNone(answer)
        print(answer.extra)
        if not is_stream:
            self.assertIsNotNone(answer)
        else:
            for a in answer.content:
                self.assertIsNotNone(a)
            self.assertIsNotNone(answer)

    def test_rag_with_baidu_search_with_none_inst(self):
        msg = "残疾人怎么办相关证件"
        msg = appbuilder.Message(msg)
        is_stream = False
        instruction = None
        answer = self.rag_with_baidu_search(msg, reject=True, clarify=True, highlight=True,
                                            friendly=True, cite=True, temperature=0.5, top_p=0.1, stream=is_stream,
                                            instruction=instruction)
        self.assertIsNotNone(answer)
        print(answer.extra)
        if not is_stream:
            self.assertIsNotNone(answer)
        else:
            for a in answer.content:
                self.assertIsNotNone(a)
            self.assertIsNotNone(answer)
