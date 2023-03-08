# AIP

> 本程序可用于项目进行应用方向的自动化巡检，可调用本地浏览器对巡检指标进行分析、截图、产出巡检报表，可以对阈值判定、异常推送

## 食用指南

使用前必装：

- 已安装firefox浏览器
- 拷贝代码中的geckodriver.exe到电脑含path变量的路径下
- 按照文档中excel配置文件解析填写需要巡检的指标项(SLI)及阈值（SLO）及其他指标（填写参考配置文件解析）

### sheet名规范

- **pwd** : 该sheet用于保存需要巡检的系统信息（指标如下）

  - **system_name** : 系统名称
  - **login_url** : 登录页面url
  - **user** ：用户名
  - **pwd**: 运行AIP_encrypt.exe程序生成加密后的密码
  - **username_label**：用户名输入框的xpath路径
  - **pwd_label** ：密码输入框的xpath路径
  - **login_btn_label**：登录按钮的xpath路径

  > 1. 如果需要巡检的网站无需登录，则仅需填入系统名称即可，其他字段留空
  >
  > 2. 

- **pic_reporter_prefix** : 该表用于巡检截图后自动生成Word报表（指标如下）：

  - main_title:
    - 如要生成word报表，该字段**必填**且仅能存储为**A2单元格**
    - 该字段将作为生成word报表的**大标题**及**文件名**
  - pic_delete：
    - 用于确定生成word报表后，是否要删除图片（如果不删除，需要手动进行图片删除或转移，否则可能出现下次巡检重复生成的情况）
    - 参考值（YES/NO）
  - title：
    - 用于word图表内容的二级标题
  - prefix
    - 分类图片的前缀

- 巡检指标表（**sheet需要自己新增且**名称需要和pwd表中**system_name**一致）

  - target_name :采集的指标名称（建议使用英文）
  - url: 采集指标的地址
  - action：采集指标的动作
    - **screenshot**:截图
    - **identification**: 识别数据
    - **general** : 仅自动跳转等待speed_time时间
  - x_path：采集指标的xpath路径
    - action为general可不填

    - 复制xpath路径方法 打开F12,利用选择元素按钮，找到需要截图的元素，在元素选项卡中右击复制xpath路径填入此处（如路径中带双引号，需手动替换为单引号）
  - SLO：阈值参数 （仅action为identification可用（默认大于该值为异常））
  - speed_time: 巡检该项的等待时间

### 字段含义

```JSON
例如：
    {
    "target_name" : "kafka_lag",
    "url": "http://10.183.11.62/zabbix/charts.php?fullscreen=0&groupid=0&hostid=10287&graphid=6131",
    "action": "screenshot",
    "x_path":"//*[@id='graph_full']",
    "SLO": 5，
    "speed_time": 5
    }
```