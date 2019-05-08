import numpy

APIs = {}

# With only one argument
APIs['count'] = {"argument":['row'], 'output': 'num', 
                 'function': lambda t :  len(t),
                 'tostr': lambda t : "count({})".format(t),
                 'append': True}

APIs['inc_num'] = {"argument":['num'], 'output': 'num',
              "function": lambda t : t,
              "tostr": lambda t : "modify({})".format(t),
              'append': False}

APIs['dec_num'] = {"argument":['num'], 'output': 'none',
              "function": lambda t : None,
              "tostr": lambda t : "modify({})".format(t),
              'append': False}

APIs['inc_str'] = {"argument":['str'], 'output': 'str',
              "function": lambda t : t,
              "tostr": lambda t : "modify({})".format(t),
              'append': False}

APIs['dec_str'] = {"argument":['str'], 'output': 'none',
              "function": lambda t : None,
              "tostr": lambda t : "modify({})".format(t),
              'append': False}

APIs['within_s_s'] = {"argument":['row', 'header_str', 'str'], 'output': 'bool',
                "function": lambda t, col, value: len(t[t[col].str.contains(value, regex=False)]) > 0,
                "tostr": lambda t, col, value : "within({}, {}, {})".format(t, col, value),
                'append': None}

APIs['within_n_n'] = {"argument":['row', 'header_num', 'num'], 'output': 'bool',
                "function": lambda t, col, value : len(t[t[col] == value]) > 0,
                "tostr": lambda t, col, value : "within({}, {}, {})".format(t, col, value),
                'append': None}

APIs['not_within_s_s'] = {"argument":['row', 'header_str', 'str'], 'output': 'bool',
                          "function": lambda t, col, value: len(t[t[col].str.contains(value, regex=False)]) == 0,
                          "tostr": lambda t, col, value : "not_within({}, {}, {})".format(t, col, value),
                          'append': None}

APIs['not_within_n_n'] = {"argument":['row', 'header_num', 'num'], 'output': 'bool',
                          "function": lambda t, col, value : len(t[t[col] == value]) == 0,
                          "tostr": lambda t, col, value : "not_within({}, {}, {})".format(t, col, value),
                          'append': None}

APIs['none'] = {"argument":['str'], 'output': 'bool',
                "function": lambda t: none(t), 
                "tostr": lambda t : "None({})".format(t),
                'append': None}

APIs['next'] = {"argument":['row', 'row'], 'output': 'row',
                "function": lambda t, t1 : row_select(t, t1, 1),
                "tostr": lambda t, t1 : "next({}, {})".format(t),
                'append': True}

APIs['prev'] = {"argument":['row', 'row'], 'output': 'row',
                "function": lambda t, t1 : row_select(t, t1, -1),
                "tostr": lambda t, t1 : "prev({}, {})".format(t),
                'append': True}
"""
APIs['idx'] = {"argument":['row', 'row'], 'output': 'num',
                "function": lambda t, t1 : get_row(t, t1),
                "tostr": lambda t : "idx({})".format(t),
                'append': True}
"""
APIs['first'] = {"argument":['row', 'row'], 'output': 'bool',
                  'function': lambda t, t1 : n_th(t, t1, 0),
                  'tostr': lambda t, t1 : "first({}, {})".format(t, t1),
                  'append': None}

APIs['second'] = {"argument":['row', 'row'], 'output': 'bool',
                  'function': lambda t, t1 : n_th(t, t1, 1),
                  'tostr': lambda t, t1 : "second({}, {})".format(t, t1),
                  'append': None}

APIs['third'] = {"argument":['row', 'row'], 'output': 'bool',
                  'function': lambda t, t1 : n_th(t, t1, 2),
                  'tostr': lambda t, t1 : "second({}, {})".format(t, t1),
                  'append': None}

APIs['last'] = {"argument":['row', 'row'], 'output': 'bool',
                  'function': lambda t, t1 : n_th(t, t1, len(t) - 1),
                  'tostr': lambda t, t1 : "last({}, {})".format(t, t1),
                  'append': None}

