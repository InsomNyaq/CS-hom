# Python 基础学习平台

一个使用 Django 构建的本地 Python 入门学习平台，包含：

- 指定账号登录
- 学习进度仪表盘
- 课程目录和课程详情
- 代码示例与输出预览
- 随堂测验
- Django Admin 后台内容管理

## 快速启动

```powershell
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py runserver
```

然后打开 http://127.0.0.1:8000/

默认账号：

- 用户名：`InsomNya`
- 密码：`9019zhyq`

后台地址：http://127.0.0.1:8000/admin/

## 目录说明

- `python_learning/`：Django 项目配置
- `learning/`：学习业务、模型、视图和后台管理
- `templates/`：页面模板
- `static/`：科技风样式与交互脚本
- `learning/management/commands/seed_data.py`：示例课程和账号初始化
