from pathlib import Path

def test_pdf_image(input_path=None):
    import fitz  # PyMuPDF

    # input_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/권한관련쿼리.pdf"

    input_path = Path(input_path)
    output_dir = input_path.parent
    output_jpeg = output_dir / f"{input_path.stem}.jpeg"
    max_side = 2000

    # PDF 열기
    with fitz.open(input_path) as file:

        # 페이지 가져오기 (keywords 가 포함된 페이지를 찾으면 그 다음 페이지를 이미지화한다)
        page_num = 0
        keywords = ["목차", "Table of Contents", "Contents"]
        for i, page in enumerate(file):
            text = page.get_text()
            if any(kw in text for kw in keywords):
                page_num = i + 1  # 목차 다음 페이지
        print(page_num)
        page = file.load_page(page_num)


        # 페이지 원본 크기
        rect = page.rect
        width, height = rect.width, rect.height

        print(f"원본 가로,세로 : {width}, {height}")
        if height > width and height > max_side: # 세로 이미지
            scale = width / height
            is_resize = True
        elif width > max_side: # 가로 이미지, 정사각형 (가로기준하면될듯)
            scale = height / width
            is_resize = True
        else: # 사이즈가 작아서 리사이즈 없음
            is_resize = False

        if is_resize:
            # scale을 이용해 매트릭스 생성 (가로/세로 비율 유지)
            matrix = fitz.Matrix(scale, scale)
        else:
            matrix = None

        # 이미지 생성
        pix = page.get_pixmap(matrix=matrix)

        # 이미지 저장
        pix.save(output_jpeg)




def test_file_to_pdf(input_path):
    # libreoffice
    import subprocess

    input_path = Path(input_path)
    output_dir = input_path.parent
    output_pdf = output_dir / f"{input_path.stem}.pdf"

    print(input_path)
    print(output_dir)
    print(output_pdf)

    if not input_path.exists():
        raise FileNotFoundError(f"{input_path} not found")

    liberoffice_path = "/Applications/LibreOffice.app/Contents/MacOS/soffice"
    # LibreOffice를 사용하여 PDF로 변환
    subprocess.run([
        liberoffice_path, "--headless", "--convert-to", "pdf", "--outdir",
        str(output_dir), str(input_path)
    ], check=True)

    if not output_pdf.exists():
        raise RuntimeError(f"PDF 변환 실패: {output_pdf}")

    print(f"✅ PDF 저장 완료: {output_pdf}")


def test_file():
    input_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/국민연금공단_오픈API활용가이드_국민연금 가입현황_v2.0.docx"

    input_path = Path(input_path)
    output_dir = input_path.parent
    output_pdf = output_dir / f"{input_path.stem}.pdf"

    # to pdf
    test_file_to_pdf(input_path)
    # to image
    test_pdf_image(output_pdf)