# With only two argument and the first is row
APIs['avg'] = {"argument":['row', 'header_num'], 'output': 'num',
              "function": lambda t, col : t[col].mean(),
              "tostr": lambda t, col : "avg({}, {})".format(t, col),
              'append': True}

APIs['sum'] = {"argument":['row', 'header_num'], 'output': 'num',
              "function": lambda t, col : t[col].sum(),
              "tostr": lambda t, col : "sum({}, {})".format(t, col),
              'append': True}

APIs['max'] = {"argument":['row', 'header_num'], 'output': 'num',
              "function": lambda t, col : t[col].max(),
              "tostr": lambda t, col : "max({}, {})".format(t, col),
              'append': True}

APIs['min'] = {"argument":['row', 'header_num'], 'output': 'num',
                "function": lambda t, col : t[col].min(),
                "tostr": lambda t, col : "min({}, {})".format(t, col),
                'append': True}

APIs['argmax'] = {"argument":['row', 'header_num'], 'output': 'row',
                  'function': lambda t, col : t[t[col].values == t[col].values.max()],
                  'tostr': lambda t, col : "argmax({}, {})".format(t, col),
                  'append': False}

APIs['argmin'] = {"argument":['row', 'header_num'], 'output': 'row',
                  'function': lambda t, col :  t[t[col].values == t[col].values.min()],
                  'tostr': lambda t, col : "argmin({}, {})".format(t, col),
                  'append': False}
"""
APIs['last'] = {"argument":['row'], 'output': 'row',
                  'function': lambda t :  t.tail(1),
                  'tostr': lambda t : "last({})".format(t),
                  'append': False}

APIs['first'] = {"argument":['row'], 'output': 'row',
                  'function': lambda t :  t.head(1),
                  'tostr': lambda t : "first({})".format(t),
                  'append': False}
"""
APIs['str_hop'] = {"argument":['row', 'header_str'], 'output': 'str', 
               'function': lambda t, col :  t[col].values[0],
               'tostr': lambda t, col : "hop({}, {})".format(t, col),
               'append': True}

APIs['most_freq'] = {"argument":['row', 'header_str'], 'output': 'str',
               'function': lambda t, col : most_freq(t, col),  
               'tostr': lambda t, col : "most_freq({}, {})".format(t, col),
               'append': True}

APIs['num_hop'] = {"argument":['row', 'header_num'], 'output': 'num', 
               'function': lambda t, col :  t[col].values[0],
               'tostr': lambda t, col : "hop({}, {})".format(t, col),
               'append': True}


# With only two argument and the first is not row
APIs['diff'] = {"argument":['num', 'num'], 'output': 'num', 
                'function': lambda t1, t2 : t1 - t2,
                'tostr': lambda t1, t2 : "diff({}, {})".format(t1, t2),
                'append': True}

APIs['add'] = {"argument":['num', 'num'], 'output': 'num', 
                'function': lambda t1, t2 : t1 + t2,
                'tostr': lambda t1, t2 : "add({}, {})".format(t1, t2),
                'append': True}

APIs['greater'] = {"argument":['num', 'num'], 'output': 'bool', 
                   'function': lambda t1, t2 :  t1 > t2,
                   'tostr': lambda t1, t2 : "greater({}, {})".format(t1, t2),
                   'append': False}

APIs['less'] = {"argument":['num', 'num'], 'output': 'bool', 
                'function': lambda t1, t2 :  t1 < t2,
                'tostr': lambda t1, t2 : "less({}, {})".format(t1, t2),
                'append': True}

APIs['eq'] = {"argument":['num', 'num'], 'output': 'bool', 
              'function': lambda t1, t2 :  t1 == t2,
              'tostr': lambda t1, t2 : "eq({}, {})".format(t1, t2),
              'append': None}

APIs['not_eq'] = {"argument":['num', 'num'], 'output': 'bool', 
                 'function': lambda t1, t2 :  t1 != t2,
                 'tostr': lambda t1, t2 : "not_eq({}, {})".format(t1, t2),
                 "append": None}

APIs['and'] = {"argument":['bool', 'bool'], 'output': 'bool',
                'function': lambda t1, t2 :  t1 and t2,
                'tostr': lambda t1, t2 : "and({}, {})".format(t1, t2),
                "append": None}

