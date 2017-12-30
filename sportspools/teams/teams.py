from django.db import models

import unicodedata

class Teams(models.Model):
    def StripAccents(self, s):
        return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')
