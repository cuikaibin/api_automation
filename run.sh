#!/bin/bash

#获得脚本所在目录
path=$(cd "$(dirname "$0")"; pwd)
export PYTHONPATH=${path}:$PYTHONPATH

#清除log日志
rm -rf /log

#首轮执行
pytest -v ./case/demo --alluredir ./result/temp

#执行首轮错误的case
pytest -v --lf --alluredir ./result/temp

#生成allure报告
allure generate ./result/temp -o ./result/report --clean
