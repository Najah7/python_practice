from optparse import OptionParser
from optparse import OptionGroup


def main():

    # 引数useage：--helpの時に出力されるもの
    usage = "usage: %prog [option] arg1 arg2"
    parser = OptionParser(usage=usage)
    
    #　一般的な使い方
    # NOTE:destは格納先、parse_args()でoptparseのValueオブジェクトのクラス変数として格納する変数名（プロパティ名）。違うオプションで同じもの指し示すことも可能。
    # HACK:もっとわかりやすい説明を↑
    parser.add_option(
        "-f",
        "--file",
        action="store",
        type="string",
        dest="filename",
        help="File name",
        default="ファイル指定されてないよ",
    )
    parser.add_option("-n", "--num", action="store", type="int", dest="num")
    parser.add_option("-v", action="store_true", dest="verbose_true")
    parser.add_option("-q", action="store_false", dest="varbose_false")
    options, args = parser.parse_args()
    print(options)
    print(args)
    
    # callbackのactionを使った場合。（シンプルに関数を呼び出せるというだけ。）
    parser.add_option('-e', dest='env')
    def is_release(option, opt_str, value, parser):
        if parser.values.env == "prd":
            raise parser.error("Can't release")
        setattr(parser.values, option.dest, True)

    parser.add_option('--release', action='callback', callback=is_release, dest='release')
    
    # OptionGroupを使ってグループを作る例（危険なオプションをまとめたり、それぞれ関係あるオプションごとにまとめたりするときに使える）
    group = OptionGroup(parser, 'Dangerous options')
    group.add_option('-g', action='store_true', help='Group option')
    parser.add_option_group(group)
    
if __name__ == "__main__":
    main()
