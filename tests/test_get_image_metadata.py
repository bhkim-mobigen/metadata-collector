# https://sample-files-online.com/


from pathlib import Path
import os

from networkx.generators.small import heawood_graph


def get_pil_metadata(file_path):
    from PIL import Image
    from PIL.ExifTags import TAGS

    metadata = {}
    try:
        with Image.open(file_path) as img:
            metadata["format"] = img.format         # JPEG, PNG 등
            metadata["mode"] = img.mode             # RGB, RGBA, L (흑백) 등
            metadata["size"] = img.size             # (width, height)

            # info : dpi-해상도 (tuple: (x_dpi, y_dpi)), comment-주석
            img_info = img.info
            if img_info:
                for k, v in img_info.items():
                    if k == 'exif':
                        continue
                    metadata[f"info.{k}"] = v

            # EXIF 데이터 추출 (JPEG, TIFF에 주로 존재)
            if hasattr(img, '_getexif'):
                img_exif = img._getexif()
                if img_exif:
                    for tag_id, value in img_exif.items():
                        tag = TAGS.get(tag_id, tag_id)
                        metadata[f"exif.{tag}"] = value

        # #대표생상 구하기
        # from collections import Counter
        #
        # # 이미지 열기 및 축소 (성능 향상)
        # img = Image.open(file_path).convert("RGB")
        # small_img = img.resize((100, 100))  # 크기 줄이기
        #
        # # 픽셀 데이터 추출
        # pixels = list(small_img.getdata())
        #
        # # 색상 빈도 계산
        # counter = Counter(pixels)
        # most_common_colors = counter.most_common(10)  # 상위 10개 색상 추출
        #
        # # RGB 값 리스트
        # palette_colors = [color for color, count in most_common_colors]
        # if len(palette_colors) > 0:
        #     metadata['palette_colors'] = palette_colors
    except Exception as e:
        return f"{file_path} err : {e}"

    print("\n")
    for key in metadata:
        print(f"{key} : {metadata[key]}")

    format = Path(file_path).name.split(".")[1]
    return f"{format} - meta len : {len(metadata)}"

def test_extract_pil_metadata():
    file_names = None
    dir_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/image"

    file_names = [
        "sample-CR2-Image-File.cr2",
        "sample-nef-files-sample1.nef",
        "1718863107_DSC00343.ARW",
        "1718867207_P4155261.ORF",
        "1718865090_RAW_CANON_DCS1.tiff",
        "1718865075_RAW_KODAK_DCS560C.tif"
    ]

    reports = []
    if file_names is None:
        file_names = os.listdir(dir_path)

    for file_name in file_names:
        file_path = os.path.join(dir_path, file_name)
        report = get_pil_metadata(file_path)
        if report:
            reports.append(report)

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> report <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    for s in reports:
        print(s)



def get_exifread_metadata(file_path):
    import exifread
    try:
        # 이미지 파일 열기 (JPEG, TIFF 권장)
        with open(file_path, 'rb') as f:
            tags = exifread.process_file(f, details=False)

        # 주요 메타데이터 출력
        print("\n촬영일시:", tags.get('EXIF DateTimeOriginal'))
        print("카메라 제조사:", tags.get('Image Make'))
        print("카메라 모델:", tags.get('Image Model'))
        print("위도:", tags.get('GPS GPSLatitude'))
        print("경도:", tags.get('GPS GPSLongitude'))
        print("색공간:", tags.get('EXIF ColorSpace'))
        print("화이트밸런스:", tags.get('EXIF WhiteBalance'))
        print("해상도:", f"{tags.get('Image ImageWidth')}, {tags.get('Image ImageLength')}")
        print("밝기:", tags.get('BrightnessValue'))

        print('==모든 메타==')

        for k in tags:
            print(f"{k} : {tags[k]}")
    except Exception as e:
        return f"{file_path} err : {e}"

    format = Path(file_path).name.split(".")[1]
    return f"{format} - meta len : {len(tags)}"

