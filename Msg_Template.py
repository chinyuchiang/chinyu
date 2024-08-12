from linebot.models import *

def others():
    content_text = "請點選以下開始其他功能"
    text_message = TextSendMessage(
                                text = content_text ,
                               quick_reply=QuickReply(
                                   items=[
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="變成巴菲特", 
                                                    text="巴菲特教室",
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="查詢幣別匯率", 
                                                    text="幣別種類",
                                                )
                                       ),
                                ]
                            ))
    return text_message

def stock_reply_rate():
    content_text = "想知道匯率?"
    text_message = TextSendMessage(
                                text = content_text ,
                               quick_reply=QuickReply(
                                   items=[
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="💜💜查詢單一幣別匯率", 
                                                    text="幣別種類",
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="💜💜查詢單一幣別匯率", 
                                                    text="幣別種類",
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="💜💜查詢單一幣別匯率", 
                                                    text="幣別種類",
                                                )
                                       ),
                                ]
                            ))
    return text_message
#測試的button
def test_Button():
    flex_message = FlexSendMessage(
            alt_text='Test',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.imgur.com/R3q6kZh.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "postback",
                    "label": "action",
                    "data": "hello"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "美金",
                        "text": "USD"
                        },
                        "style": "primary",
                        "color": "#7B7B7B",
                        "height": "md"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "港幣",
                        "text": "HKD"
                        },
                        "style": "primary",
                        "color": "#7B7B7B",
                        "height": "md"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "日圓",
                        "text": "JPY"
                        },
                        "style": "primary",
                        "color": "#7B7B7B",
                        "height": "md"
                    }
                    ],
                    "backgroundColor": "#000000"
                }
            }
    )
    return flex_message
def show_Button():
    flex_message = FlexSendMessage(
            alt_text='幣別種類',
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.imgur.com/R3q6kZh.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "postback",
                    "label": "action",
                    "data": "hello"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                    {
                        "type": "text",
                        "text": "請點選按鈕查詢幣值",
                        "weight": "bold",
                        "style": "normal",
                        "align": "center",
                        "color": "#ADADAD",
                        "size": "xl"
                    }
                    ],
                    "backgroundColor": "#000000"
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "美金",
                            "text": "USD"
                            },
                            "style": "primary",
                            "color": "#7B7B7B",
                            "height": "md"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "港幣",
                            "text": "HKD"
                            },
                            "style": "primary",
                            "color": "#7B7B7B",
                            "height": "md",
                            "margin": "md"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "日圓",
                            "text": "JPY"
                            },
                            "style": "primary",
                            "color": "#7B7B7B",
                            "height": "md",
                            "margin": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "台幣",
                            "text": "TWD"
                            },
                            "color": "#9D9D9D",
                            "style": "primary"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "澳幣",
                            "text": "AUD"
                            },
                            "color": "#9D9D9D",
                            "style": "primary",
                            "margin": "md"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "text": "GBP",
                            "label": "英鎊"
                            },
                            "style": "primary",
                            "color": "#9D9D9D",
                            "margin": "md"
                        }
                        ],
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "泰銖",
                            "text": "THB"
                            },
                            "style": "primary",
                            "color": "#BEBEBE"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "韓元",
                            "text": "KRW"
                            },
                            "style": "primary",
                            "color": "#BEBEBE",
                            "margin": "md"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "人民幣",
                            "text": "CNY"
                            },
                            "style": "primary",
                            "color": "#BEBEBE",
                            "margin": "md"
                        }
                        ],
                        "margin": "md"
                    }
                    ],
                    "backgroundColor": "#000000",
                    "margin": "md"
                }
                }
    )
    return flex_message
