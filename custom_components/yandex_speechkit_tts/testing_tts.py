from speechkit import configure_credentials, creds
from speechkit import model_repository

configure_credentials(
    yandex_credentials=creds.YandexCredentials(
        api_key='AQVN2264xeZ2aMwnSE6SpbjcDMllMPIAlCzhr1LK'
    )
)

model = model_repository.synthesis_model()

model.voice = 'alena'


result = model.synthesize('Пробуем работу спичкита', raw_format=False)  # returns audio as pydub.AudioSegment
byted = result.serialize()
print(byted)
result.export('/home/coder/result.wav', format='wav')