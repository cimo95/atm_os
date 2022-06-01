init python: 
      
    def tj():
        from datetime import datetime
        sekarang = datetime.now()
        global tgljam
        tgljam = sekarang.strftime('%d/%m/%Y,%H:%M:%S').split(',')

    def cekKartuATM():
        global onKartuMasuk, angkaEntri
        if not onKartuMasuk:
            if persistent.onBlokir:
                Show('layarBlokir')()
            else:
                onKartuMasuk = True 
                angkaEntri = ''
                Show('layarInputPin')()
            Show('layarProses',isi='#####MOHON TUNGGU, SEDANG MEMBACA KARTU...')()
        else:
            Show('confirm',message='Kartu sudah masuk !',yes_action=Hide('confirm'))()
    
    def tarikTunai(nominal):
        global onError
        saldo = persistent.saldo - persistent.saldoMin
        valNominal = int(nominal)
        if valNominal <= saldo:
            if valNominal <= persistent.maks:
                modNominal = valNominal % persistent.kelipatan
                if modNominal == 0:
                    persistent.saldo = persistent.saldo - valNominal
                    batalkan()
                    Show('layarProses',isi='MOHON TUNGGU, MENYELESAIKAN TRANSAKSI...')()
                else:
                    onError = True
                    Show('layarError',isi='NOMINAL YANG ANDA PILIH#BUKAN KELIPATAN DARI#Rp.'+str(persistent.kelipatan))()
            else:
                onError = True
                Show('layarError',isi='NOMINAL YANG ANDA PILIH#MELEBIHI TRANSAKSI MAKSIMAL#Rp.'+str(persistent.maks))()
        else:
            onError = True
            Show('layarError',isi='NOMINAL YANG ANDA PILIH#MELEBIHI SALDO YANG ADA#Rp.'+str(persistent.saldo))()
        Show('layarProses',isi='#####MOHON TUNGGU, SEDANG MEMPROSES...')()
    
    def transfer(rek=-1,nominal=-1):
        global rekEntri, onError
        if rek != -1:
            dictRek = {}
            rekAda = True
            try:
                renpy.file(config.basedir.replace('\\','/')+'/rekening.txt')
            except:
                rekAda = False
            if not rekAda:
                try:
                    with open(config.basedir+'/rekening.txt','w') as fileRekW:
                        fileRekW.write(teksRekening)
                except:
                    pass
            try:
                fileRek = open(config.basedir+'/rekening.txt','r')
                listRek = fileRek.readlines()
                for itemRek in listRek:
                    if (len(itemRek) > 1) and (itemRek[0] != '#'):
                        parseItemRek = itemRek.split(';')
                        dictRek[parseItemRek[0]] = [parseItemRek[1],parseItemRek[2]]
                if dictRek.get(rek) == None:
                    resetEntri()
                    Show('layarMenuTransfer',hal=0)()
                    Show('layarError',isi='NOMOR REKENING TERSEBUT#TIDAK DITEMUKAN / TERDAFTAR')()
                    onError = True
                else:
                    resetEntri()
                    Show('layarMenuTransfer',hal=1,nama=dictRek[rek][1]+' / '+dictRek[rek][0])()
            except:
                resetEntri()
                Show('layarMenuTransfer',hal=0)()
                Show('layarError',isi='NOMOR REKENING TERSEBUT#TIDAK DITEMUKAN / TERDAFTAR')()
                onError = True
            Show('layarProses',isi='#####MOHON TUNGGU, SEDANG MEMERIKSA...')()
        elif nominal != -1:
            if nominal <= (persistent.saldo - persistent.saldoMin):
                persistent.saldo = persistent.saldo - nominal
                Show('layarSelesaiTrans',isi='TRANSAKSI TELAH BERHASIL DILAKUKAN')()
            else:
                resetEntri()
                Show('layarError',isi='NOMINAL TRANSAKSI TIDAK CUKUP')()      
                onError = True
            Show('layarProses',isi='#####MOHON TUNGGU, SEDANG MEMPROSES...')()
        
    def isiEntri(angka):
        global angkaEntri
        if (not onError):
            if (mode != 0) or ((mode == 0) and (len(angkaEntri) < 6)):
                angkaEntri += angka
                
    def nomEntri(tambah=True,mode='-1'):
        global angkaEntri
        if angkaEntri == '': angkaEntri = '0'
        if tambah:
            valEntri = int(angkaEntri) + persistent.kelipatan
        else:
            valEntri = int(angkaEntri) - persistent.kelipatan
        if (valEntri <= persistent.maks) and (valEntri >= persistent.saldoMin) and (mode in [7,8]):
            angkaEntri = str(valEntri)

    def tampilPin():
        pjgPin = len(angkaEntri)
        pinEntri = ''
        if not onError:
            for i in range(0,pjgPin):
                pinEntri += '*'

    def resetEntri():
        global angkaEntri, onError
        if not onError:
            angkaEntri = ''

    def konfirmasi(mode):
        global angkaEntri, kesempatan, onError
        if not onError:
            if mode == 0:
                Show('layarProses',isi='#####MOHON TUNGGU, SEDANG MEMPROSES...')()
                if angkaEntri != persistent.pin:
                    if kesempatan != 0:
                        Show('layarError',isi='MASUKKAN PIN DENGAN BENAR#KESEMPATAN : '+str(kesempatan))()
                        angkaEntri =  ''
                        kesempatan -= 1
                        onError = True
                    else:
                        onError, persistent.onBlokir=True, True
                        Show('layarBlokir')()
                else:
                    Show('layarMenu')()
            elif mode == 1:
                Show('layarProses',isi='#####MOHON TUNGGU, SEDANG MEMPROSES...')()
                if angkaEntri != persistent.pin:
                    if kesempatan != 0:
                        Show('layarError',isi='MASUKKAN PIN DENGAN BENAR#KESEMPATAN : '+str(kesempatan))()
                        angkaEntri =  ''
                        kesempatan -= 1
                        onError = True
                    else:
                        onError, persistent.onBlokir=True, True
                        Show('layarBlokir')()
                else:
                    angkaEntri = ''
                    Show('layarMenuGantiPin',hal=1)()
            elif mode == 2:
                persistent.pinLama = angkaEntri
                angkaEntri = ''
                Show('layarMenuGantiPin',hal=2)()
            elif mode == 3:
                if angkaEntri != persistent.pinLama:
                    angkaEntri = ''
                    Show('layarMenuGantiPin',hal=1)()
                    Show('layarError',isi='PIN BARU TIDAK SESUAI,#PASTIKAN "PIN BARU"#DAN "KONFIRMASI PIN BARU" SAMA.')()
                    onError = True
                else:
                    persistent.pin = angkaEntri
                    Show('layarSelesaiTrans',isi='PIN ANDA TELAH BERHASIL DIGANTI')()
                    Show('layarProses',isi='#####MOHON TUNGGU, SEDANG MENGGANTI PIN...')()

    def batalkan():
        global onError
        if not persistent.onBlokir:
            if onError:
                onError = False
                Hide('layarError')()
            else:
                resetEntri()
                global mode, onKartuMasuk, onError
                onKartuMasuk = False
                onError = False
                mode = -1
                Show('layarAwal',selesai=True)()

    def resetSimulator():
        persistent._clear()
        renpy.utter_restart()
    
    def bukaBlokir():
        global onError, kesempatan
        persistent.onBlokir = False
        onError = False
        kesempatan = 3
        Show('confirm',message='Blokir telah dibuka. Simulasi bisa dilakukan kembali.')()
        
    def nilaiParam(id,nilai):
        if id == 0:
            if nilai < 100000:
                Show('confirm',message='Nominal saldo setidaknya 100000 (100 Ribu)')()
            else:
                persistent.saldo = nilai
                Show('layarAtur')()
        elif id == 1:
            if nilai < 10000:
                Show('confirm',message='Nominal saldo minimal setidaknya 10000 (10 Ribu)')()
            else:
                persistent.saldoMin = nilai
                Show('layarAtur')()
        elif id == 2:
            if nilai < 200000:
                Show('confirm',message='Nominal maksimal penarikan setidaknya 200000 (200 Ribu)')()
            else:
                persistent.maks = nilai
                Show('layarAtur')()
        elif id == 3:
            if not nilai in [20000,50000,100000]:
                Show('confirm',message='Nominal kelipatan hanya diperbolehkan\n20000 (20 Ribu), 50000 (50 Ribu) atau 100000 (100 Ribu)')()
            else:
                persistent.kelipatan = nilai
                Show('layarAtur')()
    
