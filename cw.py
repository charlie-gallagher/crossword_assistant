import re


# Define some exceptions
class CwSyntaxError(Exception):
    def __init__(self, message):
        if message is not None:
            self.message = message
        else:
            self.message = "No message given"

    def __str__(self):
        return f'Error: {self.message}'


# Parse conditions
def is_length(arg_str):
    if re.match("^\\d+$", arg_str):
        return True
    else:
        return False


def is_letter(arg_str):
    if re.match("^\\d+[A-Za-z]$", arg_str):
        return True
    else:
        return False


def is_expr(arg_str):
    if re.match("^\\d+\\(.*\\)", arg_str):
        return True
    else:
        return False


# Parse command-line
# TODO: Make this more restrictive
def cw_parse_cl(args):
    out = dict(length=0, letters=list(), positions=list())
    if len(args) == 1:
        raise CwSyntaxError("No arguments given")
    for a in args[1:]:
        if is_length(a):
            out["length"] = int(a)
        elif is_letter(a):
            out["positions"].append(int(a[0]))
            out["letters"].append(a[1])
        elif is_expr(a):
            out["positions"].append(int(a[0]))
            out["letters"].append(a[1:])
        else:
            raise CwSyntaxError(f"[{a}] invalid argument")

    if out["length"] == 0:
        raise CwSyntaxError("Must have length argument")
    return out


# Generate regular expression from parsed commands
def cw_gen_regex(letters, positions, length):
    reg_expression = "^"

    for i in range(1, length+1):
        if i in positions:
            reg_expression += letters[positions.index(i)]
        elif i not in positions:
            reg_expression += "[A-Za-z]"
    reg_expression += "\\n$"

    return reg_expression


# Search files for regular expression
def cw_search_words(reg_expression, filename):
    c_regex = re.compile(reg_expression, flags=re.IGNORECASE)
    with open(filename, "r") as lxwds:
        for line in lxwds:
            m = c_regex.fullmatch(line, )
            if m is not None:
                print(m.string, end="")
            else:
                pass






