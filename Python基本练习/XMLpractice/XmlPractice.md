利用文件对象模型（Document Object Model,简称DOM）解析XML文档<br>
首先利用函数parse打开xml文件<br>
    ``DOMTree = xml.dom.minidom.parse('mon_acct.xml')``

通过`documentElement`函数获取根节点<br>
    `RootNode = DOMTree.documentElement`

接着使用函数`getElementsByTagName`获取所有的`<module>`元素<br>
`module_db = RootNode.getElementsByTagName('module')`

最后就是遍历`<module>`元素，当`<module>`的属性值等于 `ocsm2db_bill`,则获取元素`<sql>`的值。

    # 判断模块的属性值
    if 'ocsm2db_bill' == module_v.getAttribute('name'):
        sql_str_list = []
        # 获取模块中的所有<sql>元素
        sql_coll = module_v.getElementsByTagName('sql')
        # sql节点存在sql_coll
        for sql_node in sql_coll:
            # 获取sql元素的值，并替换字符串前后的空白字符
            sql_value = re.sub(r'^\s+|\s+$','',sql_node.childNodes[0].data)
            # 获取到select语句
            sql_str_list.append(sql_value)

函数`getAttribute`获取元素的属性值。
调用方法为`[元素对象].getAttribute([元素属性名称])`

xml例子：<br>

    <module name="ocsm2db_bill" db="ocsm2db_bill" policy="demand">
        <sql name="QRYSERVCREDITLOAD" bind="2" sub="910">		
	 	select PROD_INST_ID from HB_SERV_CREDIT_LOAD_T_[@] on  index_SERV_CREDIT_LOAD_T_[@] (PROD_INST_ID = ?)
	    </sql>  
    </module>