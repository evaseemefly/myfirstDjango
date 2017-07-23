from django.forms import ModelForm      # 该类是所有django表单的基类
from app.models import Moment       # 引入app/models.py中的Moment类

class MomentForm(ModelForm):    # 定义表单类
    class Meta:     # 定义子类Meta
        model=Moment    # 声明与本表单关联的模型类及其字段
        fields="__all__"    # 导入所有字段