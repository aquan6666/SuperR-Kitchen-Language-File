# -*- coding: utf-8 -*-
# Translation by xiyan
# Date : 2019-02-04 New Year's Eve
# Happy Chinese New Year !
# Main Menu
title_main = "主菜单"
title_choose = "选择项目:"
title_delete = "删除项目:"
title_extract = "解压选项:"
menu_create = "创建新项目"
menu_choose = "选择不同项目"
menu_delete = "删除一个项目"
menu_extract = "解压新ROM"
menu_updates = "检查更新"
menu_misc = "Misc工具"
menu_boot_recovery = "Boot/Recovery工具"
menu_rom_tools = "ROM工具菜单"
menu_new = "新项目"
menu_quit = "退出"
menu_back = "返回"
menu_skip = "跳过"

# ROM Tools Menu
menu_deodex = "Deodex ROM(合并odex)"
menu_perm_type = "改变脚本授权方式"
menu_root = "ROOT/取消ROOT"
menu_asserts = "插入菜单"
menu_extra_dir = "添加/data/app"
menu_rom_debloat = "Debloat 菜单"
menu_build_menu = "ROM打包菜单"

# Startup
startup_project = "当前项目:"
startup_version = "安卓版本:"
startup_mdepend = "缺少厨房依赖: "
startup_need_java = "你的电脑必须正确安装/配置Java8+才能运行厨房."
startup_copy_extract = "放置你的ROM到目录里"
startup_copy_extract2 = "然后你按下4就可以解压以及后续操作了"
startup_title_no_rom = "没有 ROM"
startup_no_projects = "没有项目."
startup_prep_updater_script = "准备updater-script ..."
startup_no_rom = "木有ROM哟."
startup_srkuser = "输入SuperR他服务器注册新账号的用户名 (不是email地址):"
startup_srkuser_pass = "该账户密码敲一下: "
startup_srkuser_error = "不要输入email地址,只是用户名."
startup_srkuser_error2 = " <--这个名字没在厨房数据库里，或者是"
startup_srkuser_error3 = "您的密码输错了哟. 要不您再想想您的用户名和密码"
startup_srkuser_error4 = "重启厨房再运行，再输入一遍呗，这个用户名"
startup_srkuser_error5 = "是SpuerR捐赠版的下载网站(https://sr-code.com/down/),你注册新的账户名."
startup_srkuser_noauth = "您的电脑没有被授权、认可或支持."
startup_srkuser_q = "亲，这是您的用户名吗?  y/n"
startup_srkpass_q = "亲，要不要保存密码呢?  y/n"
startup_error = "初始化运行有点问题. 重新clone一下吧."
startup_checksum = "以下checksums不匹配:"

# Build
menu_build_zip = "创建完整ROM.zip"
menu_sys_img = "创建system.img"
menu_sign = "签名目录下已有zip"
donate_menu_zipalign = "Zipalign apk文件"
donate_menu_custom_id = "自定义ro.build.display.id"
menu_custom_zip = "自定义压缩菜单"
build_selinux_error = "你的内核不支持selinux, 或者是"
build_selinux_error2 = "厨房没在boot里找到所需的文件.如果你能确定"
build_selinux_error3 = "你的设备boot镜像支持selinux, 你可以复制内核的"
build_selinux_error4 = "ramdisk文件夹里file_contexts到项目00_project_files目录里"
build_selinux_error5 = "然后你就可以继续了."
build_selinux_error6 = "现在, 你将要选择set_perm 或者 raw_img."
build_patient = "这将要花费一段时间. 请耐心等待..."
build_prep_img = "正在准备创建img文件 ..."
build_check_ziplog = "出现错误. 请检查zip.log文件."
build_prep_sys_img = "正在创建system.img文件..."
build_img_error = "创建image过程中出现错误."
build_img_which = "哪种img您要去创建呢?"
build_img_nocon = "厨房没发现 file_contexts 这个文件存在. 确保"
build_img_nocon2 = "您的boot.img 是放在现在的ROM处理的文件夹里, 或者呢"
build_img_nocon3 = "你复制内核解压文件夹里file_contexts 到你现在要处理的ROM的"
build_img_nocon4 = "00_project_files 这个文件夹里面,复制了后你再试试看吧."
build_no_zip = "没有找到可签名的zip包."
build_no_boot_q = "您老的ROM木得boot.img或者kernel.img或者ramdisk.img."
build_no_boot_q2 = "还要继续吗??  y/n"
build_cho_zip = "选择zip进行签名:"
zipalign_q = "打包ROM之前需要zipalign吗?  y/n  "
zipalign = "Zipalign中"
zipalign_frame_q = "你需要对/framework中的apk执行 zipalign 吗?  y/n  "
zipalign_complete = "Zipalign完成"
donate_bdisplay = "你想要你的ROM刷机时twrp显示什么?"

