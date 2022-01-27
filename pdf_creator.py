from fpdf import FPDF


class Pdf_Creator():

    def __init__(self, filename, news_list):
        self.filename=filename

        pdf = FPDF()
        pdf.add_page()  
        pdf.set_font('Arial', size = 12)

        iter = 1
        for news in news_list:
            pdf.multi_cell(190, 8, txt= news.create_text(), border=1 , align='L')
            print('Adding news {} to PDF file...'.format(iter))
            iter += 1
            #pdf.image(name=news.img, w = 10, h= 10, type='JPG')
        pdf.output(self.filename)
        print('File created : {} '.format(self.filename))    
