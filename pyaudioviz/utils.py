import numpy as np
from pathlib import Path
from pydub import AudioSegment

TEST_AUDIO = Path('assets/audio/open-goldberg-variatio-21.mp3')

def convert_audio_to_data(audio_path, format='mp3'):
    audio = AudioSegment.from_mp3(audio_path)



def testfoo():
    audio = AudioSegment.from_mp3(TEST_AUDIO)
    duration = audio.duration_seconds
    frame_rate = audio.frame_rate
    samples = np.array(audio.get_array_of_samples())
    sample_rate = 1/40
#    sample_max = samples.max()

    sample_size = int(frame_rate * sample_rate)

    first_sample = samples[0:0+sample_size]

if __name__ == '__main__':
    testfoo()
