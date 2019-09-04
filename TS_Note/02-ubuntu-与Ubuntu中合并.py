0-基础设置
	sudo passwd 【root初始密码设置】
1-ubuntu 软件安装
	//默认都是以
	/etc/apt/source.list 【配置源(apt-yum)】
	PPA:Personal Package Archives (daily dev stable beta)
	sudo add-apt-repository ppa:chromium-daily/stable 【安装谷歌浏览器的源】
	sudo add-apt-repository ppa:videolan/stable-daily 【安装VLC播放器】
	sudo apt-get update | grep "Failed" 【搜索获取失败的源】
	sudo add-apt-repository --remove ppa:finalterm/daily 【移除失败的源】
	sudo apt-get update 【更新源】
	sudo apt-show-versions -a git 【查看软件的所有版本】
	
	apt-(tab) 【可查看所有已安装apt命令 使用参数 --help可产看帮助，要有看帮助的习惯！】
	dpkg
	curl
	wget
	snap store 	【？？？ 】
	
2-ubuntu下python版本控制
	Ubuntu16.04 有太多应用依赖自带的 python3.5，所以不能卸载.
	find / -name 'python'【所有安装路径】
	/usr/bin/ 【所有用户安装的脚本，包括所有版本的python】
	/bin 【系统级别目录】


3-ubuntu下Java版本控制
	update-alternative
4-ubuntu下MySQL的安装
5-linux中出现 Read-only file system
	mount -o,remount,rw /dev/sda18 /opt/gracenote/db/
6-由windows下拷贝的文件./install_ssh.sh 安装时出现一下错误。
	 bad interpreter: Permission denied