# Custom zip
title_cho_cust_zip = "选择创建自定义zip:"
menu_fap = "framework, app, priv-app"
menu_fapl = "framework, app, priv-app, lib"
menu_f = "framework"
menu_ap = "app, priv-app"
menu_l = "lib"
menu_m = "media"
cust_deldir_q = "您希望创建好zip后删除zip所用到的一些文件(夹)?"
cust_deldir_q2 = "就是项目目录里的system文件夹、boot.img等这些  y/n"
cust_meta_prep = "准备META-INF 文件夹..."
cust_not_exist = "您要压缩的一个或多个目录不存在."
cust_dir_info = "请确保您至少拥有以下其中一项 "
cust_file_check = "请确保有system,META-INF和boot.img "
cust_prep = "准备相关文件中 ..."
cust_convert_binary_q = "您要把updater-script转化成update-binary吗？"
cust_convert_binary_q2 = "... y/n  "
cust_convert_binary = "转化updater-script成update-binary中 ..."

# Debloat
menu_debloat = "Debloat ROM"
menu_debloat_cust = "自定义 Debloat"
menu_debloat_knox = "删除三星 Knox"
menu_debloat_restore = "还原 Bloat/Knox"
menu_debloat_refresh = "刷新 Bloat Status"
bloat_already_debloated = "本ROM已经是debloated状态"
bloat_rem = "正在删除 bloat ..."
bloat_moved = "Bloat已经被移动到:"
bloat_cust_info = "将内容添加到以下文件以使用此功能"
bloat_knox_not_exist = "ROM中没有Knox"
bloat_knox_rem = "正在删除 knox ..."
bloat_knox_moved = "Knox已被移动到:"
bloat_no_files_restore = "没有需要还原的文件"
bloat_restore = "正在还原 bloat ..."
bloat_has_restored = "已还原bloat."
bloat_q = "现在要debloat ROM吗?  y/n  "
bloat_knoz_rem_q = "要删除Knox吗?  y/n  "
bloat_restore_q = "现在要还原bloat吗?  y/n  "
debloated = "Debloated"
bloated = "Bloated"
bloat_dir_emply = "bloat_custom 为空"

# Root
title_cho_root_zip = "选择要Root的Zip:"
menu_root_method = "选择您要的ROOT方式?"
menu_ss_method = "您想安装哪种SuperSU?"
menu_supersucho = "让SuperSU决定"
menu_system_install = "安装到System (SYSTEMLESS=false)"
menu_inject = "使用注入 sepolicy 修改,并且安装到system"
menu_download_inject = "下载/安装inject-sepolicy-addon"
menu_root_unroot = "Root/Unroot ROM"
menu_busybox = "Busybox 添加/删除"
menu_add_remove_sud = "添加/删除 su.d 支持"
root_already = "您已经ROOT了."
root_must_add = "您必须先添加ROOT."
busybox_already = "您已经有Busybox."
busybox_q = "ROM需要Busybox吗?  y/n  "
root_sud_add_q = "ROM需要su.d支持吗?  y/n  "
root_sud_rem_q = "ROM需要移除su.d支持吗?  y/n  "
root_supersu_q = "SuperSU是个挂掉的项目了. 你确定要添加?  y/n"

