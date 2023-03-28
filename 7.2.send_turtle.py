class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)

        return self.message_id

    def read_inbox(self, user, N):
        '''
        Read the first N messages in the inbox of the user.
        :param user:  The user whose inbox we want to read.
        :param N:  The number of messages to read.
        :return:    A list of the first N messages in the inbox.
        '''
        return self.boxes[user][:N]

    def search_inbox(self, user, msg):
        """
        Search the inbox of the user for a message.
        :param user:  The user whose inbox we want to search.
        :param msg:    The message to search for.
        :return:    A list of messages that match the search.
        """
        return [x for x in self.boxes[user] if x['body'] == msg]


p = PostOffice(["Alice", "Bob", "Charlie"])
p.send_message("Alice", "Bob", "Hello Bob!")
p.send_message("Alice", "Bob", "Hello Bob again!")

print(p.read_inbox("Bob", 2))
print(p.search_inbox("Bob", "Hello Bob again!"))