def test_extract_exifread_metadata():
    file_names = None
    dir_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/image"

    file_names = [
        "FastRawViewer-cr2.jpeg",
        "1718882001_Sample_2.jpg",
        "shutterstock_1749060887-1-4.png",
        "1718889054_sample_1280×853.bmp",
        "1718889393_sample_640×426.gif",
        "1718890746_sample1.webp",
    ]

    reports = []
    if file_names is None:
        file_names = os.listdir(dir_path)

    for file_name in file_names:
        file_path = os.path.join(dir_path, file_name)
        report = get_exifread_metadata(file_path)
        if report:
            reports.append(report)

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> report <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    for s in reports:
        print(s)



def get_psd_metadata(file_path):
    from psd_tools import PSDImage

    metadata = {}
    try:
        psd = PSDImage.open(file_path)

        metadata['bbox'] = getattr(psd, 'bbox', None)
        metadata['bottom'] = getattr(psd, 'bottom', None)
        metadata['channels'] = getattr(psd, 'channels', None)
        metadata['color_mode'] = getattr(psd, 'color_mode', None)
        metadata['compatibility_mode'] = getattr(psd, 'compatibility_mode', None)
        metadata['depth'] = getattr(psd, 'depth', None)
        metadata['height'] = getattr(psd, 'height', None)
        metadata['imgae_resources'] = getattr(psd, 'image_resources', None)
        metadata['kind'] = getattr(psd, 'kind', None)
        metadata['left'] = getattr(psd, 'left', None)
        metadata['name'] = getattr(psd, 'name', None)
        metadata['offset'] = getattr(psd, 'offset', None)
        metadata['pil_mode'] = getattr(psd, 'pil_mode', None)
        metadata['right'] = getattr(psd, 'right', None)
        metadata['size'] = getattr(psd, 'size', None)
        metadata['tagged_blocks'] = getattr(psd, 'tagged_blocks', None)
        metadata['top'] = getattr(psd, 'top', None)
        metadata['version'] = getattr(psd, 'version', None)
        metadata['viewbox'] = getattr(psd, 'viewbox', None)
        metadata['visible'] = getattr(psd, 'visible', None)
        metadata['width'] = getattr(psd, 'width', None)

    except Exception as e:
        return f"{file_path} err : {e}"

    format = Path(file_path).name.split(".")[1]
    return f"{format} - meta len : {len(metadata)}"


def test_extract_psd_metadata():
    file_name = None
    dir_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/image"

    file_name = "1718889306_sample_640×426.exr"

    reports = []
    for filename in os.listdir(dir_path):

        if file_name is None:
            file_path = os.path.join(dir_path, filename)
            report = get_psd_metadata(file_path)
            if report:
                reports.append(report)
        else:
            if file_name == filename:
                file_path = os.path.join(dir_path, filename)
                report = get_psd_metadata(file_path)
                if report:
                    reports.append(report)

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> report <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    for s in reports:
        print(s)

# 정규 표현식으로 텍스트 정리
def get_clean_text(text):
    import re
    # 특수 문자 제거 (영어와 한글만 남기기)
    cleaned_text = re.sub(r'[^a-zA-Z0-9가-힣\s]', '', text)

    # 연속된 공백을 하나로 줄이기
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

    return cleaned_text

def get_extract_get_text(file_path):
    from metadata.ml.summarization import Summarization
    from PIL import Image
    import cv2
    #텍스트 추출
    import pytesseract

    try:
        # 이미지 열기
        image = Image.open(file_path)

        # 이미지 전처리
        image = image.convert('L')  # 흑백 변환 (그레이스케일)
        image = image.point(lambda p: p * 1.2)  # 대비 조정

        # 텍스트 추출
        text = pytesseract.image_to_string(image, lang='kor+eng')  # 필요 시 'kor'로 변경

        # print("\n추출된 텍스트:")
        # print(text)

        # # OpenCV를 이용한 전처리
        # image_cv = cv2.imread(file_path)
        #
        # # 이미지를 그레이스케일로 변환
        # gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)
        #
        # # 이미지를 이진화 (흑백으로 변환)
        # _, binary_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        #
        # # 이미지 대비 강화 (옵션)
        # contrast_image = cv2.convertScaleAbs(binary_image, alpha=1.5, beta=0)
        #
        # # 전처리된 이미지에서 텍스트 추출
        # text = pytesseract.image_to_string(contrast_image, lang='kor+eng')
        # print("추출된 텍스트:", text)


        # summarizer = Summarization()
        # str_summary = summarizer.summarize(text)
        #
        # return f"success : {file_path} \n {text} <<<\nsummary : {str_summary}<<<"
        return f"success : {file_path} \n>>>{text}<<< \n정리>>{get_clean_text(text)}<<"

    except Exception as e:
        print(e)
        return f"fail : {e}, {file_path}"

