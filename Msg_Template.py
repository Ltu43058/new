from linebot.models import *

def stock_reply_rate():
    content_text = "想知道匯率？"
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
                        label="💜💜查詢幣別匯率",
                        text="匯率兌換",
                        )
                    ),
                QuickReplyButton(
                    action=MessageAction(
                        label="💜💜關注的匯率",
                        text="我的外幣",
                        )
                    )]
            ))
    return text_message

#測試button
# def test_Button():
#         flex_message = FlexSendMessage(
#             alt_text="幣別種類",
#             contents={
#                 "type": "bubble",
#                 "hero": {
#                     "type": "image",
#                     "url": "https://i.imgur.com/zB3Mkrs.jpg",
#                     "size": "full",
#                     "aspectRatio": "20:13",
#                     "aspectMode": "cover",
#                     "action": {
#                     "type": "message",
#                     "label": "action",
#                     "text": "小幫手來此"
#                     }
#                 },
#                 "body": {
#                     "type": "box",
#                     "layout": "horizontal",
#                     "contents": [
#                     {
#                         "type": "button",
#                         "action": {
#                         "type": "message",
#                         "label": "美元",
#                         "text": "USD"
#                         },
#                         "height": "sm",
#                         "style": "primary",
#                         "color": "#8F4586"
#                     },
#                     {
#                         "type": "button",
#                         "action": {
#                         "type": "message",
#                         "label": "英鎊",
#                         "text": "GBP"
#                         },
#                         "height": "sm",
#                         "style": "secondary",
#                         "color": "#467500"
#                     },
#                     {
#                         "type": "button",
#                         "action": {
#                         "type": "message",
#                         "text": "CNY",
#                         "label": "人民幣"
#                         },
#                         "style": "primary",
#                         "height": "sm",
#                         "color": "#003060"
#                     }
#                     ],
#                     "backgroundColor": "#C48888"
#                 }
#                 }
#         )
#         return flex_message

# 幣別種類Button
def show_Button():
    flex_message = FlexSendMessage(
            alt_text="幣別種類",
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.imgur.com/zB3Mkrs.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "message",
                    "label": "action",
                    "text": "小幫手來此"
                    }
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
                            "label": "美元",
                            "text": "USD"
                            },
                            "height": "sm",
                            "style": "primary",
                            "color": "#8F4586"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "text": "CNY",
                            "label": "人民幣"
                            },
                            "style": "primary",
                            "height": "sm",
                            "color": "#003060"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "英鎊",
                            "text": "GBP"
                            },
                            "height": "sm",
                            "style": "secondary",
                            "color": "#467500"
                        }
                        ],
                        "spacing": "xl"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "日元",
                            "text": "JPY"
                            },
                            "height": "sm",
                            "style": "primary",
                            "color": "#642100"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "text": "AUD",
                            "label": "澳幣"
                            },
                            "style": "primary",
                            "height": "sm",
                            "color": "#FF8225"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "港幣",
                            "text": "HKD"
                            },
                            "height": "sm",
                            "style": "secondary",
                            "color": "#B43F3F"
                        }
                        ],
                        "spacing": "xl"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "新加坡幣",
                            "text": "SGD"
                            },
                            "height": "sm",
                            "style": "primary",
                            "color": "#173B45"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "text": "CHF",
                            "label": "瑞士法郎"
                            },
                            "style": "primary",
                            "height": "sm",
                            "color": "#7C00FE"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "加拿大幣",
                            "text": "CAD"
                            },
                            "height": "sm",
                            "style": "primary",
                            "color": "#FFAF00"
                        }
                        ],
                        "spacing": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "南非幣",
                            "text": "ZAR"
                            },
                            "height": "sm",
                            "style": "primary",
                            "color": "#F5004F"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "text": "SEK",
                            "label": "瑞典幣"
                            },
                            "style": "primary",
                            "height": "sm",
                            "color": "#003285"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "紐元",
                            "text": "NZD"
                            },
                            "height": "sm",
                            "style": "secondary",
                            "color": "#2A629A"
                        }
                        ],
                        "spacing": "xl"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "泰幣",
                            "text": "THB"
                            },
                            "height": "sm",
                            "style": "primary",
                            "color": "#FFDA78"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "text": "PHP",
                            "label": "菲國比索"
                            },
                            "style": "primary",
                            "height": "sm",
                            "color": "#006769"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "印尼幣",
                            "text": "IDR"
                            },
                            "height": "sm",
                            "style": "secondary",
                            "color": "#40A578"
                        }
                        ],
                        "spacing": "xl"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "韓元",
                            "text": "KRW"
                            },
                            "height": "sm",
                            "style": "primary",
                            "color": "#9DDE8B"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "text": "MYR",
                            "label": "馬來幣"
                            },
                            "style": "primary",
                            "height": "sm",
                            "color": "#EB5B00"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "越南盾",
                            "text": "VND"
                            },
                            "height": "sm",
                            "style": "secondary",
                            "color": "#91DDCF"
                        }
                        ],
                        "spacing": "xl"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "歐元",
                            "text": "EUR"
                            },
                            "height": "sm",
                            "style": "primary",
                            "color": "#A0937D"
                        }
                        ],
                        "spacing": "xl"
                    }
                    ],
                    "backgroundColor": "#C48888",
                    "position": "relative",
                    "spacing": "sm"
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

def realtime_currency_other(currency):
    content = "想知道更多?"
    text_message = TextSendMessage(
                                text = content ,
                               quick_reply=QuickReply(
                                   items=[
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="即時匯率", 
                                                    text="外幣"+currency,
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="加入清單", 
                                                    text="新增外幣"+currency,
                                                )
                                       ),
                                        QuickReplyButton(
                                                action=MessageAction(
                                                    label="走勢圖", 
                                                    text="CT"+currency,
                                                )
                                       ),
                                        QuickReplyButton(
                                                action=MessageAction(
                                                    label="新聞", 
                                                    text="N外匯"+currency,
                                                )
                                       )
                                ]
                            ))
    return text_message
