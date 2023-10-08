# DreamHolder
青少年身心健康检测系统

目录结构：
源代码
- model——算法模型文件
- my-project——健康检测与分析系统
- StuForum1.0——校园论坛业务系统
- chnsenticorp数据集.rar——训练模型所用数据集
- stu_forum.sql——数据库sql脚本

安装说明：
一．校园论坛业务模块安装
1. 解压项目压缩包
2. 进入项目文件夹
3. 为了方便，这里使用Anaconda Powershell进行安装requirement.txt环境依赖
        - 创建新环境conda create -n paddtest python=3.8
        - 激活环境conda activate paddtest
        - 命令行操作：pip install -r requirements.txt
4. 修改config.py配置文件
        - 系统默认数据库地址为127.0.0.1
        - 用户名和密码请改为本机数据库用户名密码
5.在项目路径下运行启动命令
- 命令行操作：flask run --host=0.0.0.0
6.根据系统提示网址进入即可
- Running on http://xxx.xxx.xxx.xxx:xxx/ (Press CTRL+C to quit)

二．健康监测与分析模块安装
1. 解压项目压缩包
2. 安装node.js、yarn
- Node.js下载地址：https://nodejs.org/zh-cn/
- Node.js安装指南：https://blog.csdn.net/qq_40712862/article/details/120231621
- yarn安装命令：npm install -g yarn
- 测试是否成功：yarn --version
3. 进入项目文件夹
4. 安装依赖
- yarn install
5. 在项目路径下运行启动命令
- yarn run serve
6. 根据系统提示网址进入即可
- Running on http://xxx.xxx.xxx.xxx:xxx/ (Press CTRL+C to quit)

三．数据库创建及数据导入
1. 解压数据库压缩包得到SQL脚本
2. 下载并安装数据库管理工具
3. 在管理工具中执行SQL脚本
4. 查看并确认数据库数据
 
四．算法安装与部署
这里Anaconda的下载安装步骤不再赘述，仅介绍算法安装部署具体步骤
1.    创建虚拟环境
      - conda create --name paddle_env python=3.8
      - conda activate paddle_env
2.    安装paddlehub及相关依赖
       - pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
       - pip install paddlehub -i https://mirror.baidu.com/pypi/simple
       - 使用pip install 库名 -i https://mirror.baidu.com/pypi/simple
3.    模型下载及配置（由于训练模型较慢，这里展示替换我们模型的方法）
      - hub install senta_lstm
      - hub run senta_lstm --input_text "这家餐厅很好吃"
      - serving start -m senta_lstm（部署使用，可自由更改相关参数）
4.    替换模型文件
- 模型文件路径为‘用户文件夹/user/ .paddlehub/ modules/ senta_lstm/ model’将我所训练的模型权重文件（源代码/model/bestmodel/*）加入该文件夹，注意除了@HUB_senta_lstm@fc_2.w_0和__model__不能替换其余均可替换
5.    投入使用
- serving start -m senta_lstm若想更改算法端口号只需要进一步添加参数即可，使用时要与论坛一起开启才会将实时数据转化为分析后的数据存入数据库
