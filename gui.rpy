################################################################################
## Inisialisasi
################################################################################

## pernyataan offset init menyebabkan pernyataan inisialisasi di file ini untuk
## berjalan lebih dahulu daripada pernyataan init di file lain nya.
init offset = -2

## Memanggil gui.init. mereset gaya ke value bawaan, dan menset lebar dan tinggi
## dari permainan.
init python:
    gui.init(1230, 720)



################################################################################
## Variabel konfigurasi GUI
################################################################################


## Warna #######################################################################
##
## Warna text pada antarmuka.

## Warna aksen yang digunakan sepanjang interface sampai pewarnaan text.
define gui.accent_color = u'#cccc00'

## Warna yang di gunakan untuk warna tombol text jika di pilih atau di tekan.
define gui.idle_color = u'#888888'

## Warna kecil yang di gunakan untuk text kecil, yang membutuhkan lebih terang/
## lebih gelap untuk mencapai efek yang sama
define gui.idle_small_color = u'#aaaaaa'

## Warna yang di gunakan untuk tombol dan bar yang di pilih.
define gui.hover_color = u'#e0e066'

## Warna yang digunakan untuk text tombol ketika di pijit tapi tidak di fokus.
## Tombol di pilih jika terdapat di layar saat ini atau value preferensi.
define gui.selected_color = u'#ffffff'

## Warna yang di gunakan untuk tombol text ketika tidak bisa di pilih.
define gui.insensitive_color = u'#8888887f'

## Warna yang di gunakan untuk beberapa bagian dari bar yang tidak terisi. Ini
## tidak di gunakan secara langsung, Tapi di gunakan ketika me regenerasi file
## gambar bar.
define gui.muted_color = u'#515100'
define gui.hover_muted_color = u'#7a7a00'

## Warna yang di gunakan untuk dialog dan text pilihan menu.
define gui.text_color = u'#ffffff'
define gui.interface_text_color = u'#ffffff'


## Font dan ukuran Font ########################################################

## Font yang digunakan untuk text in-game.
define gui.text_font = "DejaVuSans.ttf"

## Font yang di gunakan untuk nama karakter.
define gui.name_text_font = "DejaVuSans.ttf"

## Font yang digunakan untuk text di luar permainan.
define gui.interface_text_font = "DejaVuSans.ttf"

## Ukuran normal dialog text.
define gui.text_size = 22

## Ukuran dari nama karakter.
define gui.name_text_size = 30

## Ukuran text antarmuka permainan.
define gui.interface_text_size = 22

## Ukuran label di antarmuka permainan.
define gui.label_text_size = 24

## Ukuran dari text di layar notifikasi.
define gui.notify_text_size = 16

## Ukuran judul permainan.
define gui.title_text_size = 50


## Menu utama dan Menu permainan. ##############################################

## Gambar yang di gunakan untuk Menu utama dan Menu permainan.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Dialog ######################################################################
##
## Variabel ini mengendalikan bagaimana dialog di tampilkan pada layar pada satu
## waktu.

## Tinggi textbox yang berisi dialog.
define gui.textbox_height = 185

## Penempatan texbox secara vertikal pada layar. 0.0 adalah atas, 0.5 adalah
## tengah, dan 1.0 adalah bawah.
define gui.textbox_yalign = 1.0


## Penempatan nama karakter yang berbicara, hampir sama dengan kotak text. 
define gui.name_xpos = 240
define gui.name_ypos = 0

## Penempatan  horizontal nama karakter. Ini dapat berupa 0.0 untuk rata kiri,
## 0.5 untuk rata tengah, dan 1.0 untuk rata kanan. 
define gui.name_xalign = 0.0

## Lebar, panjang, dan tepi dari kotak berisi nama karakter, Atau None untuk
## secara otomatis mengukur nya.
define gui.namebox_width = None
define gui.namebox_height = None

## Tepi kotak bersisi urutan nama karakter, di kiri, atas, kanan, bawah.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Jika Benar, latar dari kotaknama akan di beri judul, jika Salah, latar dari
## kotaknama akan di ukur ulang.
define gui.namebox_tile = False


