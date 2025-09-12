import re

# def quote_name(name: str) -> str:
#     """
#     Equivalent of Java's FullyQualifiedName#quoteName
#     """
#     matcher = re.compile(r'^(")([^"]+)(")$|^(.*)$').match(name)
#     if not matcher or len(matcher.group(0)) != len(name):
#         raise ValueError("Invalid name " + name)
#
#     # Name matches quoted string "sss".
#     # If quoted string does not contain "." return unquoted sss, else return quoted "sss"
#     if matcher.group(1):
#         unquoted_name = matcher.group(2)
#         return name if "." in unquoted_name else unquoted_name
#
#     # Name matches unquoted string sss
#     # If unquoted string contains ".", return quoted "sss", else unquoted sss
#     unquoted_name = matcher.group(4)
#     print(f"1- {unquoted_name}")
#     if '"' not in unquoted_name:
#         print(f"2- {unquoted_name}")
#         return '"' + name + '"' if "." in unquoted_name else unquoted_name
#     print('"' + name + '"' if "." in unquoted_name else unquoted_name)
#     raise ValueError("Invalid name " + name)
#
# quote_name('167cf276-493e-4de4-9b3e-2a4c22c70f11.fabric.공공기관_데이터베이스표준화."공공데이터베이스-표준화-관리-매뉴얼-2023.4".공공데이터베이스 표준화 관리 매뉴얼.hwpx')

def test_re_match():
    regex = "6b68d2f1-3705-4f1b-8e9e-6653b9203828.fabricdata.Data Fabric 기획서_part2 (메인, 탐색, 데이터모델 생성).pptx"
    name = "6b68d2f1-3705-4f1b-8e9e-6653b9203828.fabricdata.Data Fabric 기획서_part2 (메인, 탐색, 데이터모델 생성).pptx"

    print(re.match(regex, name, re.IGNORECASE))

