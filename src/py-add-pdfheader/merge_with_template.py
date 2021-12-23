from PyPDF2 import PdfFileWriter, PdfFileReader


def merge_pdf(source_pdf_path, output_file_path, include_top_page=True, template_pdf_path="header_template/header_text_A4.pdf"):
    
    with open(template_pdf_path, "rb") as f_inpdf:
        template_pdf = PdfFileReader(f_inpdf)
        template_page = template_pdf.getPage(0)

        with open(source_pdf_path, 'rb') as f_srcpdf:
            source_pdf = PdfFileReader(f_srcpdf, strict=False)

            page_count = source_pdf.getNumPages()

            print(source_pdf.getPage(0).mediaBox)


            output_file = PdfFileWriter()
            for page_number in range(page_count):
                input_page = source_pdf.getPage(page_number)

                if page_number or include_top_page:
                    input_page.mergePage(template_page)
                    input_page.compressContentStreams()
                output_file.addPage(input_page)
        
            with open(output_file_path, "wb") as f:
                output_file.write(f)