screen tombol(tombol1='',tombol2='',tombol3='',tombol4='',tombol5='',tombol6='',tombol7='',tombol8='',aksi1=NullAction(),aksi2=NullAction(),aksi3=NullAction(),aksi4=NullAction(),aksi5=NullAction(),aksi6=NullAction(),aksi7=NullAction(),aksi8=NullAction(),accept=NullAction()):
    tag layar
    zorder 80
    hbox xsize 816 ypos 354 xpos 24:
        vbox xanchor 0.0 xalign 0.0 ysize 300:
            textbutton tombol1 text_style 'fonPanel' yalign 0.0 action aksi1
            textbutton tombol2 text_style 'fonPanel' yalign 0.25 action aksi2
            textbutton tombol3 text_style 'fonPanel' yalign 0.5 action aksi3
            textbutton tombol4 text_style 'fonPanel' yalign 0.75 action aksi4
        vbox xanchor 1.0 xalign 1.0 ysize 300:
            textbutton tombol5 text_style 'fonPanel' yalign 0.0 xanchor 1.0 xalign 1.0 action aksi5
            textbutton tombol6 text_style 'fonPanel' yalign 0.25 xanchor 1.0 xalign 1.0 action aksi6
            textbutton tombol7 text_style 'fonPanel' yalign 0.5 xanchor 1.0 xalign 1.0 action aksi7
            textbutton tombol8 text_style 'fonPanel' yalign 0.75 xanchor 1.0 xalign 1.0 action aksi8
            
    vbox xsize 360 xpos 870 ypos 36:
        text '  APLIKASI  SIMULATOR\nANJUNGAN TUNAI MANDIRI' style 'fonBanner'
        null height 20
        text '{size=40}{font=gui/fonts/f25.ttf}ATM_OS{/font}{/size}' style 'fonBanner'
        
    vbox xpos 870 yalign 0.95 yanchor 1.0:
        textbutton 'MASUKKAN KARTU ATM' style 'fonTombol' text_style 'fonTombol' action Function(cekKartuATM)
        textbutton 'ATUR SIMULATOR' style 'fonTombol' text_style 'fonTombol' action [SensitiveIf(mode != 2 and mode != 3),If(((mode != -1) and (not persistent.onBlokir)),true=Show('confirm',message='ATUR SIMULATOR hanya bisa diakses di halaman awal.\nSelesaikan atau batalkan transaksi terlebih dahulu.'),false=Show('layarAtur'))]
        textbutton 'PENJELASAN' style 'fonTombol' text_style 'fonTombol' action Show('confirm',message=listPenjelasan[valPenjelasan])
        textbutton 'TENTANG' style 'fonTombol' text_style 'fonTombol' action Show('layarTentang')
        textbutton 'KELUAR' style 'fonTombol' text_style 'fonTombol' action Quit(confirm=True)
        null height 25
        imagemap:
            auto 'gui/tombol_%s.png'
            hotspot (15, 15, 60, 50) action Function(isiEntri,angka='1')
            hotspot (90, 15, 60, 50) action Function(isiEntri,angka='2')
            hotspot (165, 15, 60, 50) action Function(isiEntri,angka='3')
            hotspot (15, 80, 60, 50) action Function(isiEntri,angka='4')
            hotspot (90, 80, 60, 50) action Function(isiEntri,angka='5')
            hotspot (165, 80, 60, 50) action Function(isiEntri,angka='6')
            hotspot (15, 145, 60, 50) action Function(isiEntri,angka='7')
            hotspot (90, 145, 60, 50) action Function(isiEntri,angka='8')
            hotspot (165, 145, 60, 50) action Function(isiEntri,angka='9')
            hotspot (15, 210, 60, 50) action Function(nomEntri,tambah=False,mode=mode)
            hotspot (90, 210, 60, 50) action Function(isiEntri,angka='0')
            hotspot (165, 210, 50, 50) action Function(nomEntri,mode=mode)
            hotspot (240, 15, 105, 50) action Function(batalkan)
            hotspot (240, 80, 105, 50) action Function(resetEntri)
            hotspot (225, 200, 130, 60) action [SensitiveIf(accept != NullAction()),accept]

