# Payloader Payload 手册

## intranetPayloads

### BloodHound域分析
分类: `信息收集`
使用BloodHound分析Active Directory攻击路径

### SPN扫描
分类: `信息收集`
扫描域内服务主体名称

### 内网端口扫描
分类: `信息收集`
内网端口扫描与服务识别

### 域信息收集
分类: `信息收集`
Active Directory域环境信息收集

### 网络信息收集
分类: `信息收集`
内网网络拓扑和配置信息收集

### 共享枚举
分类: `信息收集`
枚举网络共享资源

### 用户枚举
分类: `信息收集`
枚举域内用户信息

### 组枚举
分类: `信息收集`
枚举域内组信息

### GPO枚举
分类: `信息收集`
枚举组策略对象

### ACL枚举
分类: `信息收集`
枚举访问控制列表

### 信任关系枚举
分类: `信息收集`
枚举域信任关系

### 计算机枚举
分类: `信息收集`
枚举域内计算机

### Mimikatz凭证抓取
分类: `凭证窃取`
使用Mimikatz抓取Windows系统凭证

### Kerberoasting攻击
分类: `凭证窃取`
Kerberoasting攻击获取服务账户哈希

### AS-REP Roasting
分类: `凭证窃取`
AS-REP Roasting攻击获取用户哈希

### LaZagne凭证抓取
分类: `凭证窃取`
使用LaZagne抓取各种应用程序凭证

### SAM数据库导出
分类: `凭证窃取`
导出Windows SAM数据库获取本地账户哈希

### NTDS.dit导出
分类: `凭证窃取`
导出Active Directory数据库获取所有域用户哈希

### GPP密码提取
分类: `凭证窃取`
提取组策略首选项中的密码

### PsExec横向移动
分类: `横向移动`
使用PsExec进行横向移动

### WMI横向移动
分类: `横向移动`
使用WMI进行横向移动

### Pass-the-Hash攻击
分类: `横向移动`
使用NTLM哈希进行身份验证

### NTLM Relay攻击
分类: `横向移动`
NTLM中继攻击技术

### 令牌窃取与模拟
分类: `权限提升`
窃取和模拟Windows访问令牌

### 注册表持久化
分类: `权限维持`
通过注册表实现权限维持

### FRP内网穿透
分类: `隧道代理`
使用FRP建立内网穿透隧道

### Chisel内网穿透
分类: `隧道代理`
使用Chisel建立内网穿透隧道

### PowerShell免杀
分类: `免杀与规避`
PowerShell脚本免杀技术

### 域内权限提升路径
分类: `域渗透攻击`
利用ACL错误配置进行域权限提升

### 跨域信任攻击
分类: `域渗透攻击`
利用域信任关系进行跨域攻击

### Mimikatz高级技巧
分类: `凭证窃取`
Mimikatz高级凭证提取和利用技术

### 浏览器凭证提取
分类: `凭证窃取`
从浏览器中提取保存的密码和Cookie

### DPAPI凭证提取
分类: `凭证窃取`
从DPAPI保护存储中提取凭证

### RDP凭证提取
分类: `凭证窃取`
提取保存的RDP连接密码

### WiFi凭证提取
分类: `凭证窃取`
提取保存的WiFi密码

### Windows Vault凭证
分类: `凭证窃取`
从Windows凭据管理器提取凭证

### KeePass凭证提取
分类: `凭证窃取`
从KeePass数据库提取密码

### LSA Secrets提取
分类: `凭证窃取`
从LSA Secrets提取敏感数据

### 缓存凭证提取
分类: `凭证窃取`
提取域缓存凭证

### WinRM横向移动
分类: `横向移动`
通过WinRM进行横向移动

### DCOM横向移动
分类: `横向移动`
通过DCOM进行横向移动

### SSH横向移动
分类: `横向移动`
通过SSH进行横向移动

### RDP会话劫持
分类: `横向移动`
劫持已存在的RDP会话

### Overpass-the-Hash
分类: `横向移动`
使用哈希获取Kerberos票据

### Pass-the-Ticket
分类: `横向移动`
使用Kerberos票据进行横向移动

### SMBExec横向移动
分类: `横向移动`
通过SMB执行命令

### ATExec横向移动
分类: `横向移动`
通过计划任务执行命令

### WinRS横向移动
分类: `横向移动`
通过WinRS执行远程命令

### Windows权限提升
分类: `权限提升`
Windows系统提权技术

### Linux权限提升
分类: `权限提升`
Linux系统提权技术

### UAC绕过
分类: `权限提升`
绕过Windows用户账户控制

### DLL劫持
分类: `权限提升`
通过DLL劫持提权

### 服务提权
分类: `权限提升`
通过服务漏洞提权

### AlwaysInstallElevated提权
分类: `权限提升`
利用AlwaysInstallElevated提权

### Juicy Potato提权
分类: `权限提升`
利用COM对象和SeImpersonatePrivilege提权

### PrintSpoofer提权
分类: `权限提升`
利用打印机服务提权

### GodPotato提权
分类: `权限提升`
GodPotato提权工具

### SUID提权
分类: `权限提升`
利用SUID文件提权

### Sudo提权
分类: `权限提升`
利用Sudo配置提权

### Cron提权
分类: `权限提升`
利用Cron任务提权

### 内核漏洞提权
分类: `权限提升`
利用内核漏洞提权

### WMI持久化
分类: `权限维持`
通过WMI事件订阅实现持久化

### 启动文件夹持久化
分类: `权限维持`
通过启动文件夹实现持久化

### 服务持久化
分类: `权限维持`
通过创建服务实现持久化

### DLL注入持久化
分类: `权限维持`
通过DLL注入实现持久化

### 后门用户
分类: `权限维持`
创建后门用户账户

### 隐藏用户
分类: `权限维持`
创建隐藏的管理员用户

### ReGeorg隧道
分类: `隧道代理`
通过Web Shell建立隧道

### SSH本地转发
分类: `隧道代理`
SSH本地端口转发

### SSH远程转发
分类: `隧道代理`
SSH远程端口转发

### SSH动态转发
分类: `隧道代理`
SSH动态SOCKS代理

### DNS隧道
分类: `隧道代理`
通过DNS协议建立隧道

### ICMP隧道
分类: `隧道代理`
通过ICMP协议建立隧道

### Ligolo隧道
分类: `隧道代理`
Ligolo内网穿透工具

### DCSync攻击
分类: `凭证窃取`
模拟域控制器同步获取凭证

### 黄金票据攻击
分类: `凭证窃取`
使用krbtgt哈希生成黄金票据

### 白银票据攻击
分类: `凭证窃取`
使用服务账户哈希生成白银票据

### AMSI绕过
分类: `免杀与规避`
绕过反恶意软件扫描接口

### Excel DCOM横向移动
分类: `横向移动`
利用Excel DCOM进行横向移动

### MMC DCOM横向移动
分类: `横向移动`
利用MMC DCOM进行横向移动

### RDP Relay攻击
分类: `横向移动`
RDP中继攻击技术

### 计划任务持久化
分类: `权限维持`
通过计划任务实现持久化

### Skeleton Key后门
分类: `权限维持`
在域控制器植入万能密码

### DSRM后门
分类: `权限维持`
利用DSRM账户建立后门

### SID History后门
分类: `权限维持`
利用SID History建立后门

### 进程镂空持久化
分类: `权限维持`
利用进程镂空技术实现持久化

### SOCKS代理
分类: `隧道代理`
建立SOCKS代理访问内网

### Ngrok内网穿透
分类: `隧道代理`
使用Ngrok建立内网穿透

### EW内网穿透
分类: `隧道代理`
使用EW建立内网穿透

### Venom内网穿透
分类: `隧道代理`
使用Venom建立内网穿透

### Zerologon攻击
分类: `域渗透攻击`
CVE-2020-1472 Netlogon提权

### PrintNightmare攻击
分类: `域渗透攻击`
CVE-2021-34527 打印服务漏洞

### PetitPotam攻击
分类: `域渗透攻击`
CVE-2021-36942 强制认证攻击

### noPac/SAMAccountName攻击
分类: `域渗透攻击`
CVE-2021-42278/CVE-2021-42287 域提权

### ADCS滥用攻击
分类: `域渗透攻击`
Active Directory证书服务滥用

### ADCS ESC1漏洞
分类: `域渗透攻击`
证书模板ESC1滥用

### 约束委派攻击
分类: `域渗透攻击`
利用约束委派进行横向移动

### 基于资源的约束委派
分类: `域渗透攻击`
利用RBCD进行权限提升

### DCShadow攻击
分类: `域渗透攻击`
伪造域控制器注入数据

### 组策略滥用
分类: `域渗透攻击`
滥用组策略进行横向移动

### ETW Patch绕过
分类: `免杀与规避`
禁用ETW监控

### API Unhooking
分类: `免杀与规避`
移除EDR的API Hook

### 进程注入
分类: `免杀与规避`
将代码注入到其他进程

### AppLocker绕过
分类: `免杀与规避`
绕过AppLocker应用程序限制

### ProxyLogon攻击
分类: `Exchange攻击`
CVE-2021-26855 Exchange SSRF

### ProxyShell攻击
分类: `Exchange攻击`
CVE-2021-34473 Exchange RCE

### Exchange枚举
分类: `Exchange攻击`
枚举Exchange服务和配置

### SharePoint枚举
分类: `SharePoint攻击`
枚举SharePoint站点和文件

### ADCS ESC2攻击
分类: `ADCS攻击`
利用ESC2模板配置错误

### ADCS ESC3攻击
分类: `ADCS攻击`
利用ESC3注册代理配置错误

### ADCS ESC4攻击
分类: `ADCS攻击`
利用ESC4模板权限配置错误

### ADCS ESC6攻击
分类: `ADCS攻击`
利用ESC6编辑标志配置错误

### ADCS ESC8攻击
分类: `ADCS攻击`
利用ESC8 HTTP端点进行NTLM中继

### SAM The Admin攻击
分类: `域渗透攻击`
CVE-2021-42278/CVE-2021-42287域提权

### NoAuth攻击
分类: `域渗透攻击`
CVE-2022-33679 Kerberos认证绕过

### BlockDLLs技术
分类: `免杀与规避`
阻止非微软DLL加载

### Shellcode加密
分类: `免杀与规避`
加密Shellcode绕过静态检测

### 进程伪装
分类: `免杀与规避`
伪装进程名称和路径

### PPID欺骗
分类: `免杀与规避`
伪造父进程ID

### DLL侧加载
分类: `免杀与规避`
利用DLL搜索顺序加载恶意DLL

### 参数欺骗
分类: `免杀与规避`
欺骗进程参数显示

### 签名二进制利用
分类: `免杀与规避`
利用微软签名二进制执行代码

### CLR注入
分类: `免杀与规避`
CLR内存注入技术

### ProxyToken攻击
分类: `Exchange攻击`
利用Exchange ProxyToken绕过认证

### Exchange邮箱访问
分类: `Exchange攻击`
通过各种方式访问Exchange邮箱

### SharePoint文件访问
分类: `SharePoint攻击`
访问SharePoint文档库中的文件

### 无人值守安装凭证提取
分类: `凭证窃取`
从Windows无人值守安装文件(Unattend.xml/Sysprep)中提取明文或Base64编码的管理员凭证

### Potato系列提权攻击
分类: `权限提升`
利用Windows令牌模拟和NTLM中继机制从服务账户(SeImpersonatePrivilege/SeAssignPrimaryTokenPrivilege)提权到SYSTEM

