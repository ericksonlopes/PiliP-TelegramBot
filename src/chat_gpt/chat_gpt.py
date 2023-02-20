import openai
from loguru import logger


class AskChatGPT:
    def __init__(self, command: str):
        self.__command = command.removeprefix('/ask ')

    @property
    def command(self) -> str:
        return self.__command

    def get_response_int_chat_gpt(self) -> str:
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=self.command,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5
            )
        except Exception as e:
            logger.error(e)
            return 'Desculpe... Houve um erro ao tentar processar sua pergunta.'
        else:
            answer: str = response['choices'][0]['text'].replace('\n', ' ')
            logger.info("Question: {ask} - Answer: {text}".format(ask=self.command, text=answer))
            return answer
