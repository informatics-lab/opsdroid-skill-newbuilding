import random

from opsdroid.matchers import match_crontab, match_regex
from opsdroid.message import Message


@match_crontab("30 09 * * 5")
@match_regex(r".*new building.*")
async def newbuilding(opsdroid, config, message):
    sentences = [
        "Check out the progress on the new building!",
        "Here's an update on the new building.",
        "It's coming along!"
    ]
    connector = opsdroid.default_connector
    if message is None:
        message = Message("", None, connector.default_room, connector)
    await message.respond("https://timelapse.regenology.co.uk/api/latest_image/aOj/")
    await message.respond(random.choice(sentences))