screen monitor(isi=''):
    tag layar
    zorder 80
    vbox xsize 864 ysize 648 yalign 0.5:
        add body
    vbox xsize 816 ysize 612 yalign 0.5 xpos 24:
        add latarBiru
    vbox xsize 816 ysize 200 ypos 54 xpos 24:
        python:
            isi = '#PT. BANK ORANG INDONESIA##'+isi
            listIsi=isi.split('#')
        for i in range(0,len(listIsi)):
            text listIsi[i] style 'fonMonitor'
    use tombol()

screen layarAwal(selesai=False):
    tag layar
    zorder 80
    python:
        global mode, tgljam, valPenjelasan
        mode = -1
        jeda = renpy.random.randint(1,5)
        balik = 10 + (5 - jeda)
        valPenjelasan = 1 if selesai else 2
    if selesai:
        use monitor('##TERIMA KASIH ATAS TRANSAKSI ANDA##SILAHKAN AMBIL KEMBALI KARTU ATM ANDA###PASTIKAN BARANG BAWAAN ANDA, TIDAK TERTINGGAL.')
        timer 10.0 action Show('layarAwal')
    else:
        use monitor('##SELAMAT DATANG##SILAHKAN MASUKKAN KARTU ATM ANDA###PASTIKAN POSISI KARTU#BAGIAN DEPAN MENGHADAP KEATAS.')
        python:
            if persistent.pertamaKali:
                persistent.pertamaKali = False
                Show('confirm',message=listPenjelasan[0])()
    use tombol(tombol4=tgljam[0],tombol8=tgljam[1])
    timer 1.0 repeat True action Function(tj)

