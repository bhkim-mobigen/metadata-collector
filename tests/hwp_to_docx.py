import subprocess
import os

#libreoffice
liberoffice_path = "/Applications/LibreOffice.app/Contents/MacOS/soffice"

def convert_hwpx_to_docx(hwpx_path):
    cmd = [liberoffice_path, '--headless', '--convert-to', 'docx', hwpx_path]
    subprocess.run(cmd, check=True)

def convert_docx_to_pdf(docx_path):
    cmd = [liberoffice_path, '--headless', '--convert-to', 'pdf', docx_path]
    subprocess.run(cmd, check=True)

def convert_hwp_hwpx_to_pdf(file_path):
    # 확장자 구분
    ext = os.path.splitext(file_path)[1].lower()

    if ext == '.hwpx':
        convert_hwpx_to_docx(file_path)
        docx_path = os.path.splitext(file_path)[0] + '.docx'
        convert_docx_to_pdf(docx_path)
        print(f"Converted {file_path} to PDF via DOCX.")
    elif ext == '.hwp':
        # hwp는 libreoffice에서 바로 변환 시도해보고 실패하면 다른 방법 고려
        # 우선 docx 변환 시도
        convert_hwpx_to_docx(file_path)  # 시도해보는 거지만 hwp는 안 될 가능성 있음
        docx_path = os.path.splitext(file_path)[0] + '.docx'
        if os.path.exists(docx_path):
            convert_docx_to_pdf(docx_path)
            print(f"Converted {file_path} to PDF via DOCX.")
        else:
            # hwp → pdf 직접 변환 시도
            cmd = [liberoffice_path, '--headless', '--convert-to', 'pdf', file_path]
            subprocess.run(cmd, check=True)
            print(f"Converted {file_path} directly to PDF.")
    else:
        print("지원하지 않는 파일 형식입니다.")

def test_hwp_to_pdf():
    convert_hwp_hwpx_to_pdf('/Users/hy/workspace/metadata_collector/tmp/2021년도+조사료생산기반확충+사업시행지침(최종).hwpx')