## Penempatan dialog itu relatif pada kotaktext. Ini dapat berisi angka dari
## pixel yang relativ mulai dari sisi kiri sampai atas dari kotaknama, atau 0.5
## untuk tengah.
define gui.dialogue_xpos = 268
define gui.dialogue_ypos = 50

## Lebar maximum dari dialog text, dalam pixel.
define gui.dialogue_width = 744

## rata tengah dari text dialog. Ini dapat berisi 0.0 untuk rata kiri, atau 0.5
## untuk tengah, dan 1.0 untuk kanan.
define gui.dialogue_text_xalign = 0.0


## Tombol ######################################################################
##
## These variables, along with the image files in gui/button, control aspects of
## how buttons are displayed.

## The width and height of a button, in pixels. If None, Ren'Py computes a size.
define gui.button_width = None
define gui.button_height = None

## The borders on each side of the button, in left, top, right, bottom order.
define gui.button_borders = Borders(4, 4, 4, 4)

## If True, the background image will be tiled. If False, the background image
## will be linearly scaled.
define gui.button_tile = False

## The font used by the button.
define gui.button_text_font = 'gui/fonts/fjb.ttf'#gui.interface_text_font

## The size of the text used by the button.
define gui.button_text_size = gui.interface_text_size

## Warna tombol text di berbagai kondisi.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## Alignment horisontal tombol text. (0.0 itu kiri, 0.5 tengah, 1.0 kanan).
define gui.button_text_xalign = 0.0


## These variables override settings for different kinds of buttons. Please see
## the gui documentation for the kinds of buttons available, and what each is
## used for.
##
## These customizations are used by the default interface:

define gui.radio_button_borders = Borders(18, 4, 4, 4)

define gui.check_button_borders = Borders(18, 4, 4, 4)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(10, 4, 10, 4)

define gui.quick_button_borders = Borders(10, 4, 10, 0)
define gui.quick_button_text_size = 14
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## You can also add your own customizations, by adding properly-named variables.
## For example, you can uncomment the following line to set the width of a
## navigation button.

# define gui.navigation_button_width = 250


## Choice Buttons ##############################################################
##
## Choice buttons are used in the in-game menus.

define gui.choice_button_width = 790
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(100, 5, 100, 5)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = "#444444"


## File Slot Buttons ###########################################################
##
## A file slot button is a special kind of button. It contains a thumbnail
## image, and text describing the contents of the save slot. A save slot uses
## image files in gui/button, like the other kinds of buttons.

## The save slot button.
define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 256
define config.thumbnail_height = 144

## The number of columns and rows in the grid of save slots.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Positioning and Spacing #####################################################
##
## These variables control the positioning and spacing of various user interface
## elements.

## The position of the left side of the navigation buttons, relative to the left
## side of the screen.
define gui.navigation_xpos = 40

## The vertical position of the skip indicator.
define gui.skip_ypos = 10

## The vertical position of the notify screen.
define gui.notify_ypos = 45

## The spacing between menu choices.
define gui.choice_spacing = 22

## Buttons in the navigation section of the main and game menus.
define gui.navigation_spacing = 4

## Controls the amount of spacing between preferences.
define gui.pref_spacing = 10

## Controls the amount of spacing between preference buttons.
define gui.pref_button_spacing = 0

## The spacing between file page buttons.
define gui.page_spacing = 0

## The spacing between file slots.
define gui.slot_spacing = 10

## posisi text menu utama.
define gui.main_menu_text_xalign = 1.0


## Frames ######################################################################
##
## These variables control the look of frames that can contain user interface
## components when an overlay or window is not present.

## Frame generic
define gui.frame_borders = Borders(4, 4, 4, 4)

## The frame that is used as part of the confirm screen.
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)

## The frame that is used as part of the skip screen.
define gui.skip_frame_borders = Borders(16, 5, 50, 5)

## The frame that is used as part of the notify screen.
define gui.notify_frame_borders = Borders(16, 5, 40, 5)

