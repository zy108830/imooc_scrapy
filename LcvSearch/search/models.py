from django.db import models
from elasticsearch_dsl import DocType, Date, Nested, Boolean, \
    analyzer, InnerObjectWrapper, Completion, Keyword, Text, Integer
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl.analysis import CustomAnalysis as _CustomAnalysis

connections.create_connection(hosts=["localhost"])
# Create your models here.

class ArticleType(DocType):
    # 伯乐在线文章类型
    suggest = Completion(analyzer="ik_max_word") # 官方代码有问题，不能这么用，事实证明可以这么用
    # suggest = Completion(analyzer=ik_analyzer) # 这么用
    title = Text(analyzer="ik_max_word")
    create_date = Date()
    url = Keyword()
    url_object_id = Keyword()
    front_image_url = Keyword()
    front_image_path = Keyword()
    praise_nums = Integer()
    comment_nums = Integer()
    fav_nums = Integer()
    tags = Text(analyzer="ik_max_word")
    content = Text(analyzer="ik_max_word")

    class Meta:
        index = "jobbole"
        doc_type = "article"

if __name__ == "__main__":
    ArticleType.init()