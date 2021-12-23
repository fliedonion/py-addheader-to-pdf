# make image pdf for merge

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, A3, landscape
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics, ttfonts



def create_header_logo_pdf(size, header_left_text, header_right_text):
    (key, w, h, pagesize) = size
    

    MS_P_GO_KEY = 'MsP Gothic' # register key for this program.
    pdfmetrics.registerFont(ttfonts.TTFont(MS_P_GO_KEY, 'c:/Windows/Fonts/msgothic.ttc'))

    c = canvas.Canvas(f'header_template/header_text_{key}.pdf', pagesize=pagesize)

    ## (x:0, y:0) points bottom left of page (NOT top left).
    # target_x, target_y = 10 * mm, (h - 9) * mm
    # c.drawImage('image.jpg', target_x, target_y)

    c.setFillColorRGB(0.2, 0.2, 0.2) # in case drawString, this means fore color.
    c.setFont(MS_P_GO_KEY, 9) #choose your font type and font size

    header_left, header_right = header_left_text, header_right_text 
    target_x, target_y = 6 * mm, (h - 9) * mm
    c.drawString(target_x, target_y, header_left)

    target_x, target_y = (w - 6) * mm, (h - 9) * mm
    c.drawRightString(target_x, target_y, header_right)
    # the x axis value of right side of last char of header_right is target_x.
    
    ## or we can use Canvas#stringWidth to measure text length
    # target_x, target_y = ((w - 6) * mm  - c.stringWidth(text=header_right)), (h - 9) * mm
    # c.drawString(target_x, target_y, header_right)

    ## sample footer
    # target_x, target_y = 6 * mm, 6 * mm
    # c.drawString(target_x, target_y, "Footer!")

    c.save()



"""
## decorate sample:

from reportlab.pdfgen import canvas

def hello(c):
    from reportlab.lib.units import inch

    #First Example
    c.setFillColorRGB(1,0,0) #choose your font colour
    c.setFont("Helvetica", 30) #choose your font type and font size
    c.drawString(100,100,"Hello World") # write your text

    #Second Example
    c.setStrokeColorRGB(0,1,0.3) #choose your line color
    c.line(2,2,2*inch,2*inch)

    #Third Example
    c.setFillColorRGB(1,1,0) #choose fill colour
    c.rect(4*inch,4*inch,2*inch,3*inch, fill=1) #draw rectangle

c = canvas.Canvas("hello.pdf")

hello(c)
c.showPage()
c.save()

"""