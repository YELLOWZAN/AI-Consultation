# AI-Consultation
基于ERNIE-Bot+Gradio的赛博问诊交互页面

# 框架结构
本项目基于ERNIE+Gradio搭建，使用Python语言编写

# 项目结构
主要有两个文件
文件名 | 用途
------ | -----
medical.py | 项目主程序文件
requirements.txt | 项目环境依赖

# 如何运行本项目？
请先搭建并激活虚拟环境（建议），或者直接使用基础环境。

1.先准备python环境，python版本需要大于等于3.7，若未具备这方面的知识请自行度娘如何操作。

2.安装环境依赖（若有虚拟环境请注意环境启用情况）
```shell
pip install -r requirements.txt
```
3.启动主应用文件app.gradio.py
```shell
(venv)powershell:python ./medical.py
```
# 程序解释
```
程序启动前，请准备好自己的AIStudio access_token
启动后，程序会生成本地或者互联网链接，默认开启本地127.0.0.1访问，程序运行后输出框会生成本地访问的链接。
请在页面对应位置下输入access_token，并在"描述"框中输入信息。
请在"模型"选项中选择所想使用的模型，目前程序支持调用如下模型
"ernie-3.5", "ernie-turbo", "ernie-4.0", "ernie-longtext"
```