### BloodHound域分析
分类: `信息收集`
使用BloodHound分析Active Directory攻击路径

### SPN扫描
分类: `信息收集`
扫描域内服务主体名称

### 内网端口扫描
分类: `信息收集`
内网端口扫描与服务识别

### 域信息收集
分类: `信息收集`
Active Directory域环境信息收集

### 网络信息收集
分类: `信息收集`
内网网络拓扑和配置信息收集

### 共享枚举
分类: `信息收集`
枚举网络共享资源

### 用户枚举
分类: `信息收集`
枚举域内用户信息

### 组枚举
分类: `信息收集`
枚举域内组信息

### GPO枚举
分类: `信息收集`
枚举组策略对象

### ACL枚举
分类: `信息收集`
枚举访问控制列表

### 信任关系枚举
分类: `信息收集`
枚举域信任关系

### 计算机枚举
分类: `信息收集`
枚举域内计算机

### Mimikatz凭证抓取
分类: `凭证窃取`
使用Mimikatz抓取Windows系统凭证

### Kerberoasting攻击
分类: `凭证窃取`
Kerberoasting攻击获取服务账户哈希

### AS-REP Roasting
分类: `凭证窃取`
AS-REP Roasting攻击获取用户哈希

### LaZagne凭证抓取
分类: `凭证窃取`
使用LaZagne抓取各种应用程序凭证

### SAM数据库导出
分类: `凭证窃取`
导出Windows SAM数据库获取本地账户哈希

### NTDS.dit导出
分类: `凭证窃取`
导出Active Directory数据库获取所有域用户哈希

### GPP密码提取
分类: `凭证窃取`
提取组策略首选项中的密码

### PsExec横向移动
分类: `横向移动`
使用PsExec进行横向移动

### WMI横向移动
分类: `横向移动`
使用WMI进行横向移动

### Pass-the-Hash攻击
分类: `横向移动`
使用NTLM哈希进行身份验证

### NTLM Relay攻击
分类: `横向移动`
NTLM中继攻击技术

### 令牌窃取与模拟
分类: `权限提升`
窃取和模拟Windows访问令牌

### 注册表持久化
分类: `权限维持`
通过注册表实现权限维持

### FRP内网穿透
分类: `隧道代理`
使用FRP建立内网穿透隧道

### Chisel内网穿透
分类: `隧道代理`
使用Chisel建立内网穿透隧道

### PowerShell免杀
分类: `免杀与规避`
PowerShell脚本免杀技术

### 域内权限提升路径
分类: `域渗透攻击`
利用ACL错误配置进行域权限提升

### 跨域信任攻击
分类: `域渗透攻击`
利用域信任关系进行跨域攻击

### Mimikatz高级技巧
分类: `凭证窃取`
Mimikatz高级凭证提取和利用技术

### 浏览器凭证提取
分类: `凭证窃取`
从浏览器中提取保存的密码和Cookie

### DPAPI凭证提取
分类: `凭证窃取`
从DPAPI保护存储中提取凭证

### RDP凭证提取
分类: `凭证窃取`
提取保存的RDP连接密码

### WiFi凭证提取
分类: `凭证窃取`
提取保存的WiFi密码

### Windows Vault凭证
分类: `凭证窃取`
从Windows凭据管理器提取凭证

### KeePass凭证提取
分类: `凭证窃取`
从KeePass数据库提取密码

### LSA Secrets提取
分类: `凭证窃取`
从LSA Secrets提取敏感数据

### 缓存凭证提取
分类: `凭证窃取`
提取域缓存凭证

### WinRM横向移动
分类: `横向移动`
通过WinRM进行横向移动

### DCOM横向移动
分类: `横向移动`
通过DCOM进行横向移动

### SSH横向移动
分类: `横向移动`
通过SSH进行横向移动

### RDP会话劫持
分类: `横向移动`
劫持已存在的RDP会话

### Overpass-the-Hash
分类: `横向移动`
使用哈希获取Kerberos票据

### Pass-the-Ticket
分类: `横向移动`
使用Kerberos票据进行横向移动

### SMBExec横向移动
分类: `横向移动`
通过SMB执行命令

### ATExec横向移动
分类: `横向移动`
通过计划任务执行命令

### WinRS横向移动
分类: `横向移动`
通过WinRS执行远程命令

### Windows权限提升
分类: `权限提升`
Windows系统提权技术

### Linux权限提升
分类: `权限提升`
Linux系统提权技术

### UAC绕过
分类: `权限提升`
绕过Windows用户账户控制

### DLL劫持
分类: `权限提升`
通过DLL劫持提权

### 服务提权
分类: `权限提升`
通过服务漏洞提权

### AlwaysInstallElevated提权
分类: `权限提升`
利用AlwaysInstallElevated提权

### Juicy Potato提权
分类: `权限提升`
利用COM对象和SeImpersonatePrivilege提权

### PrintSpoofer提权
分类: `权限提升`
利用打印机服务提权

### GodPotato提权
分类: `权限提升`
GodPotato提权工具

### SUID提权
分类: `权限提升`
利用SUID文件提权

### Sudo提权
分类: `权限提升`
利用Sudo配置提权

### Cron提权
分类: `权限提升`
利用Cron任务提权

### 内核漏洞提权
分类: `权限提升`
利用内核漏洞提权

### WMI持久化
分类: `权限维持`
通过WMI事件订阅实现持久化

### 启动文件夹持久化
分类: `权限维持`
通过启动文件夹实现持久化

### 服务持久化
分类: `权限维持`
通过创建服务实现持久化

### DLL注入持久化
分类: `权限维持`
通过DLL注入实现持久化

### 后门用户
分类: `权限维持`
创建后门用户账户

### 隐藏用户
分类: `权限维持`
创建隐藏的管理员用户

### ReGeorg隧道
分类: `隧道代理`
通过Web Shell建立隧道

### SSH本地转发
分类: `隧道代理`
SSH本地端口转发

### SSH远程转发
分类: `隧道代理`
SSH远程端口转发

### SSH动态转发
分类: `隧道代理`
SSH动态SOCKS代理

### DNS隧道
分类: `隧道代理`
通过DNS协议建立隧道

### ICMP隧道
分类: `隧道代理`
通过ICMP协议建立隧道

### Ligolo隧道
分类: `隧道代理`
Ligolo内网穿透工具

### DCSync攻击
分类: `凭证窃取`
模拟域控制器同步获取凭证

### 黄金票据攻击
分类: `凭证窃取`
使用krbtgt哈希生成黄金票据

### 白银票据攻击
分类: `凭证窃取`
使用服务账户哈希生成白银票据

### AMSI绕过
分类: `免杀与规避`
绕过反恶意软件扫描接口

### Excel DCOM横向移动
分类: `横向移动`
利用Excel DCOM进行横向移动

### MMC DCOM横向移动
分类: `横向移动`
利用MMC DCOM进行横向移动

### RDP Relay攻击
分类: `横向移动`
RDP中继攻击技术

### 计划任务持久化
分类: `权限维持`
通过计划任务实现持久化

### Skeleton Key后门
分类: `权限维持`
在域控制器植入万能密码

### DSRM后门
分类: `权限维持`
利用DSRM账户建立后门

### SID History后门
分类: `权限维持`
利用SID History建立后门

### 进程镂空持久化
分类: `权限维持`
利用进程镂空技术实现持久化

### SOCKS代理
分类: `隧道代理`
建立SOCKS代理访问内网

### Ngrok内网穿透
分类: `隧道代理`
使用Ngrok建立内网穿透

### EW内网穿透
分类: `隧道代理`
使用EW建立内网穿透

### Venom内网穿透
分类: `隧道代理`
使用Venom建立内网穿透

### Zerologon攻击
分类: `域渗透攻击`
CVE-2020-1472 Netlogon提权

### PrintNightmare攻击
分类: `域渗透攻击`
CVE-2021-34527 打印服务漏洞

### PetitPotam攻击
分类: `域渗透攻击`
CVE-2021-36942 强制认证攻击

### noPac/SAMAccountName攻击
分类: `域渗透攻击`
CVE-2021-42278/CVE-2021-42287 域提权

### ADCS滥用攻击
分类: `域渗透攻击`
Active Directory证书服务滥用

### ADCS ESC1漏洞
分类: `域渗透攻击`
证书模板ESC1滥用

### 约束委派攻击
分类: `域渗透攻击`
利用约束委派进行横向移动

### 基于资源的约束委派
分类: `域渗透攻击`
利用RBCD进行权限提升

### DCShadow攻击
分类: `域渗透攻击`
伪造域控制器注入数据

### 组策略滥用
分类: `域渗透攻击`
滥用组策略进行横向移动

### ETW Patch绕过
分类: `免杀与规避`
禁用ETW监控

### API Unhooking
分类: `免杀与规避`
移除EDR的API Hook

### 进程注入
分类: `免杀与规避`
将代码注入到其他进程

### AppLocker绕过
分类: `免杀与规避`
绕过AppLocker应用程序限制

### ProxyLogon攻击
分类: `Exchange攻击`
CVE-2021-26855 Exchange SSRF

### ProxyShell攻击
分类: `Exchange攻击`
CVE-2021-34473 Exchange RCE

### Exchange枚举
分类: `Exchange攻击`
枚举Exchange服务和配置

### SharePoint枚举
分类: `SharePoint攻击`
枚举SharePoint站点和文件

### ADCS ESC2攻击
分类: `ADCS攻击`
利用ESC2模板配置错误

### ADCS ESC3攻击
分类: `ADCS攻击`
利用ESC3注册代理配置错误

### ADCS ESC4攻击
分类: `ADCS攻击`
利用ESC4模板权限配置错误

### ADCS ESC6攻击
分类: `ADCS攻击`
利用ESC6编辑标志配置错误

### ADCS ESC8攻击
分类: `ADCS攻击`
利用ESC8 HTTP端点进行NTLM中继

### SAM The Admin攻击
分类: `域渗透攻击`
CVE-2021-42278/CVE-2021-42287域提权

### NoAuth攻击
分类: `域渗透攻击`
CVE-2022-33679 Kerberos认证绕过

### BlockDLLs技术
分类: `免杀与规避`
阻止非微软DLL加载

### Shellcode加密
分类: `免杀与规避`
加密Shellcode绕过静态检测

### 进程伪装
分类: `免杀与规避`
伪装进程名称和路径

### PPID欺骗
分类: `免杀与规避`
伪造父进程ID

### DLL侧加载
分类: `免杀与规避`
利用DLL搜索顺序加载恶意DLL

### 参数欺骗
分类: `免杀与规避`
欺骗进程参数显示

### 签名二进制利用
分类: `免杀与规避`
利用微软签名二进制执行代码

### CLR注入
分类: `免杀与规避`
CLR内存注入技术

### ProxyToken攻击
分类: `Exchange攻击`
利用Exchange ProxyToken绕过认证

### Exchange邮箱访问
分类: `Exchange攻击`
通过各种方式访问Exchange邮箱

### SharePoint文件访问
分类: `SharePoint攻击`
访问SharePoint文档库中的文件

### 无人值守安装凭证提取
分类: `凭证窃取`
从Windows无人值守安装文件(Unattend.xml/Sysprep)中提取明文或Base64编码的管理员凭证

### Potato系列提权攻击
分类: `权限提升`
利用Windows令牌模拟和NTLM中继机制从服务账户(SeImpersonatePrivilege/SeAssignPrimaryTokenPrivilege)提权到SYSTEM

