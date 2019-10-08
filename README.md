# Django Rest Framework 集成 MongoDB 数据库


## 环境配置

- Django
- django-rest-framework-mongoengine
- djangorestframework
- mongoengine
- pymongo


## 过程


### 创建一个新的 Django 项目


### 在 settings.py 中进行基本的配置

```python
DATABASES = {
    'default': {
        # 把默认的数据库连接置为 None
        'ENGINE': None,
    }
}

from mongoengine import connect

DB_MONGO_NAME = 'test'
DB_MONGO_HOST = '127.0.0.1'
DB_MONGO_PORT = 27017

connect(DB_MONGO_NAME, host=DB_MONGO_HOST, port=DB_MONGO_PORT)
```

### 新建一个 app: polls

```bash
python manage.py startapp polls
```


### 在新建的 app: polls 的 models.py 中新建数据模型

```python
from mongoengine import Document, fields


class Poll(Document):
    name = fields.StringField(required=True)
    votes = fields.IntField(required=True)
```

### 在应用中创建一个序列化器

```python
from rest_framework_mongoengine import serializers

from polls import models


class PollSerializer(serializers.DocumentSerializer):
    class Meta:
        model = models.Poll
        fields = '__all__'
```


### 在视图文件中创建一个视图

```python
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from polls import models
from polls import serializers


class PollViewSet(MongoModelViewSet):
    """"""

    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer
```


### 配置 URL

- polls/urls.py

```python
from django.conf.urls import url

from polls import views

urlpatterns = [
    url(r'^$', views.PollViewSet.as_view())
]
```

- drf_mongo_example/urls.py

```python
from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]
```


### 运行并访问

```bash
python manage.py runserver

```

访问 `http:127.0.0.1:8000/polls/`


### 关于增删改查


#### 增加数据

```python

```


#### 删除数据

```python

```


#### 查询数据

```python

```


#### 修改数据

```python

```
