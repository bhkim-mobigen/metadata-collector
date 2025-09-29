import ffmpeg
import os

# MP4 파일의 메타데이터 추출
def test_get_audio_metadata():
    dir_path = "/Users/hy/workspace/metadata_collector/tmp/vidio"
    file_name = "대전교통공사_지족역 지진대피장소_20221231.mp4"


    file_path = os.path.join(dir_path, file_name)

    probe = ffmpeg.probe(file_path)
    metadata = {}
    if 'format' in probe:
        metadata.update(get_metadata(probe['format'], 'format'))

    if 'streams' in probe:
        for i, stream in enumerate(probe['streams']):
            metadata.update(get_metadata(stream, f"stream.{i}"))


    for k, v in metadata.items():
        print(f"{k} : {v}")

def get_metadata(data :dict, key):
    metadata = {}
    for k, v in data.items():
        if k in ('tags', 'disposition'):
            metadata.update(get_metadata(data[k], f"{key}.{k}"))
        else:
            metadata[f"{key}.{k}"] = v

    return metadata