## navigation

### 🌐 Web应用攻防

### 🏢 内网渗透与横向移动

### 🌐 Web应用攻防

### 🏢 内网渗透与横向移动

### 🔍 信息收集工具

### 🌐 Web渗透工具

### 💥 漏洞利用工具

### 🔐 密码攻击工具

### 🏢 内网渗透工具

### 💻 系统命令

### 🐚 反弹Shell

### 🔧 编码解码工具

## toolCommands

### Nmap
分类: `信息收集`
网络扫描和安全审计工具

### SQLMap
分类: `Web渗透`
自动化SQL注入工具

### Metasploit
分类: `漏洞利用`
渗透测试框架

### Hydra
分类: `密码攻击`
网络登录破解工具

### John the Ripper
分类: `密码攻击`
密码破解工具

### Hashcat
分类: `密码攻击`
GPU加速密码破解工具

### CrackMapExec
分类: `内网渗透`
内网渗透瑞士军刀

### Impacket
分类: `内网渗透`
Python网络协议库

### PowerShell渗透命令
分类: `Windows渗透`
PowerShell渗透测试常用命令

### Linux提权命令
分类: `权限提升`
Linux系统提权常用命令

### Gobuster
分类: `信息收集`
目录和子域名爆破工具

### Burp Suite
分类: `Web渗透`
Web安全测试平台

### FFUF
分类: `Web渗透`
快速Web模糊测试工具

### Responder
分类: `内网渗透`
LLMNR/NBT-NS/MDNS Poisoner

### Evil-WinRM
分类: `内网渗透`
WinRM远程管理工具

### ProxyChains
分类: `内网渗透`
代理链工具

### Bash反弹Shell
分类: `反弹Shell`
Bash反弹Shell命令

### Python反弹Shell
分类: `反弹Shell`
Python反弹Shell命令

### PowerShell反弹Shell
分类: `反弹Shell`
PowerShell反弹Shell命令

### Netcat反弹Shell
分类: `反弹Shell`
Netcat反弹Shell命令

### Nuclei
分类: `信息收集`
快速漏洞扫描工具

### Windows CMD命令
分类: `系统命令`
Windows系统常用命令

### NET命令集合
分类: `系统命令`
Windows NET命令完整集合

### BloodHound
分类: `内网渗透`
Active Directory关系分析工具

### Mimikatz
分类: `凭证窃取`
Windows凭证提取工具

### Rubeus
分类: `凭证窃取`
Kerberos攻击工具

### Certipy
分类: `域渗透`
ADCS证书服务攻击工具

### Kerbrute
分类: `密码攻击`
Kerberos暴力破解工具

### SharpHound
分类: `内网渗透`
BloodHound数据采集器

### Seatbelt
分类: `信息收集`
Windows安全信息收集工具

### WinPEAS
分类: `权限提升`
Windows提权辅助工具

### LinPEAS
分类: `权限提升`
Linux提权辅助工具

### Chisel
分类: `隧道代理`
HTTP隧道工具

### Ligolo-ng
分类: `隧道代理`
隧道工具

### SharpSMBClient
分类: `内网渗透`
SMB客户端工具

### DonPAPI
分类: `凭证窃取`
DPAPI凭证提取工具

### PowerSploit
分类: `内网渗透`
PowerShell渗透测试框架

### Cobalt Strike
分类: `红队工具`
红队渗透测试框架

### SearchSploit
分类: `信息收集`
漏洞搜索工具

### WFuzz
分类: `Web渗透`
Web模糊测试工具

### Amass
分类: `信息收集`
子域名枚举工具

### Subfinder
分类: `信息收集`
子域名发现工具

### HTTPX
分类: `信息收集`
HTTP探测工具

### Masscan
分类: `信息收集`
最快的互联网端口扫描器，可在5分钟内扫描整个互联网

### Dirsearch
分类: `信息收集`
高级Web目录和文件暴力破解工具

### FeroxBuster
分类: `信息收集`
用Rust编写的高性能递归目录发现工具

### MassDNS
分类: `信息收集`
高性能DNS解析器，用于子域名暴力枚举

### Amass
分类: `信息收集`
OWASP出品的深度攻击面映射和资产发现工具

### Subfinder
分类: `信息收集`
被动子域名发现工具，支持多种在线数据源

### HTTPX
分类: `信息收集`
快速多功能HTTP探针工具，用于批量探测Web服务

### WhatWeb
分类: `信息收集`
Web指纹识别工具，识别网站使用的技术栈

### WAFW00F
分类: `信息收集`
Web应用防火墙(WAF)检测和指纹识别工具

### DNSRecon
分类: `信息收集`
DNS枚举和信息收集工具

### DNSEnum
分类: `信息收集`
DNS信息收集工具，支持区域传送和子域名枚举

### theHarvester
分类: `信息收集`
邮箱、子域名、IP等OSINT信息收集工具

### Nikto
分类: `Web渗透`
Web服务器漏洞扫描器，检测危险文件、过时组件和配置问题

### OWASP ZAP
分类: `Web渗透`
OWASP官方Web应用安全测试平台

### Arjun
分类: `Web渗透`
HTTP参数发现工具，发现隐藏的GET/POST参数

### WFuzz
分类: `Web渗透`
Web应用模糊测试工具，用于暴力破解参数、目录、认证等

### Commix
分类: `Web渗透`
自动化命令注入漏洞检测和利用工具

### Dalfox
分类: `Web渗透`
基于Go的高性能XSS漏洞扫描和参数分析工具

### XSStrike
分类: `Web渗透`
高级XSS检测工具，支持反射/存储/DOM型XSS检测

### Gopherus
分类: `Web渗透`
生成Gopher协议Payload，用于SSRF攻击内部服务

### Smuggler
分类: `Web渗透`
HTTP请求走私漏洞检测工具

### JWT Tool
分类: `Web渗透`
JSON Web Token安全测试工具，支持伪造/破解/注入

### GraphQLmap
分类: `Web渗透`
GraphQL API渗透测试工具，支持自省查询和注入

### Cadaver
分类: `Web渗透`
WebDAV客户端工具，用于测试WebDAV服务

### Searchsploit
分类: `漏洞利用`
Exploit-DB本地搜索工具，离线查找漏洞利用代码

### ExploitDB
分类: `漏洞利用`
漏洞利用代码数据库在线搜索

### ysoserial
分类: `漏洞利用`
Java反序列化漏洞利用Payload生成工具

### ysoserial.net
分类: `漏洞利用`
.NET反序列化Payload生成工具

### Marshalsec
分类: `漏洞利用`
Java反序列化利用工具，支持多种Marshal格式和JNDI注入

### JNDIExploit
分类: `漏洞利用`
JNDI注入利用工具，集成多种Gadget和Bypass

### Rogue JNDI
分类: `漏洞利用`
恶意JNDI服务器，提供多种攻击向量

### Cobalt Strike
分类: `漏洞利用`
商业化红队C2框架，支持多种攻击和后渗透功能

### Sliver
分类: `漏洞利用`
开源跨平台红队C2框架，Cobalt Strike替代品

### Mythic
分类: `漏洞利用`
模块化C2框架，支持多种Agent和自定义扩展

### Medusa
分类: `密码攻击`
快速并行网络登录暴力破解工具

### Ncrack
分类: `密码攻击`
Nmap项目出品的高速网络认证破解工具

### Crowbar
分类: `密码攻击`
专注RDP/VNC/SSH密钥/OpenVPN的暴力破解工具

### Patator
分类: `密码攻击`
多用途模块化暴力破解工具，支持数十种协议

### CrackStation
分类: `密码攻击`
在线哈希查询和离线超大字典

### SecLists字典
分类: `密码攻击`
安全测试人员必备的字典集合(目录、密码、用户名、Payload等)

### RockYou字典
分类: `密码攻击`
来自2009年RockYou数据泄露的经典密码字典(1400万+)

### NetExec
分类: `内网渗透`
CrackMapExec的继任者，网络渗透测试自动化工具

### Ligolo-ng
分类: `内网渗透`
高级内网隧道代理工具，基于TUN接口

### SharpHound
分类: `内网渗透`
BloodHound的C#数据收集器，在Windows域内收集AD信息

### BloodHound-Python
分类: `内网渗透`
BloodHound的Python数据收集器，可从Linux远程收集AD信息

### Rubeus
分类: `内网渗透`
Kerberos攻击工具集，用于票据操作和Kerberos攻击

### Certipy
分类: `内网渗透`
AD CS(Active Directory证书服务)攻击工具

### LaZagne
分类: `内网渗透`
自动化本地密码恢复工具，支持数十种应用

### Seatbelt
分类: `内网渗透`
C#安全审计工具，快速收集Windows系统安全相关信息

### WinPEAS
分类: `内网渗透`
Windows权限提升辅助脚本，自动发现提权路径

### LinPEAS
分类: `内网渗透`
Linux权限提升辅助脚本，自动发现提权路径

### PowerShell AMSI绕过
分类: `系统命令`
Windows AMSI(反恶意软件扫描接口)绕过技术集合

### WMIC命令
分类: `系统命令`
Windows Management Instrumentation命令行工具

### DSQuery命令
分类: `系统命令`
Active Directory查询命令行工具

### AD Explorer
分类: `系统命令`
Sysinternals出品的Active Directory浏览器和快照工具

### ldeep
分类: `系统命令`
LDAP深度枚举工具，用于从Linux远程查询AD信息

### BloodHound Cypher
分类: `系统命令`
BloodHound Neo4j Cypher查询语句集合

### PHP反弹Shell
分类: `反弹Shell`
PHP语言反弹Shell命令集合

### Java反弹Shell
分类: `反弹Shell`
Java语言反弹Shell命令集合

### Perl反弹Shell
分类: `反弹Shell`
Perl语言反弹Shell命令

### Ruby反弹Shell
分类: `反弹Shell`
Ruby语言反弹Shell命令

### Node.js反弹Shell
分类: `反弹Shell`
Node.js语言反弹Shell命令

### Groovy反弹Shell
分类: `反弹Shell`
Groovy语言反弹Shell(常用于Jenkins)

### Lua反弹Shell
分类: `反弹Shell`
Lua语言反弹Shell命令

### AWK反弹Shell
分类: `反弹Shell`
AWK语言反弹Shell命令

### Base64编码
分类: `编码解码`
Base64编码/解码命令集合

### URL编码
分类: `编码解码`
URL编码/解码命令集合

### Hex编码
分类: `编码解码`
十六进制编码/解码命令集合

### HTML编码
分类: `编码解码`
HTML实体编码/解码命令集合

### Unicode编码
分类: `编码解码`
Unicode编码/解码命令集合

### JWT解码
分类: `编码解码`
JWT(JSON Web Token)解码和分析工具

### Nmap
分类: `信息收集`
网络扫描和安全审计工具

### SQLMap
分类: `Web渗透`
自动化SQL注入工具

### Metasploit
分类: `漏洞利用`
渗透测试框架

### Hydra
分类: `密码攻击`
网络登录破解工具

### John the Ripper
分类: `密码攻击`
密码破解工具

### Hashcat
分类: `密码攻击`
GPU加速密码破解工具

### CrackMapExec
分类: `内网渗透`
内网渗透瑞士军刀

### Impacket
分类: `内网渗透`
Python网络协议库

