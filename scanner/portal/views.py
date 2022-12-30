from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic.base import View
from portal.models import Category
import PyPDF2
from io import BytesIO
from reportlab.pdfgen import canvas
from django.template.context_processors import csrf
from rest_framework.parsers import FormParser, MultiPartParser, FileUploadParser, JSONParser
import pandas as pd
from pathlib import Path
from datetime import datetime
from django.http import HttpResponse
import os


class LoginView(View):
    pass

class DocumentView(APIView):
    # parser_classes = [JSONParser, FormParser, MultiPartParser]
    # parser_classes = [JSONParser, MultiPartParser, ]
    parser_classes = [FormParser, MultiPartParser]

    def get(self, request, *args, **kwargs):
        categories = Category.objects.filter(active=True)

        context = {
            'categories': categories
        }
        return render(request, 'index.html', context)


    def post(self, request, *args, **kwargs):
        print(request.headers)
        status, message, data = 200, 'Document Uploaded Successfully', request.data
        
        category = data.get('category', '')
        find_text = data.get('find_text', '')
        notes = data.get('notes', '')
        file =  data.get('file') # None
        print('category', 'find_text', find_text)
        # ----
        # file = open('docs/sample.pdf', 'rb')
        pdf_reader = PyPDF2.PdfReader(file)
        text = pdf_reader.pages[0].extract_text()
        print(text)
        df = pd.DataFrame(text.split('\n'), columns=['text'])
        print(df)

        df_final = df[df['text'].str.contains(find_text)]
        print('Result')
        print(df_final)
        print(Path.home())

        # try:
        #     path = os.sep.join(['docs', 'output', f'Scanned_Output_{datetime.now()}.pdf'])
        #     with Path(path).open(mode='wb') as fw:
        #         final_lines = '\n'.join(df_final['text'])
        #         print('Ok->', final_lines, type(final_lines))
        #         fw.write('Property Scan Findings\n'.encode('utf8'))
        #         fw.write(final_lines.encode('utf8'))
        #         fw.write(f'\n{notes}'.encode('utf8'))

        #     content_type = 'application/pdf'
        #     response = HttpResponse(open(path, 'rb'), content_type=content_type)
        #     response['Content-Disposition'] = 'attachment; filename="Pdf Report - {}"'.format(path.split('/')[-1])
        #     # ----

        #     print('category', category, 'find_text', find_text, 'notes', notes, 'file', file)
        #     # c = {}
        #     # c.update(csrf(request))
        #     return response
        # except Exception as exc:
        #     return Response({
        #         'status': 400,
        #         'message': f'{exc}'
        #     })

        try:
            print('Starting the work!')
            op_buf = BytesIO()
            writer = PyPDF2.PdfWriter()
            print('canvas', canvas)
            page = writer.add_blank_page(width=595, height=842)
            canvas_obj = canvas.Canvas(op_buf, pagesize=(595, 842))
            canvas_obj.drawString(100, 750, '\n'.join(df_final['text']))
            canvas_obj.save()

            filepath = os.sep.join(['docs', 'output', f'Scanned_Output_{datetime.now()}.pdf'])

            with open(filepath, 'wb') as f:
                f.write(op_buf.getvalue())

            content_type = 'application/pdf'
            response = HttpResponse(open(filepath, 'rb'), content_type=content_type)
            response['Content-Disposition'] = 'attachment; filename="Pdf Report - {}"'.format(filepath.split('/')[-1])
        
            print(filepath)
            print('category', category, 'find_text', find_text, 'notes', notes, 'file', file)
            return response
        except Exception as exc:
            raise
            return Response({
                'status': 400,
                'message': f'{exc}'
            })

