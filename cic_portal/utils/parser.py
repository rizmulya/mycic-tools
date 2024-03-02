import argparse


def parser():
    parser = argparse.ArgumentParser(
        description='Mycic Tools',
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument('-a', '--absen', action='store_true',
                        help='Absen mycic')
    parser.add_argument('-m', '--manual', action='store_true',
                        help='Absen manual [-a -m]')
    parser.add_argument('-j', '--jadwal', action='store_true',
                        help='Extract jadwal ke png & csv')
    
    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.print_help()
    else:
        return args