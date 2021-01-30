class QQperson:
    def __init__(self,
                 Nickname,
                 Name,
                 Phone,
                 Mobile,
                 PagerHome,
                 HomePhone,
                 QQ,
                 BQQ,
                 Email):
        self.Nickname = Nickname
        self.Name = Name
        self.Phone = Phone
        self.Mobile = Mobile
        self.PagerHome = PagerHome
        self.HomePhone = HomePhone
        self.QQ = QQ
        self.BQQ = BQQ
        self.Email = Email

    def sendsms(self):
        pass

    def sendmail(self):
        pass

    def phonecall(self):
        pass
