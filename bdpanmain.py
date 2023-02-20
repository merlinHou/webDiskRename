# encoding:utf-8

from meijuTiantang import gainSeason

if __name__ == '__main__':
    get_ed2k_url = gainSeason()
    f = open(r'b_cookie.txt', 'r')  # 打开所保存的cookies内容文件
    cookies = {}  # 初始化cookies字典变量
    for line in f.read().split(';'):  # 按照字符：进行划分读取
        # 其设置为1就会把字符串拆分成2份
        name, value = line.strip().split('=', 1)
        cookies[name] = value  # 为字典cookies添加内容
    # app_id, dp_logid, bdpath, num, page
    app_id = ''
    dp_log_id = ''
    dir_path = ''
    num = '100'
    page = '1'
    get_season_url = get_ed2k_url.bdList(cookies, app_id, dp_log_id, dir_path, num, page)
    get_season_data = get_season_url['list']
    get_list = str(get_season_data)[:-1]
    get_list2 = str(get_list)[1:]
    get_json = eval(get_list2)
    lid = get_season_url['request_id'] + 1000
    for season_data in get_json:
        fpath = season_data['path']
        fsid = season_data['fs_id']
        old_name = season_data['server_filename']
        new_name = old_name
        print('fs_id:' + str(fsid) + ';new_name:' + new_name)
        get_value = get_ed2k_url.bdRename(cookies, fsid, fpath, new_name, lid)
        print('post_value:' + str(get_value))
        post_json = eval(get_value)
        lid = post_json['request_id'] + 1000
