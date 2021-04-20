import  re


def extract_table_name_from_sql(sql_str):

    # remove the /* */ comments
    q = re.sub(r"/\*[^*]*\*+(?:[^*/][^*]*\*+)*/", "", sql_str)

    # remove whole line -- and # comments
    lines = [line for line in q.splitlines() if not re.match("^\s*(--|#)", line)]

    # remove trailing -- and # comments
    q = " ".join([re.split("--|#", line)[0] for line in lines])

    # split on blanks, parens and semicolons
    tokens = re.split(r"[\s)(;]+", q)
    print(tokens)

    # scan the tokens. if we see a FROM or JOIN, we set the get_next
    # flag, and grab the next one (unless it's SELECT).

    result = set()
    get_next = False
    for token in tokens:
        if get_next:
            if token.lower() not in ["", "select"]:
                result.add(token)
            get_next = False
        get_next = token.lower() in ["from", "join"]

    return result

sql2="select b.priority from tb_prd_ofr a,tb_pricing_plan b on idx_tb_prd_ofr_ofr_id(a.ofr_id=?), index_tb_pricing_plan(b.pricing_plan_id =[a.pricing_plan_id])"
print(extract_table_name_from_sql(sql2))