# 理財頻道
def youtube_channel():
    flex_message = FlexSendMessage(
            alt_text="youtube_channel",
            contents=
            {
                "type": "carousel",
                "contents": [
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/SJPH542.jpg",
                        "aspectMode": "fit",
                        "aspectRatio": "320:213",
                        "size": "full",
                        "backgroundColor": "#000000"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "理財達人秀",
                            "weight": "bold",
                            "size": "lg",
                            "wrap": True,
                            "align": "center"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "最精彩最好懂",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我觀看",
                            "uri": "https://www.youtube.com/channel/UCQvsuaih5lE0n_Ne54nNezg"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財youtuber",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    },
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/dPW0jcC.jpg",
                        "size": "full",
                        "aspectMode": "fit",
                        "aspectRatio": "320:213",
                        "backgroundColor": "#AA0000"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "CMoney理財寶",
                            "weight": "bold",
                            "size": "lg",
                            "wrap": True,
                            "align": "center"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "基本理財知識",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我觀看",
                            "uri": "https://www.youtube.com/user/CMoneySchool"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財youtuber",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    },
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/zkUZrCj.jpg",
                        "size": "full",
                        "aspectMode": "fit",
                        "aspectRatio": "320:213",
                        "backgroundColor": "#444444"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "我要做富翁",
                            "weight": "bold",
                            "size": "lg",
                            "wrap": True,
                            "align": "center"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "平民化&分享形式",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我觀看",
                            "uri": "https://www.youtube.com/user/SyLingHim"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財youtuber",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    }
                ]
            }
        )
    return flex_message