### PowerShell渗透命令
分类: `Windows渗透`
PowerShell渗透测试常用命令

### Linux提权命令
分类: `权限提升`
Linux系统提权常用命令

### Gobuster
分类: `信息收集`
目录和子域名爆破工具

### Burp Suite
分类: `Web渗透`
Web安全测试平台

### FFUF
分类: `Web渗透`
快速Web模糊测试工具

### Responder
分类: `内网渗透`
LLMNR/NBT-NS/MDNS Poisoner

### Evil-WinRM
分类: `内网渗透`
WinRM远程管理工具

### ProxyChains
分类: `内网渗透`
代理链工具

### Bash反弹Shell
分类: `反弹Shell`
Bash反弹Shell命令

### Python反弹Shell
分类: `反弹Shell`
Python反弹Shell命令

### PowerShell反弹Shell
分类: `反弹Shell`
PowerShell反弹Shell命令

### Netcat反弹Shell
分类: `反弹Shell`
Netcat反弹Shell命令

### Nuclei
分类: `信息收集`
快速漏洞扫描工具

### Windows CMD命令
分类: `系统命令`
Windows系统常用命令

### NET命令集合
分类: `系统命令`
Windows NET命令完整集合

### BloodHound
分类: `内网渗透`
Active Directory关系分析工具

### Mimikatz
分类: `凭证窃取`
Windows凭证提取工具

### Rubeus
分类: `凭证窃取`
Kerberos攻击工具

### Certipy
分类: `域渗透`
ADCS证书服务攻击工具

### Kerbrute
分类: `密码攻击`
Kerberos暴力破解工具

### SharpHound
分类: `内网渗透`
BloodHound数据采集器

### Seatbelt
分类: `信息收集`
Windows安全信息收集工具

### WinPEAS
分类: `权限提升`
Windows提权辅助工具

### LinPEAS
分类: `权限提升`
Linux提权辅助工具

### Chisel
分类: `隧道代理`
HTTP隧道工具

### Ligolo-ng
分类: `隧道代理`
隧道工具

### SharpSMBClient
分类: `内网渗透`
SMB客户端工具

### DonPAPI
分类: `凭证窃取`
DPAPI凭证提取工具

### PowerSploit
分类: `内网渗透`
PowerShell渗透测试框架

### Cobalt Strike
分类: `红队工具`
红队渗透测试框架

### SearchSploit
分类: `信息收集`
漏洞搜索工具

### WFuzz
分类: `Web渗透`
Web模糊测试工具

### Amass
分类: `信息收集`
子域名枚举工具

### Subfinder
分类: `信息收集`
子域名发现工具

### HTTPX
分类: `信息收集`
HTTP探测工具

### Masscan
分类: `信息收集`
最快的互联网端口扫描器，可在5分钟内扫描整个互联网

### Dirsearch
分类: `信息收集`
高级Web目录和文件暴力破解工具

### FeroxBuster
分类: `信息收集`
用Rust编写的高性能递归目录发现工具

### MassDNS
分类: `信息收集`
高性能DNS解析器，用于子域名暴力枚举

### Amass
分类: `信息收集`
OWASP出品的深度攻击面映射和资产发现工具

### Subfinder
分类: `信息收集`
被动子域名发现工具，支持多种在线数据源

### HTTPX
分类: `信息收集`
快速多功能HTTP探针工具，用于批量探测Web服务

### WhatWeb
分类: `信息收集`
Web指纹识别工具，识别网站使用的技术栈

### WAFW00F
分类: `信息收集`
Web应用防火墙(WAF)检测和指纹识别工具

### DNSRecon
分类: `信息收集`
DNS枚举和信息收集工具

### DNSEnum
分类: `信息收集`
DNS信息收集工具，支持区域传送和子域名枚举

### theHarvester
分类: `信息收集`
邮箱、子域名、IP等OSINT信息收集工具

### Nikto
分类: `Web渗透`
Web服务器漏洞扫描器，检测危险文件、过时组件和配置问题

### OWASP ZAP
分类: `Web渗透`
OWASP官方Web应用安全测试平台

### Arjun
分类: `Web渗透`
HTTP参数发现工具，发现隐藏的GET/POST参数

### WFuzz
分类: `Web渗透`
Web应用模糊测试工具，用于暴力破解参数、目录、认证等

### Commix
分类: `Web渗透`
自动化命令注入漏洞检测和利用工具

### Dalfox
分类: `Web渗透`
基于Go的高性能XSS漏洞扫描和参数分析工具

### XSStrike
分类: `Web渗透`
高级XSS检测工具，支持反射/存储/DOM型XSS检测

### Gopherus
分类: `Web渗透`
生成Gopher协议Payload，用于SSRF攻击内部服务

### Smuggler
分类: `Web渗透`
HTTP请求走私漏洞检测工具

### JWT Tool
分类: `Web渗透`
JSON Web Token安全测试工具，支持伪造/破解/注入

### GraphQLmap
分类: `Web渗透`
GraphQL API渗透测试工具，支持自省查询和注入

### Cadaver
分类: `Web渗透`
WebDAV客户端工具，用于测试WebDAV服务

### Searchsploit
分类: `漏洞利用`
Exploit-DB本地搜索工具，离线查找漏洞利用代码

### ExploitDB
分类: `漏洞利用`
漏洞利用代码数据库在线搜索

### ysoserial
分类: `漏洞利用`
Java反序列化漏洞利用Payload生成工具

### ysoserial.net
分类: `漏洞利用`
.NET反序列化Payload生成工具

### Marshalsec
分类: `漏洞利用`
Java反序列化利用工具，支持多种Marshal格式和JNDI注入

### JNDIExploit
分类: `漏洞利用`
JNDI注入利用工具，集成多种Gadget和Bypass

### Rogue JNDI
分类: `漏洞利用`
恶意JNDI服务器，提供多种攻击向量

### Cobalt Strike
分类: `漏洞利用`
商业化红队C2框架，支持多种攻击和后渗透功能

### Sliver
分类: `漏洞利用`
开源跨平台红队C2框架，Cobalt Strike替代品

### Mythic
分类: `漏洞利用`
模块化C2框架，支持多种Agent和自定义扩展

### Medusa
分类: `密码攻击`
快速并行网络登录暴力破解工具

### Ncrack
分类: `密码攻击`
Nmap项目出品的高速网络认证破解工具

### Crowbar
分类: `密码攻击`
专注RDP/VNC/SSH密钥/OpenVPN的暴力破解工具

### Patator
分类: `密码攻击`
多用途模块化暴力破解工具，支持数十种协议

### CrackStation
分类: `密码攻击`
在线哈希查询和离线超大字典

### SecLists字典
分类: `密码攻击`
安全测试人员必备的字典集合(目录、密码、用户名、Payload等)

### RockYou字典
分类: `密码攻击`
来自2009年RockYou数据泄露的经典密码字典(1400万+)

### NetExec
分类: `内网渗透`
CrackMapExec的继任者，网络渗透测试自动化工具

### Ligolo-ng
分类: `内网渗透`
高级内网隧道代理工具，基于TUN接口

### SharpHound
分类: `内网渗透`
BloodHound的C#数据收集器，在Windows域内收集AD信息

### BloodHound-Python
分类: `内网渗透`
BloodHound的Python数据收集器，可从Linux远程收集AD信息

### Rubeus
分类: `内网渗透`
Kerberos攻击工具集，用于票据操作和Kerberos攻击

### Certipy
分类: `内网渗透`
AD CS(Active Directory证书服务)攻击工具

### LaZagne
分类: `内网渗透`
自动化本地密码恢复工具，支持数十种应用

### Seatbelt
分类: `内网渗透`
C#安全审计工具，快速收集Windows系统安全相关信息

### WinPEAS
分类: `内网渗透`
Windows权限提升辅助脚本，自动发现提权路径

### LinPEAS
分类: `内网渗透`
Linux权限提升辅助脚本，自动发现提权路径

### PowerShell AMSI绕过
分类: `系统命令`
Windows AMSI(反恶意软件扫描接口)绕过技术集合

### WMIC命令
分类: `系统命令`
Windows Management Instrumentation命令行工具

### DSQuery命令
分类: `系统命令`
Active Directory查询命令行工具

### AD Explorer
分类: `系统命令`
Sysinternals出品的Active Directory浏览器和快照工具

### ldeep
分类: `系统命令`
LDAP深度枚举工具，用于从Linux远程查询AD信息

### BloodHound Cypher
分类: `系统命令`
BloodHound Neo4j Cypher查询语句集合

### PHP反弹Shell
分类: `反弹Shell`
PHP语言反弹Shell命令集合

### Java反弹Shell
分类: `反弹Shell`
Java语言反弹Shell命令集合

### Perl反弹Shell
分类: `反弹Shell`
Perl语言反弹Shell命令

### Ruby反弹Shell
分类: `反弹Shell`
Ruby语言反弹Shell命令

### Node.js反弹Shell
分类: `反弹Shell`
Node.js语言反弹Shell命令

### Groovy反弹Shell
分类: `反弹Shell`
Groovy语言反弹Shell(常用于Jenkins)

### Lua反弹Shell
分类: `反弹Shell`
Lua语言反弹Shell命令

### AWK反弹Shell
分类: `反弹Shell`
AWK语言反弹Shell命令

### Base64编码
分类: `编码解码`
Base64编码/解码命令集合

### URL编码
分类: `编码解码`
URL编码/解码命令集合

### Hex编码
分类: `编码解码`
十六进制编码/解码命令集合

### HTML编码
分类: `编码解码`
HTML实体编码/解码命令集合

### Unicode编码
分类: `编码解码`
Unicode编码/解码命令集合

### JWT解码
分类: `编码解码`
JWT(JSON Web Token)解码和分析工具

## webPayloads

### MySQL注入 - 基础探测
分类: `SQL/NoSQL注入`
MySQL数据库注入基础探测与数据提取技术

### MySQL注入 - 高级技术
分类: `SQL/NoSQL注入`
MySQL高级注入技术：文件读写、UDF提权、命令执行

### MSSQL注入 - 基础探测
分类: `SQL/NoSQL注入`
Microsoft SQL Server数据库注入技术

### MSSQL注入 - 高级技术
分类: `SQL/NoSQL注入`
MSSQL高级注入：xp_cmdshell、SP_OACREATE命令执行

### Oracle注入 - 基础探测
分类: `SQL/NoSQL注入`
Oracle数据库注入基础技术

### Oracle注入 - 高级技术
分类: `SQL/NoSQL注入`
Oracle高级注入技术：Java存储过程、UTL_FILE文件操作

### PostgreSQL注入 - 基础探测
分类: `SQL/NoSQL注入`
PostgreSQL数据库注入技术

### SQLite注入
分类: `SQL/NoSQL注入`
SQLite数据库注入攻击

### MongoDB注入
分类: `SQL/NoSQL注入`
NoSQL数据库注入攻击技术

### Redis未授权访问
分类: `SQL/NoSQL注入`
Redis未授权访问和命令注入

### 布尔盲注
分类: `SQL/NoSQL注入`
基于布尔条件的SQL盲注技术

### 时间盲注
分类: `SQL/NoSQL注入`
基于时间延迟的SQL盲注技术

### 报错注入
分类: `SQL/NoSQL注入`
利用错误信息提取数据的SQL注入

### 二阶SQL注入
分类: `SQL/NoSQL注入`
存储后触发的SQL注入攻击

### 联合查询注入
分类: `SQL/NoSQL注入`
使用UNION SELECT提取数据

