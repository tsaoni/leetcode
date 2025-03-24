nested_dict_str = """{
    'key1': 'value1',
    'key2': {
        'key2_1': 'value2_1',
        'key2_2': {
            'key2_2_1': 'value2_2_1',
            'key2_2_2': 'value2_2_2'
        }
    },
    'key3': {
        'key3_1': 'value3_1'
    }
}"""
 

def parse_dict(s): 
    stack = []
    s_lst = s.split("\n")
    pre_k = []
    for x in s_lst:
        if "{" in x: 
            stack += [{}]
            if ":" in x: 
                tmpk = x.split(":")[0].replace("'", "")
                pre_k += [tmpk.strip()]
        elif "}" in x: 
            tmp = stack.pop(-1)
            if len(pre_k) > 0:
                tmpk = pre_k.pop(-1)
                stack[-1][tmpk] = tmp
        else: 
            k, v = x.split(":")
            k = k.replace("'", "").strip()
            v = v.replace("'", "").replace(",", "").strip()
            stack[-1][k] = v
        
    return tmp
    
    
tmp = parse_dict(nested_dict_str)
# print(tmp)
    

def dict_to_string(d): 
    s = "{\n"
    for k, v in d.items(): 
        if type(v) == dict: 
            tmp = dict_to_string(v)
            t_lst = tmp.split('\n')
            tmp = ""
            for i, t in enumerate(t_lst):
                if i == 0: 
                    tmp += f"{t}\n"
                else: 
                    tmp += f"\t{t}\n"
        else: tmp = v
        s += f"\t{k}: {tmp}, \n"
    s += "}\n"
    return s
    
s = dict_to_string(tmp)
print(s)