# # 幣別種類Button
# def show_Button():
#     flex_message = FlexSendMessage(
#             alt_text="幣別種類",
#             contents={
#                 "type": "bubble",
#                 "body": {
#                     "type": "box",
#                     "layout": "vertical",
#                     "contents": [
#                     {
#                         "type": "text",
#                         "text": "幣別種類",
#                         "weight": "bold",
#                         "size": "xl",
#                         "color": "#AA2B1D"
#                     }
#                     ]
#                 },
#                 "footer": {
#                     "type": "box",
#                     "layout": "vertical",
#                     "contents": [
#                     {
#                         "type": "box",
#                         "layout": "horizontal",
#                         "contents": [
#                         {
#                             "type": "button",
#                             "action": {
#                             "type": "message",
#                             "label": "美金",
#                             "text": "USD"
#                             },
#                             "gravity": "center",
#                             "style": "primary",
#                             "color": "#CC561E",
#                             "margin": "sm"
#                         },
#                         {
#                             "type": "button",
#                             "action": {
#                             "type": "message",
#                             "label": "日圓",
#                             "text": "JPY"
#                             },
#                             "gravity": "center",
#                             "style": "primary",
#                             "color": "#CC561E",
#                             "margin": "sm"
#                         },
#                         {
#                             "type": "button",
#                             "action": {
#                             "type": "message",
#                             "label": "港幣",
#                             "text": "HKD"
#                             },
#                             "gravity": "center",
#                             "style": "primary",
#                             "color": "#CC561E",
#                             "margin": "sm"
#                         }
#                         ]
#                     },
#                     {
#                         "type": "separator",
#                         "margin": "md"
#                     },
#                     {
#                         "type": "box",
#                         "layout": "horizontal",
#                         "contents": [
#                         {
#                             "type": "button",
#                             "action": {
#                             "type": "message",
#                             "label": "英鎊",
#                             "text": "GBP"
#                             },
#                             "gravity": "center",
#                             "style": "primary",
#                             "color": "#CC561E",
#                             "margin": "sm"
#                         },
#                         {
#                             "type": "button",
#                             "action": {
#                             "type": "message",
#                             "label": "澳幣",
#                             "text": "AUD"
#                             },
#                             "gravity": "center",
#                             "style": "primary",
#                             "color": "#CC561E",
#                             "margin": "sm"
#                         },
#                         {
#                             "type": "button",
#                             "action": {
#                             "type": "message",
#                             "label": "加拿大幣",
#                             "text": "CAD"
#                             },
#                             "gravity": "center",
#                             "style": "primary",
#                             "color": "#CC561E",
#                             "margin": "sm"
#                         }
#                         ]
#                     },
#                     {
#                         "type": "separator",
#                         "margin": "md"
#                     },
#                     {
#                         "type": "box",
#                         "layout": "horizontal",
#                         "contents": [
#                         {
#                             "type": "button",
#                             "action": {
#                             "type": "message",
#                             "label": "瑞士法郎",
#                             "text": "CHF"
#                             },
#                             "gravity": "center",
#                             "style": "primary",
#                             "color": "#CC561E",
#                             "margin": "sm"
#                         },
#                         {
#                             "type": "button",
#                             "action": {
#                             "type": "message",
#                             "label": "新加坡",
#                             "text": "SGD"
#                             },
#                             "gravity": "center",
#                             "style": "primary",
#                             "color": "#CC561E",
#                             "margin": "sm"
#                         },
#                         {
#                             "type": "button",
#                             "action": {
#                             "type": "message",
#                             "label": "南非幣",
#                             "text": "ZAR"
#                             },
#                             "gravity": "center",
#                             "style": "primary",
#                             "color": "#CC561E",
#                             "margin": "sm"
#                         }
#                         ]
#                     },
#                     {
#                         "type": "separator",
#                         "margin": "md"
#                     },
#                     {
#                         "type": "box",
#                         "layout": "horizontal",
#                         "contents": [
#                         {
#                             "type": "button",
#                             "action": {
#                             "type": "message",
#                             "label": "瑞典幣",
#                             "text": "SEK"
#                             },
#                             "gravity": "center",
#                             "style": "primary",
#                             "color": "#CC561E",
#                             "margin": "sm"
#                         },
#                         {
#                             "type": "button",
#                             "action": {
#                             "type": "message",
#                             "label": "泰幣",
#                             "text": "THB"
#                             },
#                             "gravity": "center",
#                             "style": "primary",
#                             "color": "#CC561E",
#                             "margin": "sm"
#                         },
#                         {
#                             "type": "button",
#                             "action": {
#                             "type": "message",
#                             "label": "菲比索",
#                             "text": "PHP"
#                             },
#                             "gravity": "center",
#                             "style": "primary",
#                             "color": "#CC561E",
#                             "margin": "sm"
#                         }
#                         ]
#                     },
#                     {
#                         "type": "separator",
#                         "margin": "md"
#                     },
#                     {
#                         "type": "box",
#                         "layout": "horizontal",
#                         "contents": [
#                         {
#                             "type": "button",
#                             "action": {
#                             "type": "message",
#                             "label": "印尼幣",
#                             "text": "IDR"
#                             },
#                             "gravity": "center",
#                             "style": "primary",
#                             "color": "#CC561E",
#                             "margin": "sm"
#                         },
#                         {
#                             "type": "button",
#                             "action": {
#                             "type": "message",
#                             "label": "韓元",
#                             "text": "KRW"
#                             },
#                             "gravity": "center",
#                             "style": "primary",
#                             "color": "#CC561E",
#                             "margin": "sm"
#                         },
#                         {
#                             "type": "button",
#                             "action": {
#                             "type": "message",
#                             "label": "馬來幣",
#                             "text": "MYR"
#                             },
#                             "gravity": "center",
#                             "style": "primary",
#                             "color": "#CC561E",
#                             "margin": "sm"
#                         }
#                         ]
#                     },
#                     {
#                         "type": "separator",
#                         "margin": "md"
#                     },
#                     {
#                         "type": "box",
#                         "layout": "horizontal",
#                         "contents": [
#                         {
#                             "type": "button",
#                             "action": {
#                             "type": "message",
#                             "label": "越南盾",
#                             "text": "VND"
#                             },
#                             "gravity": "center",
#                             "style": "primary",
#                             "color": "#CC561E",
#                             "margin": "sm"
#                         },
#                         {
#                             "type": "button",
#                             "action": {
#                             "type": "message",
#                             "label": "人民幣",
#                             "text": "CNY"
#                             },
#                             "gravity": "center",
#                             "style": "primary",
#                             "color": "#CC561E",
#                             "margin": "sm"
#                         },
#                         {
#                             "type": "button",
#                             "action": {
#                             "type": "message",
#                             "label": "紐元",
#                             "text": "NZD"
#                             },
#                             "gravity": "center",
#                             "style": "primary",
#                             "color": "#CC561E",
#                             "margin": "sm"
#                         }
#                         ]
#                     }
#                     ]
#                 }
#         }
                    
#     )
#     return flex_message