### 堆叠查询注入
分类: `SQL/NoSQL注入`
执行多条SQL语句的注入

### 反射型XSS
分类: `XSS跨站脚本`
反射型跨站脚本攻击技术

### 存储型XSS
分类: `XSS跨站脚本`
存储型跨站脚本攻击技术

### DOM型XSS
分类: `XSS跨站脚本`
基于DOM的跨站脚本攻击

### CSP绕过
分类: `XSS跨站脚本`
绕过内容安全策略(CSP)的XSS技术

### 基础SSRF攻击
分类: `SSRF服务端请求伪造`
服务端请求伪造基础攻击技术

### AWS元数据攻击
分类: `SSRF服务端请求伪造`
利用SSRF访问AWS EC2元数据服务

### 命令注入
分类: `RCE远程代码执行`
操作系统命令注入攻击技术

### XXE基础攻击
分类: `XXE实体注入`
XML外部实体注入基础攻击技术

### Jinja2模板注入
分类: `SSTI模板注入`
Jinja2/Twig模板注入攻击技术

### FreeMarker模板注入
分类: `SSTI模板注入`
FreeMarker模板引擎注入攻击技术

### Velocity模板注入
分类: `SSTI模板注入`
Velocity模板引擎注入攻击技术

### Thymeleaf模板注入
分类: `SSTI模板注入`
Thymeleaf模板引擎注入攻击技术

### Smarty模板注入
分类: `SSTI模板注入`
Smarty模板引擎注入攻击技术

### Mako模板注入
分类: `SSTI模板注入`
Mako模板引擎注入攻击技术

### Tornado模板注入
分类: `SSTI模板注入`
Tornado模板引擎注入攻击技术

### Django模板注入
分类: `SSTI模板注入`
Django模板引擎注入攻击技术

### ERB模板注入
分类: `SSTI模板注入`
ERB(Ruby)模板引擎注入攻击技术

### Pug/Jade模板注入
分类: `SSTI模板注入`
Pug/Jade模板引擎注入攻击技术

### 本地文件包含
分类: `LFI/RFI文件包含`
本地文件包含漏洞利用技术

### 远程文件包含
分类: `LFI/RFI文件包含`
远程文件包含漏洞利用技术

### 日志投毒LFI
分类: `LFI/RFI文件包含`
通过日志投毒实现LFI到RCE

### PHP伪协议利用
分类: `LFI/RFI文件包含`
利用PHP伪协议进行LFI攻击

### 目录遍历技术
分类: `LFI/RFI文件包含`
LFI目录遍历绕过技术

### PHP Filter链攻击
分类: `LFI/RFI文件包含`
利用PHP Filter链进行LFI攻击

### PHP Input执行
分类: `LFI/RFI文件包含`
利用php://input执行PHP代码

### PHP Data协议攻击
分类: `LFI/RFI文件包含`
利用data://协议执行PHP代码

### PHP Zip协议攻击
分类: `LFI/RFI文件包含`
利用zip://协议进行LFI攻击

### Phar反序列化攻击
分类: `LFI/RFI文件包含`
利用Phar反序列化进行RCE

### Session文件包含
分类: `LFI/RFI文件包含`
利用Session文件进行LFI攻击

### Proc文件系统利用
分类: `LFI/RFI文件包含`
利用/proc文件系统进行LFI攻击

### CSRF基础攻击
分类: `CSRF跨站请求伪造`
跨站请求伪造基础攻击技术

### JSON CSRF攻击
分类: `CSRF跨站请求伪造`
针对JSON请求的CSRF攻击技术

### CSRF绕过技术
分类: `CSRF跨站请求伪造`
绕过CSRF防护的各种技术

### SameSite绕过技术
分类: `CSRF跨站请求伪造`
绕过SameSite Cookie属性的CSRF攻击

### Token绕过技术
分类: `CSRF跨站请求伪造`
绕过CSRF Token验证的技术

### Referer绕过技术
分类: `CSRF跨站请求伪造`
绕过Referer验证的CSRF攻击

### Flash CSRF攻击
分类: `CSRF跨站请求伪造`
利用Flash进行CSRF攻击

### CORS配置错误利用
分类: `CSRF跨站请求伪造`
利用CORS配置错误进行CSRF攻击

### JWT安全漏洞
分类: `API安全`
JSON Web Token安全漏洞利用

### Log4j RCE (Log4Shell)
分类: `框架漏洞`
Apache Log4j远程代码执行漏洞

### Spring Actuator漏洞
分类: `框架漏洞`
Spring Boot Actuator端点安全漏洞

### Fastjson RCE
分类: `框架漏洞`
Alibaba Fastjson反序列化远程代码执行

### 突变型XSS(mXSS)
分类: `XSS跨站脚本`
利用浏览器解析差异导致的XSS攻击

### Unicode XSS
分类: `XSS跨站脚本`
利用Unicode编码特性绕过过滤

### XSS过滤器绕过
分类: `XSS跨站脚本`
各种绕过XSS过滤器的技术

### XSS编码绕过
分类: `XSS跨站脚本`
利用各种编码技术绕过XSS过滤

### Polyglot XSS
分类: `XSS跨站脚本`
多环境通用的XSS payload

### XSS Cookie窃取
分类: `XSS跨站脚本`
利用XSS窃取用户Cookie

### XSS键盘记录
分类: `XSS跨站脚本`
利用XSS记录用户键盘输入

### BeEF框架利用
分类: `XSS跨站脚本`
使用BeEF框架进行XSS利用

### GCP元数据攻击
分类: `SSRF服务端请求伪造`
利用SSRF攻击Google Cloud元数据服务

### Azure元数据攻击
分类: `SSRF服务端请求伪造`
利用SSRF攻击Azure元数据服务

### SSRF协议利用
分类: `SSRF服务端请求伪造`
利用各种协议进行SSRF攻击

### Gopher协议攻击
分类: `SSRF服务端请求伪造`
利用Gopher协议攻击内网服务

### Dict协议攻击
分类: `SSRF服务端请求伪造`
利用Dict协议探测和攻击内网服务

### File协议攻击
分类: `SSRF服务端请求伪造`
利用File协议读取本地文件

### SSRF绕过技术
分类: `SSRF服务端请求伪造`
各种绕过SSRF过滤的技术

### DNS重绑定攻击
分类: `SSRF服务端请求伪造`
利用DNS重绑定绕过SSRF防护

### SSRF攻击Redis
分类: `SSRF服务端请求伪造`
利用SSRF攻击内网Redis服务

### SSRF攻击MySQL
分类: `SSRF服务端请求伪造`
利用SSRF攻击内网MySQL服务

### PHP代码执行
分类: `RCE远程代码执行`
PHP代码执行漏洞利用技术

### PHP Filter链RCE
分类: `RCE远程代码执行`
利用PHP Filter链构造RCE

### 盲命令注入
分类: `RCE远程代码执行`
无回显的命令注入利用技术

### 反序列化漏洞
分类: `RCE远程代码执行`
利用反序列化漏洞实现RCE

### PHP反序列化
分类: `RCE远程代码执行`
PHP反序列化漏洞利用技术

### Java反序列化
分类: `RCE远程代码执行`
Java反序列化漏洞利用技术

### 文件上传漏洞
分类: `RCE远程代码执行`
利用文件上传漏洞获取RCE

### 文件包含RCE
分类: `RCE远程代码执行`
利用文件包含漏洞实现RCE

### 日志投毒RCE
分类: `RCE远程代码执行`
利用日志投毒实现RCE

### 图片马RCE
分类: `RCE远程代码执行`
利用图片马实现RCE

### .htaccess利用
分类: `RCE远程代码执行`
利用.htaccess文件实现RCE

### 盲注XXE攻击
分类: `XXE实体注入`
无回显的XXE攻击技术

### XXE OOB外带攻击
分类: `XXE实体注入`
利用OOB技术外带XXE数据

### XXE+SSRF组合攻击
分类: `XXE实体注入`
利用XXE实现SSRF攻击

### XXE到RCE
分类: `XXE实体注入`
利用XXE实现远程代码执行

### XXE文件读取
分类: `XXE实体注入`
利用XXE读取服务器文件

### XXE外部DTD利用
分类: `XXE实体注入`
利用外部DTD文件进行XXE攻击

### XLSX文件XXE
分类: `XXE实体注入`
利用XLSX文件进行XXE攻击

### DOCX文件XXE
分类: `XXE实体注入`
利用DOCX文件进行XXE攻击

### GraphQL注入攻击
分类: `API安全`
GraphQL API注入与信息泄露攻击

### GraphQL内省攻击
分类: `API安全`
利用GraphQL内省功能获取API结构

### GraphQL批量查询攻击
分类: `API安全`
利用GraphQL批量查询绕过速率限制

### REST API安全测试
分类: `API安全`
REST API安全测试与漏洞利用

### JWT None算法攻击
分类: `API安全`
利用JWT None算法绕过签名验证

### JWT密钥混淆攻击
分类: `API安全`
利用JWT算法混淆实现签名绕过

### IDOR不安全的直接对象引用
分类: `API安全`
利用IDOR漏洞访问未授权资源

### API速率限制绕过
分类: `API安全`
绕过API速率限制进行暴力攻击

### 批量赋值漏洞
分类: `API安全`
利用批量赋值漏洞修改敏感字段

### BOLA破坏对象级授权
分类: `API安全`
利用BOLA漏洞访问未授权对象

### API注入攻击
分类: `API安全`
API端点中的各类注入攻击

### Spring SpEL注入
分类: `框架漏洞`
Spring表达式语言注入攻击

### Spring Cloud漏洞
分类: `框架漏洞`
Spring Cloud相关漏洞利用

### Struts2远程代码执行
分类: `框架漏洞`
Apache Struts2框架RCE漏洞

### Struts2 OGNL表达式注入
分类: `框架漏洞`
Struts2 OGNL表达式注入技术详解

### WebLogic远程代码执行
分类: `框架漏洞`
Oracle WebLogic Server RCE漏洞

### WebLogic T3协议攻击
分类: `框架漏洞`
WebLogic T3协议反序列化漏洞

### WebLogic IIOP协议攻击
分类: `框架漏洞`
WebLogic IIOP协议反序列化漏洞

### ThinkPHP远程代码执行
分类: `框架漏洞`
ThinkPHP框架RCE漏洞

### Laravel远程代码执行
分类: `框架漏洞`
Laravel框架RCE漏洞

### Apache Shiro反序列化
分类: `框架漏洞`
Apache Shiro RememberMe反序列化漏洞

### JBoss漏洞利用
分类: `框架漏洞`
JBoss应用服务器漏洞

### Apache Tomcat漏洞
分类: `框架漏洞`
Apache Tomcat服务器漏洞利用

### Django框架漏洞
分类: `框架漏洞`
Django框架安全漏洞

### Flask框架漏洞
分类: `框架漏洞`
Flask框架安全漏洞

### SQL注入WAF绕过
分类: `SQL/NoSQL注入`
绕过Web应用防火墙的技术

### 认证绕过
分类: `认证漏洞`
Web应用认证绕过技术

### 文件上传绕过
分类: `文件漏洞`
文件上传限制绕过技术

### 缓存投毒
分类: `缓存与CDN安全`
Web缓存投毒攻击

### CL-TE请求走私
分类: `请求走私`
Content-Length与Transfer-Encoding走私

### 基础开放重定向
分类: `开放重定向`
URL跳转漏洞利用

