# 语言资源文件
class Localization:
    zh_CN = {
        # 主窗口
        "app_title": "Chusan Segatools INI GUI v{0}",
        "open_config": "打开配置文件",
        "save_config": "保存配置文件",
        "error": "错误",
        "success": "成功",
        "warning": "警告",
        "cannot_read_config": "无法读取配置文件: {0}",
        "config_saved": "配置文件已保存",
        "save_error": "保存配置文件时出错: {0}",
        
        # 标签页名称
        "tab_path": "路径设置",
        "tab_device": "设备设置",
        "tab_network": "网络设置",
        "tab_board": "主板设置",
        "tab_window": "窗口设置",
        "tab_led": "LED设置",
        "tab_io": "自定义IO设置",
        "tab_input": "输入设置",
        
        # 备份信息
        "backup_error_title": "备份错误",
        "backup_error_msg": "创建备份文件时出错：{0}",
        "save_success_title": "保存成功",
        "save_success_msg": "配置已成功保存到 {0}\n同时创建了备份文件 {0}.bak",
        "save_error_title": "保存错误",
        "save_error_msg": "保存配置文件时出错：{0}",
        
        # 路径标签页
        "path_tips": "提示：\n① 可使用相对路径(如amfs)或绝对路径(如X:/amfs)\n② 同一个AppData目录可与多个Sega游戏共同使用",
        "vfs_settings": "VFS 路径设置",
        "amfs_path": "AMFS 路径:",
        "option_path": "Option 路径:",
        "appdata_path": "AppData 路径:",
        "browse": "浏览...",
        "create_default_folders": "创建默认文件夹",
        "open_folder_dialog": "选择文件夹",
        "open_file_dialog": "选择文件",
        "please_open_config": "请先打开配置文件",
        "folders_created": "已创建文件夹: {0}",
        "all_folders_exist": "所有文件夹已存在",
        "create_folder_error": "创建 {0} 文件夹失败: {1}",
        
        # 设备标签页
        "aime_settings": "Aime 设置",
        "use_virtual_reader": "使用虚拟读卡器",
        "aime_path": "Aime 路径:",
        "path_tip": "提示: 可使用相对路径或绝对路径",
        "edit_aime_card": "编辑Aime卡号",
        "enable_high_baud": "启用高波特率",
        "vfd_settings": "VFD 设置",
        "enable_vfd": "启用 VFD 模拟",
        "vfd_tip": "提示: 使用真实VFD请关闭这个选项，如果你不清楚什么是VFD请不要随意修改这个选项",
        "edit_aime_title": "编辑Aime卡号",
        "edit_aime_desc": "请输入Aime卡号 (通常为20位数字):",
        "edit_aime_placeholder": "例如: 51073710566476005666",
        "ok": "确定",
        "cancel": "取消",
        "aime_updated": "Aime卡号已更新",
        "edit_aime_error": "编辑Aime卡号时出错: {0}",
        "file_not_exist": "文件不存在: {0}",
        
        # 网络标签页
        "offline": "离线",
        "custom_selecton": "自定义",
        "dns_settings": "DNS 设置",
        "default_server": "默认服务器:",
        "custom_dns": "自定义DNS:",
        "netenv_settings": "网络环境设置",
        "lan_simulation": "局域网模拟",
        "ip_suffix": "IP地址后缀:",
        "suffix_tip": "提示: 请填入zerotier中设置的后缀",
        
        # 主板标签页
        "keychip_settings": "Keychip 设置",
        "subnet": "子网:",
        "id": "狗号(ID):",
        "id_tip": "提示: 请在对应服务器后端获取加密狗号",
        "system_settings": "系统设置",
        "enable_alls": "启用 ALLS 系统设置",
        "system_tip": "提示: 请不要随意修改此选项",
        "enable_freeplay": "启用FreePlay",
        "freeplay_tip": "提示: FreePlay模式下无法买票，默认禁用",
        "dipsw1": "DIPSW1: LAN 安装:",
        "dipsw1_client": "0: 客户端",
        "dipsw1_server": "1: 服务端",
        "dipsw1_tip": "提示: 多机联机时，子机修改为0",
        "dipsw2": "DIPSW2: 显示器类型:",
        "dipsw3": "DIPSW3: 机柜类型:",
        "display_tip": "提示: 显示器帧率小于120请使用60FPS+CVT，显示器帧率大于等于120请使用120FPS+SP",
        
        # 窗口标签页
        "window_settings": "窗口设置",
        "windowed_mode": "窗口模式运行",
        "show_frame": "显示窗口边框",
        "monitor": "显示器:",
        "monitor_tip": "提示: 一般不需要修改，0代表当前主屏幕",
        
        # LED标签页
        "led_warning": "如你不知道这是什么，请不要修改本页面任何选项",
        "led15093_settings": "LED15093 设置",
        "enable_led15093": "启用15093-06灯光模拟",
        "led_settings": "LED 设置",
        "led_tip": "如需自定义LED配置，请直接在ini文件中修改",
        
        # IO标签页
        "aimeio_settings": "AimeIO 设置",
        "aimeio_tip": "提示: 如果使用虚拟读卡器，这里的设置将被忽略",
        "aimeio_dll": "AimeIO DLL:",
        "custom_dll_path": "自定义DLL路径:",
        "chuniio_settings": "ChuniIO 设置",
        "use_builtin_chuniio": "使用内建chuniio映射",
        "chuniio_dll": "ChuniIO DLL:",
        
        # 输入标签页
        "io3_settings": "IO3 按键设置",
        "keycode_tip": "提示: 点击输入框并按键盘按键来设置按键",
        "vk_tip": "提示: 按键设置参照十六进制虚拟键位表: https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes",
        "test_key": "测试按钮键码 (默认 F1):",
        "service_key": "服务按钮键码 (默认 F2):",
        "coin_key": "投币按钮键码 (默认 F3):",
        "ir_key": "IR 按钮键码 (默认 空格键):",
        "use_custom_air": "使用定制AIR硬件",
        "ir_tip": "提示: 定制的AIR硬件请修改下方IR传感器设置",
        "reset": "重置",
        "ir_sensor_settings": "IR 传感器设置",
        "ir_sensor_tip": "提示: 如需自定义配置，请直接修改ini文件",
        "slider_settings": "滑块设置",
        "enable_slider": "启用滑块模拟 (如有实体滑块，请禁用)",
        "slider_tip": "提示: 使用官机协议手台请禁用此选项",
        "slider_note": "注意: 如需配置自定义触摸条控制器，请直接编辑 INI 文件",

        # Misc 标签页
        "tab_misc": "杂项",
        "common_config_settings": "修改 config_common.json",
        "common_config_desc": "使用 allnet_auth1.0 认证，并禁用allnet_accounting。",
        "fix_common_config": "修复 config_common.json",
        "sp_config_settings": "修改 config_sp.json",
        "sp_config_desc": "禁用emoney。",
        "fix_sp_config": "修复 config_sp.json",
        "select_bin_folder": "选择游戏bin文件夹",
        "folder_not_found_title": "文件夹未找到",
        "bin_folder_not_found": "未找到bin文件夹，请手动选择。",
        "file_not_found_title": "文件未找到",
        "common_config_not_found": "未找到config_common.json文件。",
        "sp_config_not_found": "未找到config_sp.json文件。",
        "success_title": "操作成功",
        "common_config_fixed": "config_common.json文件已成功修改，并创建了备份文件。",
        "sp_config_fixed": "config_sp.json文件已成功修改，并创建了备份文件。",
        "error_title": "错误",
        "fix_error": "修改文件时出错：{0}",
        "openssl_fix_settings": "修复 OpenSSL",
        "openssl_fix_desc": "添加OpenSSL修复代码以解决某些系统上存在的兼容性问题而导致amdaemon崩溃。",
        "fix_openssl": "修复 OpenSSL 设置",
        "start_bat_not_found": "未找到start.bat文件。",
        "openssl_already_fixed": "OpenSSL设置已经修复，无需再次修改。",
        "openssl_fixed": "start.bat文件已成功修改，并创建了备份文件。",
        "info_title": "提示",
        "online_flag_settings": "修复 OnlineFlag (灰网修复)",
        "online_flag_desc": "修改OnlineFlag事件，解决此事件造成的灰网问题。",
        "fix_online_flag": "修复 OnlineFlag",
        "select_game_root": "选择游戏根目录",
        "game_root_not_found": "未找到游戏根目录，请手动选择。",
        "a001_not_found": "opt内不存在A001，请安装A001或A999。",
        "event_xml_not_found": "未找到Event.xml文件。",
        "online_flag_already_fixed": "OnlineFlag已经修复，无需再次修改。",
        "online_flag_not_found": "在Event.xml中未找到需要修改的OnlineFlag设置。",
        "online_flag_fixed": "OnlineFlag已成功修复，并创建了备份文件。",
        "warning_title": "警告",

        
        # 其它
        "TODO_tip": "未完成",

        # 语言设置
        "language": "语言(Language):",
        "language_zh": "中文",
        "language_en": "English",
    }
    
    # 英文语言包
    en_US = {
        # 主窗口
        "app_title": "Chusan Segatools INI GUI v{0}",
        "open_config": "Open Config",
        "save_config": "Save Config",
        "error": "Error",
        "success": "Success",
        "warning": "Warning",
        "cannot_read_config": "Cannot read config file: {0}",
        "config_saved": "Configuration saved",
        "save_error": "Error saving config file: {0}",
        
        # 标签页名称
        "tab_path": "Path Settings",
        "tab_device": "Device Settings",
        "tab_network": "Network Settings",
        "tab_board": "Board Settings",
        "tab_window": "Window Settings",
        "tab_led": "LED Settings",
        "tab_io": "Custom IO Settings",
        "tab_input": "Input Settings",

        # 备份信息
        "backup_error_title": "Backup Error",
        "backup_error_msg": "Error creating backup file: {0}",
        "save_success_title": "Save Successful",
        "save_success_msg": "Configuration successfully saved to {0}\nA backup file {0}.bak was also created",
        "save_error_title": "Save Error",
        "save_error_msg": "Error saving configuration file: {0}",
        
        # 路径标签页
        "path_tips": "Tips:\n① You can use relative paths (e.g., amfs) or absolute paths (e.g., X:/amfs)\n② The same AppData directory can be shared among multiple Sega games",
        "vfs_settings": "VFS Path Settings",
        "amfs_path": "AMFS Path:",
        "option_path": "Option Path:",
        "appdata_path": "AppData Path:",
        "browse": "Browse...",
        "create_default_folders": "Create Default Folders",
        "open_folder_dialog": "Select Folder",
        "open_file_dialog": "Select File",
        "please_open_config": "Please open a config file first",
        "folders_created": "Folders created: {0}",
        "all_folders_exist": "All folders already exist",
        "create_folder_error": "Failed to create {0} folder: {1}",
        
        # 设备标签页
        "aime_settings": "Aime Settings",
        "use_virtual_reader": "Use Virtual Reader",
        "aime_path": "Aime Path:",
        "path_tip": "Tip: You can use relative or absolute paths",
        "edit_aime_card": "Edit Aime Card",
        "enable_high_baud": "Enable High Baud Rate",
        "vfd_settings": "VFD Settings",
        "enable_vfd": "Enable VFD Emulation",
        "vfd_tip": "Tip: Disable this option if using real VFD. If you don't know what VFD is, don't modify this option",
        "edit_aime_title": "Edit Aime Card Number",
        "edit_aime_desc": "Please enter Aime card number (usually 20 digits):",
        "edit_aime_placeholder": "Example: 51073710566476005666",
        "ok": "OK",
        "cancel": "Cancel",
        "aime_updated": "Aime card number updated",
        "edit_aime_error": "Error editing Aime card: {0}",
        "file_not_exist": "File does not exist: {0}",
        
        # 网络标签页
        "offline": "Offline",
        "custom_selecton": "CUSTOM",
        "dns_settings": "DNS Settings",
        "default_server": "Default Server:",
        "custom_dns": "Custom DNS:",
        "netenv_settings": "Network Environment Settings",
        "lan_simulation": "LAN Simulation",
        "ip_suffix": "IP Address Suffix:",
        "suffix_tip": "Tip: Enter the suffix set in zerotier",
        
        # 主板标签页
        "keychip_settings": "Keychip Settings",
        "subnet": "Subnet:",
        "id": "ID:",
        "id_tip": "Tip: Get the keychip ID from your server backend",
        "system_settings": "System Settings",
        "enable_alls": "Enable ALLS System Settings",
        "system_tip": "Tip: Please do not modify this option randomly",
        "enable_freeplay": "Enable FreePlay",
        "freeplay_tip": "Tip: Cannot purchase tickets in FreePlay mode, disabled by default",
        "dipsw1": "DIPSW1: LAN Installation:",
        "dipsw1_client": "0: Client",
        "dipsw1_server": "1: Server",
        "dipsw1_tip": "Tip: Set to 0 for secondary machines in multi-cabinet setup",
        "dipsw2": "DIPSW2: Display Type:",
        "dipsw3": "DIPSW3: Cabinet Type:",
        "display_tip": "Tip: Use 60FPS+CVT for monitors with refresh rate less than 120Hz, use 120FPS+SP for 120Hz or higher",
        
        # 窗口标签页
        "window_settings": "Window Settings",
        "windowed_mode": "Run in Windowed Mode",
        "show_frame": "Show Window Frame",
        "monitor": "Monitor:",
        "monitor_tip": "Tip: Usually no need to modify, 0 represents the primary display",
        
        # LED标签页
        "led_warning": "If you don't know what this is, please don't modify any options on this page",
        "led15093_settings": "LED15093 Settings",
        "enable_led15093": "Enable 15093-06 light simulation",
        "led_settings": "LED Settings",
        "led_tip": "To customize LED configuration, please modify directly in the ini file",
        
        # IO标签页
        "aimeio_settings": "AimeIO Settings",
        "aimeio_tip": "Tip: These settings will be ignored if using virtual reader",
        "aimeio_dll": "AimeIO DLL:",
        "custom_dll_path": "Custom DLL Path:",
        "chuniio_settings": "ChuniIO Settings",
        "use_builtin_chuniio": "Use Built-in chuniio Mapping",
        "chuniio_dll": "ChuniIO DLL:",
        
        # 输入标签页
        "io3_settings": "IO3 Key Settings",
        "keycode_tip": "Tip: Click input box and press a key to set",
        "vk_tip": "Tip: Key settings refer to hexadecimal virtual key codes: https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes",
        "test_key": "Test Button Key (Default F1):",
        "service_key": "Service Button Key (Default F2):",
        "coin_key": "Coin Button Key (Default F3):",
        "ir_key": "IR Button Key (Default Space):",
        "use_custom_air": "Use Custom AIR Hardware",
        "ir_tip": "Tip: For custom AIR hardware, modify IR sensor settings below",
        "reset": "Reset",
        "ir_sensor_settings": "IR Sensor Settings",
        "ir_sensor_tip": "Tip: For custom configuration, edit the ini file directly",
        "slider_settings": "Slider Settings",
        "enable_slider": "Enable Slider Emulation (Disable if using physical slider)",
        "slider_tip": "Tip: Disable this option when using official protocol controller",
        "slider_note": "Note: To configure custom touch slider controller, edit the INI file directly",

        # Misc 标签页
        "tab_misc": "Miscs",
        "common_config_settings": "Modify config_common.json",
        "common_config_desc": "Use allnet_auth1.0 authentication and disable allnet_accounting.",
        "fix_common_config": "Fix config_common.json",
        "sp_config_settings": "Modify config_sp.json",
        "sp_config_desc": "Disable Emoney.",
        "fix_sp_config": "Fix config_sp.json",
        "select_bin_folder": "Select game bin folder",
        "folder_not_found_title": "Folder Not Found",
        "bin_folder_not_found": "Bin folder not found. Please select manually.",
        "file_not_found_title": "File Not Found",
        "common_config_not_found": "config_common.json file not found.",
        "sp_config_not_found": "config_sp.json file not found.",
        "success_title": "Success",
        "common_config_fixed": "config_common.json has been successfully modified and a backup file has been created.",
        "sp_config_fixed": "config_sp.json has been successfully modified and a backup file has been created.",
        "error_title": "Error",
        "fix_error": "Error modifying file: {0}",
        "openssl_fix_settings": "Fix OpenSSL",
        "openssl_fix_desc": "Added OpenSSL fix code to address a compatibility issue that causes amdaemon to crash on some systems.",
        "fix_openssl": "Fix OpenSSL Settings",
        "start_bat_not_found": "start.bat file not found.",
        "openssl_already_fixed": "OpenSSL settings are already fixed, no need to modify again.",
        "openssl_fixed": "start.bat file has been successfully modified and a backup file has been created.",
        "info_title": "Information",
        "online_flag_settings": "Fix OnlineFlag (Gray Network Fix)",
        "online_flag_desc": "Modify the OnlineFlag event to solve the problem of not being able to connect to the server caused by this event.",
        "fix_online_flag": "Fix OnlineFlag",
        "select_game_root": "Select Game Root Directory",
        "game_root_not_found": "Game root directory not found. Please select manually.",
        "a001_not_found": "A001 not found in option folder. Please install A001 or A999.",
        "event_xml_not_found": "Event.xml file not found.",
        "online_flag_already_fixed": "OnlineFlag is already fixed, no need to modify again.",
        "online_flag_not_found": "OnlineFlag setting not found in Event.xml.",
        "online_flag_fixed": "OnlineFlag has been successfully fixed and a backup file has been created.",
        "warning_title": "Warning",



        
        # 其它
        "TODO_tip": "Coming soon",
        
        # 语言设置
        "language": "Language(语言):",
        "language_zh": "中文",
        "language_en": "English",
    }
    
    @staticmethod
    def get_text(lang, key, *args):
        """获取指定语言的文本，支持格式化参数"""
        if lang == "en_US":
            text = Localization.en_US.get(key, key)
        else:  # 默认中文
            text = Localization.zh_CN.get(key, key)
            
        # 如果有格式化参数
        if args:
            return text.format(*args)
        return text
