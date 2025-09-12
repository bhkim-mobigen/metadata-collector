from tika import parser

def test_tika_parser():
    # file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/[별표 1] 데이터 표준사전 관리항목(공공기관의 데이터베이스 표준화 지침).hwpx"
    # file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/대전 교통문화연수원 교육일정.hwpx"
    # file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/참여인력 이력사항_모비젠.hwp"
    # file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/250807_남북기금_홈페이지_통계(2507)_업데이트용.hwp"
    # file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/KDN_성능테스트_V001.doc"
    file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/데이터패브릭_설계서_v0.4.docx"
    # file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/1990년~2013년 전국,대전 최종에너지 소비(부문별에너지 소비).xls"
    # file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/2021년자치구별인구이동 (1).xlsx"
    # file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/Data Fabric 기획서_part2 (메인, 탐색, 데이터모델 생성).pptx"
    # file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/r_keras_dense_mnist_model.h5"
    # file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/데이터페브릭_DB설계서_v1.1.3.xlsx"
    # file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/101_DT_1YL0000_20231130090340.txt"
    # file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/01c6edea-195f-42e4-ba6a-a8e71101f9cd.json"
    # file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/KDN_성능테스트_V001.pdf"
    parsed = parser.from_file(file_path)
    # 메타데이터 추출
    metadata = parsed['metadata']

    metadata_key = []
    for key in metadata:
        print(f"{key} : {metadata[key]}")
#         metadata_key.append(key)
#
#     list_key = ['Content-Type','X-TIKA:digest:MD5','resourceName','Content-Length','X-TIKA:content','X-TIKA:content_handler','X-TIKA:embedded_resource_path','X-TIKA:embedded_depth','X-TIKA:encrypted','tika:file_ext'
# ,'dc:creator','dcterms:created','dcterms:modified','dc:rights','dc:contributor','dc:title','dc:relation','dc:type','dc:identifier','dc:publisher','dc:description','dc:subject','dc:language','dc:format'
# ,'xmp:About','xmp:CreateDate','xmp:CreatorTool','xmp:Identifier','xmp:Label','xmp:MetadataDate','xmp:ModifyDate','xmp:Rating','xmpDM:album','xmpDM:albumArtist','xmpDM:artist','xmpDM:audioChannelType','xmpDM:audioCompressor','xmpDM:audioSampleRate','xmpDM:audioSampleType','xmpDM:compilation','xmpDM:composer','xmpDM:copyright','xmpDM:discNumber','xmpDM:duration','xmpDM:genre','xmpDM:logComment','xmpDM:releaseDate','xmpDM:trackNumber','xmpDM:videoCompressor','xmpMM:DerivedFrom:DocumentID','xmpMM:DerivedFrom:InstanceID','xmpMM:DocumentID','xmpMM:History:Action','xmpMM:History:InstanceID','xmpMM:History:SoftwareAgent','xmpMM:History:When','xmpTPg:NPages'
# ,'embeddedRelationshipId'
# ,'Content-Encoding'
# ,'tiff:ImageWidth','tiff:ImageLength','tiff:BitsPerSample'
# ]
#
#     print("\n")
#     print("====")
#     for key in list_key:
#         if key in metadata:
#             value = metadata[key]
#             metadata_key.remove(key)
#         else:
#             value = ''
#         print(f"{value}")
#         if key in ['tika:file_ext', 'dc:format', 'xmpTPg:NPages','embeddedRelationshipId','Content-Encoding','tiff:BitsPerSample']:
#             print('--')
#
#     print("====")
#     for key in metadata_key:
#         print(f"{key} | {metadata[key]}")




def test_docx():
    from docx import Document

    file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/KDN_성능테스트_V001.doc"
    # 문서 열기
    doc = Document(file_path)

    # 메타데이터 추출
    metadata = doc.core_properties


    print(metadata)


import zipfile
import xml.etree.ElementTree as ET
from collections import defaultdict

def test_extract_hwpx_structure():
    file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/[별표 1] 데이터 표준사전 관리항목(공공기관의 데이터베이스 표준화 지침).hwpx"

    all_namespaces = dict()
    tag_paths = set()

    def traverse(element, path=""):
        tag = element.tag.split("}")[-1] if "}" in element.tag else element.tag
        current_path = f"{path}/{tag}" if path else tag
        tag_paths.add(current_path)
        for child in element:
            traverse(child, current_path)

    with zipfile.ZipFile(file_path, 'r') as z:
        # section XML 파일들과 content.hpf 파일만 대상으로
        xml_files = [f.filename for f in z.filelist if f.filename.endswith(".xml") or f.filename.endswith(".hpf")]

        for xml_file in xml_files:
            try:
                with z.open(xml_file) as f:
                    # 네임스페이스 추출
                    events = ("start", "start-ns")
                    ns_map = {}
                    for event, elem in ET.iterparse(f, events):
                        if event == "start-ns":
                            prefix, uri = elem
                            if prefix not in all_namespaces:
                                all_namespaces[prefix] = uri
                    break  # 첫 파일만으로 네임스페이스 충분
            except Exception as e:
                print(f"Failed to parse namespaces in {xml_file}: {e}")

        # 다시 순회해서 태그 경로 추출
        for xml_file in xml_files:
            try:
                with z.open(xml_file) as f:
                    tree = ET.parse(f)
                    root = tree.getroot()
                    traverse(root)
            except Exception as e:
                print(f"Failed to parse tags in {xml_file}: {e}")

    print("네임스페이스 목록:")
    for prefix, uri in all_namespaces.items():
        print(f"  {prefix}: {uri}")

    paths = sorted(tag_paths)
    print("\n태그 경로 목록:")
    for path in paths:
        print("  /" + path)