APIs['str_eq'] = {"argument":['str', 'str'], 'output': 'bool', 
                  'function': lambda t1, t2 :  t1 in t2 or t2 in t1,
                  'tostr': lambda t1, t2 : "eq({}, {})".format(t1, t2),
                  "append": None}

APIs['not_str_eq'] = {"argument":['str', 'str'], 'output': 'bool', 
                     'function': lambda t1, t2 :  t1 not in t2 and t2 not in t1,
                     'tostr': lambda t1, t2 : "not_eq({}, {})".format(t1, t2),
                     "append": None}

#APIs['str_not_eq'] = {"argument":['str', 'str'], 'output': 'bool', 
#                        'function': lambda t1, t2 :  t1 != t2,
#                        'tostr': lambda t1, t2 : "not_eq({}, {})".format(t1, t2)}

#APIs['neither'] = {"argument":['bool', 'bool'], 'output': 'bool', 
#                        'function': lambda t1, t2 :  (not t1) and (not t2),
#                        'tostr': lambda t1, t2 : "neither({}, {})".format(t1, t2)}

# With only three argument and the first is row
APIs["filter_str_eq"] = {"argument": ['row', ['header_str', 'str']], "output": "row", 
                        "function": lambda t, col, value: t[t[col].str.contains(value, regex=False)],
                        "tostr":lambda t, col, value: "filter_str_eq({}, {}, {})".format(t, col, value),
                        'append': False}

APIs["filter_str_not_eq"] = {"argument": ['row', ['header_str', 'str']], "output": "row", 
                        "function": lambda t, col, value: t[~t[col].str.contains(value, regex=False)],
                        "tostr":lambda t, col, value: "filter_str_not_eq({}, {}, {})".format(t, col, value),
                        'append': False}


APIs["filter_eq"] = {"argument": ['row', ['header_num', 'num']], "output": "row", 
                    "function": lambda t, col, value: t[t[col] == value],
                    "tostr":lambda t, col, value: "filter_eq({}, {}, {})".format(t, col, value),
                    'append': False}

APIs["filter_not_eq"] = {"argument": ['row', ['header_num', 'num']], "output": "row", 
                    "function": lambda t, col, value: t[t[col] != value],
                    "tostr":lambda t, col, value: "filter_not_eq({}, {}, {})".format(t, col, value),
                    'append': False}

APIs["filter_less"] = {"argument": ['row', ['header_num', 'num']], "output": "row", 
                        "function": lambda t, col, value: t[t[col] < value],
                        "tostr":lambda t, col, value: "filter_less({}, {}, {})".format(t, col, value),
                        "append": False}

APIs["filter_greater"] = {"argument": ['row', ['header_num', 'num']], "output": "row",
                        "function": lambda t, col, value: t[t[col] > value],
                        "tostr":lambda t, col, value: "filter_greater({}, {}, {})".format(t, col, value),
                        "append": False}

APIs["filter_greater_eq"] = {"argument": ['row', ['header_num', 'num']], "output": "row",
                             "function": lambda t, col, value: t[t[col] >= value],
                             "tostr":lambda t, col, value: "filter_greater_eq({}, {}, {})".format(t, col, value),
                             "append": False}

APIs["filter_less_eq"] = {"argument": ['row', ['header_num', 'num']], "output": "row",
                          "function": lambda t, col, value: t[t[col] <= value],
                          "tostr":lambda t, col, value: "filter_less_eq({}, {}, {})".format(t, col, value),
                          "append": False}

APIs["all_str_eq"] = {"argument": ['row', ['header_str', 'str']], "output": "bool",
                        "function": lambda t, col, value: len(t) == len(t[t[col].str.contains(value, regex=False)]),
                        "tostr":lambda t, col, value: "all_eq({}, {}, {})".format(t, col, value),
                        "append": None}

APIs["all_eq"] = {"argument": ['row', ['header_num', 'num']], "output": "bool",
                  "function": lambda t, col, value: len(t) == len(t[t[col] == value]),
                  "tostr":lambda t, col, value: "all_eq({}, {}, {})".format(t, col, value),
                  "append": None}

