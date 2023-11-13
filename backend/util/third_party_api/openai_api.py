from openai import OpenAI
from app.settings.local import *


class OpenAiApi:
    def __init__(self):
        self.__logger = ""

    def evaluate(self, query="", tweet=""):
        client = OpenAI(
            api_key=OPENAI_API_KEY,
        )
        prompt = (
            "ユーザーが「"
            + query
            + "」と検索した結果「"
            + tweet
            + "」というツイートがヒットしました。検索したユーザーが本当に知りたい情報である可能性が高ければ「はい」、そうでなければ「いいえ」とだけ答えてください。"
        )

        try:
            response = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="gpt-3.5-turbo",
            )
            if response.choices[0].message.content == "はい":
                result = True
            else:
                result = False
        except:
            raise Exception

        return result