## Should frame backgrounds be tiled?
define gui.frame_tile = False


## Bars, Scrollbars, and Sliders ###############################################
##
## These control the look and size of bars, scrollbars, and sliders.
##
## GUI Bawaan hanya menggunakan slider dan scrollbars vertikal. Bar lainnya
## hanya di gunakan pada layar GUI yang di tulis sendiri oleh pembuat/creator.

## The height of horizontal bars, scrollbars, and sliders. The width of vertical
## bars, scrollbars, and sliders.
define gui.bar_size = 25
define gui.scrollbar_size = 12
define gui.slider_size = 25

## True if bar images should be tiled. False if they should be linearly scaled.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Horizontal borders.
define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)

## Vertical borders.
define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)

## What to do with unscrollable scrollbars in the gui. "hide" hides them, while
## None shows them.
define gui.unscrollable = "hide"


## History #####################################################################
##
## The history screen displays dialogue that the player has already dismissed.

## The number of blocks of dialogue history Ren'Py will keep.
define config.history_length = 250

## The height of a history screen entry, or None to make the height variable at
## the cost of performance.
define gui.history_height = 140

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.history_name_xpos = 155
define gui.history_name_ypos = 0
define gui.history_name_width = 155
define gui.history_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.history_text_xpos = 170
define gui.history_text_ypos = 2
define gui.history_text_width = 740
define gui.history_text_xalign = 0.0


## NVL-Mode ####################################################################
##
## The NVL-mode screen displays the dialogue spoken by NVL-mode characters.

## The borders of the background of the NVL-mode background window.
define gui.nvl_borders = Borders(0, 10, 0, 20)

## The maximum number of NVL-mode entries Ren'Py will display. When more entries
## than this are to be show, the oldest entry will be removed.
define gui.nvl_list_length = 6

## The height of an NVL-mode entry. Set this to None to have the entries
## dynamically adjust height.
define gui.nvl_height = 115

## The spacing between NVL-mode entries when gui.nvl_height is None, and between
## NVL-mode entries and an NVL-mode menu.
define gui.nvl_spacing = 10

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 150
define gui.nvl_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 590
define gui.nvl_text_xalign = 0.0

## The position, width, and alignment of nvl_thought text (the text said by the
## nvl_narrator character.)
define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 780
define gui.nvl_thought_xalign = 0.0

## The position of nvl menu_buttons.
define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0

## Lokalisasi ##################################################################

## Ini mengendalikan dimana line break di ijinkan. Pengaturan bawaan sudah
## cocok untuk kebanyakan bahasa. Daftar value yang tersedia dapat di lihat di
## https://www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Perangkat mobile
################################################################################

init python:

    ## This increases the size of the quick buttons to make them easier to touch
    ## on tablets and phones.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(40, 14, 40, 0)

    ## This changes the size and spacing of various GUI elements to ensure they
    ## are easily visible on phones.
    @gui.variant
    def small():

        ## Font sizes.
        gui.text_size = 30
        gui.name_text_size = 36
        gui.notify_text_size = 25
        gui.interface_text_size = 30
        gui.button_text_size = 30
        gui.label_text_size = 34

        ## Adjust the location of the textbox.
        gui.textbox_height = 240
        gui.name_xpos = 80
        gui.dialogue_xpos = 90
        gui.dialogue_width = 1100

        ## Ubah ukuran dan jarak dari berbagai hal.
        gui.slider_size = 36

        gui.choice_button_width = 1240
        gui.choice_button_text_size = 30

        gui.navigation_spacing = 20
        gui.pref_button_spacing = 10

        gui.history_height = 190
        gui.history_text_width = 690

        gui.quick_button_text_size = 20

        ## File button layout.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-mode.
        gui.nvl_height = 170

        gui.nvl_name_width = 305
        gui.nvl_name_xpos = 325

        gui.nvl_text_width = 915
        gui.nvl_text_xpos = 345
        gui.nvl_text_ypos = 5

        gui.nvl_thought_width = 1240
        gui.nvl_thought_xpos = 20

        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 20
