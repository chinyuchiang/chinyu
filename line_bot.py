from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, FollowEvent, UnfollowEvent,
    TemplateSendMessage,CarouselTemplate,CarouselColumn,URIAction
)
# CHANNEL_ACCESS_TOKEN
line_bot_api = LineBotApi('zQIbXL3LKpmEfDPfpdK3tpSv6xQ3mDsislvgROljfJhOLf147UBGbIW0ZqWCQsKGLnMzd4m/9GhyN7TnaCJ5gtfJe9+/qfE9BS4UfODMqEgH5fG/9m7KQ1+x8+VT0zLKZvFF7dDZZnhVqJOQtAGQVAdB04t89/1O/w1cDnyilFU=')
# CHANNEL_SECRET
handler = WebhookHandler('b643a3b7a60a79cc953bc3fe6a13211b')