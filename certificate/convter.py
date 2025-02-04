# import json
# import requests



# def ppt2pdf(f_path,filename, token):

#     headers = {"Authorization": token}
#     para = {
#         "name": filename,
#         "parents": ["13GzxN9pBRmFPP960zK0xfDbZbCll0w_Q"]
#         }
#     files = {
#         'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
#         'file': open(f_path, "rb")
#         }
#     r = requests.post(
#         "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
#         headers=headers,
#         files=files
#         )
#     fi = r.text.split()
#     st = fi[4]
#     st = st[1:-2]
#     return st

import subprocess
import os

def convert_pptx_to_pdf(input_file, output_file):
    try:
        subprocess.run(['/Applications/LibreOffice.app/Contents/MacOS/soffice', 
                        '--headless', '--convert-to', 'pdf', input_file, 
                        '--outdir', os.path.dirname(output_file)], 
                       check=True)
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"Error converting {input_file} to PDF: {e}")
        return None
