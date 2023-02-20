# encoding:utf-8
import requests
import json

from number import numto


class gainSeason:
    def __init__(self):
        self.qukpanList = 'https://drive.quark.cn/1/clouddrive/file/sort?pr=ucpro&fr=pc&pdir_fid={0}&_page={1}&_size={2}&_fetch_total=1&_fetch_sub_dirs=0&_sort=file_type:asc,file_name:asc'
        self.qukpanRename = 'https://drive.quark.cn/1/clouddrive/file/rename?pr=ucpro&fr=pc'
        self.baiduList = 'https://pan.baidu.com/api/list?clienttype=0&app_id={0}&web=1&dp-logid={1}&order=size&desc=1&dir={2}&num={3}&page={4}'
        self.baiduRename = 'https://pan.baidu.com/api/filemanager?async=2&onnest=fail&opera=rename&bdstoken={0}&clienttype=0&app_id={1}&web=1&dp-logid={2}'
        self.alilist = 'https://api.aliyundrive.com/adrive/v3/file/list?jsonmask=next_marker,items(name,file_id,drive_id)'
        self.aliRename = 'https://api.aliyundrive.com/v3/file/update'
        self.xlpanList = 'https://api-pan.xunlei.com/drive/v1/files?parent_id={0}'
        self.xunleiRename = 'https://api-pan.xunlei.com/drive/v1/files/{0}'

    def getQpList(self, cookies, pdir_fid, page, size):
        host = self.qukpanList.format(pdir_fid, page, size)
        response = requests.get(host, cookies=cookies)
        if response:
            return response.json()

    def postQpRename(self, cookies1, fid, file_name):
        host = self.qukpanRename
        data1 = {'fid': str(fid), 'file_name': str(file_name)}
        data2 = json.dumps(data1)
        headers = {'content-Type': 'application/json', }
        response = requests.request('post', host, data=data2, cookies=cookies1, headers=headers)
        if response:
            return response.text

    # app_id = {0} & web = 1 & dp - logid = {1} & order = size & desc = 1 & dir = {2} & num = {3} & page = {4}
    def bdList(self, cookies, app_id, dp_log_id, dir_path, num, page):
        host = self.baiduList.format(app_id, dp_log_id, dir_path, num, page)
        response = requests.get(host, cookies=cookies)
        if response:
            return response.json()

    # bdstoken = {0} & clienttype = 0 & app_id = {1} & web = 1 & dp - logid = {2}
    def bdRename(self, cookies, bdstoken, app_id, dp_log_id, fid, file_path, new_name):
        host = self.baiduRename.format(str(bdstoken), str(app_id), str(dp_log_id))
        data1 = 'filelist=[{"id":' + str(fid) + ',"path":"' + file_path + '","newname":"' + new_name + '"}]'
        headers = {'Content-Type': 'text/plain',
                   'Accept': 'application/json, text/plain, */*',
                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
        response = requests.request('post', host, data=data1.encode('utf-8'), headers=headers, cookies=cookies)
        if response:
            return response.text

    def apLister(self, drive_id, pfid, headers):
        host = self.alilist
        data1 = '{"drive_id": "' + drive_id + '","parent_file_id": "' + pfid + '"}'
        response = requests.request('post', host, data=data1.encode('utf-8'), headers=headers)
        if response:
            return response.text

    def apRename(self, drive_id, fid, name, headers):
        host = self.aliRename
        data1 = '{"drive_id": "' + drive_id + '","file_id": "' + fid + '","name":"' + str(
            name) + '","check_name_mode":"refuse"}'
        response = requests.request('post', host, data=data1.encode('utf-8'), headers=headers)
        if response:
            return response.text

    def getxlList(self, parent_id, authorization, token, x_device_id):
        host = self.xlpanList.format(str(parent_id))
        headers = {
            'authorization': authorization,
            'x-captcha-token': token,
            'x-device-id': x_device_id
        }
        response = requests.request('get', host, headers=headers)
        if response:
            return response.json()

    def xlRename(self, fid, name, authorization, token, x_device_id):
        host = self.xunleiRename.format(str(fid))
        headers = {
            'authorization': authorization,
            'x-captcha-token': token,
            'x-device-id': x_device_id
        }
        data1 = '{"name":"' + str(name) + '","space":""}'
        response = requests.request('patch', host, data=data1.encode('utf-8'), headers=headers)
        if response:
            return response.text

    def cnToNum(self, fname_num):
        cn_to_num = numto()
        return cn_to_num.forward_cn2an_one(fname_num)
