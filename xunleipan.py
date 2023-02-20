# encoding:utf-8

from meijuTiantang import gainSeason

if __name__ == '__main__':
    get_ed2k_url = gainSeason()
    authorization = ''
    token = ''
    parent_id = ''
    x_device_id = ''
    get_season_url = get_ed2k_url.getxlList(parent_id, authorization, token, x_device_id)
    print(get_season_url)
    get_season_data = get_season_url['files']
    for season_data in get_season_data:
        fid = season_data['id']
        name = season_data['name']
        new_name = name
        print('fid:' + fid + ',new_name:' + new_name)
        post_name = get_ed2k_url.xlRename(fid, name, authorization, token, x_device_id)
        print(post_name)
