# freescan
A repository which contains Django code frontend + backend with few pages to process &amp; extract info from the uploaded PDF files.


## How did I resolve the issue of creating documents!


```python
>>> from PyPDF2 import PdfReader, PdfFileWriter
>>> 
>>> writer = PdfFileWriter()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/hygull/Projects/Python/Django/AIPALETTE/FORESIGHT_ENGINE_PROJ/try/freescan/venv3.6.7/lib/python3.6/site-packages/PyPDF2/_writer.py", line 2821, in __init__
    deprecation_with_replacement("PdfFileWriter", "PdfWriter", "3.0.0")
  File "/Users/hygull/Projects/Python/Django/AIPALETTE/FORESIGHT_ENGINE_PROJ/try/freescan/venv3.6.7/lib/python3.6/site-packages/PyPDF2/_utils.py", line 369, in deprecation_with_replacement
    deprecation(DEPR_MSG_HAPPENED.format(old_name, removed_in, new_name))
  File "/Users/hygull/Projects/Python/Django/AIPALETTE/FORESIGHT_ENGINE_PROJ/try/freescan/venv3.6.7/lib/python3.6/site-packages/PyPDF2/_utils.py", line 351, in deprecation
    raise DeprecationError(msg)
PyPDF2.errors.DeprecationError: PdfFileWriter is deprecated and was removed in PyPDF2 3.0.0. Use PdfWriter instead.
>>> 'There is no data on ES for this Query. Total count'.upper()
'THERE IS NO DATA ON ES FOR THIS QUERY. TOTAL COUNT'
>>> 
```

```python
>>> from PyPDF2 import PdfReader, PdfFileWriter
>>> 
>>> from io import BytesIO
>>> from PyPDF2 import PdfWriter
>>> 
>>> op_buf = BytesIO()
>>> 
>>> writer = PdfWriter()
>>> 
>>> page = writer.addBlankPage(width=595, height=842)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/hygull/Projects/Python/Django/AIPALETTE/FORESIGHT_ENGINE_PROJ/try/freescan/venv3.6.7/lib/python3.6/site-packages/PyPDF2/_writer.py", line 442, in addBlankPage
    deprecation_with_replacement("addBlankPage", "add_blank_page", "3.0.0")
  File "/Users/hygull/Projects/Python/Django/AIPALETTE/FORESIGHT_ENGINE_PROJ/try/freescan/venv3.6.7/lib/python3.6/site-packages/PyPDF2/_utils.py", line 369, in deprecation_with_replacement
    deprecation(DEPR_MSG_HAPPENED.format(old_name, removed_in, new_name))
  File "/Users/hygull/Projects/Python/Django/AIPALETTE/FORESIGHT_ENGINE_PROJ/try/freescan/venv3.6.7/lib/python3.6/site-packages/PyPDF2/_utils.py", line 351, in deprecation
    raise DeprecationError(msg)
PyPDF2.errors.DeprecationError: addBlankPage is deprecated and was removed in PyPDF2 3.0.0. Use add_blank_page instead.
>>> 
>>> page = writer.add_blank_page(width=595, height=842)
>>> 
>>> canvas = page.getCanvas()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'PageObject' object has no attribute 'getCanvas'
>>> 
>>> canvas = page.get_canvas()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'PageObject' object has no attribute 'get_canvas'
>>> 
>>> dir(page
... )
['__abstractmethods__', '__annotations__', '__args__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__extra__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__next_in_mro__', '__orig_bases__', '__origin__', '__parameters__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__tree_hash__', '__weakref__', '_abc_cache', '_abc_generic_negative_cache', '_abc_generic_negative_cache_version', '_abc_registry', '_add_transformation_matrix', '_clone', '_content_stream_rename', '_debug_for_extract', '_expand_mediabox', '_extract_text', '_get_fonts', '_gorg', '_is_protocol', '_merge_page', '_merge_resources', '_push_pop_gs', '_reference_clone', 'addTransformation', 'add_transformation', 'annotations', 'artBox', 'artbox', 'bleedBox', 'bleedbox', 'clear', 'clone', 'compressContentStreams', 'compress_content_streams', 'copy', 'createBlankPage', 'create_blank_page', 'cropBox', 'cropbox', 'extractText', 'extract_text', 'extract_xform_text', 'fromkeys', 'get', 'getContents', 'getObject', 'getXmpMetadata', 'get_contents', 'get_object', 'hash_func', 'hash_value', 'hash_value_data', 'images', 'indirect_ref', 'indirect_reference', 'items', 'keys', 'mediaBox', 'mediabox', 'mergePage', 'mergeRotatedPage', 'mergeRotatedScaledPage', 'mergeRotatedScaledTranslatedPage', 'mergeRotatedTranslatedPage', 'mergeScaledPage', 'mergeScaledTranslatedPage', 'mergeTransformedPage', 'mergeTranslatedPage', 'merge_page', 'pdf', 'pop', 'popitem', 'raw_get', 'readFromStream', 'read_from_stream', 'rotate', 'rotateClockwise', 'rotateCounterClockwise', 'rotate_clockwise', 'rotation', 'scale', 'scaleBy', 'scaleTo', 'scale_by', 'scale_to', 'setdefault', 'transfer_rotation_to_content', 'trimBox', 'trimbox', 'update', 'user_unit', 'values', 'writeToStream', 'write_to_stream', 'xmpMetadata', 'xmp_metadata']
>>> 

>>> canvas = writer.create_canvas(page)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'PdfWriter' object has no attribute 'create_canvas'
>>> 
>>> from reportlab
  File "<console>", line 1
    from reportlab
                 ^
SyntaxError: invalid syntax
>>> from reportlab.pdfgen import anvas
Traceback (most recent call last):
  File "<console>", line 1, in <module>
ModuleNotFoundError: No module named 'reportlab'
>>> from reportlab.pdfgen import canvas
Traceback (most recent call last):
  File "<console>", line 1, in <module>
ModuleNotFoundError: No module named 'reportlab'
>>> 
>>> import os
>>> os.system('pip install reportlab')
Collecting reportlab
  Downloading reportlab-3.6.8.tar.gz (4.5 MB)
     |████████████████████████████████| 4.5 MB 806 kB/s            
  Preparing metadata (setup.py) ... done
Collecting pillow>=4.0.0
  Downloading Pillow-8.4.0-cp36-cp36m-macosx_10_10_x86_64.whl (3.0 MB)
     |████████████████████████████████| 3.0 MB 608 kB/s            
Building wheels for collected packages: reportlab
  Building wheel for reportlab (setup.py) ... done
  Created wheel for reportlab: filename=reportlab-3.6.8-cp36-cp36m-macosx_10_9_x86_64.whl size=2001873 sha256=b37f8be34ce1500354dca505608529340fbf961dce2b62b44731ea7f5bd7e150
  Stored in directory: /Users/hygull/Library/Caches/pip/wheels/c2/59/40/3b6524114e76b895cb6fe13bd6c6f2356ad4734650f6414a59
Successfully built reportlab
Installing collected packages: pillow, reportlab
Successfully installed pillow-8.4.0 reportlab-3.6.8
0
>>> from reportlab.pdfgen import canvas
>>> canvas = canvas.Canvas(op_buf, pagesize=(595, 842))
>>> 
>>> canvas.drawString(100, 750, "Ok fine!")
>>> canvas.save()
>>> 
>>> with open('Test.pdf', 'wb') as f:
...     f.write(op_buf.getvalue())
... 
1403
>>> 
```