APIs["all_less"] = {"argument": ['row', ['header_num', 'num']], "output": "bool",
                    "function": lambda t, col, value: len(t) == len(t[t[col] < value]),
                    "tostr":lambda t, col, value: "all_less({}, {}, {})".format(t, col, value),
                    "append": None}

APIs["all_less_eq"] = {"argument": ['row', ['header_num', 'num']], "output": "bool",
                        "function": lambda t, col, value: len(t) == len(t[t[col] <= value]),
                        "tostr":lambda t, col, value: "all_less_eq({}, {}, {})".format(t, col, value),
                        "append": None}

APIs["all_greater"] = {"argument": ['row', ['header_num', 'num']], "output": "bool",
                       "function": lambda t, col, value: len(t) == len(t[t[col] > value]),
                       "tostr":lambda t, col, value: "all_greater({}, {}, {})".format(t, col, value),
                       "append": None}

APIs["all_greater_eq"] = {"argument": ['row', ['header_num', 'num']], "output": "bool",
                          "function": lambda t, col, value: len(t) == len(t[t[col] >= value]),
                          "tostr":lambda t, col, value: "all_greater_eq({}, {}, {})".format(t, col, value),
                          "append": None}


APIs['samerow_num_str'] = {"argument": [['header_str', 'str'], ['header_num', 'num']], "output": "bool",
                          "function": lambda t, col1, value1, col2, value2: len(t[(t[col1].str.contains(value1, regex=False)) & (t[col2] == value2)]) > 0,
                          "tostr": lambda col1, value1, col2 , value2: "same({}, {}, {}, {})".format(col1, value1, col2, value2),
                          "append": None}

APIs['samerow_num'] = {"argument": [['header_num', 'num'], ['header_num', 'num']], "output": "bool",
                        "function": lambda t, col1, value1, col2, value2: len(t[(t[col1] == value1) & (t[col2] == value2)]) > 0,
                        "tostr": lambda col1, value1, col2 , value2: "same({}, {}, {}, {})".format(col1, value1, col2, value2),
                        "append": None}

APIs['samerow_str'] = {"argument": [['header_str', 'str'], ['header_str', 'str']], "output": "bool",
                        "function": lambda t, col1, value1, col2, value2: len(t[(t[col1].str.contains(value1, regex=False)) & (t[col2].str.contains(value2, regex=False))]) > 0,
                        "tostr": lambda col1, value1, col2 , value2: "same({}, {}, {}, {})".format(col1, value1, col2, value2),
                        "append": None}

def none(t):
  if 'none' in t or 'n / a' in t or t == '-' or 'no information' in t or 'no' in t:
    return True
  else:
    return False

def n_th(t, t1, num):
  def inner(t, t1):
    if len(t) == 1:
      t, t1 = t1, t
    col1, col2, col3, col4 = t.columns[0], t.columns[1], t.columns[2], t.columns[3]
    val1, val2, val3, val4 = t1[col1].values[0], t1[col2].values[0],  t1[col3].values[0], t1[col4].values[0]
    idx = t.loc[(t[col1] == val1) & (t[col2] == val2) & (t[col3] == val3) & (t[col4] == val4)].index
    if len(idx) > 0:
      return idx[0].item()
    else:
      return None
  tmp = inner(t, t1)
  if tmp is None:
    return None
  else:
    return tmp == num

def row_select(t, t1, bias):
  col1, col2, col3, col4 = t.columns[0], t.columns[1], t.columns[2], t.columns[3]
  val1, val2, val3, val4 = t1[col1].values[0], t1[col2].values[0],  t1[col3].values[0], t1[col4].values[0]
  idx = t.loc[(t[col1] == val1) & (t[col2] == val2) & (t[col3] == val3) & (t[col4] == val4)].index + bias
  if idx[0] < len(t) and idx[0] >= 0:
    return t.loc[idx]
  else:
    return None

def most_freq(t, col):
  value_counts = t[col].value_counts()
  if value_counts.max() == value_counts.min():
    return None
  else:
    return value_counts.idxmax()

triggers = {}
non_triggers = {}

non_triggers['avg'] = ['average']
non_triggers['diff'] = ['difference', 'gap', 'than', 'separate']
non_triggers['add'] = ['sum', 'summation', 'combine', 'combined', 'total', 'add', 'all', 'there are']
non_triggers['sum'] = non_triggers['add']