# General
general_remove_q = "要删除它?  y/n  "
general_continue_q = "确认继续?  y/n  "
general_cont_anyway_q = "无论咋地都要继续?  y/n  "
general_extracting = "提取"
general_create = "已创建"
general_build = "正在创建"
no_python = "要用这个功能要安装 Python3.5+ (曦颜提醒：如果还出问题，切换默认PY版本试试吧)."
more_info_link = "想解决目前问题，你可以访问下面的链接:"
spaces_not_allowed = "不允许有空格"

# Status
enabled = "启用"
disabled = "禁用"
add_support = "添加支持"
yes = "是"
no = "否"
secure = "安全"
insecure = "不安全"
no_knox = "木有Knox"
knox = "Knox不存在"
no_root = "未Root"

# Boot/Recovery Tools
title_boot = "Boot/Recovery工具"
title_cho_boot = "选择boot或者recovery img"
title_unpack = "解包显示更多选项 "
title_current = "当前: "
menu_pack_boot = "打包"
menu_insecure = "Insecure/Secure 这个"
menu_dmverity = "删除 dm-verity"
menu_forcee = "添加/删除 forceencrypt"
menu_deopatch = "给sepolicy打补丁--安卓Oreo deodex操作"
menu_deopatch_fail = "打补丁失败, 可能sepolicy 已经patch了."
menu_deopatch_sepol = "sepolicy没看到啊"
menu_deopatch_add = "sepolicy 已经patch了--Oreo deodex操作"
menu_unpack = "解包"
menu_boot_flashable = "创建单刷包:"
menu_boot_restore = "恢复默认: "
menu_switch_boot = "在boot/recovery之间切换"
boot_repack = "打包中 "
boot_repack_problem = "这出现一个问题在打包你的"
boot_packed_d = " 已打包"
boot_no_img = "木有boot.img 或者recovery.img "
boot_prop_warn = "请复制build.prop到项目目录并重试."
boot_prep_build = "准备创建 ..."
boot_unpack = "解压中 "
boot_unpack_problem = "这出现一个问题在解包你的 "
boot_need_img = "你需要一个img文件来完成这个操作."
boot_permission_error = "出现权限错误. 你去看看 boot.log 文件"
boot_permission_error2 = "提供解决方法你看看:"

# Misc Tools Menu
title_misc = "Misc工具菜单"
menu_plugin_menu = "插件管理"
menu_plugin_run = "运行插件"
menu_plugin_install = "安装插件"
menu_plugin_delete = "删除插件"
menu_plugin_updates = "检查插件更新"
menu_plugin_updates_info = "有可用更新:"
menu_plugin_get = "获取插件列表中 ..."
menu_plugin_bashwin = "你不可以在windwos运行Bash插件."
menu_plugin_bashwin2 = "使用插件管理去删除和重新安装正确插件版本.'
menu_zip_devices = "压缩devices/capfiles并分享"
menu_language = "重置语言"
menu_heapsize = "Heapsize菜单"
menu_support = "支持: 创建zip发送"
menu_ubinary = "update-binary脚本选项"
menu_tools_reset = "重置所有工具"
menu_tools_reset_go = "移除所有工具 ..."
menu_device_reset = "升级设备数据库"
menu_choose_server = "主服务器位置"
menu_tools_update = "更新后必须退出重新运行下"
support_create = "创建support.zip ..."
support_finish = "Support zip已创建在你的目录里了"
support_finish_up = "Support zip 已上传完毕"
heapsize_q = "请输入您的heapsize大小（MB）."
heapsize_q2 = " 它必须小于你的总物理RAM:"
heapsize_choose = "你想干什么?"
heapsize_custom = "改变java的heapsize大小"
heapsize_reset = "返回默认heapsize检测"
heapsize_num_error = "您必须输入一个数字MB (Ex. 1024)"
heapsize_error = "Heapsize必须等于或小于物理RAM的大小."
heapsize_error2 = "..."
physical_ram = "物理RAM: "
heapsize_auto = "默认"
title_ubinary = "可刷入zip选项 "
ask_b = "每次询问转换到update-binary脚本"
ask_s = "每次询问"
always_b = "总是转换到update-binary脚本"
always_s = "总是转换"
never_b = "从不转换到update-binary脚本"
never_s = "从不转换"
metasize = "短的/长的 set_metadata updater-script（全局）"
metasize_s = "短的"
metasize_l = "长的"
metasize_q = "用哪种 set_metadata updater-script 长度?"

