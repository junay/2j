# -*- coding: utf-8 -*-
from ragendja.settings_post import settings
settings.add_app_media('combined-%(LANGUAGE_CODE)s.js',
    'blog/code.js',
)
