import os
import shutil

num = 425

for n in range(1,num+1):
    # 対象ディレクトリ（必要に応じて変更）
    n = str(n)
    if len(n)==1:
        n = '00'+n
    elif len(n)==2:
        n = '0'+n
    target_dir = r"./atcoder/ABC"+n

    # ディレクトリ内のファイル一覧
    files = os.listdir(target_dir)

    # 拡張子なしファイルと.pyファイルを探す
    for file in files:
        file_path = os.path.join(target_dir, file)
        
        # 拡張子なしファイルかつ通常ファイルであること
        if os.path.isfile(file_path) and '.' not in file:
            py_file = file + '.py'
            py_path = os.path.join(target_dir, py_file)
            
            # 対応する.pyファイルが存在する場合
            if os.path.exists(py_path):
                # 内容をコピー
                with open(file_path, 'r', encoding='utf-8') as f_src:
                    content = f_src.read()
                with open(py_path, 'w', encoding='utf-8') as f_dst:
                    f_dst.write(content)
                
                # 拡張子なしファイルを削除
                os.remove(file_path)
                print(f"Copied {file} to {py_file} and deleted {file}")
