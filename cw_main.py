import cw
import sys
from pathlib import Path


def main():
    arg_dict = cw.cw_parse_cl(sys.argv)
    tmp_reg = cw.cw_gen_regex(arg_dict["letters"],
                           arg_dict["positions"],
                           arg_dict["length"])
    print("Linux words\n-----------")
    cw.cw_search_words(tmp_reg, Path("wordlists", "linuxwords.txt"))
    print("\nCrossword Nexus words\n-----------")
    cw.cw_search_words(tmp_reg, Path("wordlists", "crossword_nexus_wordlist.txt"))


if __name__ == '__main__':
    main()
