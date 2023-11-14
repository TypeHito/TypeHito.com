def inline_keyboard_markup():
    return {'inline_keyboard': []}


def inline_keyboard_button(text, callback_data=None, url=None):
    if url:
        return {"text": text, "url": url}
    return {"text": text, "callback_data": callback_data}


def ok_cancel(strings, ok_key, cancel_key):
    kb = inline_keyboard_markup()
    kb['inline_keyboard'].append(
        [
            inline_keyboard_button(strings["send_post"], ok_key),
            inline_keyboard_button(strings["cancel_post"], cancel_key)
        ]
    )
    return kb
