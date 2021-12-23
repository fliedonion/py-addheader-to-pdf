
from sys import stderr


def main():
    import sys
    from .merge_with_template import merge_pdf

    if len(sys.argv) > 2:
        
        source = sys.argv[1] 
        template_size_key = sys.argv[2]

   
        outname = "{0}_{2}.{1}".format(*source.rsplit('.', 1) + ["with_header"]) # "+": concat 2 items array + one item array.
        
        include_top_page = True

        try:
            merge_pdf(source, outname, include_top_page, f"./header_template/header_text_{template_size_key}.pdf")
        except Exception as err:
            print(err.message, file = sys.stderr )

    else:
        print('missing filename or paper sie argument')
        print('usage: py -m py-add-pdfheader sample.pdf A3')


if __name__ == '__main__':
    # importされたときのために一応。
    main()
