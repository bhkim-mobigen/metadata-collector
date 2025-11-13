import ffmpeg
import os

# MP4 파일의 메타데이터 추출
def test_get_ffmpeg_metadata():
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


from pymediainfo import MediaInfo
def test_get_mediainfo_metadata():
    dir_path = "/Users/hy/workspace/metadata_collector/tmp/vidio"
    file_name = "sample_2560x1440.m4v"

    file_path = os.path.join(dir_path, file_name)

    media_info = MediaInfo.parse(file_path)

    metadata = {}
    for track in media_info.tracks:
        if track.track_type == "General":
            metadata['general.file_size'] = int(getattr(track, 'file_size', 0))
            metadata['general.format'] = getattr(track, 'format', None)
            metadata['general.duration_ms'] = int(getattr(track, 'duration', 0))
            metadata['general.overall_bit_rate'] = int(getattr(track, 'overall_bit_rate', 0))
            metadata['general.frame_count'] = int(getattr(track, 'frame_count', 0))
            metadata['general.frame_rate'] = float(getattr(track, 'frame_rate', 0))

        elif track.track_type == "Video":
            metadata['video.video_codec'] = getattr(track, 'codec_id', None)
            metadata['video.video_format'] = getattr(track, 'format', None)
            metadata['video.width'] = int(getattr(track, 'width', 0))
            metadata['video.height'] = int(getattr(track, 'height', 0))
            metadata['video.bit_depth'] = int(getattr(track, 'bit_depth', 0))
            metadata['video.frame_rate_video'] = float(getattr(track, 'frame_rate', 0))
            metadata['video.color_space'] = getattr(track, 'color_space', None)
            metadata['video.scan_type'] = getattr(track, 'scan_type', None)
            metadata['video.display_aspect_ratio'] = getattr(track, 'display_aspect_ratio', None)
            metadata['video.encoded_library_name'] = getattr(track, 'encoded_library_name', None)


    for k, v in metadata.items():
        print(f"{k} : {v}")
