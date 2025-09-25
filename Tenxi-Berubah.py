import os
import time
from colorama import init, Fore, Style

# Inisialisasi Colorama
init(autoreset=True)

# Data Lirik dengan durasi yang sudah diperlambat
# Nilai duration telah ditambah agar tempo lebih lambat
LYRICS_DATA = [
    {'text': "Jangan nyesel semua problem kamu yang start", 'duration': 3500},
    {'text': "Jangan minta rewind aku kamu udah finish", 'duration': 3300},
    {'text': "Pasang mata sinis, mata jadi gerimis", 'duration': 3700},
    {'text': "Emang paling narsis", 'duration': 1500},
    {'text': "Apa kita udahan? Kok kamu masih nanya?", 'duration': 3200},
    {'text': "Mendengarmu membual banyak nyanya-nyanya", 'duration': 3500},
    {'text': "Kau main belakang, enggak usah pakai lama", 'duration': 3800},
    {'text': "Cuma gitu aku juga bisa", 'duration': 3000},
    {'text': "Sudah selesai, cerita pun berakhir", 'duration': 3500},
    {'text': "Kau yang memulai memang penulis mahir", 'duration': 3200},
    {'text': "Ku tak mau mengulang, i said no no not again", 'duration': 3500},
    {'text': "Jangan follow aku lagi, aku udah enggak naksir", 'duration': 3700},
    {'text': "Hey... hey...", 'duration': 2000},
    {'text': "Belaga buta, tapi tak pernah lupa", 'duration': 3500},
    {'text': "Kamu mendua, jadi aku bertiga", 'duration': 3500},
    {'text': "Masih terasa, mata balas mata", 'duration': 3500},
    {'text': "Tak mau terluka, jadi aku berubah", 'duration': 3500},
    {'text': "Aku berubah...", 'duration': 2000},
    {'text': "Aku berubah...", 'duration': 2000},
]

def clear_screen():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_ui(current_line_index, status_text):
    """Menampilkan antarmuka karaoke di terminal."""
    clear_screen()
    
    # Header
    print(Fore.CYAN + "=" * 60)
    print(Fore.CYAN + " " * 18 + "KARAOKE PLAYER TERMINAL")
    print(Fore.CYAN + "=" * 60)
    print("\n")
    print(Style.BRIGHT + Fore.WHITE + "Tenxi - Berubah".center(60))
    print(Fore.YELLOW + status_text.center(60))
    print("\n" + "-" * 60 + "\n")

    # Menampilkan 5 baris lirik (2 sebelum, 1 aktif, 2 sesudah)
    start = max(0, current_line_index - 2)
    end = min(len(LYRICS_DATA), current_line_index + 3)

    for i in range(start, end):
        line = LYRICS_DATA[i]['text']
        if i == current_line_index:
            # Baris aktif: warna kuning cerah dan ada penanda
            print(Style.BRIGHT + Fore.YELLOW + f"▶ {line}".center(60))
        else:
            # Baris tidak aktif: warna redup
            print(Style.DIM + Fore.WHITE + line.center(60))
    
    print("\n" + "-" * 60)


def run_karaoke():
    """Fungsi utama untuk menjalankan logika karaoke."""
    # Hitung mundur sebelum mulai
    for index, line_data in enumerate(LYRICS_DATA):
        display_ui(index, "Now Playing...")
        time.sleep(line_data['duration'] / 1000)

    # Tampilan setelah selesai
    display_ui(-1, "Karaoke Selesai!")
    print("\n" + "Terima kasih!".center(60))


def main():
    """Fungsi pembungkus untuk mengelola program."""
    while True:
        clear_screen()
        print(Fore.GREEN + "Selamat Datang di Karaoke Terminal!")
        try:
            input(Fore.YELLOW + "\nTekan ENTER untuk memulai karaoke...")
            run_karaoke()
        except KeyboardInterrupt:
            print("\nKaraoke dihentikan.")
            break

        # Opsi untuk mengulang
        ulangi = input("\nApakah Anda ingin mengulang? (y/n): ").lower()
        if ulangi != 'y':
            break

    print(Fore.CYAN + "\nProgram ditutup. Sampai jumpa!")


if __name__ == "__main__":
    main()
