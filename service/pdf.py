import PyPDF2
import re
from env import PUBLIC_DIR
def get_abstract(filename):
    with open(f'{PUBLIC_DIR}/{filename}', 'rb') as pdf_file:

        # creating a pdf reader object
        pdfReader = PyPDF2.PdfReader(pdf_file)

        full_text = ""

        for i in range(len(pdfReader.pages)):
            pageObj = pdfReader.pages[i]
            text = pageObj.extract_text()
            last_digits = text[-10:]
            latest_digit = 0
            for i in range(len(last_digits)):
                if last_digits[i].isdigit():
                    latest_digit = i
                    break

            if latest_digit != 0:
                text = text[:-latest_digit]
            text = text.lower()
            full_text += text+"\n"
            
            # extracting text from page

        word = 'abstract'

        ini = full_text.find('abstract')
        full_text = full_text[ini+len(word):]


        pattern = re.compile(r'^(\d+)[\s.]\s*(?!\d)(.+)$', re.MULTILINE)

        matches = pattern.finditer(full_text)

        titles = []
        # Extracted titles
        for match in matches:
            title_number = match.group(1)
            title_text = match.group(2)
            start_index = match.start()
            end_index = match.end()
            if len(title_text) < 25 and int(title_number) < 100:
                titles.append((title_number, title_text, start_index, end_index))

    return full_text[ini:titles[0][2]]