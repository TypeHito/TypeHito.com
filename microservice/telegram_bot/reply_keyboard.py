def reply_keyboard_markup(resize_keyboard, one_time_keyboard):
    return {'keyboard': [], 'resize_keyboard': resize_keyboard, 'one_time_keyboard': one_time_keyboard}


def reply_keyboard_button(text, request_user=None, request_chat=None, request_contact=None,
                          request_location=None, request_poll=None, web_app=None):
    button = {"text": text}
    if request_user:
        button["request_user"] = request_user
    if request_chat:
        button["request_chat"] = request_chat
    if request_contact:
        button["request_contact"] = request_contact
    if request_location:
        button["request_location"] = request_location
    if request_poll:
        button["request_poll"] = request_poll
    if web_app:
        button["web_app"] = web_app
    return button


def request_contact_button(text):
    kb = reply_keyboard_markup(True, False)
    kb['keyboard'].append([reply_keyboard_button(text, request_contact=True)])
    return kb


def ok_cancel(ok, cancel):
    kb = reply_keyboard_markup(True, False)
    kb['keyboard'].append([reply_keyboard_button(ok), reply_keyboard_button(cancel)])
    return kb
