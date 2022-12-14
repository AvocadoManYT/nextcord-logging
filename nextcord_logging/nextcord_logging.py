import aiohttp
import asyncio
import logging
from logging import Handler

class Discord_Handler(Handler):

    def __init__(self, url):
        logging.Handler.__init__(self)
        self.url = url

    def mapLogRecord(self, record):
        return record.__dict__

    def emit(self, record):
        asyncio.create_task(self.emitting(record))

    async def emitting(self, record):
        try:
            msg = self.format(record)
            url = self.url
            headers = {}
            headers["Content-type"] = "application/x-www-form-urlencoded"
            if len(msg) > 1900:
                msg_list = [msg[i: i+1900] for i in range(0, len(msg), 1900)]
                for i in msg_list:
              	    async with aiohttp.request("POST", url, data={'content':f"```{i}```"}, headers=headers):
                        pass
            else:
                async with aiohttp.request("POST", url, data={'content':f"```{msg}```"}, headers=headers):
                    pass
        except Exception:
            self.handleError(record)