define config.name = _("ATM_OS")
define config.save_physical_size = False
define gui.show_name = True
define config.version = "1.1.35F4E"#'1.0-061022'
define gui.about = _p("""
""")
define build.name = "ATM_OS"
define config.has_sound = False
define config.has_music = False
define config.has_voice = False
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)
define config.save_directory = "ATM_OS"
define config.window_icon = "gui/window_icon.png"
define body = u'#888888'
define latarBiru = u'#000088'
define latarMerah = u'#880000'
define softkey = 'gui/tombol_idle.png'

default preferences.text_cps = 0
default preferences.afm_time = 15
default persistent.pin = '123456'
default persistent.pinLama = ''
default persistent.saldo = 5000000
default persistent.saldoMin = 50000
default persistent.maks = 2500000
default persistent.kelipatan = 50000
default persistent.onBlokir = False
default persistent.denganProses = True
default persistent.pertamaKali = True
default tgljam = '  '
default onKartuMasuk = False
default onError = False
default mode = 0
default angkaEntri = ''
default pinEntri = ''
default rekEntri = ''
default kesempatan = 3
default halLayarKodeBank = 0
default valPenjelasan = 2

init python:
    build.archive("0", "all")
    build.classify("game/**.rpyc", "0")
    build.archive("1", "all")
    build.classify("game/**.jpg", "1")
    build.classify("game/**.png", "1")
    build.classify("game/**.ttf", "1")
    build.classify("game/**.rpymc", "1")

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.rpyc', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('script_version.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)
    build.classify('/game/**.rpym', None)