def test_extract_get_text():
    file_name = None
    dir_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/image_resize"

    # file_name = "6f82c0e7-0ebf-4bca-a751-3386b3274c3b.jpeg"

    reports = []
    for filename in os.listdir(dir_path):

        if file_name is None:
            file_path = os.path.join(dir_path, filename)
            report = get_extract_get_text(file_path)
            if report:
                reports.append(report)
        else:
            if file_name == filename:
                file_path = os.path.join(dir_path, filename)
                report = get_extract_get_text(file_path)
                if report:
                    reports.append(report)

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> report <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    for s in reports:
        print(s)


def test_extract_imageio_metadata():
    import imageio.v2 as imageio

    file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/image/1718889478_sample_1280×853.hdr"
    hdr = imageio.imread(file_path)
    print("Shape:", hdr.shape)  # (height, width, channels)
    print("Data type:", hdr.dtype)


def test_extract_exr_metadata():
    import OpenEXR

    file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/image/1718889306_sample_640×426.exr"

    exr_file = OpenEXR.InputFile(file_path)
    header = exr_file.header()

    print("EXR Header Metadata:")
    for key, value in header.items():
        print(f"{key}: {value}")



from colorthief import ColorThief

#PIL에서도 색상 추출 가능 : 정확도 가 다른가봄... ??
def test_extract_colorthief_metadata():
    # file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/KDN_성능테스트_V001.pdf"
    # file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/page1.jpg"
    # file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/page1.png"
    file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/TW0101.jpeg"
    # file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/풍경1.jpeg"

    color_thief = ColorThief(file_path)
    dominant_color = color_thief.get_color(quality=1)

    print("대표 색상 (RGB):", dominant_color)





def test_extract_image_metadata():
    from PIL import Image
    import exifread
    import cv2

    file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/KakaoTalk_Photo_2025-08-29-15-46-05.jpeg"

    metadata = {}

    # 기본 이미지 정보 (Pillow)
    with Image.open(file_path) as img:
        metadata["format"] = img.format
        metadata["mode"] = img.mode
        metadata["size"] = img.size
        metadata["bands"] = img.getbands()
        metadata["dpi"] = img.info.get('dpi', None) #해상도
        metadata["histogram"] = img.histogram()

    # EXIF (촬영 정보 등)
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f)
        metadata["camera"] = tags.get('Image Model')
        metadata["datetime"] = tags.get('EXIF DateTimeOriginal')
        metadata["exposure"] = tags.get('EXIF ExposureTime')
        metadata["iso"] = tags.get('EXIF ISOSpeedRatings')
        metadata["white_balance"] = tags.get('EXIF WhiteBalance')
        metadata["gps"] = {
            "lat": tags.get('GPS GPSLatitude'),
            "lon": tags.get('GPS GPSLongitude')
        }

    # 주 색상
    ct = ColorThief(file_path)
    metadata["dominant_color"] = ct.get_color(quality=1)
    metadata["palette"] = ct.get_palette(color_count=5)

    # 밝기/대비
    img_cv = cv2.imread(file_path)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    metadata["brightness"] = gray.mean()
    metadata["contrast"] = gray.std()


    for k in metadata:
        print(f"{k}: {metadata[k]}")


from pypdf import PdfReader

def test_pdf_extract():
    file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/KDN_성능테스트_V001.pdf"
    reader = PdfReader(file_path)
    metadata = reader.metadata
    print(metadata.get("/Author"))
    if "/Author" in metadata.keys():
        print(True)
    print(metadata)



