# encoding:utf-8

from meijuTiantang import gainSeason

if __name__ == '__main__':
    get_ed2k_url = gainSeason()
    f = open(r'q_cookie.txt', 'r')  # 打开所保存的cookies内容文件
    cookies = {}  # 初始化cookies字典变量
    for line in f.read().split(';'):  # 按照字符：进行划分读取
        # 其设置为1就会把字符串拆分成2份
        name, value = line.strip().split('=', 1)
        cookies[name] = value  # 为字典cookies添加内容
    pdir_fid = ''
    page = '1'
    size = '100'
    cm = get_ed2k_url.getQpList(cookies, pdir_fid, page, size)
    cm_data = cm['data']
    for cm_list in cm_data['list']:
        fid = cm_list['fid']
        file_name = cm_list['file_name']
        new_name = file_name
        print('fid:' + fid + ',' + 'new_name:' + new_name)
        post_value = get_ed2k_url.postQpRename(cookies, fid, new_name)
        print('post_value:' + str(post_value))
