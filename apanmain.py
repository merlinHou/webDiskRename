# encoding:utf-8

from meijuTiantang import gainSeason

if __name__ == '__main__':
    get_ed2k_url = gainSeason()
    authorization = ''
    x_device_id = ''
    x_signature = ''
    headers = {'authorization': authorization,
               'x-canary': 'client=web,app=adrive,version=v3.17.0',
               'x-device-id': x_device_id,
               'x-signature': x_signature,
               }
    drive_id = ''
    parent_file_id = ''
    get_season_url = get_ed2k_url.apLister(drive_id, parent_file_id, headers)
    print(get_season_url)
    get_season_data = eval(get_season_url)['items']
    print(get_season_data)
    for season_data in get_season_data:
        # 目录id
        file_id = season_data['file_id']
        # 文件名
        name = season_data['name']
        # 文件后缀
        file_extension = season_data['file_extension']
        # 你要替换的名称
        new_name = name.replace(file_extension)+'.'+file_extension
        print("file_id:" + file_id + ",new_name:" + new_name)
        # repack you file name
        post_value = get_ed2k_url.apRename(drive_id, file_id, new_name, headers)
        print(str(post_value))
