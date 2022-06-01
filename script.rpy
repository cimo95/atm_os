image bg blck = "#000000"

define listPenjelasan = [
'Selamat datang di ATM_OS, Aplikasi Simulator ATM\n\nPIN Anda saat ini : 123456\n\nPilih "MASUKKAN KARTU SIM" terlebih dahulu, lalu...\nMasukkan pin dengan menekan tombol angka pada gambar.\nGunakan "CANCEL" untuk membatalkan transaksi\nGunakan "CORRECTION" untuk menghapus entri jika salah\nGunakan "ACCEPT" untuk menyetujui.',
'{b}Transaksi telah selesai{/b}\n\nKetika tampilan ini muncul, seluruh transaksi yang Anda lakukan sudah selesai.\nJangan lupa untuk mengambil kartu ATM Anda.',
'{b}Transaksi dimulai{/b}\n\nKetika tampilan ini muncul, Anda bisa memasukkan kartu ATM Anda, sebelum memulai transaksi. Pastikan kartu ATM tidak terbalik (posisi kartu ATM bagian depan, menghadap keatas, dengan sisi kiri kartu ATM menghadap lubang kartu).',
#'{b}{/b}\n\n'
'{b}MASUKKAN PIN{/b}\n\nAnda diminta untuk memasukkan nomor PIN (biasanya sebanyak 6 angka).\nAnda harus memasukkan nomor PIN dengan teliti.\n{b}3x (tiga kali){/b} salah memasukkan nomor PIN, kartu ATM Anda akan terblokir, dan Anda harus menghubungi bank Anda untuk membuka blokirnya.',
'{b}KARTU ATM Anda TERBLOKIR{/b}\n\nAnda harus segera menghubungi bank Anda (bank dimana Anda mengurus kartu ATM Anda) untuk membuka blokirnya.\nKetika kartu ATM terblokir, Anda tidak dapat melakukan aktivitas transaksi apapun menggunakan kartu tersebut.\n\nDalam simulasi ini, Anda bisa membuka blokir melalui menu ATUR SIMULATOR.',
'{b}ATUR SIMULATOR{/b}\n\nUbah parameter simulator sesuai dengan kebutuhan Anda,\ndengan memilih salah satu dari 7 (tujuh) pilihan.\n\n{b}SALDO{/b} : Mengubah nominal saldo yang Anda miliki\n{b}SALDO MINIMAL{/b} : Mengubah minimal saldo yang harus tertinggal dan minimal jumlah yang bisa di transaksikan.\n{b}MAKS PENARIKAN{/b} : Mengubah nominal saldo maksimal yang diperbolehkan\ndalam sekali transaksi\n{b}KELIPATAN{/b} : Mengubah nominal kelipatan transaksi yang bisa digunakan (20 ribu, 50 ribu, atau 100 ribu)\n{b}BUKA BLOKIR{/b} : Membuka blokir simulasi ATM Anda\n{b}SIM. PROSES{/b} : Mengaktifkan / mematikan simulasi tampilan proses transaksi\n{b}RESET{/b} : Mengembalikan seluruh pengaturan ke nilai awal, dimana Anda pertama kali menggunakan ATM_OS',
'{b}MENU TRANSAKSI{/b}\n\nDaftar stAndar fitur transaksi yang ada pada mesin ATM.\nMesin ATM lain mungkin juga memiliki menu fitur transaksi tambahan.\n\n{b}GANTI PIN{/b} : Ubah PIN Anda.\n{b}INFORMASI SALDO{/b} : Menampilkan jumlah saldo yang Anda miliki saat ini.\n{b}TARIK TUNAI{/b} : Mengambil uang Anda.\n{b}TRANSFER{/b} : Mengirim saldo Anda ke rekening lain. (Pada simulator ini, daftar rekening penerima bisa Anda lihat di\n'+config.basedir.replace('/','\\' if renpy.windows else '/')+'rekening.txt',
'{b}GANTI PIN : PIN LAMA{/b}\n\nAnda diminta memasukkan PIN lama Anda.\nPIN lama adalah PIN yang Anda gunakan untuk masuk saat ini.\nIni berguna untuk memastikan, bahwa yang melakukan perubahan ini adalah benar-benar Anda, atau yang mengetahui PIN Anda.',
'{b}GANTI PIN : PIN BARU{/b}\n\nAnda diminta memasukkan PIN baru Anda.\nDi beberapa bank, untuk alasan keamanan, Anda tidak boleh menggunakan PIN yang terlalu mudah, seperti deretan angka berulang, angka urut, atau angka simetris (seperti : 123321).',
'{b}GANTI PIN : KONFIRMASI PIN BARU{/b}\n\nAnda diminta memasikkan PIN baru sekali lagi.\nIni berguna untuk memastikan, bahwa Anda tidak melakukan kesalahan dalam memasukkan nomor PIN (misal : salah tekan tombol angka).',
'{b}INFORMASI SALDO{/b}\n\nSaldo / jumlah uang yang Anda miliki akan ditampilkan disini',
'{b}TARIK TUNAI{/b}\n\nPilih nominal yang akan Anda ambil, atau pilih NOMINAL LAIN untuk memasukkan jumlah nominal sesuai kebutuhan Anda.\nDalam proses TARIK TUNAI, Anda tidak dapat menarik keseluruhan uang Anda. Biasanya, bank akan {i}menahan{/i} sebagian kecil saldo Anda, untuk biaya administrasi bulanan ATM.',
'{b}DAFTAR KODE BANK{/b}\n\nMenampilkan nama dan kode bank yang digunakan, jika Anda ingin mengirim uang ke penerima dengan bank yang berbeda (misal : dari BCA ke BANK MANDIRI).\nBeberapa bank tidak menyediakan menu daftar kode bank ini.\nJadi, lebih baik Anda mencari tahu terlebih dulu, kode bank tujuan Anda.',
'{b}TRANFER : NO. REKENING TUJUAN{/b}\n\nAnda diminta memasukkan nomor rekening penerima.\nPanjang nomor rekening tiap bank berbeda-beda,\nAnda harus menambahkan kode bank diikuti nomor rekening penerima, jika bank milik penerima berbeda dengan bank Anda.',
'{b}TRANSFER : NOMINAL{/b}\n\nAnda diminta memasukkan nominal uang yang akan dikirim.\nPastikan jumlah saldo cukup. Biaya transfer akan dikenakan ke pengirim (Anda) dengan memotong dari saldo Anda saat ini.',
'{b}KONFIRMASI PENYELESAIAN{/b}\n\nSetiap selesai transaksi, Anda akan diminta konfirmasi apakah ingin melanjutkan transaksi atau tidak.\nBeberapa jenis transaksi di beberapa bank meminta Anda untuk memasukkan PIN kembali, setiap Anda ingin melanjutkan transaksi.'
]

define teksRekening = '# ini adalah sampel daftar rekening\n# anda bisa menambahkan data sesuai keinginan\n# ikuti format simulasi nomor rekening sbb :\n# NOMOR REKENING;BANK;NAMA TUJUAN\n\n# contoh rekening beda bank (bank pada simulator bernama BOI)\n7894561230147369;BCA;ARACHMADI PUTRA\n\n# contoh rekening bank yang sama\n4567891230;BOI;AURELIA NOUMI'

label start:       
    $ quick_menu = False
    scene bg blck with dissolve
    call screen layarAwal
    return
