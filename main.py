import PySimpleGUI as sg
from tkinter import filedialog
import yt_dlp as y_dl

layout =  [
            [sg.Text("フォルダを選択してください", key="folder"), sg.Button("フォルダ選択")],
            [sg.Text("URL"), sg.InputText(key="URL")],
            [sg.Button("ダウンロード開始")]
          ]

def sel_folder():
  fid = filedialog.askdirectory()
  return fid+"/"

def download(path: str, url: str):
  try:
    ydl_op = {
      'format': 'best',
      'outtmpl': path+"%(title)s.mp4"
    }
    with y_dl.YoutubeDL(ydl_op) as ydl:
      ydl.download([url])
      return True
  except:
    return False

def main():
  window = sg.Window("movie downloader", layout)
  f : str = ""
  while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
      break
    elif event == "フォルダ選択":
      f = sel_folder()
      window["folder"].update(f)
    elif event == "ダウンロード開始":
      url : str = values["URL"]
      if len(f) <= 2 and len(url) <= 8:
        sg.popup("フォルダパスまたはURLを確認してください")
        continue
      b = download(f, url)
      if not b:
        sg.popup("ダウンロードに失敗しました")

main()
