import GetTable_2


        




if __name__ == "__main__":
    demo = GetTable_2.SimpleTable()

    table_list = demo.open_xml_file(r"C:\Users\lcy_yy\Documents\GitHub\Python\config\AcctItemIvpn_910.sql.xml")
    m2db_dict = demo.open_m2db_file(r"C:\Users\lcy_yy\Documents\GitHub\Python\m2db__136.96.61.177.sql")
    

    for i_name in table_list:
        print("table name is",i_name)
        print("============create {0}".format(i_name),"===================")

        if i_name in m2db_dict:
            print(m2db_dict[i_name])
        else:
            print("Create table string is not exists!!!!!!!!")
            print("The table name is [{0}]".format(i_name))

        print("===============华丽分割符================")