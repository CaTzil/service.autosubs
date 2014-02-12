# -*- coding: utf-8 -*-

import os
import sys
import xbmc
import xbmcaddon

__addon__ = xbmcaddon.Addon()
__author__ = __addon__.getAddonInfo('author')
__scriptid__ = __addon__.getAddonInfo('id')
__scriptname__ = __addon__.getAddonInfo('name')
__cwd__ = __addon__.getAddonInfo('path')
__version__ = __addon__.getAddonInfo('version')
__language__ = __addon__.getLocalizedString

__cwd__ = xbmc.translatePath(__addon__.getAddonInfo('path')).decode("utf-8")
__profile__ = xbmc.translatePath(__addon__.getAddonInfo('profile')).decode("utf-8")
__resource__ = xbmc.translatePath(os.path.join(__cwd__, 'resources')).decode("utf-8")

__settings__ = xbmcaddon.Addon("service.autosubs")

ignore_words = (__settings__.getSetting('ignore_words').split(','))

sys.path.append(__resource__)

LANGUAGES = (

    # Full Language name[0] podnapisi[1] ISO 639-1[2] ISO 639-1 Code[3] Script Setting Language[4] localized name id number[5]

    ("Albanian", "29", "sq", "alb", "0", 30201 ),
    ("Arabic", "12", "ar", "ara", "1", 30202 ),
    ("Belarusian", "0", "hy", "arm", "2", 30203 ),
    ("Bosnian", "10", "bs", "bos", "3", 30204 ),
    ("Bulgarian", "33", "bg", "bul", "4", 30205 ),
    ("Catalan", "53", "ca", "cat", "5", 30206 ),
    ("Chinese", "17", "zh", "chi", "6", 30207 ),
    ("Croatian", "38", "hr", "hrv", "7", 30208 ),
    ("Czech", "7", "cs", "cze", "8", 30209 ),
    ("Danish", "24", "da", "dan", "9", 30210 ),
    ("Dutch", "23", "nl", "dut", "10", 30211 ),
    ("English", "2", "en", "eng", "11", 30212 ),
    ("Estonian", "20", "et", "est", "12", 30213 ),
    ("Persian", "52", "fa", "per", "13", 30247 ),
    ("Finnish", "31", "fi", "fin", "14", 30214 ),
    ("French", "8", "fr", "fre", "15", 30215 ),
    ("German", "5", "de", "ger", "16", 30216 ),
    ("Greek", "16", "el", "ell", "17", 30217 ),
    ("Hebrew", "22", "he", "heb", "18", 30218 ),
    ("Hindi", "42", "hi", "hin", "19", 30219 ),
    ("Hungarian", "15", "hu", "hun", "20", 30220 ),
    ("Icelandic", "6", "is", "ice", "21", 30221 ),
    ("Indonesian", "0", "id", "ind", "22", 30222 ),
    ("Italian", "9", "it", "ita", "23", 30224 ),
    ("Japanese", "11", "ja", "jpn", "24", 30225 ),
    ("Korean", "4", "ko", "kor", "25", 30226 ),
    ("Latvian", "21", "lv", "lav", "26", 30227 ),
    ("Lithuanian", "0", "lt", "lit", "27", 30228 ),
    ("Macedonian", "35", "mk", "mac", "28", 30229 ),
    ("Malay", "0", "ms", "may", "29", 30248 ),
    ("Norwegian", "3", "no", "nor", "30", 30230 ),
    ("Polish", "26", "pl", "pol", "31", 30232 ),
    ("Portuguese", "32", "pt", "por", "32", 30233 ),
    ("PortugueseBrazil", "48", "pb", "pob", "33", 30234 ),
    ("Romanian", "13", "ro", "rum", "34", 30235 ),
    ("Russian", "27", "ru", "rus", "35", 30236 ),
    ("Serbian", "36", "sr", "scc", "36", 30237 ),
    ("Slovak", "37", "sk", "slo", "37", 30238 ),
    ("Slovenian", "1", "sl", "slv", "38", 30239 ),
    ("Spanish", "28", "es", "spa", "39", 30240 ),
    ("Swedish", "25", "sv", "swe", "40", 30242 ),
    ("Thai", "0", "th", "tha", "41", 30243 ),
    ("Turkish", "30", "tr", "tur", "42", 30244 ),
    ("Ukrainian", "46", "uk", "ukr", "43", 30245 ),
    ("Vietnamese", "51", "vi", "vie", "44", 30246 ),
    ("BosnianLatin", "10", "bs", "bos", "100", 30204 ),
    ("Farsi", "52", "fa", "per", "13", 30247 ),
    ("English (US)", "2", "en", "eng", "100", 30212 ),
    ("English (UK)", "2", "en", "eng", "100", 30212 ),
    ("Portuguese (Brazilian)", "48", "pt-br", "pob", "100", 30234 ),
    ("Portuguese (Brazil)", "48", "pb", "pob", "33", 30234 ),
    ("Portuguese-BR", "48", "pb", "pob", "33", 30234 ),
    ("Brazilian", "48", "pb", "pob", "33", 30234 ),
    ("Español (Latinoamérica)", "28", "es", "spa", "100", 30240 ),
    ("Español (España)", "28", "es", "spa", "100", 30240 ),
    ("Spanish (Latin America)", "28", "es", "spa", "100", 30240 ),
    ("Español", "28", "es", "spa", "100", 30240 ),
    ("SerbianLatin", "36", "sr", "scc", "100", 30237 ),
    ("Spanish (Spain)", "28", "es", "spa", "100", 30240 ),
    ("Chinese (Traditional)", "17", "zh", "chi", "100", 30207 ),
    ("Chinese (Simplified)", "17", "zh", "chi", "100", 30207 ) )


def languageTranslate(lang, lang_from, lang_to):
    for x in LANGUAGES:
        if lang == x[lang_from]:
            return x[lang_to]


def log(txt):
    if isinstance(txt, str):
        txt = txt.decode("utf-8")
    message = u'%s: %s' % (__scriptname__, txt)
    xbmc.log(msg=message.encode("utf-8"))


log('[%s] - Version: %s Started' % (__scriptname__, __version__))


class MyPlayer(xbmc.Player):
    def __init__(self, *args, **kwargs):
        xbmc.Player.__init__(self)
        log('MyPlayer - init')
        self.run = True

    def onPlayBackStopped(self):
        self.run = True

    def onPlayBackEnded(self):
        self.run = True

    def onPlayBackStarted(self):
        check_for_specific = (__addon__.getSetting('check_for_specific').lower() == 'true')
        specific_language = (__addon__.getSetting('selected_language'))
        specific_language = languageTranslate(specific_language, 0, 2)

        if self.run:
            movie_full_path = xbmc.Player().getPlayingFile()
            available_subs = xbmc.Player().getAvailableSubtitleStreams()
            available_langs = []
            for sub in available_subs:
                available_langs.append(sub.split('.')[-2])

            if (((not xbmc.getCondVisibility("VideoPlayer.HasSubtitles")) or (
                        check_for_specific and not specific_language in available_langs)) and all(
                        movie_full_path.find(v) <= -1 for v in ignore_words)):
                self.run = False
                xbmc.sleep(1000)
                log('AutoSearching for Subs')
                xbmc.executebuiltin('XBMC.RunScript(script.xbmc.subtitles)')
            else:
                self.run = False


player_monitor = MyPlayer()

while not xbmc.abortRequested:
    xbmc.sleep(1000)

del player_monitor