# Asserts
menu_add_assert = "增加或删除机型"
menu_asserts_custom = "增加自定义授权方式"
menu_asserts_remove = "从ROM移除授权方式"
menu_asserts_reset = "恢复默认的授权方式"
asserts_no_assert = "没有授权方式要修改."
asserts_current = "当前机型授权方式: "
asserts_enter = "机型授权方式可以判断是否允许刷入ROM."
asserts_enter2 = "如果你允许把一个ROM刷到一个错误的机型上,"
asserts_enter3 = "将会导致严重的问题! 我告诉你了哦，别怪我！"
asserts_enter4 = "请用逗号隔开机型授权方式."
asserts_enter5 = "当前机型已经在列表中,请确保正确."
asserts_enter6 = "输入完成后,按回车结束."
asserts_prep = "正在生成机型授权方式 ..."
asserts_type = "在下面输入你的自定义授权方式. 按回车键结束."
asserts_cust_error = "语法必须 "
asserts_prep_cust = "正在生成自定义授权方式 ..."

# Extra Directory
menu_data = "/data/app"
menu_cust_dir = "自定义"
menu_cctr = "未启用"
extra_data_added = "/data/app 文件夹已添加. 请将第三方app放入:"
extra_already_data = "/data/app 文件夹已存在."
extra_already_data2 = "项目中的 /data 文件夹会一直保留."
extra_already_data3 = "要删除吗?  y/n"
extra_data_rem = "/data/app支持已删除"
extra_cust_name = "键入自定义目录的名称和刷入的位置，然后按ENTER键."
extra_cust_loc = "包含在你的ROM里的自定义目录在哪呢?"
extra_cust_name_q = "是否应该刷入到分区?  y/n"
extra_cust_setup = "配置 "
extra_cust_add = "支持已添加"
extra_data = "Data perm 类型:"
extra_data_q = "您要添加/ data / app支持?  y/n  "
extra_data_perm = "请选择/ data perm类型: "
extra_cust_already = " 已然存在."

# Selection
select = "请选择:  "
select_enter = "请选择并回车:  "

# Notices
example = "例如:"
warning = "警告:"
notice = "注意:"
missing = "缺少文件:"
current = "当前"
error = "错误:"
success = "成功:"
error_mess = "出现错误."

# Press ENTER
enter_rom_tools = "按ENTER返回ROM工具菜单"
enter_continue = "按ENTER继续"
enter_main_menu = "按ENTER返回主菜单"
enter_boot_menu = "按ENTER返回到Boot/Recovery工具菜单"
enter_build_menu = "按ENTER返回创建菜单"
enter_change_perm_menu = "按ENTER返回改变授权方式菜单"
enter_debloat_menu = "按ENTER返回Debloat菜单"
enter_extra_dir_menu = "按ENTER返回到其他目录菜单"
enter_cho_another_detection = "按ENTER键选择另一种检测方法"
enter_ready = "准备好就按ENTER键"
enter_kitchen_updater = "按ENTER返回Kitchen更新"
enter_misc_tools_menu = "按ENTER返回Misc工具菜单"
enter_heapsize_menu = "按ENTER返回heapsize菜单"
enter_continue_extracting = "按ENTER继续提取"
enter_try_again = "按ENTER键重试"
enter_root_menu = "按ENTER返回ROOT菜单"
enter_exit = "按ENTER键退出"

# Perm Type
perm_title = "更改/选择授权菜单"
perm_set_metadata_cur = "set_metadata"
perm_set_metadata = "set_metadata (For KitKat+)"
perm_set_perm = "set_perm"
perm_sparse = "Sparse dat"
perm_sparse_red = "Sparse dat (该设备不支持)"
perm_raw_img = "raw_img"
perm_check_symlinks = "检查symlinks ..."
perm_set_metadata_error = "这个ROM不是 KitKat+"
perm_set_perm_error = "这个ROM不是JellyBean或更低"
perm_changing_perm = "改变授权方式 ..."
perm_which = "你想使用哪种刷机脚本授权类型?"