def test_image_resize():
    from PIL import Image
    from PIL.ExifTags import TAGS

    file_names = None
    dir_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/image"
    resize_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/image_resize"

    file_names = [
        "sample-CR2-Image-File.cr2",
        "sample-nef-files-sample1.nef",
        "1718865090_RAW_CANON_DCS1.tiff",
        "1718865075_RAW_KODAK_DCS560C.tif"
    ]

    reports = []
    if file_names is None:
        file_names = os.listdir(dir_path)

    for file_name in file_names:
        file_path = os.path.join(dir_path, file_name)

        image = Image.open(file_path)

        # EXIF 회전 정보 적용
        try:
            # EXIF 정보에서 회전 값 추출
            for orientation in TAGS.keys():
                if TAGS[orientation]=='Orientation':
                    break
            exif=dict(image._getexif().items())
            if exif.get(orientation) == 3:
                image = image.rotate(180, expand=True)
            elif exif.get(orientation) == 6:
                image = image.rotate(270, expand=True)
            elif exif.get(orientation) == 8:
                image = image.rotate(90, expand=True)
        except (AttributeError, KeyError, IndexError):
            # EXIF 정보가 없거나 문제가 발생한 경우에는 예외 처리
            pass

        sample_width = 2000
        sample_height = 2000

        width, height = image.size

        is_resize = False
        if height > width and height > sample_height: # 세로 이미지
            aspect_ratio = width / height
            sample_width = int(sample_height * aspect_ratio)
            is_resize = True
        elif width > sample_width: # 가로 이미지, 정사각형 (가로기준하면될듯)
            aspect_ratio = height / width
            sample_height = int(sample_width * aspect_ratio)
            is_resize = True
        else: # 사이즈가 작아서 리사이즈 없음
            pass

        if is_resize:

            print(f"\n원본 크기 : {width, height} \n resize : {sample_width, sample_height}")

            resized_image = image.resize((sample_width, sample_height))

            print(f"{resize_path}/{file_name}")
            resized_image.save(f"{resize_path}/{file_name}.jpeg", format="JPEG")
        else:
            print(f"\n원본 크기 : {width, height}")
            image.save(f"{resize_path}/{file_name}.jpeg", format="JPEG")


#exifread
def test_sample_data_from_exifread(sample_width: int = 2000, sample_height: int = 2000):
    import base64
    from io import BytesIO
    from PIL import Image
    import exifread


    dir_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/image"
    resize_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/image_resize"

    file_names = [
        "sample-CR2-Image-File.cr2",
        "sample-nef-files-sample1.nef",
        "1718863107_DSC00343.ARW",
        "1718867207_P4155261.ORF",
        "1718865090_RAW_CANON_DCS1.tiff",
        "1718865075_RAW_KODAK_DCS560C.tif"
                  ]

    for file_name in file_names:
        file_path = os.path.join(dir_path, file_name)
        print(file_path)
        with Image.open(file_path) as img:

            # EXIF 회전 정보 적용
            try:
                # EXIF 정보에서 회전 값 추출
                with open(file_path, 'rb') as f:
                    tags = exifread.process_file(f)

                orientation_tag = 'Image Orientation'

                # Check if 'Orientation' tag is in the EXIF data
                if orientation_tag in tags:
                    orientation_value = tags[orientation_tag]
                    if orientation_value.values == '3':  # 180 degrees
                        img = img.rotate(180, expand=True)
                    elif orientation_value.values == '6':  # 270 degrees (90 clockwise)
                        img = img.rotate(270, expand=True)
                    elif orientation_value.values == '8':  # 90 degrees (counter-clockwise)
                        img = img.rotate(90, expand=True)

            except (AttributeError, KeyError, IndexError, FileNotFoundError):
                # EXIF 정보가 없거나 문제가 발생한 경우에는 예외 처리
                pass

            width, height = img.size

            is_resize = False
            if height > width and height > sample_height:  # 세로 이미지
                aspect_ratio = width / height
                sample_width = int(sample_height * aspect_ratio)
                is_resize = True
            elif width > sample_width:  # 가로 이미지, 정사각형 (가로기준하면될듯)
                aspect_ratio = height / width
                sample_height = int(sample_width * aspect_ratio)
                is_resize = True
            else:  # 사이즈가 작아서 리사이즈 없음
                pass


            if is_resize:

                print(f"\n원본 크기 : {width, height} \n resize : {sample_width, sample_height}")

                resized_image = img.resize((sample_width, sample_height))

                print(f"{resize_path}/{file_name}")
                resized_image.save(f"{resize_path}/{file_name}.jpeg", format="JPEG")
            else:
                print(f"\n원본 크기 : {width, height}")
                img.save(f"{resize_path}/{file_name}.jpeg", format="JPEG")







