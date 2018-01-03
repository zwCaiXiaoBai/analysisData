爬虫架构
* url管理器
* 网页下载器，urllib
* 网页解析器，BeautifulSoup
* 结果输出器，html.outputer
* 实战编写爬取百度百科页面

分析目标
目标：百度百科python词条相关业-标题和简介
入口页：https://baike.baidu.com/item/Python/407313?fr=aladdin
url格式：
    - 词条页面url:/item/%E9%98%BF%E5%A7%86%E6%96%AF%E7%89%B9%E4%B8%B9/2259975.htm
数据格式
    - 标题
        <dd class="lemmaWgt-lemmaTitle-title">
        <h1>****</h1>
        </dd>
    - 简介
        <div class="para" label-module="para">m">***</div>

页面编码
    utf-8