# Delete Project
delete_has_been = " 这个已删除."
delete_q = "要删除这个的项目?  y/n  "

# Deodex
deodex_copy_frame_prop = "您必须将framework目录和\nbuild.prop从您的ROM里复制"
deodex_copy_frame_prop2 = "... "
deodex_no_odex = "在这个rom没有odex文件."
deodex_no_boot_oat = "在这个ROM没有boot.oat. 它不能deodexed."
deodex_no_plat = "在目前电脑环境下无法Deodex 此API"
deodex_no_valgrind = "请安装valgrind后再次尝试"
deodex_disclaimer = "Deodexing ROM可能工作，也可能不工作. "
deodex_disclaimer2 = "您可能会收到错误,它可能无法启动,或两者都有可能"
deodex_disclaimer3 = "（这我知道的问题）.除非你知道如何解决它们,"
deodex_disclaimer4 = "请不要因为这个问题去xda找我问哦. 谢谢 :)"
deodex_use_method = "使用哪种deodex方法?"
deodex_oat2dex_ver = "使用哪个oat2dex版本?"
deodex_oat2dex_official = "官方v0.86"
deodex_oat2dex_latest = "最新的版本"
title_cho_oat2dex = "选择oat2dex:"
title_cho_smali = "选择smali:"
title_cho_baksmali = "选择baksmali:"
deodex_no_api = "无法检测Android版本."
deodex_config_arch = "设置下手机的arch."
deodex_config_arch2 = "提示(arch是啥):"
deodex_config_arch3 = "检查framework文件夹, 里面可以看到另一个文件夹."
deodex_config_arch4 = "文件夹的名字可能是以下之一："
deodex_config_arch5 = "(ex. arm, arm64, x86)."
deodex_config_arch6 = "如果这里有问题, 检查以下问题:"
deodex_config_arch7 = "1. 确保输入的arch参数是正确的."
deodex_config_arch8 = "2. 确保ROM没有已经deodex."
deodex_config_arch9 = "输入手机的arch并且按回车继续.."
deodex_extract_txt = "提取odex文件 ..."
deodex_extract = "提取中... "
deodex_move = "移动额外的应用程序 ..."
deodex_deop = "Deoptimizing boot.oat ..."
deodex_start_app = "开始 deodexing /system/app ..."
deodex_start_priv = "开始 deodexing /system/priv-app ..."
deodex_start_frame = "开始 deodexing /system/framework ..."
deodex_deodexing = "Deodex中... "
deodex_app_already = "deodex完成 ..."
deodex_clean = "清理 ..."
deodex_complete = "Deodexing完成"
deodex_remain = "以下odex文件仍在您的ROM中"
deodex_method = "方法:"
deodex_problems = "如果deodexing存在问题"
deodex_problems2 = "你刷入的ROM就有问题."
deodex_problems3 = "我告诉你了哦，个人建议:"
deodex_try_smali = "建议: 尝试用 smali/baksmali"
deodex_api = "API等级: "
deodex_arch = "ARCH: "
deodex_arch2 = "ARCH2: "
deodex_move_odex = "移动odex文件 ..."
deodex_try_anyway = "怎搞都去试试?  y/n  "
deodex_continue_q = "您要继续deodexing?  y/n  "
deodex_del_meta_inf_q = "Android Nougat使用APK签名方案v2,"
deodex_del_meta_inf_q2 = "这可能会导致deodexing时出现问题. "
deodex_del_meta_inf_q3 = 从apk文件中删除META-INF应该可以解决这个问题."
deodex_del_meta_inf_q4 = "您是否要从ROM中的所有apk文件中"
deodex_del_meta_inf_q5 = "删除META-INF目录?  y/n  "
deodex_del_meta_inf = "从apk的删除META-INF..."
deodex_del_arch = "是否删除下列的framework文件夹?  y/n"
deodex_pack_jar = "将dex压缩进jar文件中..."
deodex_server_disabled = "目前已禁用云端服务器上的cdex转换"
deodex_server_cdex = "在云端服务器上转换cdex ..."
deodex_server_error1 = "上传失败"
deodex_server_error2 = "移动文件到工作目录失败"
deodex_server_error3 = "cdex zip提取失败"
deodex_server_error4 = "云端服务器上的dex zip创建失败"