### 基础点击劫持
分类: `点击劫持`
通过透明iframe覆盖诱使用户在不知情的情况下点击隐藏的恶意按钮或链接

### WebLogic XMLDecoder
分类: `框架漏洞`
利用WebLogic Server中XMLDecoder反序列化漏洞(CVE-2017-10271/CVE-2017-3506)实现远程代码执行

### 暴力破解
分类: `认证漏洞`
自动化密码猜测攻击

### 会话劫持
分类: `认证漏洞`
利用会话管理缺陷劫持或伪造用户会话，获取未授权访问权限

### 密码重置漏洞
分类: `认证漏洞`
绕过密码重置流程

### OAuth漏洞
分类: `认证漏洞`
OAuth认证流程漏洞

### SAML漏洞
分类: `认证漏洞`
SAML断言攻击

### 2FA绕过
分类: `认证漏洞`
绕过双因素认证

### 验证码绕过
分类: `认证漏洞`
绕过图形验证码

### 记住我漏洞
分类: `认证漏洞`
Remember Me功能漏洞

### JWT认证漏洞
分类: `认证漏洞`
利用JWT(JSON Web Token)实现缺陷伪造或篡改认证令牌，实现未授权访问或权限提升

### 任意文件下载
分类: `文件漏洞`
利用文件下载功能中的路径控制缺陷下载服务器上的任意敏感文件

### 条件竞争
分类: `文件漏洞`
利用文件上传/处理过程中的竞态条件(Race Condition)，在安全检查与文件使用之间的时间窗口内执行恶意操作

### 路径遍历
分类: `文件漏洞`
利用路径遍历(../)序列突破文件访问的目录限制，读取或写入Web根目录以外的任意文件

### Zip Slip
分类: `文件漏洞`
利用恶意构造的压缩包文件(ZIP/TAR)中的路径遍历实现任意文件写入，覆盖服务器上的关键文件或写入Webshell

### MIME类型绕过
分类: `文件漏洞`
通过伪造MIME类型(Content-Type)绕过文件上传的类型检查，上传恶意可执行文件

### 空字节截断
分类: `文件漏洞`
利用空字节(%00/\x00)截断文件名的扩展名验证，绕过文件上传白名单限制

### 缓存欺骗
分类: `缓存与CDN安全`
利用Web缓存和服务器路径解析的差异，诱导CDN/缓存层缓存包含敏感信息的动态页面

### CDN绕过
分类: `缓存与CDN安全`
绕过CDN查找真实IP

### CL-CL走私
分类: `请求走私`
利用前端代理和后端服务器同时处理Content-Length头但对多个CL头的处理差异实现HTTP请求走私

### TE-CL走私
分类: `请求走私`
利用前端使用Transfer-Encoding而后端使用Content-Length的差异实现HTTP请求走私

### TE-TE走私
分类: `请求走私`
利用前端和后端对Transfer-Encoding头的不同混淆变体的处理差异实现请求走私

### 重定向绕过
分类: `开放重定向`
开放重定向绕过技巧

### 重定向到SSRF
分类: `开放重定向`
利用开放重定向漏洞作为跳板将SSRF探测引导到内部网络，绕过SSRF的URL白名单/黑名单限制

### 点击劫持+XSS
分类: `点击劫持`
将点击劫持与XSS攻击结合，先通过点击劫持触发XSS攻击向量获取更深层的控制

### IDOR越权访问
分类: `业务逻辑漏洞`
不安全的直接对象引用(IDOR)，通过篡改请求参数中的对象ID越权访问他人数据。攻击者可遍历用户ID、订单号等参数获取未授权资源。

### 竞态条件攻击
分类: `业务逻辑漏洞`
利用服务端TOCTOU(Time-of-Check to Time-of-Use)漏洞，通过并发请求在检查与执行之间的时间窗口内多次触发同一操作，实现重复领券、重复提现、超额购买等业务逻辑突破。

### 支付逻辑篡改
分类: `业务逻辑漏洞`
通过修改支付请求中的金额、数量、折扣等参数来操纵交易逻辑。常见于电商平台和在线支付系统中，可导致0元购、负价格、折扣叠加等严重业务风险。

### 密码重置逻辑缺陷
分类: `业务逻辑漏洞`
密码重置流程中的逻辑漏洞，包括重置令牌泄露、验证码爆破、响应操纵、Host头注入等攻击手法，可实现任意用户密码重置。

### 验证码绕过技术
分类: `业务逻辑漏洞`
绕过图形验证码、短信验证码、滑动验证等人机验证机制的各种技术手法，包括响应泄露、复用攻击、OCR识别、逻辑缺陷利用等。

### JWT None算法攻击
分类: `JWT安全`
利用JWT库对"none"算法的支持缺陷，将JWT头部的签名算法修改为none后移除签名部分，构造无需密钥即可通过验证的伪造令牌。这是最经典的JWT漏洞之一。

### JWT密钥混淆攻击(RS→HS)
分类: `JWT安全`
当服务端使用RSA公钥验证JWT时，攻击者将算法从RS256改为HS256，此时服务端会错误地使用RSA公钥作为HMAC密钥进行验证。由于RSA公钥是公开的，攻击者可用它签名任意JWT。

### JWT密钥爆破
分类: `JWT安全`
当JWT使用HMAC对称算法(HS256/HS384/HS512)且密钥为弱密码时，可通过字典或暴力破解还原签名密钥，进而伪造任意JWT令牌。

### JWT JKU/X5U头注入
分类: `JWT安全`
利用JWT Header中的jku(JWK Set URL)或x5u(X.509 URL)参数，将密钥来源指向攻击者控制的服务器，使服务端使用攻击者的公钥验证JWT，从而实现令牌伪造。

### NPM包名仿冒(Typosquatting)
分类: `供应链攻击`
通过注册与流行NPM包名高度相似的恶意包(如lodash→1odash, colors→co1ors)，诱导开发者误安装。恶意包在install/postinstall钩子中执行反弹Shell、窃取环境变量或植入后门。

### CI/CD管道投毒
分类: `供应链攻击`
通过恶意Pull Request、Actions注入或构建脚本篡改来攻击CI/CD管道。攻击者可窃取构建密钥、投毒构建产物或在部署流程中植入后门代码。

### 依赖混淆攻击
分类: `供应链攻击`
利用包管理器在公共注册表和私有注册表之间的解析优先级漏洞。当企业使用内部包名时，攻击者在公共NPM/PyPI注册更高版本号的同名包，包管理器会优先安装公共高版本包从而执行恶意代码。

### 服务端原型链污染到RCE
分类: `原型链污染`
通过污染JavaScript对象原型链(__proto__/constructor.prototype)注入恶意属性，在Node.js服务端利用child_process或EJS/Pug等模板引擎的gadget链实现远程代码执行。

### 客户端原型链污染到XSS
分类: `原型链污染`
通过URL参数、postMessage或DOM操作污染前端JavaScript原型链，利用jQuery/DOM操作库的gadget在客户端实现XSS。攻击者可通过精心构造的URL链接诱导受害者触发漏洞。

### 原型链污染结合NoSQL注入
分类: `原型链污染`
将原型链污染与MongoDB/NoSQL注入组合利用。通过污染查询对象的原型链属性，绕过认证逻辑或构造恶意查询条件，实现认证绕过和数据泄露。

### 云SSRF窃取元数据凭据
分类: `云安全漏洞`
利用SSRF漏洞访问云服务(AWS/GCP/Azure)的实例元数据服务(IMDS)获取临时IAM凭据。攻击者可通过获取的Access Key接管云资源，实现从Web漏洞到云环境的横向升级。

### S3存储桶配置错误利用
分类: `云安全漏洞`
利用AWS S3存储桶的访问控制配置错误(公开读/写/列举)获取敏感数据或植入恶意文件。常见于静态网站托管、日志存储和备份桶，可能导致数据泄露、网站篡改或供应链攻击。

### AWS IAM权限提升
分类: `云安全漏洞`
在已获取低权限AWS凭据后，利用IAM策略中的过度授权(如iam:PassRole、lambda:CreateFunction等)实现权限提升至管理员。涵盖20+种已知的AWS IAM提权路径。

### Kubernetes容器逃逸
分类: `云安全漏洞`
在已获取Kubernetes Pod Shell的前提下，利用配置错误(特权容器、挂载宿主机路径、ServiceAccount高权限)实现容器逃逸，进而控制宿主机或整个Kubernetes集群。

### WebSocket跨站劫持(CSWSH)
分类: `WebSocket安全`
利用WebSocket握手阶段缺少Origin验证的漏洞，通过恶意网页建立跨站WebSocket连接。攻击者可劫持受害者的WebSocket会话，窃取实时数据或以受害者身份发送消息。类似于CSRF但针对WebSocket协议。

### WebSocket走私攻击
分类: `WebSocket安全`
利用反向代理/负载均衡器对WebSocket协议处理的差异，通过WebSocket升级请求走私HTTP请求到内网服务。攻击者可绕过前端安全控制直接与后端通信，访问受保护的内部API或管理接口。

### WebSocket认证与授权绕过
分类: `WebSocket安全`
利用WebSocket连接建立后缺少持续认证检查的漏洞，通过会话固定、令牌重放、频道越权订阅等方式绕过认证和授权机制。WebSocket的长连接特性使得权限变更后原连接仍可保持访问。

### LLM提示注入攻击
分类: `AI安全`
通过精心构造的用户输入覆盖或绕过LLM(大语言模型)的系统提示(System Prompt)，使AI执行非预期的操作。包括直接注入(DPI)和间接注入(IPI)，可导致系统提示泄露、安全护栏绕过、数据泄露和未授权操作。

### AI模型窃取与推理攻击
分类: `AI安全`
通过大量精心构造的查询对AI模型进行黑盒攻击，窃取模型参数(Model Extraction)、推断训练数据(Membership Inference)或发现模型决策边界。攻击者可以此构建功能等价的替代模型或提取隐私数据。

### 对抗样本攻击
分类: `AI安全`
通过向输入数据中添加人类不可感知的微小扰动，使AI模型产生错误的预测结果。对抗样本攻击可应用于图像分类、文本分析、语音识别等多种AI模型，威胁自动驾驶、安全检测和内容审核系统。

### RAG投毒与知识库注入
分类: `AI安全`
针对使用RAG(Retrieval-Augmented Generation)架构的AI应用，通过投毒知识库中的文档来影响AI的回答。攻击者可在向量数据库中注入包含恶意指令的文档，当用户查询触发检索时，恶意文档被注入到AI上下文中执行间接提示注入。

### MySQL注入 - 基础探测
分类: `SQL/NoSQL注入`
MySQL数据库注入基础探测与数据提取技术

### MySQL注入 - 高级技术
分类: `SQL/NoSQL注入`
MySQL高级注入技术：文件读写、UDF提权、命令执行

### MSSQL注入 - 基础探测
分类: `SQL/NoSQL注入`
Microsoft SQL Server数据库注入技术

### MSSQL注入 - 高级技术
分类: `SQL/NoSQL注入`
MSSQL高级注入：xp_cmdshell、SP_OACREATE命令执行

### Oracle注入 - 基础探测
分类: `SQL/NoSQL注入`
Oracle数据库注入基础技术

### Oracle注入 - 高级技术
分类: `SQL/NoSQL注入`
Oracle高级注入技术：Java存储过程、UTL_FILE文件操作

