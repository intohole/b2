#coding=utf-8


import re
import sys
_parser_regx = re.compile(ur"""^(
            [\w\d\.\*\+\\]+
            )(
                \[
                @([\w\d]+)
                (=|>=|<=|>|<|~){1}
                ([\d\w]+)\]
            )?""" ,re.VERBOSE)
for query_params in sys.argv[1].split("/"):
    if query_params == "":
        continue
    print _parser_regx.match(query_params).groups()
    print _parser_regx.match(query_params).groups()