def test_check_hwpx_contents():
    file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/[별표 1] 데이터 표준사전 관리항목(공공기관의 데이터베이스 표준화 지침).hwpx"
    with zipfile.ZipFile(file_path, 'r') as z:
        for name in z.namelist():
            print(name)

import zipfile
import xml.etree.ElementTree as ET

def test_check_hwpx_inspect_section_namespace():
    file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/대전 교통문화연수원 교육일정.hwpx"

    with zipfile.ZipFile(file_path, 'r') as z:
        with z.open('Contents/section0.xml') as f:
            events = ('start', 'start-ns')
            for event, elem in ET.iterparse(f, events):
                if event == 'start-ns':
                    prefix, uri = elem
                    print(f"xmlns:{prefix or '(default)'} = {uri}")
                elif event == 'start':
                    print(f"\n[Root Element] {elem.tag}")
                    break

def test_inspect_run_structure():
    file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/[별표 1] 데이터 표준사전 관리항목(공공기관의 데이터베이스 표준화 지침).hwpx"
    ns = {
        'hp': 'http://www.hancom.co.kr/hwpml/2011/paragraph',
        'hp10': 'http://www.hancom.co.kr/hwpml/2016/paragraph',
    }

    with zipfile.ZipFile(file_path, 'r') as z:
        for f in z.filelist:
            if f.filename.startswith("Contents/section") and f.filename.endswith(".xml"):
                with z.open(f.filename) as xml_file:
                    tree = ET.parse(xml_file)
                    root = tree.getroot()

                    for prefix in ['hp', 'hp10']:
                        # runs = root.findall(f'.//{prefix}:run', ns)
                        # if runs:
                        #     print(f"🔍 Found {len(runs)} runs with prefix '{prefix}' in {f.filename}")
                        #     for i, run in enumerate(runs[:3]):  # 샘플 3개만
                        #         print(f"\n[Run {i+1} with {prefix}]")
                        #         for child in run:
                        #             tag = child.tag
                        #             text = child.text.strip() if child.text else ''
                        #             print(f"  {tag} → '{text}'")
                        #     return  # 첫 발견에서 종료

                        # paras = root.findall(f'.//{prefix}:para', ns)
                        # if paras:
                        #     print(f"🔍 Found {len(paras)} para with prefix '{prefix}' in {f.filename}")
                        #     for i, para in enumerate(paras[:3]):  # 샘플 3개만
                        #         print(f"\n[Run {i+1} with {prefix}]")
                        #         for child in para:
                        #             tag = child.tag
                        #             text = child.text.strip() if child.text else ''
                        #             print(f"  {tag} → '{text}'")
                        #     return  # 첫 발견에서 종료

                        pictures = root.findall(f'.//{prefix}:pic', ns)
                        if pictures:
                            print(f"🔍 Found {len(pictures)} para with prefix '{prefix}' in {f.filename}")
                            for i, pic in enumerate(pictures[:3]):  # 샘플 3개만
                                print(f"\n[Run {i+1} with {prefix}]")
                                for child in pic:
                                    tag = child.tag
                                    text = child.text.strip() if child.text else ''
                                    print(f"  {tag} → '{text}'")
                            return  # 첫 발견에서 종료

    print("❌ No elements found.")

def test_extract_hwpx_content_stats():
    file_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/[별표 1] 데이터 표준사전 관리항목(공공기관의 데이터베이스 표준화 지침).hwpx"

    ns = {
        'hp': 'http://www.hancom.co.kr/hwpml/2011/paragraph',
        'hp10': 'http://www.hancom.co.kr/hwpml/2016/paragraph'
    }

    para_count = 0
    char_count = 0
    word_count = 0
    image_count = 0
    object_count = 0
    line_count = 0

    with zipfile.ZipFile(file_path, 'r') as z:
        section_files = [f.filename for f in z.filelist if f.filename.startswith("Contents/section") and f.filename.endswith(".xml")]

        for section in section_files:
            with z.open(section) as f:
                tree = ET.parse(f)
                root = tree.getroot()

                # 문단 추출 (두 네임스페이스 모두 시도)
                for prefix in ns:
                    paras =  root.findall(f'.//{prefix}:para', ns)
                    if paras:
                        for para in paras:
                            para_count += 1
                            for run in para.findall(f'.//{prefix}:run', ns):
                                text_elem = run.find(f'{prefix}:t', ns)
                                if text_elem is not None and text_elem.text:
                                    text = text_elem.text
                                    char_count += len(text)
                                    word_count += len(text.split())
                    else:
                        for run in root.findall(f'.//{prefix}:run', ns):
                            text_elem = run.find(f'{prefix}:t', ns)
                            if text_elem is not None and text_elem.text:
                                text = text_elem.text
                                char_count += len(text)
                                word_count += len(text.split())

                    # 이미지 수 세기
                    pic_len = len(root.findall(f'.//{prefix}:pic', ns))
                    print(f"pic>>>{pic_len}")
                    for pic in root.findall(f'.//{prefix}:pic', ns):
                        image_count += 1

                    # 도형/오브젝트 수 세기 (shape 포함)
                    shape_len = len(root.findall(f'.//{prefix}:shape', ns))
                    print(f"shape>>>{shape_len}")
                    for shape in root.findall(f'.//{prefix}:shape', ns):
                        object_count += 1


                    #라인 수 추출
                    linesegs = root.findall(f'.//{prefix}:lineseg', ns)

                    line_count += len(linesegs)

    print(f"문단 수: {para_count},\n "
          f"글자 수: {char_count},\n "
          f"단어 수: {word_count},\n "
          f"이미지 수: {image_count},\n "
          f"오브젝트 수: {object_count},\n "
          f"라인 수: {line_count}"
    )
