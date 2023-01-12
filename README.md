# tg_notifications_handler
handler for telegram notifications (messages) from bots or whatever

when a new message arrives to a specified chat, if it satisfies black and white lists, it will be sent to a specified receiver<br>
note: the message won't be forwarded, the new message with exact same text will be sent from your account<br>
that means you'll be online when the message is being sent<br>

you probably want to keep your api_id and api_hash and other things private, perhaps environmental variables or smth can help with that<br>
(haven't checked myself, can't say for sure)
