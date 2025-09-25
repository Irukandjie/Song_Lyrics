import os
import sys
import time
import datetime
from colorama import init, Fore, Style

# Inisialisasi Colorama
init(autoreset=True)

# Data Lirik "Too Soon" - Joji
LYRICS_DATA = [
    {'text': "Drank too much, got the sickness", 'duration': 3000},
    {'text': "Pray to God and his son for forgiveness", 'duration': 3000},
    {'text': "Same crew but another mistress", 'duration': 2500},
    {'text': "Every day, every night getting wasted", 'duration': 3000},
    {'text': "But I miss you, what did I do?", 'duration': 2500},
    {'text': "Fuck it up, laugh it off, and I lost you", 'duration': 2500},
    {'text': "If I pull through, is it too soon?", 'duration': 2500},
    {'text': "Turn it up, close my eyes, then I'm with you", 'duration': 3000}
]

# --- PENGATURAN TAMPILAN ---
BOX_WIDTH = 70
LYRIC_DISPLAY_HEIGHT = 5
ANIMATION_SPEED = 0.008 
WIPE_HEAD = "█▓▒░"

# Komponen bingkai
TOP_BORDER = Fore.BLUE + "╔" + "═" * (BOX_WIDTH - 2) + "╗"
SIDE_BORDER = Fore.BLUE + "║"
BOTTOM_BORDER = Fore.BLUE + "╚" + "═" * (BOX_WIDTH - 2) + "╝"
SEPARATOR = Fore.BLUE + "╟" + "─" * (BOX_WIDTH - 2) + "╢"

def clear_screen():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_boxed(text, color="", style="", align="center"):
    """Fungsi untuk mencetak teks di dalam bingkai dengan perataan."""
    if align == "center":
        padded_text = text.center(BOX_WIDTH - 4)
    elif align == "left":
        padded_text = text.ljust(BOX_WIDTH - 4)
    elif align == "right":
        padded_text = text.rjust(BOX_WIDTH - 4)
    print(f"{SIDE_BORDER} {style}{color}{padded_text}{Style.RESET_ALL} {SIDE_BORDER}")

def create_progress_bar(current, total, width=50):
    """Membuat string untuk progress bar."""
    percent = current / total
    filled = int(width * percent)
    bar = '█' * filled + '░' * (width - filled)
    return f"[{bar}] {current}/{total}"

def display_ui(current_line_index, status_text):
    """Menampilkan antarmuka karaoke yang baru."""
    clear_screen()
    
    # Header
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    header_text = f"♫ SPOTIFY CHRST ♫{current_time.rjust(BOX_WIDTH - 25)}"
    print(TOP_BORDER)
    print_boxed(header_text, Fore.CYAN, Style.DIM, align="left")
    print(SEPARATOR)
    print_boxed("Keshi - 2 Soon", Fore.WHITE, Style.NORMAL)
    print_boxed(status_text, Fore.MAGENTA, Style.DIM)
    print(SEPARATOR)

    # Area Lirik dengan efek "Running Text"
    lyric_lines_to_show = []
    start_index = current_line_index - (LYRIC_DISPLAY_HEIGHT // 2)
    
    for i in range(LYRIC_DISPLAY_HEIGHT):
        line_index = start_index + i
        is_active = (line_index == current_line_index)
        
        # Logika baru untuk "Running Text"
        if 0 <= line_index < len(LYRICS_DATA):
            if line_index < current_line_index: # Lirik yang sudah lewat
                lyric_lines_to_show.append({'text': LYRICS_DATA[line_index]['text'], 'type': 'past'})
            elif is_active: # Lirik aktif
                lyric_lines_to_show.append({'text': LYRICS_DATA[line_index]['text'], 'type': 'active'})
            else: # Lirik yang akan datang (disembunyikan)
                lyric_lines_to_show.append({'text': '...', 'type': 'future'})
        else:
            lyric_lines_to_show.append({'text': '', 'type': 'empty'})

    for line in lyric_lines_to_show:
        if line['type'] == 'past':
            print_boxed(line['text'], Fore.WHITE, Style.DIM)
        elif line['type'] == 'active':
            # Kosongkan tempat untuk diisi animasi
            print_boxed("", Fore.WHITE, Style.DIM)
        else: # future atau empty
            print_boxed(line['text'], Fore.BLUE, Style.DIM)
            
    # Progress Bar
    progress_bar_str = create_progress_bar(current_line_index + 1, len(LYRICS_DATA), width=BOX_WIDTH - 15)
    print(SEPARATOR)
    print_boxed(progress_bar_str, Fore.GREEN)
    
    # Footer
    print(BOTTOM_BORDER)
    print(Fore.BLUE + "♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫".center(BOX_WIDTH))


def run_gradient_wipe_animation(line_text):
    padded_text = line_text.center(BOX_WIDTH - 4)
    animation_duration = 0
    
    for i in range(len(padded_text) + len(WIPE_HEAD)):
        full_line = ""
        for j in range(len(padded_text)):
            gradient_index = i - j
            if 0 <= gradient_index < len(WIPE_HEAD):
                full_line += WIPE_HEAD[gradient_index]
            elif j < i:
                full_line += padded_text[j]
            else:
                full_line += " "
        
        print(f"{SIDE_BORDER} {Style.BRIGHT}{Fore.YELLOW}{full_line}{Style.RESET_ALL} {SIDE_BORDER}", end="\r")
        time.sleep(ANIMATION_SPEED)
        animation_duration += ANIMATION_SPEED

    return animation_duration

def run_karaoke():
    for i in range(3, 0, -1):
        display_ui(-1, f"Mulai dalam {i}...")
        time.sleep(1)

    for index, line_data in enumerate(LYRICS_DATA):
        display_ui(index, f"🎤 Now Playing...")
        active_line_text = f"~ {LYRICS_DATA[index]['text']} ~"
        
        num_lines_up = (LYRIC_DISPLAY_HEIGHT // 2) + 4 # Disesuaikan dengan layout baru
        sys.stdout.write(f'\x1b[{num_lines_up}A\r')

        animation_duration = run_gradient_wipe_animation(active_line_text)
        
        sys.stdout.write(f'\x1b[{num_lines_up}B\r')

        remaining_duration = (line_data['duration'] / 1000) - animation_duration
        if remaining_duration > 0:
            time.sleep(remaining_duration)

    display_ui(len(LYRICS_DATA), "Selesai.")
    print("\n" + "♪ TERIMA KASIH ♫".center(BOX_WIDTH))


def main():
    while True:
        clear_screen()
        print(TOP_BORDER)
        print_boxed("Selamat Datang!", Fore.CYAN, Style.DIM)
        print_boxed("Lagu saat ini: Keshi - 2 Soon", Fore.WHITE, Style.NORMAL)
        print(BOTTOM_BORDER)
        
        try:
            input(Fore.YELLOW + "\nTekan ENTER untuk memulai...")
            run_karaoke()
        except KeyboardInterrupt:
            print("\n...Keluar.")
            break

        ulangi = input("\nUlangi lagi? (y/n): ").lower()
        if ulangi != 'y':
            break

    print(Fore.CYAN + "\nSampai jumpa.")

if __name__ == "__main__":
    main()
