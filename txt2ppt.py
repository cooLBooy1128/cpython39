import tkinter
from tkinter import Tk, Label, Entry, Button
from time import sleep
import win32com.client as win32

INDENT = '    '
DEMO = '''
PRESENTATION TITLE
    optional subtitle
slide 1 title
    slide 1 bullet 1
    slide 1 bullet 2
slide 2 title
    slide 2 bullet 1
    slide 2 bullet 2
        slide 2 bullet 2a
        slide 2 bullet 2b
'''


def txt2ppt(lines):
    ppoint = win32.gencache.EnsureDispatch(
        'PowerPoint.Application')
    ppoint.Visible = True
    pres = ppoint.Presentations.Add()
    sleep(2)
    nslide = 1
    for line in lines:
        if not line:
            continue
        linedata = line.split(INDENT)
        if len(linedata) == 1:
            title = (line == line.upper())
            if title:
                stype = win32.constants.ppLayoutTitle
            else:
                stype = win32.constants.ppLayoutText

            s = pres.Slides.Add(nslide, stype)
            ppoint.ActiveWindow.View.GotoSlide(nslide)
            it = iter(s.Shapes)
            next(it).TextFrame.TextRange.Text = line.title()
            body = next(it).TextFrame.TextRange
            nline = 1
            nslide += 1
            sleep((nslide <= 4) and 1 or 0.01)  # 2.5+: sleep(0.5 if nslide <= 4 else 0.01)
        else:
            # print(line)
            line = f'{line.lstrip()}\r\n'
            body.InsertAfter(line)
            para = body.Paragraphs(nline)
            para.IndentLevel = len(linedata) - 1
            nline += 1
            sleep((nslide <= 4) and 1 or 0.01)  # 2.5+: sleep(0.25 if nslide <= 4 else 0.01)

    s = pres.Slides.Add(nslide, win32.constants.ppLayoutTitle)
    ppoint.ActiveWindow.View.GotoSlide(nslide)
    it = list(s.Shapes)
    it[0].TextFrame.TextRange.Text = "It's time for a slideshow!".upper()
    sleep(1.)
    for i in range(3, 0, -1):
        it[1].TextFrame.TextRange.Text = str(i)
        sleep(1.)

    pres.SlideShowSettings.ShowType = win32.constants.ppShowTypeSpeaker
    pres.SlideShowSettings.Run()
    pres.ApplyTemplate(r'D:\Microsoft Office\ppt\templates\ClassicPhotoAlbum.potx')
    it[0].TextFrame.TextRange.Text = 'FINIS'
    it[1].TextFrame.TextRange.Text = ''


def _start(ev=None):
    fn = en.get().strip()
    try:
        f = open(fn)
    except IOError as e:
        from io import StringIO
        f = StringIO(DEMO)
        en.delete(0, 'end')
        if fn.lower() == 'demo':
            en.insert(0, fn)
        else:
            import os
            en.insert(0,
                      r"DEMO (can't open %s: %s)" % (
                          os.path.join(os.getcwd(), fn), str(e)))
        en.update_idletasks()
    txt2ppt(line.rstrip() for line in f)
    f.close()


if __name__ == '__main__':
    tk = Tk()
    lb = Label(tk, text='Enter file [or "DEMO"]:')
    lb.pack()
    en = Entry(tk)
    en.bind('<Return>', _start)
    en.pack(fill=tkinter.BOTH, expand=True)
    en.focus_set()
    quit_ = Button(tk, text='QUIT', command=tk.quit, fg='white', bg='red')
    quit_.pack(fill=tkinter.BOTH)
    tk.mainloop()