# Extract
extract_title = "提取菜单"
extract_no_files_message = "1) 首先添加一个zip格式的ROM、tar/boot.img"
extract_no_files_message2 = "system.img/boot.img或win/boot.win,然后选择该选项.."
extract_no_files_message3 = "2) 在已经ROOT的设备或在第三方Recovery中"
extract_no_files_message4 = "提取system、vendor、boot、和recovery."
extract_cho_option = "选择提取方式"
extract_cho_option2 = "**如果遇到错误,请尝试另一种方式**"
extract_cho_option3 = "1) 手机启动在第三方Recovery (官方Recovery不可用)"
extract_cho_option4 = "2) 手机必须开机状态 (必须已经ROOT)"
extract_plug = "** 连接手机"
extract_detect_part = "正在检测分区信息 ..."
extract_detect_part2 = "如果您遇到困难，请在手机上更改USB模式"
extract_detect_part3 = "下拉状态栏把 '充电模式(或其他)' 改到 '媒体模式 (MTP)'"
extract_pull_error = "出错了.可能是没有权限从设备里出镜像"
extract_pull_error2 = "(#^.^#)."
extract_pulling = "拉取中 "
extract_prep = "正在准备提取 ..."
extract_zip_fail = "这个zip不包含厨房可以提取的任何东西."
extract_zip_fail2 = "...."
extract_zip = "提取 zip ..."
extract_dat = "正在提取 system.new.dat, system.transfer.list, 和 boot.img ..."
extract_convert_br = "解压 dat.br ..."
extract_convert_sys = "转换到 "
extract_img_from_zip = "正在从zip包中提取镜像 ..."
extract_tar_boot = "正在提取 system.ext4.tar.a 和 boot.img ..."
extract_img = "正在提取 images ..."
extract_fail = "提取过程中出现错误."
extract_tar_md5 = "提取 tar.md5 文件 ..."
extract_chunk = "提取 sparsechunks 和 boot.img ..."
extract_pbin = "提取 payload.bin ..."
extract_multi = "提取多 system ..."
extract_convert_chunk = "转换 sparse chunks 到 system.img ..."
extract_fix_img = "修复中 ..."
extract_general = "提取到 "
extract_check_firm = "正在检测固件包 ..."
extract_tgz_fail = "该tgz文件似乎不是Nexus官方固件."
extract_tgz_fail2 = "...."
extract_files = "正在提取文件 ..."
extract_md5_fail = "在tar.md5文件中没有system.img.ext4"
extract_tar_fail = "这个tar文件看起来不是android备份文件"
extract_tar = "提取名称"
extract_extra_extract_q = "您想提取其他的分区吗？ (modem.bin, etc.)?  y/n  "
extract_cache_extract_q = "要提取 cache.img?  y/n  "
extract_cache_include_q = "你想在ROM中包含cache.img中的文件吗？"
extract_cache_include_q2 = "....  y/n  "
extract_cache = "包括cache.img文件 ..."
extract_cache_fail = "在cache.img中没有csc.zip"
extract_rom_fail = "提取中发生错误."
extract_cho_part_detect = "选择分区检测方法 "
extract_adb_shell = "通过adb shell"
extract_project_dir = "项目目录 (BETA): "
extract_manual = "手动输入"
extract_detect = "确定分区大小 "
extract_beta = "此功能是测试版. 它可能无法正常刷入."
extract_beta2 = "您可能会收到类似以下的错误:"
extract_beta3 = "blkdiscard failed: Invalid argument"
extract_beta4 = "您可以将perms更改为set_metadata或set_perm以避免使用此功能"
extract_beta5 = "...."
extract_manual_bytes = "输入分区大小（以字节为单位） "
extract_detect_fail = " 分区大小为空. 请重试."
extract_sparse_convert = "检查并转换sparse img ..."
extract_img_fail = "没有"
extract_copy_e = "正在将文件复制到 "
extract_moved_old_rom = "以下已被移动至:"
extract_q = "要提取 "
extract_q2 = "到当前项目?  y/n  "
extract_extra_extract = "要提取 "
extract_extra_q = "..?  y/n  "
extract_extra_include = "你想包含你的ROM中的文件 "
extract_extra_include_q = " 是哪些?  y/n  "
extract_autorom_sudo = "sudo执行厨房可以让AutoROM不意外中断"

