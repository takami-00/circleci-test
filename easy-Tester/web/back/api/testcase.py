# coding: utf-8

import json
import os
import yaml
import inspect
import importlib
import glob

TEST_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../test/')

class TestCase:

    def on_get(self, req, resp):
        testcase_list = self.getTestCaseList(TEST_PATH + req.params['p'] + '/' + req.params['b'] + '/testcase/' + req.params['t'])

        resp.body = json.dumps(testcase_list)

        resp.append_header('Access-Control-Allow-Origin', req.get_header('Origin'))


    def getTestCaseList(self, branch_path):
        testcase_list = os.listdir(branch_path)
        testcase_list = [test for test in testcase_list if test != '.DS_Store']
        testcase_list = [os.path.splitext(test)[0] for test in testcase_list]
        return testcase_list