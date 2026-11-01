# Distributed Digit Relay (Turtlesim) - Kelompok 3

Tugas kelompok ROS2: delapan node menggambar angka secara bergantian di `turtlesim`. Giliran diatur otomatis lewat topic, tanpa intervensi manual atau hardcoded delay.

## Anggota kelompok

| Member | Nama | NRP |
|---|---|---|
| 1 | Ferri Adi Prasetya | 5054241019 |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |
| 7 | | |
| 8 | | |

## Tugas yang diminta

Sistem berjalan tepat 2 siklus, lalu berhenti (node masuk ke state idle):

1. **Siklus 1:** Anggota 1–8 menggambar angka 1–8 di slot masing-masing.
2. **Transisi:** giliran kembali ke Anggota 1, yang memanggil service `/clear`.
3. **Siklus 2:** Anggota 1–8 menggambar angka 9–16 di slot yang sama.

Ketentuan utama:

- Setiap anggota memakai warna pena berbeda melalui `/turtle1/set_pen`.
- Pena diangkat saat kura-kura berpindah antar-slot.
- Angka tidak boleh menabrak dinding kanvas atau tumpang tindih.
- Node tetap idle sampai gilirannya tiba.
- Seluruh sistem berjalan dengan satu perintah launch.
- Git commit history mencerminkan kontribusi tiap anggota.

## Pembagian tugas

| Anggota | File | Warna | Slot (kiri-bawah) | Angka | Digit yang dibuat |
|---|---|---|---|---|---|
| 1 | `digit_relay/member_1.py` | Merah | (0.8, 7.8) | 1, 9 | 1, 9 |
| 2 | `digit_relay/member_2.py` | Hijau | (4.0, 7.8) | 2, 10 | 2, 1, 0 |
| 3 | `digit_relay/member_3.py` | Hitam | (7.2, 7.8) | 3, 11 | 3, 1 |
| 4 | `digit_relay/member_4.py` | Kuning | (0.8, 4.5) | 4, 12 | 4, 1, 2 |
| 5 | `digit_relay/member_5.py` | Putih | (4.0, 4.5) | 5, 13 | 5, 1, 3 |
| 6 | `digit_relay/member_6.py` | Cyan | (7.2, 4.5) | 6, 14 | 6, 1, 4 |
| 7 | `digit_relay/member_7.py` | Magenta | (2.4, 1.2) | 7, 15 | 7, 1, 5 |
| 8 | `digit_relay/member_8.py` | Oranye | (5.6, 1.2) | 8, 16 | 8, 1, 6 |

Anggota 1 juga menyiapkan repo, package, `digit_relay/relay_base.py`, dan `launch/relay.launch.py`, serta memulai relay dan membersihkan kanvas.

Anggota 2–8 mengganti `BOX` di file masing-masing dengan bentuk digit. Koordinat digit memakai rentang x 0–1 dan y 0–2, dengan (0, 0) di kiri bawah. Setiap `[...]` di dalam digit adalah satu garis tanpa mengangkat pena:

```python
DIGITS = {
    '7': [[(0, 2), (1, 2), (0.4, 0)]],
}
```

## Cara kerja

Node berkomunikasi lewat topic `/relay_turn` bertipe `std_msgs/Int32MultiArray`, dengan format `data = [current_number, active_member]`. Setelah selesai menggambar, node mengirim token ke anggota berikutnya. Setelah angka 16, token tidak dikirim lagi sehingga semua node idle.

## Cara menjalankan

Kebutuhan: ROS2 Jazzy, `turtlesim`, dan `colcon`.

```bash
sudo apt install ros-jazzy-desktop python3-colcon-common-extensions
```

Jalankan dari root repo. Kalau memakai zsh, ganti `setup.bash` dengan `setup.zsh`:

```bash
source /opt/ros/jazzy/setup.bash
export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST
colcon build --symlink-install
source install/setup.bash
ros2 launch digit_relay relay.launch.py
```

Untuk melihat token giliran, buka terminal lain dan jalankan `source install/setup.bash`, lalu:

```bash
ros2 topic echo /relay_turn
```

Tekan Ctrl+C untuk menghentikan sistem.
