from ..papersizes import sizes
from .create_template import create_header_logo_pdf

def main():
    for size in sizes:
        create_header_logo_pdf(size, "【社外秘】", "とうきょうとっきょきょかきょく株式会社")

    # import sys
    # 
    # for pos, arg in enumerate(sys.argv):
    #     print('Argument %d: %s' % (pos, arg))


if __name__ == '__main__':
    main()
