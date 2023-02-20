python3.9

<h1>1.apanmain--操作阿里云盘</h1>
<h2>一、获取信息参数说明：</h2>
<h4>头文参数信息：</h4>
浏览器打开开发者工具在网络中找到"list?jsonmask=next_marker"请求

在请求的request headers中找到一下参数，填入

    authorization = ''
    x_device_id = ''
    x_signature = ''

<h2>二、修名请求参数说明：</h2>
<h4>请求参数：</h4>
这里只需要两个就可以查询，一个是设备id，一个是目录的id <br>
设备id标识的设备本身，统一太机器不会改变，目录的id在浏览器的URL上可以找到就是folder后面的信息 <br>
https://www.aliyundrive.com/drive/folder/***

    drive_id = ''
    parent_file_id = ''

<h4>批量修改文件夹中文件名：</h4>

name = season_data['name'] #用来获取原名称 <br>
new_name = name.replace('',''') #这里根据需要设定一个新的名称，注意如果保留源文件名的后缀 <br>

----------

<h1>2.bdpanmain--操作百度云盘</h1>
<h2>一、获取信息参数说明：</h2>
<h4>头文参数信息：</h4>
浏览器打开开发者工具在网络中找到"list?clienttype"请求

在请求的request headers中找到cookie填入b_cookie.txt
在请求参数中找到
   
    app_id = '' 设备的id，填写一次就行
    dp_log_id = '' 填写一个基本不用改
    dir_path = '' 文件目录，在url有


<h4>批量修改文件夹中文件名：</h4>

old_name = season_data['server_filename'] #用来获取原名称 <br>
new_name = old_name.replace('',''') #这里根据需要设定一个新的名称，注意如果保留源文件名的后缀 <br>

--------

<h1>3.qpanmain--操作百度云盘</h1>
<h2>一、获取信息参数说明：</h2>
<h4>头文参数信息：</h4>
浏览器打开开发者工具在网络中找到"/file/sort?pr=ucpro"请求

在请求的request headers中找到cookie填入q_cookie
在请求参数中找到
   
     pdir_fid = '' 文件目录的id，记住主目录即可，后面检索会打印出对应目录的id


<h4>批量修改文件夹中文件名：</h4>

file_name = cm_list['file_name'] #用来获取原名称 <br>
new_name = file_name.replace('',''') #这里根据需要设定一个新的名称，注意如果保留源文件名的后缀 <br>

----

<h1>4.xlpanmain--操作百度云盘</h1>
<h2>一、获取信息参数说明：</h2>
<h4>头文参数信息：</h4>
浏览器打开开发者工具在网络中找到"/file/sort?pr=ucpro"请求

在请求的request headers中找到cookie填入q_cookie
在请求参数中找到
   
     pdir_fid = '' 文件目录的id，记住主目录即可，后面检索会打印出对应目录的id


<h4>批量修改文件夹中文件名：</h4>

file_name = cm_list['file_name'] #用来获取原名称 <br>
new_name = file_name.replace('',''') #这里根据需要设定一个新的名称，注意如果保留源文件名的后缀 <br>
