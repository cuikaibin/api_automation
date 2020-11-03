# MTX
基于Pytest+request+Allure的接口自动化方案

----
## 模块介绍
`case`接口case所在目录
`conf`配置文件所在目录
`lib`封装公共模块所在目录
`result`接口case执行结果保存目录
`log`保存log日志

----
#### lib目录模块类的设计
`RequestBase.py` 封装request方法，可以支持多协议扩展（get\post\put）
`Log.py` 封装记录log方法，分为：debug、info、warning、error、critical
`assertion.py` 封装assert方法

----
#### 执行某个目录下的所有case，sh run.sh