screen layarError(isi):
    zorder 90
    use monitor()
    vbox xsize 816 ysize 612 yalign 0.5 xpos 24:
        add latarMerah
    vbox xsize 864 yalign 0.5:
        python:
            listIsi=isi.split('#')
        for i in range(0,len(listIsi)):
            textbutton ' '+listIsi[i]+' ' text_style 'fonError' xalign 0.5
        textbutton '{size=30} tekan CANCEL untuk menutup pesan ini {/size}' text_style 'fonError' xalign 0.5   

screen layarPin(isi,aksi,imode=0):
    python:
        global mode, angkaEntri
        mode = imode
        pinEntri = ''
        for i in range(0,len(angkaEntri)):
            pinEntri += '*'
        pinEntri = pinEntri.ljust(6,'_')
    tag layar
    zorder 80
    use monitor(isi.replace('[pinEntri]','##{b}{size=50}'+pinEntri+'{/size}{/b}##'))
    use tombol(tombol6='BENAR -->',aksi6=If(len(angkaEntri)==6,true=aksi,false=NullAction()),accept=If(len(angkaEntri)==6,true=aksi,false=NullAction()))

screen layarProses(isi=''):
    zorder 100
    use monitor()
    vbox xsize 816 ysize 612 yalign 0.5 xpos 24:
        add latarBiru
    vbox xsize 816 ysize 200 ypos 54 xpos 24:
        python:
            if not persistent.denganProses:
                Hide('layarProses')()
            jeda = renpy.random.randint(1,5)
            isi = '#PT. BANK ORANG INDONESIA##'+isi
            listIsi=isi.split('#')
        for i in range(0,len(listIsi)):
            text listIsi[i] style 'fonMonitor'      
    timer jeda action Hide('layarProses')

screen layarSelesaiTrans(isi=''):
    tag layar
    zorder 80
    python:
        global valPenjelasan
        valPenjelasan = 15
    use monitor(isi+'####INGIN MELANJUTKAN TRANSAKSI ?')
    use tombol(tombol6='YA -->',aksi6=[Function(batalkan),SetVariable('onKartuMasuk',True),SetVariable('angkaEntri',''),Show('layarInputPin')],tombol7='TIDAK -->',aksi7=Function(batalkan))
    
screen layarInputPin:
    tag layar
    zorder 80
    python :
        global valPenjelasan
        valPenjelasan = 3
    use layarPin(isi='MASUKKAN PIN ATM ANDA[pinEntri]DEMI KEAMANAN DAN KENYAMANAN,#SILAKAN GANTI PIN ANDA SECARA BERKALA.#####TEKAN "BENAR" UNTUK MELANJUTKAN#TEKAN "CANCEL" UNTUK MEMBATALKAN',aksi=Function(konfirmasi,mode=0))

screen layarBlokir:
    python:
        global mode,valPenjelasan
        mode = 1
        valPenjelasan = 4
    tag layar
    zorder 80
    use monitor('\nTRANSAKSI GAGAL##ANDA SUDAH 3X SALAH PIN##KARTU ANDA DIBLOKIR##HARAP HUBUNGI CARD CENTER')
    