# by-name
byname_how_to_get_q = "你想如何得到你的分区信息?"
menu_byname_detect_boot = "从boot.img/recovery.img里查询by-name代码 (小姐姐强烈推荐)"
menu_byname_detect_device = "从设备检测by-name相关代码"
menu_byname_detect_manual = "手动输入by-name代码"
menu_byname_detect_mmc = "从recovery.img检测mmcblk分区"
byname_usb_debug = "** 在系统设置中在Android设备上启用usb调试"
byname_usb_debug2 = "** 连接你的设备"
byname_usb_debug_root = "此操作需要root."
byname_usb_debug_root2 = "您可能需要手动在您的手机su弹窗点击允许root."
byname_error_device = "从设备未检测到by-name相关代码."
byname_error_device2 = "尝试检测mmc分区从recovery.img"
byname_no_boot = "请复制boot.img, recovery.img, 或者kernel.elf到"
byname_no_boot2 = "项目目录，然后重试"
byname_which_img_q = "要用哪个image文件搞?"
byname_detect = "从recovery.img里查询by-name相关代码"
byname_no_files = "此项操作你需要boot.img, recovery.img, 或者kernel.elf."
byname_boot_fail = "by-name未检测到."
byname_try_recovery = "尝试从recovery.img代码里查询mmc分区"
byname_detect_manual = "请输入您的by-name目录，然后按ENTER键"
byname_no_byname = "by-name目录为空."
byname_create_mmc = "基于recovery.img信息里创建mmc ..."
byname_need_recovery = "此项操作你需要recovery.img."
byname_no_mmc = "厨房找不到mmc代码信息."
byname_recovery_fail = "在recovery.img未找到mmc相关代码."
byname_try_boot = "尝试从boot.img里检测by-name分区"

# Signature
sig_info = "问题的意思就是"
sig_info2 = "你创建rom后刷入呢TWRP会显示的信息"
sig_info3 = "你输入你想显示的东西就行了."
sig_info_q = "你的zip的名称是?"
sig_info_error = "在rom里不显示你要的信息"
donate_sig_cust = "这里将显示刷入ROM时一些信息"
donate_sig_cust2 = "默认的信息写着Built with SuperR's Kitchen."
donate_sig_q = "输入你的要显示的信息?"

# Zip devices
zipdev_info = "此选项将压缩您在厨房处理过的手机型号.它将在以下位置创建一个zip:"
zipdev_building = "创建 device zip ..."
zipdev_uploading = "上传到服务器 ..."
zipdev_finished = "device zip已经创建完成:"
zipdev_upload = "你想要现在去上传然后"
zipdev_upload2 = "就可以添加到云端数据库供其他人使用?  y/n"
support_upload = "你要现在上传support zip 吗?  y/n"
xdauser_q = "你的XDA用户名是(如果你么有就输入guest) ?"
zipdev_no_new = "device目录中没有你曾经处理的手机型号."