#non_triggers['str_not_eq'] = ['not', 'no', 'never', "'nt", 'neither', 'none']
#non_triggers['not_eq'] = ['not', 'no', 'never', "'nt", 'neither', 'none']
non_triggers['not_eq'] = ['not', 'no', 'never', "didn't", "won't", "wasn't", "isn't", 
                          "haven't", "weren't", "won't", 'neither', 'none', 'unable', 
                          'fail', 'different', 'outside', 'unable', 'fail']

non_triggers['not_str_eq'] = non_triggers['not_eq']
non_triggers['not_within_s_s'] = non_triggers['not_eq']
non_triggers['not_within_n_n'] = non_triggers['not_eq']
non_triggers['filter_str_not_eq'] = non_triggers['not_eq']
non_triggers['filter_not_eq'] = non_triggers['not_eq']
non_triggers['none'] = ['not', 'no', 'none']

non_triggers['first'] = ['first', 'top', 'latest', 'most']
non_triggers['last'] = ['last', 'bottom', 'latest', 'most']

non_triggers["filter_greater"] = ['RBR', 'JJR', 'more', 'than', 'above', 'after']
non_triggers["filter_less"] = ['RBR', 'JJR', 'less', 'than', 'below', 'under']
non_triggers['less'] = ['RBR', 'JJR', 'less', 'than', 'below', 'under']
non_triggers['greater'] = ['RBR', 'JJR', 'more', 'than', 'above', 'after', 'exceed']

non_triggers['all_eq'] = ['all', 'equal', 'every', 'each']
non_triggers['all_less'] = [['all', 'equal', 'every', 'each'], ['RBR', 'JJR']]
non_triggers['all_greater'] = [['all', 'equal', 'every', 'each'], ['RBR', 'JJR']]
non_triggers['all_str_eq'] = ['all', 'equal', 'every', 'each']

non_triggers['filter_less_eq'] = ['at most', 'than']
non_triggers['filter_greater_eq'] = ['at least', 'than']

non_triggers['all_less_eq'] = [['at least', 'than'], ['all', 'equal', 'while', 'every', 'each']]
non_triggers['all_greater_eq'] = non_triggers['all_less_eq']

non_triggers['inc_num'] = ['and', 'while', 'when', ',', 'both', 'neither', 'none', 'all', 'which', 'who', 'that', 'whose']
non_triggers['inc_str'] = non_triggers['inc_num']

non_triggers['max'] = ['RBR', 'RBS', 'JJR', 'JJS']
non_triggers['min'] = non_triggers['max']
non_triggers['argmax'] = ['JJR', 'JJS', 'RBR', 'RBS', 'top', 'first']
non_triggers['argmin'] = non_triggers['argmax']

non_triggers['within_s_s'] = ['within', 'one', 'of', 'among']
non_triggers['within_n_n'] = non_triggers['within_s_s']

non_triggers['next'] = ['follow', 'following', 'followed', 'under', 'after']
non_triggers['prev'] = ['before', 'above', 'precede', 'preceded', 'preceding']

non_triggers['most_freq'] = ['RBS', 'JJS', 'RBR', 'JJR']
non_triggers['first'] = ['first', '1st', 'top']
non_triggers['second'] = ['second', '2nd']
non_triggers['third'] = ['third', '3rd']
non_triggers['last'] = ['last', 'bottom']
#non_triggers['istype_s_n'] = ['is', 'are', 'were', 'was', 'be', 'within', 'one', 'of']
#non_triggers['istype_n_s'] = ['is', 'are', 'were', 'was', 'be', 'within', 'one', 'of']
#non_triggers['count'] = ['there', 'num', 'amount', 'have', 'has', 'had', 'are', 'more']
#non_triggers['max'] = [k for k, v in triggers.iteritems() if v == 'max']
#non_triggers['argmax'] = [k for k, v in triggers.iteritems() if v == 'argmax']
#non_triggers['and'] = ['and', 'while', 'when', ',', 'neither', 'none', 'all', 'both']
#non_triggers['neither'] = ['neither', 'none', 'not', "'nt", 'both']