screen layarAtur:
    tag layar
    zorder 80
    python:
        global mode,valPenjelasan
        mode = 2
        valPenjelasan = 5
    use monitor('\nUBAH NILAI PARAMETER SIMULATOR#TEKAN "CANCEL" UNTUK MEMBATALKAN')
    use tombol(tombol1='<-- SALDO',aksi1=[SetVariable('angkaEntri',''),Show('layarAturUbah',id=0)],
    tombol2='<-- SALDO MINIMAL',aksi2=[SetVariable('angkaEntri',''),Show('layarAturUbah',id=1)],
    tombol3='<-- MAKS. PENARIKAN',aksi3=[SetVariable('angkaEntri',''),Show('layarAturUbah',id=2)],
    tombol4='<-- KELIPATAN',aksi4=[SetVariable('angkaEntri',''),Show('layarAturUbah',id=3)],
    tombol5='BUKA BLOKIR -->',aksi5=If(persistent.onBlokir,true=Function(bukaBlokir),false=Show('confirm',message='Anda tidak sedang dalam status terblokir.')),
    tombol6='SIM. PROSES -->',aksi6=If(persistent.denganProses,true=Show('confirm',message='Apakah anda tidak ingin mensimulasikan tampilan proses?\n\nJika ya, setiap kali proses transaksi dilakukan,\nhasil proses akan ditampilkan secara langsung.',yes_action=[SetField(persistent,'denganProses',False),Hide('confirm')],no_action=Hide('confirm')),false=Show('confirm',message='Apakah anda ingin mensimulasikan tampilan proses?\n\nJika ya, setiap kali proses transaksi dilakukan,\nmaka tampilan "sedang memproses..." akan ditampilkan\ndengan jeda waktu tertentu',yes_action=[SetField(persistent,'denganProses',True),Hide('confirm')],no_action=Hide('confirm'))),
    tombol7='RESET -->',aksi7=Show('confirm',message='Anda yakin ingin mereset simulator?\nSeluruh pengaturan dan nominal, akan dikembalikan ke nilai asal.',yes_action=[Hide('confirm'),Function(resetSimulator)],no_action=Hide('confirm')))
            
screen layarAturUbah(id):
    python:
        global mode, angkaEntri
        mode = 3
        if angkaEntri == '': angkaEntri = '0'
    tag layar
    zorder 80
    use monitor('\nATUR SIMULATOR ATM_OS#UBAH NOMINAL '+'SALDO SAAT INI,SALDO MINIMAL,MAKSIMAL PENARIKAN,KELIPATAN PENARIKAN'.split(',')[id]+'##NOMINAL LAMA : '+str((persistent.saldo,persistent.saldoMin,persistent.maks,persistent.kelipatan)[id])+'\nNOMINAL BARU : '+str(int(angkaEntri)))
    use tombol(tombol7='SIMPAN -->',aksi7=Function(nilaiParam,id,int(angkaEntri)),tombol8='BATAL -->',aksi8=Show('layarAtur'),accept=Function(nilaiParam,id,int(angkaEntri)))

screen layarMenu():
    python:
        global mode, valPenjelasan
        mode = 4
        valPenjelasan = 6
    tag layar
    zorder 80
    use monitor('\nSILAHKAN PILIH JENIS TRANSAKSI#YANG ANDA INGINKAN########TEKAN "CANCEL"#UNTUK MEMBATALKAN TRANSAKSI')
    use tombol(tombol1='<-- GANTI PIN',aksi1=[Function(resetEntri),Show('layarMenuGantiPin')],
    tombol5='INFORMASI SALDO -->', aksi5=[Show('layarMenuInfoSaldo'),Show('layarProses',isi='#####MOHON TUNGGU, SEDANG MEMPROSES...')],
    tombol6='TARIK TUNAI -->', aksi6=Show('layarMenuTarikTunai'),
    tombol7='TRANSFER -->', aksi7=[Function(resetEntri),Show('layarMenuTransfer')])