# Kitchen updater
update_check_kitchen = "检查更新 ..."
update_down = "文件服务必须暂时关闭."
update_down2 = "请稍后再试."
update_update_avail = "云端存在新版本"
update_update_cv = "当期版本:"
update_update_nv = "新版本:"
update_update_now = "现在更新"
update_update_view = "查看更新日志"
update_changelog = "更新日志 (最后3个版本):"
update_updating = "更新中 ..."
update_finished = "SuperR's Kitchen 已更新，你需要重启厨房一下下"
update_finished_win = "厨房目录里的 superr1.exe 可忽略或删除."
update_finished_win2 = "待君重启就自动删除了呢"
update_finished_win3 = "^_^"
update_already = "SuperR's Kitchen 已经是最新的"
update_check_launcher = "检查厨房启动器更新 ..."
update_launcher_avail = "启动器更新可用"
update_launcher_cv = "当前版本:"
update_launcher_nv = "新版本:"
update_launcher_finished = "安装程序/启动程序已更新"
update_problem_download = "下载更新时出现问题."
update_no_internet = "厨房无法检测到互联网连接."
update_fail = "更像出错."
update_fail2 = "试试重新下载吧."
update_fail3 = "非常抱歉带来不便."
update_q = "你想现在更新吗?  y/n  "
update_auto_q = "你想在厨房启动时检查更新?  y/n  "
update_auto_toggle = "在启动时检查更新"
update_cred_fail = "您的付费用户认证未成功,因为在数据库中未找到."
update_cred_fail2 = "你可以在你付费后并且注册后下载最新的厨房."
update_cred_fail3 = "..."
update_reg_address = "下载地址:https://sr-code.com/reg.php"
update_verify = "检查中 ..."

# New Project
new_q = "请输入新项目名称(输入后在厨房目录生成文件夹:superr_您输入名称):"
new_already = "已有相同名称的项目"

# Plugin
donate_plugin_cho = "选择要运行的插件:"
donate_plugin_install_cho = "选择要安装的插件:"
donate_plugin_delete_cho = "选择要删除的插件:"
donate_plugin_error = "插件脚本必须位于与插件脚本名称相同的目录中"
donate_plugin_error2 = "...."
donate_plugin_server = "看起来像插件服务不可用。 请稍后再试"
donate_plugin_reinstall_q = "无法检查更新，因为它是在更新系统"
donate_plugin_reinstall_q2 = "之前安装的."
donate_plugin_reinstall_q3 = "你想现在重新安装吗?  y/n"
donate_plugin_crash = "在插件里发生冲突错误: "
donate_plugin_crash2 = "你仔细看看 plugin.log文件."

# Sign
sign_ram_check = "检查RAM ..."
sign_no_ram = "电脑没有足够的RAM签名这个zip."
sign_signing = "签名中..."
sign_signed = "搞定，签名完成!"
sign_fail = "签名中出现错误."
sign_q = "要把这个zip签个名吗?  y/n  "

# Build img
img_add = "添加中"
img_flash_fail = "无法刷入,因为缺少分区信息"
img_flash_fail2 = "... "
img_create_dat = "创建sparse dat镜像"
img_create_symlinks = "创建 symlinks"
img_create_raw = "创建中..."
img_fail = "创建image出现错误."
img_fail2 = "请确认文件夹大小没有过大"
img_fail3 = "厨房不支持太大的文件夹哦."
img_dir_open = "确保system没有在你系统文件管理器"
img_dir_open2 = "或者其他地方，然后重试."
img_flash_failB = "无法刷入, 因为缺少分区信息"
img_flash_failB2 = "请创建一个device文件夹"
img_flash_failB3 = "或着在zip包创建之后手动输入分区信息"
img_sparse_q = "想创建什么类型的img?"

# Language
reset_language = "语言设定已重置. 等到下次你"
reset_language2 = "使用厨房就可以重新选择了"
lang_added = "添加了未汉化的新的英语提示"
lang_translate = "去翻译一下."

# Tools
tools_dl = "下载中 "
tools_dl_failed = "所需工具下载失败,请挂VPN下载:"
tools_dl_install_failed = "所需工具 下载/安装 失败."
tools_dl_device_failed = "本次无法下载一些device数据库."
tools_dl_device_failed2 = "你稍后可以使用Misc Tools升级设备数据库"
tools_dl_device_failed3 = "升级到最新的版本"
wintools_dl = "(大概要下载 17MB 大小文件 )"
lintools_dl = "(大概要下载 24MB 大小文件)"
tools_need = "你需要安装厨房必须的工具才能继续."
tools_dl_install = "下载/安装中 ..."
tools_dl_q = "你要现在下载/安装?  y/n  "

#Example Plugin
plug_example_text = " 添加更多插件到 "