### PostgreSQL注入 - 基础探测
分类: `SQL/NoSQL注入`
PostgreSQL数据库注入技术

### SQLite注入
分类: `SQL/NoSQL注入`
SQLite数据库注入攻击

### MongoDB注入
分类: `SQL/NoSQL注入`
NoSQL数据库注入攻击技术

### Redis未授权访问
分类: `SQL/NoSQL注入`
Redis未授权访问和命令注入

### 布尔盲注
分类: `SQL/NoSQL注入`
基于布尔条件的SQL盲注技术

### 时间盲注
分类: `SQL/NoSQL注入`
基于时间延迟的SQL盲注技术

### 报错注入
分类: `SQL/NoSQL注入`
利用错误信息提取数据的SQL注入

### 二阶SQL注入
分类: `SQL/NoSQL注入`
存储后触发的SQL注入攻击

### 联合查询注入
分类: `SQL/NoSQL注入`
使用UNION SELECT提取数据

### 堆叠查询注入
分类: `SQL/NoSQL注入`
执行多条SQL语句的注入

### 反射型XSS
分类: `XSS跨站脚本`
反射型跨站脚本攻击技术

### 存储型XSS
分类: `XSS跨站脚本`
存储型跨站脚本攻击技术

### DOM型XSS
分类: `XSS跨站脚本`
基于DOM的跨站脚本攻击

### CSP绕过
分类: `XSS跨站脚本`
绕过内容安全策略(CSP)的XSS技术

### 基础SSRF攻击
分类: `SSRF服务端请求伪造`
服务端请求伪造基础攻击技术

### AWS元数据攻击
分类: `SSRF服务端请求伪造`
利用SSRF访问AWS EC2元数据服务

### 命令注入
分类: `RCE远程代码执行`
操作系统命令注入攻击技术

### XXE基础攻击
分类: `XXE实体注入`
XML外部实体注入基础攻击技术

### Jinja2模板注入
分类: `SSTI模板注入`
Jinja2/Twig模板注入攻击技术

### FreeMarker模板注入
分类: `SSTI模板注入`
FreeMarker模板引擎注入攻击技术

### Velocity模板注入
分类: `SSTI模板注入`
Velocity模板引擎注入攻击技术

### Thymeleaf模板注入
分类: `SSTI模板注入`
Thymeleaf模板引擎注入攻击技术

### Smarty模板注入
分类: `SSTI模板注入`
Smarty模板引擎注入攻击技术

### Mako模板注入
分类: `SSTI模板注入`
Mako模板引擎注入攻击技术

### Tornado模板注入
分类: `SSTI模板注入`
Tornado模板引擎注入攻击技术

### Django模板注入
分类: `SSTI模板注入`
Django模板引擎注入攻击技术

### ERB模板注入
分类: `SSTI模板注入`
ERB(Ruby)模板引擎注入攻击技术

### Pug/Jade模板注入
分类: `SSTI模板注入`
Pug/Jade模板引擎注入攻击技术

### 本地文件包含
分类: `LFI/RFI文件包含`
本地文件包含漏洞利用技术

### 远程文件包含
分类: `LFI/RFI文件包含`
远程文件包含漏洞利用技术

### 日志投毒LFI
分类: `LFI/RFI文件包含`
通过日志投毒实现LFI到RCE

### PHP伪协议利用
分类: `LFI/RFI文件包含`
利用PHP伪协议进行LFI攻击

### 目录遍历技术
分类: `LFI/RFI文件包含`
LFI目录遍历绕过技术

### PHP Filter链攻击
分类: `LFI/RFI文件包含`
利用PHP Filter链进行LFI攻击

### PHP Input执行
分类: `LFI/RFI文件包含`
利用php://input执行PHP代码

### PHP Data协议攻击
分类: `LFI/RFI文件包含`
利用data://协议执行PHP代码

### PHP Zip协议攻击
分类: `LFI/RFI文件包含`
利用zip://协议进行LFI攻击

### Phar反序列化攻击
分类: `LFI/RFI文件包含`
利用Phar反序列化进行RCE

### Session文件包含
分类: `LFI/RFI文件包含`
利用Session文件进行LFI攻击

### Proc文件系统利用
分类: `LFI/RFI文件包含`
利用/proc文件系统进行LFI攻击

### CSRF基础攻击
分类: `CSRF跨站请求伪造`
跨站请求伪造基础攻击技术

### JSON CSRF攻击
分类: `CSRF跨站请求伪造`
针对JSON请求的CSRF攻击技术

### CSRF绕过技术
分类: `CSRF跨站请求伪造`
绕过CSRF防护的各种技术

### SameSite绕过技术
分类: `CSRF跨站请求伪造`
绕过SameSite Cookie属性的CSRF攻击

### Token绕过技术
分类: `CSRF跨站请求伪造`
绕过CSRF Token验证的技术

### Referer绕过技术
分类: `CSRF跨站请求伪造`
绕过Referer验证的CSRF攻击

### Flash CSRF攻击
分类: `CSRF跨站请求伪造`
利用Flash进行CSRF攻击

### CORS配置错误利用
分类: `CSRF跨站请求伪造`
利用CORS配置错误进行CSRF攻击

### JWT安全漏洞
分类: `API安全`
JSON Web Token安全漏洞利用

### Log4j RCE (Log4Shell)
分类: `框架漏洞`
Apache Log4j远程代码执行漏洞

### Spring Actuator漏洞
分类: `框架漏洞`
Spring Boot Actuator端点安全漏洞

### Fastjson RCE
分类: `框架漏洞`
Alibaba Fastjson反序列化远程代码执行

### 突变型XSS(mXSS)
分类: `XSS跨站脚本`
利用浏览器解析差异导致的XSS攻击

### Unicode XSS
分类: `XSS跨站脚本`
利用Unicode编码特性绕过过滤

### XSS过滤器绕过
分类: `XSS跨站脚本`
各种绕过XSS过滤器的技术

### XSS编码绕过
分类: `XSS跨站脚本`
利用各种编码技术绕过XSS过滤

### Polyglot XSS
分类: `XSS跨站脚本`
多环境通用的XSS payload

### XSS Cookie窃取
分类: `XSS跨站脚本`
利用XSS窃取用户Cookie

### XSS键盘记录
分类: `XSS跨站脚本`
利用XSS记录用户键盘输入

### BeEF框架利用
分类: `XSS跨站脚本`
使用BeEF框架进行XSS利用

### GCP元数据攻击
分类: `SSRF服务端请求伪造`
利用SSRF攻击Google Cloud元数据服务

### Azure元数据攻击
分类: `SSRF服务端请求伪造`
利用SSRF攻击Azure元数据服务

### SSRF协议利用
分类: `SSRF服务端请求伪造`
利用各种协议进行SSRF攻击

### Gopher协议攻击
分类: `SSRF服务端请求伪造`
利用Gopher协议攻击内网服务

### Dict协议攻击
分类: `SSRF服务端请求伪造`
利用Dict协议探测和攻击内网服务

### File协议攻击
分类: `SSRF服务端请求伪造`
利用File协议读取本地文件

### SSRF绕过技术
分类: `SSRF服务端请求伪造`
各种绕过SSRF过滤的技术

### DNS重绑定攻击
分类: `SSRF服务端请求伪造`
利用DNS重绑定绕过SSRF防护

### SSRF攻击Redis
分类: `SSRF服务端请求伪造`
利用SSRF攻击内网Redis服务

### SSRF攻击MySQL
分类: `SSRF服务端请求伪造`
利用SSRF攻击内网MySQL服务

### PHP代码执行
分类: `RCE远程代码执行`
PHP代码执行漏洞利用技术

### PHP Filter链RCE
分类: `RCE远程代码执行`
利用PHP Filter链构造RCE

### 盲命令注入
分类: `RCE远程代码执行`
无回显的命令注入利用技术

### 反序列化漏洞
分类: `RCE远程代码执行`
利用反序列化漏洞实现RCE

### PHP反序列化
分类: `RCE远程代码执行`
PHP反序列化漏洞利用技术

### Java反序列化
分类: `RCE远程代码执行`
Java反序列化漏洞利用技术

### 文件上传漏洞
分类: `RCE远程代码执行`
利用文件上传漏洞获取RCE

### 文件包含RCE
分类: `RCE远程代码执行`
利用文件包含漏洞实现RCE

### 日志投毒RCE
分类: `RCE远程代码执行`
利用日志投毒实现RCE

### 图片马RCE
分类: `RCE远程代码执行`
利用图片马实现RCE

### .htaccess利用
分类: `RCE远程代码执行`
利用.htaccess文件实现RCE

### 盲注XXE攻击
分类: `XXE实体注入`
无回显的XXE攻击技术

### XXE OOB外带攻击
分类: `XXE实体注入`
利用OOB技术外带XXE数据

### XXE+SSRF组合攻击
分类: `XXE实体注入`
利用XXE实现SSRF攻击

### XXE到RCE
分类: `XXE实体注入`
利用XXE实现远程代码执行

### XXE文件读取
分类: `XXE实体注入`
利用XXE读取服务器文件

### XXE外部DTD利用
分类: `XXE实体注入`
利用外部DTD文件进行XXE攻击

### XLSX文件XXE
分类: `XXE实体注入`
利用XLSX文件进行XXE攻击

### DOCX文件XXE
分类: `XXE实体注入`
利用DOCX文件进行XXE攻击

### GraphQL注入攻击
分类: `API安全`
GraphQL API注入与信息泄露攻击

### GraphQL内省攻击
分类: `API安全`
利用GraphQL内省功能获取API结构

### GraphQL批量查询攻击
分类: `API安全`
利用GraphQL批量查询绕过速率限制

### REST API安全测试
分类: `API安全`
REST API安全测试与漏洞利用

### JWT None算法攻击
分类: `API安全`
利用JWT None算法绕过签名验证

### JWT密钥混淆攻击
分类: `API安全`
利用JWT算法混淆实现签名绕过

### IDOR不安全的直接对象引用
分类: `API安全`
利用IDOR漏洞访问未授权资源

### API速率限制绕过
分类: `API安全`
绕过API速率限制进行暴力攻击

### 批量赋值漏洞
分类: `API安全`
利用批量赋值漏洞修改敏感字段

### BOLA破坏对象级授权
分类: `API安全`
利用BOLA漏洞访问未授权对象

### API注入攻击
分类: `API安全`
API端点中的各类注入攻击

### Spring SpEL注入
分类: `框架漏洞`
Spring表达式语言注入攻击

### Spring Cloud漏洞
分类: `框架漏洞`
Spring Cloud相关漏洞利用

### Struts2远程代码执行
分类: `框架漏洞`
Apache Struts2框架RCE漏洞

### Struts2 OGNL表达式注入
分类: `框架漏洞`
Struts2 OGNL表达式注入技术详解

### WebLogic远程代码执行
分类: `框架漏洞`
Oracle WebLogic Server RCE漏洞

### WebLogic T3协议攻击
分类: `框架漏洞`
WebLogic T3协议反序列化漏洞

### WebLogic IIOP协议攻击
分类: `框架漏洞`
WebLogic IIOP协议反序列化漏洞

### ThinkPHP远程代码执行
分类: `框架漏洞`
ThinkPHP框架RCE漏洞

### Laravel远程代码执行
分类: `框架漏洞`
Laravel框架RCE漏洞

### Apache Shiro反序列化
分类: `框架漏洞`
Apache Shiro RememberMe反序列化漏洞