screen layarMenuGantiPin(hal=0):
    tag layar
    zorder 80
    python:
        global valPenjelasan
        valPenjelasan = hal + 7
    if hal == 0:
        use layarPin(isi='MASUKKAN PIN LAMA ATM ANDA[pinEntri]######TEKAN "BENAR" UNTUK MELANJUTKAN#TEKAN "CANCEL" UNTUK MEMBATALKAN TRANSAKSI',aksi=Function(konfirmasi,mode=1))
        use tombol(tombol7='KEMBALI -->', aksi7=Show('layarMenu'))
    elif hal == 1:
        use layarPin(isi='MASUKKAN PIN BARU ATM ANDA[pinEntri]ISIKAN 6 DIGIT PIN BARU ANDA######TEKAN "BENAR" UNTUK MELANJUTKAN#TEKAN "CANCEL" UNTUK MEMBATALKAN TRANSAKSI',aksi=Function(konfirmasi,mode=2))
    elif hal == 2:
        use layarPin(isi='KONFIRMASI PIN BARU ATM ANDA[pinEntri]ISIKAN LAGI 6 DIGIT PIN BARU ANDA#UNTUK MEMASTIKAN PIN YANG ANDA MASUKKAN BENAR#####TEKAN "BENAR" UNTUK MELANJUTKAN#TEKAN "CANCEL" UNTUK MEMBATALKAN TRANSAKSI',aksi=Function(konfirmasi,mode=3))
           
screen layarMenuInfoSaldo():
    python:
        global mode, valPenjelasan
        mode = 6
        valPenjelasan = 10
    tag layar
    zorder 80
    use monitor('\nINFORMASI SALDO##SALDO : Rp. '+str(persistent.saldo)+'##LANJUTKAN TRANSAKSI LAINNYA ?')
    use tombol(tombol6='YA -->', aksi6=Show('layarMenu'),tombol7='TIDAK -->',aksi7=Function(batalkan))
    
screen layarMenuTarikTunai():
    python:
        global mode, valPenjelasan
        mode = 7
        valPenjelasan = 11
    tag layar
    zorder 80
    use monitor('\nPILIH NOMINAL PENARIKAN##TEKAN "CANCEL" UNTUK MEMBATALKAN TRANSAKSI')
    use tombol(tombol1='<-- 100.000', aksi1=Function(tarikTunai,nominal='100000'),
    tombol2='<-- 200.000', aksi2=Function(tarikTunai,nominal='200000'),
    tombol3='<-- 300.000', aksi3=Function(tarikTunai,nominal='300000'),
    tombol4='<-- NOMINAL LAIN', aksi4=[resetEntri(),Show('layarMenuTarikTunaiLain')],
    tombol5='1.000.000 -->', aksi5=Function(tarikTunai,nominal='1000000'),
    tombol6='1.500.000 -->', aksi6=Function(tarikTunai,nominal='1500000'),
    tombol7='2.000.000 -->', aksi7=Function(tarikTunai,nominal='2000000'),
    tombol8='KEMBALI -->', aksi8=Show('layarMenu'))
    
screen layarMenuTarikTunaiLain():
    python:
        global mode, angkaEntri
        mode = 7
        if angkaEntri == '': angkaEntri = '0'
    tag layar
    zorder 80
    use monitor('\nMASUKKAN NOMINAL PENARIKAN#(DALAM KELIPATAN Rp.'+str(persistent.kelipatan)+')#MAKSIMAL Rp.'+str(persistent.maks)+'##Rp.'+str(int(angkaEntri))+'#####TEKAN "BENAR" UNTUK MELANJUTKAN#TEKAN "CANCEL" UNTUK MEMBATALKAN TRANSAKSI')
    use tombol(tombol6='BENAR -->',aksi6=Function(tarikTunai,nominal=str(angkaEntri)),tombol7='KEMBALI -->', aksi7=Show('layarMenu'))

