

class Mail:

  def __init__(self, stdin):
    self._raw_mail = stdin


  @property
  def raw_mail(self):
    return self._raw_mail

  @raw_mail.setter
  def raw_mail(self, raw_mail):
    self._raw_mail = raw_mail

  def transform_json(self):
    pass

  def generate_message(self, json):
    pass

  def send_slack(self, ):
    pass
