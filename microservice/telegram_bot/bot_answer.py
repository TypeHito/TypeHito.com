import requests
from microservice.telegram_bot.bot_configs import URL


def send_message(chat_id, text, parse_mode="markdown", reply_markup=None):
    url = URL + "sendMessage"
    data = {"chat_id": chat_id, "text": text, "parse_mode": parse_mode}
    if reply_markup:
        data["reply_markup"] = reply_markup
    response = requests.post(url, json=data)
    return response.json()


def send_photo(chat_id, photo, caption=None, parse_mode="markdown", reply_markup=None):
    url = URL + "sendPhoto"
    data = {"chat_id": chat_id, "photo": photo, "parse_mode": parse_mode}
    if caption:
        data["caption"] = caption
    if reply_markup:
        data["reply_markup"] = reply_markup
    response = requests.post(url, json=data)
    return response.json()


def send_video(chat_id, video, caption=None, parse_mode="markdown", reply_markup=None):
    url = URL + "sendVideo"
    data = {"chat_id": chat_id, "video": video, "parse_mode": parse_mode}
    if caption:
        data["caption"] = caption
    if reply_markup:
        data["reply_markup"] = reply_markup
    response = requests.post(url, json=data)
    return response.json()


def send_document(chat_id, document):
    url = URL + 'sendDocument'
    r = requests.post(url=url, data={'chat_id': chat_id, 'document': 'attach://file'},
                      files={'file': open(document, 'rb')})
    return r.json()


def edit_message_text(chat_id, text, message_id, parse_mode='markdown', reply_markup=None):
    url = URL + 'editMessageText'
    data = {'chat_id': chat_id, 'message_id': int(message_id),
            'text': text, 'parse_mode': parse_mode}
    if reply_markup:
        data["reply_markup"] = reply_markup
    response = requests.post(url, json=data)
    return response.json()


def delete_message(chat_id, message_id):
    url = URL + "deleteMessage"
    data = {"chat_id": chat_id, "message_id": message_id}
    response = requests.post(url, json=data)
    return response.json()


