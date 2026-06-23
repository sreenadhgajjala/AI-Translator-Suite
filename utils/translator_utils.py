from deep_translator import GoogleTranslator

def get_languages():
    return GoogleTranslator().get_supported_languages(as_dict=True)

def translate_text(text, source, target):
    translator = GoogleTranslator(
        source=source,
        target=target
    )
    return translator.translate(text)