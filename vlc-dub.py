import os, sys, subprocess
"""
Инпуты:
python main.py <dir_video> <dir_dub>

Возможно ли формировать плейлист таким образом? Да. Передаём список и к каждому элементу подставляем :input-slave="file:///..."
1. Пройтись по папке-инпуту и найти все видео в нужных форматах
2. отсортировать их по имени
3. Пройтись по каждому:
3.1. Получить имя
3.2. Найти в папке даба файл с таким же названием
3.3. суффиксы?/префиксы? Добавить оба?
4. Соединить
5. Исполнить
"""
ALLOWED_EXT = [".mp4",".mov"]
ALLOWED_DUB_EXT = [".mp3",".ogg",".wav",".m4a",".flac"]
vlc_path = os.path.abspath(r"C:\Program Files\VideoLan\VLC\vlc.exe")

if len(sys.argv) < 2:
    print("Provide at least the folder with videos")
    quit()
elif len(sys.argv) < 3:
    input_folder = os.path.abspath(sys.argv[1])
    slave_folder = os.path.abspath(sys.argv[1])
else:
    input_folder = os.path.abspath(sys.argv[1])
    slave_folder = os.path.abspath(sys.argv[2])


slave_gen = list(os.walk(slave_folder))
inputs = []
slaves = []
i=-1
for element in os.walk(input_folder):
    # print(element)
    dir, subdir, files = element
    for file in files:
        name, ext = os.path.splitext(file)
        if ext in ALLOWED_EXT:
            inputs.append(os.path.join(dir,file))
            slaves.append([])
            i+=1
            for slave_emlement in slave_gen:
                slave_dir, _ , slave_files = slave_emlement
                for a in slave_files:
                    if name in a and os.path.splitext(a)[1] in ALLOWED_DUB_EXT:
                        slaves[i].append("file:///"+os.path.join(slave_dir,a))
                        break
args = [vlc_path]
for i in range(len(inputs)):
    vid = f"file:///{inputs[i]}"
    dubs = ":input-slave=" + "#".join(slaves[i])
    args.extend([vid,dubs])
subprocess.run(args)