screen layarKodeBank():
    python:
        global mode, halLayarKodeBank, valPenjelasan
        valPenjelasan = 12
        listKodeBank = [[['002 - BRI','002'], ['422 - BRI SYARIAH','422'], ['014 - BCA','014'], ['BCA SYARIAH - 536','536'], ['MANDIRI - 008','008'], ['BNI - 009','009']], [['427 - BNI SYARIAH','427'], ['022 - CIMB NIAGA','022'], ['147 - MUAMALAT','147'], ['BTPN / JENIUS - 213','213'], ['BTPN SYARIAH - 547','547'], ['BTN - 200','200'], ],[['013 - PERMATA','013'], ['011 - DANAMON','011'], ['016 - BII MAYBANK','016'], ['BANK MEGA - 426','426'], ['BUKOPIN - 441','441'], ['CITIBANK - 031','031']]]
        nextHal = [1,2,0]
        selListKodeBank = listKodeBank[halLayarKodeBank]
        mode = 10
    tag layar
    zorder 80
    use monitor('\nDAFTAR KODE DAN NAMA BANK#PILIH SALAH SATU YANG SESUAI BANK TUJUAN ANDA')
    use tombol(tombol1=selListKodeBank[0][0],aksi1=[SetVariable('angkaEntri',selListKodeBank[0][1]),Show('layarMenuTransfer')],
    tombol2=selListKodeBank[1][0],aksi2=[SetVariable('angkaEntri',selListKodeBank[1][1]),Show('layarMenuTransfer')],
    tombol3=selListKodeBank[2][0],aksi3=[SetVariable('angkaEntri',selListKodeBank[2][1]),Show('layarMenuTransfer')],
    tombol4='<-- KEMBALI',aksi4=Show('layarMenuTransfer'),
    tombol5=selListKodeBank[3][0],aksi5=[SetVariable('angkaEntri',selListKodeBank[3][1]),Show('layarMenuTransfer')],
    tombol6=selListKodeBank[4][0],aksi6=[SetVariable('angkaEntri',selListKodeBank[4][1]),Show('layarMenuTransfer')],
    tombol7=selListKodeBank[5][0],aksi7=[SetVariable('angkaEntri',selListKodeBank[5][1]),Show('layarMenuTransfer')],
    tombol8='LAINNYA -->', aksi8=SetVariable('halLayarKodeBank',nextHal[halLayarKodeBank]))
    
screen layarMenuTransfer(hal=0,nama=''):
    python:
        global mode, angkaEntri,valPenjelasan
        mode = 8
        valPenjelasan = 13 if hal == 0 else 14
    tag layar
    zorder 80
    if hal == 0:
        python:
            outEntri = angkaEntri.ljust(16,'_')
        use monitor('\nMOHON MASUKKAN NOMOR REKENING#TUJUAN TRANSFER ANDA DENGAN TELITI#(AWALI KODE BANK, JIKA BANK TUJUAN BERBEDA)##'+outEntri+'#####TEKAN "BENAR" UNTUK MELANJUTKAN#TEKAN "CANCEL" UNTUK MEMBATALKAN TRANSAKSI')
        use tombol(tombol3='<-- KODE BANK', aksi3=Show('layarKodeBank'),tombol6='BENAR -->', aksi6=Function(transfer,rek=angkaEntri),tombol7='KEMBALI -->', aksi7=Show('layarMenu'))
    elif hal == 1:
        $ outEntri = '0' if angkaEntri == '' else angkaEntri
        use monitor('\nMOHON MASUKKAN NOMINAL#YANG AKAN DIKIRIM#(PENERIMA : '+nama+')##Rp.'+str(int(outEntri))+'#####TEKAN "BENAR" UNTUK MELANJUTKAN#TEKAN "CANCEL" UNTUK MEMBATALKAN TRANSAKSI')
        use tombol(tombol6='BENAR -->', aksi6=Function(transfer,nominal=int(outEntri)))
        
screen layarTentang():
    zorder 110
    use monitor('DIBUAT OLEH : ARACHMADI PUTRA##VERSI ATM_OS : [config.version]#VERSI ENGINE : Ren\'Py [renpy.version_only]##PROGRAM INI DIBUAT UNTUK MEMBANTU MEREKA#YANG MASIH AWAM DENGAN PENGGUNAAN#MESIN ATM (ANJUNGAN TUNAI MANDIRI)')
    use tombol(tombol4='<-- CIMOSOFT.COM', aksi4=OpenURL('https://me.cimosoft.com/?ref=atmos'), tombol8='KEMBALI -->', aksi8=Hide('layarTentang'))
    
#blok style font

style fonMonitor:
    font 'gui/fonts/fibm.ttf'
    size 40
    xalign 0.5
    color u'#AAAA00'
    line_spacing 0.1

style fonError:
    font 'gui/fonts/fibm.ttf'
    size 60
    xalign 0.5
    color u'#CCCCCC'
    background '#990000'
    
style fonBanner:
    font 'gui/fonts/f25.ttf'
    size 20
    xalign 0.5
    color u'#FFFFFF'
    
style fonTombol:
    font 'gui/fonts/fjb.ttf'
    size 25
    xalign 0.5
    color '#AAA'
    hover_color '#FFF'
    line_spacing 13
    
style fonPanel:
    font 'gui/fonts/fibm.ttf'
    size 45
    color '#DDDD55'
    hover_color '#FFFF99'
    line_spacing 13
    kerning 3
    xalign 0.5