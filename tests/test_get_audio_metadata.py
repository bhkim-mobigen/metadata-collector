import parselmouth
from pydub.utils import mediainfo
from parselmouth.praat import call
import os
"""
pip install praat-parselmouth==0.4.6
pip install pydub==0.25.1
sudo apt install ffmpeg
"""

def test_get_audio_metadata():

    dir_path = "/Users/hy/workspace/ot_data_catalog_server/metadata_collector/tmp/audio"
    file_name = "03-01-01-01-01-01-06.wav"


    file_path = os.path.join(dir_path, file_name)

    print("\n")
    # [1] 기술 메타데이터
    info = mediainfo(file_path)
    if len(info) > 0:
        for k, v in info.items():
            print(f"{k} : {v}")

        print("===meta===")
        print("파일 길이:", info['duration'], "초")
        print("샘플링 주파수:", info['sample_rate'], "Hz")
        print("채널 수:", info['channels'])

    # [2] 음성 분석
    sound = parselmouth.Sound(file_path)
    pitch = sound.to_pitch()
    formants = sound.to_formant_burg()
    intensity = sound.to_intensity()
    point_process = call(sound, "To PointProcess (periodic, cc)", 75, 500)

    # 피치 평균
    mean_pitch = call(pitch, "Get mean", 0, 0, "Hertz")
    # 첫번째 포먼트 (F1) 0.5초 시점
    f1 = call(formants, "Get value at time", 1, 0.5, 'Hertz', 'Linear')
    # 평균 강도
    mean_intensity = call(intensity, "Get mean", 0, 0, 'dB')
    # 떨림 계수
    jitter = call(point_process, "Get jitter (local)", 0, 0, 0.0001, 0.02, 1.3)


    """
    mean_pitch : 발화 중 평균 기본 주파수
        화자의 성별: 보통 남성은 85180 Hz, 여성은 165255 Hz
        감정 상태: 화날 때나 놀랐을 때 피치가 높아짐
        억양/말투: 낭독 vs 자연 대화 구분 등
    formant : 포먼트는 성도(성대 이후 발화 기관)의 공명 주파수
        모음 종류 판단 가능 (예: /a/는 F1 높고, /i/는 F1 낮음)
        발음 습관, 발성 이상 탐지
        화자의 언어/억양 스타일 분석 가능
    mean_intensity : 전체 발화에서의 평균 음량 또는 세기
        말하는 사람의 에너지 수준 (낮으면 기운 없음, 높으면 활기참)
        감정 상태 (예: 분노나 흥분 → 강도 높음)
        녹음 품질 평가 기준이 될 수 있음
    jitter : 연속된 피치 주기 간의 미세한 시간 변화(떨림)
        발성의 안정성 평가
        음성 장애 여부(예: 성대 문제, 떨림 등) 진단 보조
        감정 상태: 불안하거나 긴장되었을 때 jitter가 증가하는 경향
    """


    print("피치 평균:", mean_pitch)
    print("포먼트 F1 @0.5초:", f1) #0.5초 시점의
    print("강도 평균:", mean_intensity)
    print("Jitter (local):", jitter)