### JBoss漏洞利用
分类: `框架漏洞`
JBoss应用服务器漏洞

### Apache Tomcat漏洞
分类: `框架漏洞`
Apache Tomcat服务器漏洞利用

### Django框架漏洞
分类: `框架漏洞`
Django框架安全漏洞

### Flask框架漏洞
分类: `框架漏洞`
Flask框架安全漏洞

### SQL注入WAF绕过
分类: `SQL/NoSQL注入`
绕过Web应用防火墙的技术

### 认证绕过
分类: `认证漏洞`
Web应用认证绕过技术

### 文件上传绕过
分类: `文件漏洞`
文件上传限制绕过技术

### 缓存投毒
分类: `缓存与CDN安全`
Web缓存投毒攻击

### CL-TE请求走私
分类: `请求走私`
Content-Length与Transfer-Encoding走私

### 基础开放重定向
分类: `开放重定向`
URL跳转漏洞利用

### 基础点击劫持
分类: `点击劫持`
通过透明iframe覆盖诱使用户在不知情的情况下点击隐藏的恶意按钮或链接

### WebLogic XMLDecoder
分类: `框架漏洞`
利用WebLogic Server中XMLDecoder反序列化漏洞(CVE-2017-10271/CVE-2017-3506)实现远程代码执行

### 暴力破解
分类: `认证漏洞`
自动化密码猜测攻击

### 会话劫持
分类: `认证漏洞`
利用会话管理缺陷劫持或伪造用户会话，获取未授权访问权限

### 密码重置漏洞
分类: `认证漏洞`
绕过密码重置流程

### OAuth漏洞
分类: `认证漏洞`
OAuth认证流程漏洞

### SAML漏洞
分类: `认证漏洞`
SAML断言攻击

### 2FA绕过
分类: `认证漏洞`
绕过双因素认证

### 验证码绕过
分类: `认证漏洞`
绕过图形验证码

### 记住我漏洞
分类: `认证漏洞`
Remember Me功能漏洞

### JWT认证漏洞
分类: `认证漏洞`
利用JWT(JSON Web Token)实现缺陷伪造或篡改认证令牌，实现未授权访问或权限提升

### 任意文件下载
分类: `文件漏洞`
利用文件下载功能中的路径控制缺陷下载服务器上的任意敏感文件

### 条件竞争
分类: `文件漏洞`
利用文件上传/处理过程中的竞态条件(Race Condition)，在安全检查与文件使用之间的时间窗口内执行恶意操作

### 路径遍历
分类: `文件漏洞`
利用路径遍历(../)序列突破文件访问的目录限制，读取或写入Web根目录以外的任意文件

### Zip Slip
分类: `文件漏洞`
利用恶意构造的压缩包文件(ZIP/TAR)中的路径遍历实现任意文件写入，覆盖服务器上的关键文件或写入Webshell

### MIME类型绕过
分类: `文件漏洞`
通过伪造MIME类型(Content-Type)绕过文件上传的类型检查，上传恶意可执行文件

### 空字节截断
分类: `文件漏洞`
利用空字节(%00/\x00)截断文件名的扩展名验证，绕过文件上传白名单限制

### 缓存欺骗
分类: `缓存与CDN安全`
利用Web缓存和服务器路径解析的差异，诱导CDN/缓存层缓存包含敏感信息的动态页面

### CDN绕过
分类: `缓存与CDN安全`
绕过CDN查找真实IP

### CL-CL走私
分类: `请求走私`
利用前端代理和后端服务器同时处理Content-Length头但对多个CL头的处理差异实现HTTP请求走私

### TE-CL走私
分类: `请求走私`
利用前端使用Transfer-Encoding而后端使用Content-Length的差异实现HTTP请求走私

### TE-TE走私
分类: `请求走私`
利用前端和后端对Transfer-Encoding头的不同混淆变体的处理差异实现请求走私

### 重定向绕过
分类: `开放重定向`
开放重定向绕过技巧

### 重定向到SSRF
分类: `开放重定向`
利用开放重定向漏洞作为跳板将SSRF探测引导到内部网络，绕过SSRF的URL白名单/黑名单限制

### 点击劫持+XSS
分类: `点击劫持`
将点击劫持与XSS攻击结合，先通过点击劫持触发XSS攻击向量获取更深层的控制

### IDOR越权访问
分类: `业务逻辑漏洞`
不安全的直接对象引用(IDOR)，通过篡改请求参数中的对象ID越权访问他人数据。攻击者可遍历用户ID、订单号等参数获取未授权资源。

### 竞态条件攻击
分类: `业务逻辑漏洞`
利用服务端TOCTOU(Time-of-Check to Time-of-Use)漏洞，通过并发请求在检查与执行之间的时间窗口内多次触发同一操作，实现重复领券、重复提现、超额购买等业务逻辑突破。

### 支付逻辑篡改
分类: `业务逻辑漏洞`
通过修改支付请求中的金额、数量、折扣等参数来操纵交易逻辑。常见于电商平台和在线支付系统中，可导致0元购、负价格、折扣叠加等严重业务风险。

### 密码重置逻辑缺陷
分类: `业务逻辑漏洞`
密码重置流程中的逻辑漏洞，包括重置令牌泄露、验证码爆破、响应操纵、Host头注入等攻击手法，可实现任意用户密码重置。

### 验证码绕过技术
分类: `业务逻辑漏洞`
绕过图形验证码、短信验证码、滑动验证等人机验证机制的各种技术手法，包括响应泄露、复用攻击、OCR识别、逻辑缺陷利用等。

### JWT None算法攻击
分类: `JWT安全`
利用JWT库对"none"算法的支持缺陷，将JWT头部的签名算法修改为none后移除签名部分，构造无需密钥即可通过验证的伪造令牌。这是最经典的JWT漏洞之一。

### JWT密钥混淆攻击(RS→HS)
分类: `JWT安全`
当服务端使用RSA公钥验证JWT时，攻击者将算法从RS256改为HS256，此时服务端会错误地使用RSA公钥作为HMAC密钥进行验证。由于RSA公钥是公开的，攻击者可用它签名任意JWT。

### JWT密钥爆破
分类: `JWT安全`
当JWT使用HMAC对称算法(HS256/HS384/HS512)且密钥为弱密码时，可通过字典或暴力破解还原签名密钥，进而伪造任意JWT令牌。

### JWT JKU/X5U头注入
分类: `JWT安全`
利用JWT Header中的jku(JWK Set URL)或x5u(X.509 URL)参数，将密钥来源指向攻击者控制的服务器，使服务端使用攻击者的公钥验证JWT，从而实现令牌伪造。

### NPM包名仿冒(Typosquatting)
分类: `供应链攻击`
通过注册与流行NPM包名高度相似的恶意包(如lodash→1odash, colors→co1ors)，诱导开发者误安装。恶意包在install/postinstall钩子中执行反弹Shell、窃取环境变量或植入后门。

### CI/CD管道投毒
分类: `供应链攻击`
通过恶意Pull Request、Actions注入或构建脚本篡改来攻击CI/CD管道。攻击者可窃取构建密钥、投毒构建产物或在部署流程中植入后门代码。

### 依赖混淆攻击
分类: `供应链攻击`
利用包管理器在公共注册表和私有注册表之间的解析优先级漏洞。当企业使用内部包名时，攻击者在公共NPM/PyPI注册更高版本号的同名包，包管理器会优先安装公共高版本包从而执行恶意代码。

### 服务端原型链污染到RCE
分类: `原型链污染`
通过污染JavaScript对象原型链(__proto__/constructor.prototype)注入恶意属性，在Node.js服务端利用child_process或EJS/Pug等模板引擎的gadget链实现远程代码执行。

### 客户端原型链污染到XSS
分类: `原型链污染`
通过URL参数、postMessage或DOM操作污染前端JavaScript原型链，利用jQuery/DOM操作库的gadget在客户端实现XSS。攻击者可通过精心构造的URL链接诱导受害者触发漏洞。

### 原型链污染结合NoSQL注入
分类: `原型链污染`
将原型链污染与MongoDB/NoSQL注入组合利用。通过污染查询对象的原型链属性，绕过认证逻辑或构造恶意查询条件，实现认证绕过和数据泄露。

### 云SSRF窃取元数据凭据
分类: `云安全漏洞`
利用SSRF漏洞访问云服务(AWS/GCP/Azure)的实例元数据服务(IMDS)获取临时IAM凭据。攻击者可通过获取的Access Key接管云资源，实现从Web漏洞到云环境的横向升级。

### S3存储桶配置错误利用
分类: `云安全漏洞`
利用AWS S3存储桶的访问控制配置错误(公开读/写/列举)获取敏感数据或植入恶意文件。常见于静态网站托管、日志存储和备份桶，可能导致数据泄露、网站篡改或供应链攻击。

### AWS IAM权限提升
分类: `云安全漏洞`
在已获取低权限AWS凭据后，利用IAM策略中的过度授权(如iam:PassRole、lambda:CreateFunction等)实现权限提升至管理员。涵盖20+种已知的AWS IAM提权路径。

### Kubernetes容器逃逸
分类: `云安全漏洞`
在已获取Kubernetes Pod Shell的前提下，利用配置错误(特权容器、挂载宿主机路径、ServiceAccount高权限)实现容器逃逸，进而控制宿主机或整个Kubernetes集群。

### WebSocket跨站劫持(CSWSH)
分类: `WebSocket安全`
利用WebSocket握手阶段缺少Origin验证的漏洞，通过恶意网页建立跨站WebSocket连接。攻击者可劫持受害者的WebSocket会话，窃取实时数据或以受害者身份发送消息。类似于CSRF但针对WebSocket协议。

### WebSocket走私攻击
分类: `WebSocket安全`
利用反向代理/负载均衡器对WebSocket协议处理的差异，通过WebSocket升级请求走私HTTP请求到内网服务。攻击者可绕过前端安全控制直接与后端通信，访问受保护的内部API或管理接口。

### WebSocket认证与授权绕过
分类: `WebSocket安全`
利用WebSocket连接建立后缺少持续认证检查的漏洞，通过会话固定、令牌重放、频道越权订阅等方式绕过认证和授权机制。WebSocket的长连接特性使得权限变更后原连接仍可保持访问。

### LLM提示注入攻击
分类: `AI安全`
通过精心构造的用户输入覆盖或绕过LLM(大语言模型)的系统提示(System Prompt)，使AI执行非预期的操作。包括直接注入(DPI)和间接注入(IPI)，可导致系统提示泄露、安全护栏绕过、数据泄露和未授权操作。

### AI模型窃取与推理攻击
分类: `AI安全`
通过大量精心构造的查询对AI模型进行黑盒攻击，窃取模型参数(Model Extraction)、推断训练数据(Membership Inference)或发现模型决策边界。攻击者可以此构建功能等价的替代模型或提取隐私数据。

### 对抗样本攻击
分类: `AI安全`
通过向输入数据中添加人类不可感知的微小扰动，使AI模型产生错误的预测结果。对抗样本攻击可应用于图像分类、文本分析、语音识别等多种AI模型，威胁自动驾驶、安全检测和内容审核系统。

### RAG投毒与知识库注入
分类: `AI安全`
针对使用RAG(Retrieval-Augmented Generation)架构的AI应用，通过投毒知识库中的文档来影响AI的回答。攻击者可在向量数据库中注入包含恶意指令的文档，当用户查询触发检索时，恶意文档被注入到AI上下文中执行间接提示注入。
