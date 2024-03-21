from tkinter import *
import pyautogui as p
from pyperclip import copy as pcopy
from os import startfile, makedirs, environ, path
from tkinter.messagebox import showinfo, showerror
from tkinter.simpledialog import askstring
from random import choice
from pyvda import AppView

#### default funcs

def able():
	global able_state
	if b3["state"]==DISABLED:
		root.title(f"Volume_Panel")
		b3.config(state=NORMAL)
		b4.config(state=NORMAL)
		b3.bind("<Enter>", lambda e: b3.config(background="lightgreen", foreground="black"))
		b3.bind("<Leave>", lambda e: b3.config(background="green", foreground="white"))
		b4.bind("<Enter>", lambda e: b4.config(background="lightgreen", foreground="black"))
		b4.bind("<Leave>", lambda e: b4.config(background="green", foreground="white"))
		b.bind(f"<Escape>", lambda e:scrn_move('e', side="left"))
		b.bind(f"<`>", lambda e:scrn_move('e', side="right"))
	else:
		root.title(f"{firstword} {lastword}")
		b3.config(state=DISABLED)
		b4.config(state=DISABLED)
		b3.unbind("<Enter>")
		b3.unbind("<Leave>")
		b4.unbind("<Enter>")
		b4.unbind("<Leave>")
		b.unbind("<`>")
		b.unbind("<Escape>")

def ss_here():
	from tkinter.filedialog import asksaveasfile
	pic = p.screenshot()
	files = [('PNG Image', '*.png'), ('Jpg File', '*.jpg'), ('Other', '*.*')]
	file = asksaveasfile(filetypes = files, defaultextension = files)
	# print(file.name)
	if file != None:
		try:
			pic.save(file.name)
			showinfo("Image Saved", f"Image Saved at {file.name}")
		except:
			pass

def adjust(e):
	b2["height"] = (root.winfo_height() - 15)/2
	b["height"] = b2["height"]
	b3["height"], b4["height"] = root.winfo_height(), root.winfo_height()
	b3["width"], b4["width"] = root.winfo_width()/4, root.winfo_width()/4
	b["width"], b2["width"] = root.winfo_width()/2, root.winfo_width()/2

def malert(e=None):
	root.iconify()
	media_pauseplay(pspl=False)

def volume(e, side, times=1):
	for x in range(times):
		p.press("volume"+side)

def scrn_move(e, side="left"):
	if side == "left":
		media_pauseplay(togl=False, pspl=True)
		# startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\HideVolumeOSD\Hide VolumeOSD.lnk')
	elif side == "right":
		pass
		# startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\HideVolumeOSD\Show VolumeOSD.lnk')
	p.hotkey('ctrl', 'win', side)

def scrnmove_mousewhell(e="None"):
	p.hotkey('ctrl', 'win', "left")
	if e.delta > 0:
		pass
	elif e.delta < -100:
		pass
		# startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\HideVolumeOSD\Hide VolumeOSD.lnk')
	print(e)

def random_title(e=None):
	global firstword
	global lastword
	firstword = choice(firstword_list)
	lastword = choice(lastword_list)
	root.title(f"{firstword} {lastword}")

def manual_title(changing):
	def ok_click(e=None):
		if changing == "foreword" :
			global firstword
			firstword = inp_word.get()
		else:
			global lastword
			lastword = inp_word.get()
		ttl_popup.destroy()
		root.title(f"{firstword} {lastword}")
	fore = Wm.wm_title(root).split(" ")[0]
	hind = Wm.wm_title(root).split(" ")[1]

	ttl_popup = Toplevel(root)
	ttl_popup.title(f"Change {changing}")
	ttl_popup.iconbitmap(r"C:\Windows\System32\control.exe")
	ttl_popup.geometry("340x100")
	ttl_popup.attributes('-topmost', True)

	inp_word = Entry(ttl_popup, text=fore+hind, width=25, selectbackground="green")
	inp_word.delete(0, END)
	if changing == "foreword":
		inp_word.insert(END, f'{fore}')
	else:
		inp_word.insert(END, f'{hind}')
	inp_word.pack(pady=10)
	inp_word.focus_set()

	btn_grp = Frame(ttl_popup)
	btn_grp.pack(side=BOTTOM, pady=10)

	btn_ok = Button(btn_grp, text="OK", command=ok_click, width=75, height=100, **btnargs)
	btn_ok.pack(side=LEFT, padx=5)
	btn_ok = Button(btn_grp, text="Cancel", command=ttl_popup.destroy, width=75, height=100, **btnargs)
	btn_ok.pack(side=RIGHT, padx=5)

	inp_word.bind("<Return>", ok_click)

	ttl_popup.mainloop()

def rpc():
	from pypresence import Presence
	from time import time as now
	import json

	terminal.destroy()
	rpcgui = Toplevel(root)
	rpcgui.iconbitmap(r"C:\Users\PVER\AppData\Local\Discord/app.ico")
	rpcgui.title("RPC Editor")
	rpcgui.config(bg="green")

	def value(truval=False):
		CLIENT_ID = client_entry.get()
		STATE = state_entry.get()
		DETAILS = det_entry.get()
		START = str_entry.get()
		END = end_entry.get()
		LIMAGE = Limg_entry.get()
		SIMAGE = Simg_entry.get()
		LTXT = Ltxt_entry.get()
		STXT = Stxt_entry.get()
		PSIZE = partysize_entry.get()
		PMAX = partymax_entry.get()
		B1TXT = btn1_entry.get()
		B1URL = url1_entry.get()
		B2TXT = btn2_entry.get()
		B2URL = url2_entry.get()

		if CLIENT_ID == "":
			CLIENT_ID = "935585892033265764"
		if STATE == "":
			STATE = None
		if DETAILS == "":
			DETAILS = None
		if START == "":
			START = None
		elif START == "Now":
			START = now()
		if END == "":
			END = None
		if LIMAGE == "":
			LIMAGE = None
		if SIMAGE == "":
			SIMAGE = None
		if LTXT == "":
			LTXT = None
		if STXT == "":
			STXT = None

		def calc_party():
			if PSIZE == "" or PMAX == "":
				PARTY = None
			else:
				PARTY = [int(PSIZE), int(PMAX)]
			return PARTY

		def calc_btns():
			BUTTONS = []
			URL1 = not (B1TXT == "" or B1URL == "")
			URL2 = not (B2TXT == "" or B2URL == "")
			if URL1:
				BUTTONS.append({"label":B1TXT, "url":B1URL})
			if URL2:
				BUTTONS.append({"label":B2TXT, "url":B2URL})
			if len(BUTTONS) == 0:
				BUTTONS = None
			return BUTTONS

		if truval:
			return {"client_id":CLIENT_ID, "state":STATE, "details":DETAILS, "start":START, "end":END, "large_text":LTXT, "small_text":STXT, "large_image":LIMAGE, "small_image":SIMAGE, "party_size":calc_party(), "buttons":calc_btns()}
		else:
			return {"CLIENT_ID":CLIENT_ID, "STATE":STATE, "DETAILS":DETAILS, "START":START, "END":END, "LTXT":LTXT, "STXT":STXT, "LIMAGE":LIMAGE, "SIMAGE":SIMAGE, "PARTY":calc_party(), "BUTTONS":calc_btns()}

	def rpcRun():
		global RPC_handler
		try:
			RPC_handler = Presence(client_id=value()["CLIENT_ID"])
			RPC_handler.connect()
			RPC_handler.update(state=value()["STATE"], details=value()["DETAILS"], start=value()["START"], end=value()["END"],
				large_image=value()["LIMAGE"], small_image=value()["SIMAGE"], party_size=value()["PARTY"],
				buttons = value()["BUTTONS"], large_text=value()["LTXT"],small_text=value()["STXT"])
			showinfo("Rich Presence", "Rich Presence has Started.")
		except Exception as e:
			showerror("RPC Error", e)

	def rpcExmpl(client_id = "872466409240801341", state = "Viewing", details = "Custom RPC",
		start = str(int(now())), end = str(int(now())+120), large_image = "big_img", small_image = "css_bg",
		large_text = "Cluster Series", small_text = "Busy", party_size = [1, 1],
		buttons = [{"label": "Github", "url": "https://github.com/PVER-Programz"}, {"label": "CSs Bot", "url": "https://discord.com/oauth2/authorize?client_id=872466409240801341&permissions=549755813887&scope=bot"}]):
		entrys = [client_entry, state_entry, det_entry, str_entry, end_entry, Limg_entry, Simg_entry, Ltxt_entry, Stxt_entry, partysize_entry, partymax_entry, btn1_entry, url1_entry, btn2_entry, url2_entry]
		for x in entrys:
			x.delete(0,END)
		client_entry.insert(0, client_id)
		state_entry.insert(0, state)
		det_entry.insert(0, details)
		str_entry.insert(0, start)
		end_entry.insert(0, end)
		Limg_entry.insert(0, large_image)
		Simg_entry.insert(0, small_image)
		Ltxt_entry.insert(0, large_text)
		Stxt_entry.insert(0, small_text)
		partysize_entry.insert(0, str(party_size[0]))
		partymax_entry.insert(0, str(party_size[1]))
		btn1_entry.insert(0, buttons[0]["label"])
		url1_entry.insert(0, buttons[0]["url"])
		btn2_entry.insert(0, buttons[1]["label"])
		url2_entry.insert(0, buttons[1]["url"])

	def rpcLoad():
		idname = askstring("RPC ID", "Enter RPC id")
		c = 0
		entrys = [client_entry, state_entry, det_entry, str_entry, end_entry, Limg_entry, Simg_entry, Ltxt_entry, Stxt_entry, partysize_entry, partymax_entry, btn1_entry, url1_entry, btn2_entry, url2_entry]
		with open(f"{appdir}/rpcData.PVER", "r") as f:
			for x in f.read().split("\n"):
				try:
					y = json.loads(x)
				except:
					showerror("ID Not found", f"The id '{idname}' doesn't exist")
				if y['idname'] == idname:
					for x in entrys:
						x.delete(0,END)
					y.pop("idname")
					rpcExmpl(**y)
					break

	def rpcSave():
		idname = askstring("RPC ID", "Enter RPC id")
		with open(f"{appdir}/rpcData.PVER", "r") as f:
			if idname + " = {'client_id': '" in f.read():
				showerror("ID exists", f"The id '{idname} already exists")
			else:
				with open(f"{appdir}/rpcData.PVER", "a") as f:
					jason = value(True)
					jason['idname'] = idname
					f.write(str(jason).replace("'", '"') + "\n")
				showinfo("Saved", f"{idname} saved.")
		try:
			makedirs(appdir)
		except FileExistsError:
			pass
		# print(value(True))

	def rpcStop():
		RPC_handler.close()
		showinfo("Rich Presence", "Rich Presence has been Killed.")

	rpc_menu = Menu(root)
	rpc_menu.add_command(label="Run", command=rpcRun)
	rpc_menu.add_command(label="Save", command=rpcSave)
	rpc_menu.add_command(label="Example", command=rpcExmpl)

	loadmenu = Menu(rpc_menu, tearoff=0, **args)
	rpc_menu.add_command(label="Load", command=rpcLoad)
	rpc_menu.add_command(label="Stop", command=rpcStop)
	rpcgui.config(menu=rpc_menu)

	window_height = 800
	window_width = 900
	screen_width = rpcgui.winfo_screenwidth()
	screen_height = rpcgui.winfo_screenheight()
	x_cordinate = int((screen_width/2) - (window_width/2))
	y_cordinate = int((screen_height/2) - (window_height/2))
	rpcgui.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

	client_frame = LabelFrame(rpcgui, text="Client ID", bg="Green", fg="white", padx=5, pady=5)
	client_frame.pack(expand="yes")
	client_entry = Entry(client_frame, font=("Verdana", 17))
	client_entry.pack()


	info_frame = LabelFrame(rpcgui, text="Rich Presence", bg="Green", fg="white", padx=10, pady=10)
	info_frame.pack(expand="yes")

	holderframe = Frame(info_frame, bg="Green", padx=8, pady=8)
	holderframe.pack(expand="yes")

	state_frame = LabelFrame(holderframe, text="State", bg="Green", fg="white", padx=5, pady=5)
	state_frame.grid(row=1, column=1)
	state_entry = Entry(state_frame, font=("Verdana", 13), width=25)
	state_entry.pack()

	det_frame = LabelFrame(holderframe, text="Details", bg="Green", fg="white", padx=5, pady=5)
	det_frame.grid(row=2, column=1, padx=7)
	det_entry = Entry(det_frame, font=("Verdana", 13), width=25)
	det_entry.pack()

	img_frame = LabelFrame(holderframe, text="Image", bg="Green", fg="white", padx=8, pady=8)
	img_frame.grid(row=1, column=2, rowspan=2)

	Limg_frame = LabelFrame(img_frame, text="Large Image", bg="Green", fg="white", padx=5, pady=5)
	Limg_frame.grid(row=1, column=1)
	Limg_entry = Entry(Limg_frame, font=("Verdana", 13), width=25)
	Limg_entry.pack()
	Ltxt_entry = Entry(Limg_frame, font=("Verdana", 13), width=25)
	Ltxt_entry.pack()

	Simg_frame = LabelFrame(img_frame, text="Small Image", bg="Green", fg="white", padx=5, pady=5)
	Simg_frame.grid(row=2, column=1)
	Simg_entry = Entry(Simg_frame, font=("Verdana", 13), width=25)
	Simg_entry.pack()
	Stxt_entry = Entry(Simg_frame, font=("Verdana", 13), width=25)
	Stxt_entry.pack()

	time_frame = LabelFrame(info_frame, text="Timer", bg="Green", fg="white", padx=8, pady=8)
	time_frame.pack(expand="yes")

	str_frame = LabelFrame(time_frame, text="Start", bg="Green", fg="white", padx=5, pady=5)
	str_frame.grid(row=1, column=1)
	str_entry = Entry(str_frame, font=("Verdana", 13), width=25)
	str_entry.pack(side=LEFT)

	end_frame = LabelFrame(time_frame, text="End", bg="Green", fg="white", padx=5, pady=5)
	end_frame.grid(row=1, column=2)
	end_entry = Entry(end_frame, font=("Verdana", 13), width=25)
	end_entry.pack(side=RIGHT)

	holderframe2 = Frame(info_frame, bg="Green", padx=8, pady=8)
	holderframe2.pack(expand="yes")

	party_frame = LabelFrame(holderframe2, text="Party", bg="Green", fg="white", padx=5, pady=5)
	party_frame.grid(row=1, column=1)

	partysize_frame = LabelFrame(party_frame, text="Party Size", bg="Green", fg="white", padx=5, pady=5)
	partysize_frame.pack(expand=True)
	partysize_entry = Entry(partysize_frame, font=("Verdana", 13), width=25)
	partysize_entry.pack()

	partymax_frame = LabelFrame(party_frame, text="Party Max", bg="Green", fg="white", padx=5, pady=5)
	partymax_frame.pack(expand=True)
	partymax_entry = Entry(partymax_frame, font=("Verdana", 13), width=25)
	partymax_entry.pack()

	holder3 = Frame(holderframe2, bg="Green", padx=5, pady=5)
	holder3.grid(row=1, column=2)

	btn1_frame = LabelFrame(holder3, text="Button 1", bg="Green", fg="white", padx=5, pady=5)
	btn1_frame.pack(expand=True)
	btn1_entry = Entry(btn1_frame, font=("Verdana", 13), width=25)
	btn1_entry.pack()
	url1_entry = Entry(btn1_frame, font=("Verdana", 13), width=25)
	url1_entry.pack()

	btn2_frame = LabelFrame(holder3, text="Button 2", bg="Green", fg="white", padx=5, pady=5)
	btn2_frame.pack(expand=True)
	btn2_entry = Entry(btn2_frame, font=("Verdana", 13), width=25)
	btn2_entry.pack()
	url2_entry = Entry(btn2_frame, font=("Verdana", 13), width=25)
	url2_entry.pack()

	finalbtn_frame = Frame(rpcgui, bg="Green", padx=5, pady=5)
	finalbtn_frame.pack(expand=True)

	postbtn = Button(finalbtn_frame, text="Post to Client", **btnargs, width=150, command=rpcRun)
	postbtn.bind("<Enter>", lambda e: postbtn.config(background="lightgreen", foreground="black"))
	postbtn.bind("<Leave>", lambda e: postbtn.config(background="green", foreground="white"))
	postbtn.grid(row=1, column=1, padx=10)

	stopbtn = Button(finalbtn_frame, text="Kill RPC", **btnargs, width=150, command=rpcStop)
	stopbtn.bind("<Enter>", lambda e: stopbtn.config(background="lightgreen", foreground="black"))
	stopbtn.bind("<Leave>", lambda e: stopbtn.config(background="green", foreground="white"))
	stopbtn.grid(row=1, column=2, padx=10)

	rpcgui.mainloop()

def sticky(e=None):
	stickyfile="sticky"
	def sticky_save(e=None):
		appdata = environ["appdata"]
		try:
			makedirs(f"{appdata}\\VolumePanel\\data")
		except FileExistsError:
			pass
		with open(f"{appdata}/VolumePanel/data/{stickyfile}.PVER", "wt") as f:
			f.write(area.get(0.1, END).strip())
		stickyWin.title(f"Sticky - {stickyfile}")

	def sticky_load():
		stickyWin.title(f"Sticky - {stickyfile}")
		area.delete(1.0, END)
		appdata = environ["appdata"]
		if path.isfile(f"{appdata}/VolumePanel/data/{stickyfile}.PVER"):
			with open(f"{appdata}/VolumePanel/data/{stickyfile}.PVER", "rt") as f:
				area.insert(INSERT, f.read())
				if area.get(1.0, END).strip() is "":
					stickyWin.config(bg="white")
					showinfo("[[ Emptiness ]]", "Sticky contains nothing except dust.")
					stickyWin.config(bg="green")
				area.focus_set()
		else:
			showerror("Nope !!", "Sticky not saved to load")

	def cmd_load():
		pass

	def sticky_close(e=None):
		pcopy(area.get(0.1, END).strip())
		stickyWin.destroy()

	def unsaved_notice(e=None):
		appdata = environ["appdata"]
		if path.isfile(f"{appdata}/VolumePanel/data/{stickyfile}.PVER"):
			with open(f"{appdata}/VolumePanel/data/{stickyfile}.PVER", "rt") as f:
				if f.read() is area.get("0.0", END):
					stickyWin.title(f"Sticky - {stickyfile}")
				else:
					stickyWin.title(f"** Sticky - {stickyfile}")

	def do_popup(event):
		try:
			rytclk_menu.tk_popup(event.x_root, event.y_root)
		finally:
			rytclk_menu.grab_release()

	def more_opt(func):
		sticky_close()
		func()

	def switch_load(fname):
		nonlocal stickyfile
		print("Loaded", fname)
		stickyfile=fname
		sticky_load()


	stickyWin = Toplevel(root)
	stickyWin.iconbitmap(r"C:\Windows\System32\notepad.exe")
	stickyWin.config(bg="green")
	stickyWin.attributes('-topmost', True)
	stickyWin.title(f"Sticky")
	stickyWin.geometry("500x400")
	stickyWin.maxsize(700, 500)

	sticky_menu = Menu(root)
	sticky_menu.add_command(label="Save", command=sticky_save)
	sticky_menu.add_command(label="Load", command=sticky_load)
	sticky_menu.add_command(label="Close", command=sticky_close)
	stickyWin.config(menu=sticky_menu)

	rytclk_menu = Menu(root, tearoff = 0, **args)
	rytclk_menu.add_command(label ="Command", command=lambda: more_opt(key_command))
	rytclk_menu.add_command(label ="Switch Load 4", command=lambda: switch_load("sticky4444"))

	area = Text(stickyWin, selectbackground="green", width=100, height=100)
	sticky_load()
	area.pack(pady=5, padx=5)

	area.bind("<Control-s>", sticky_save)
	area.bind("<Double-Escape>", sticky_close)
	area.bind("<Key>", unsaved_notice)
	area.bind("<Button-3>", do_popup)

	stickyWin.mainloop()

def media_pauseplay(e=None, togl=True, pspl=True):
	if pspl:
		p.press("playpause")
	else:
		pass
	if Wm.wm_title(root)=="Volume_Panel":
		if togl:
			able()
		else:
			pass

def key_command(e=None):
	valid_cmds=["sticky", "shots", "capture", "10mat", "pgms", "rpc"]
	def run_click(e=None):
		try:
			cmdline = inp_cmd.get()
			if mvs[:-1] in cmdline:
				if "more" in cmdline:
					try:
						startfile(f"D:/{mvs}/More.lnk")
					except:
						startfile(f"{ws[2]}://{ws[1]}free.{ws[0]}")
				elif "watched" in cmdline:
					startfile(f"D:/{mvs}/")
				elif "archive" in cmdline:
					startfile(f"D:/{mvs}/archived")
				else:
					startfile(f"D:/{mvs}")
			if "sticky" in cmdline:
				terminal.destroy()
				sticky()
			if "rpc" in cmdline:
				rpc()
			if "shot" in cmdline:
				startfile(r"C:\Users\PVER\OneDrive\Pictures\Screenshots")
			if "capture" in cmdline:
				ss_here()
			if len(cmdline)==2:
				if "tf" == cmdline:
					manual_title("foreword")
				elif "th" == cmdline:
					manual_title("hindword")
				elif "tr" == cmdline:
					random_title()
			if "10mat" in cmdline:
				startfile(environ['10mat'])
			if ("pgms" in cmdline) or ("programs" in cmdline) or ("programfiles" in cmdline):
				startfile(environ['pgms'])
			if cmdline[:4] == "game":
				if "on" in cmdline:
					bind_gm(None)
				elif "off" in cmdline:
					unbind_gm(None)
				else:
					gm = choice([bind_gm, unbind_gm])
					gm(None)
			if cmdline[:3] == "run":
				startfile(cmdline[4:])
		except Exception as errorLine:
			showerror("Exception Case", errorLine)
		try:
			terminal.destroy()
		except:
			pass

	def shortc(e=None, wrd=""):
		inp_cmd.delete(0, END)
		inp_cmd.insert(0, wrd)

	def close_terminal(e=None):
		terminal.destroy()

	def scroll_thru(e=None):
		inp_cmd.delete(0, END)
		inp_cmd.insert(0, choice(valid_cmds))

	global terminal
	terminal = Toplevel(root)
	terminal.title(f"Command Terminal")
	terminal.iconbitmap(r"C:\Windows\System32\cmd.exe")
	terminal.geometry("360x120")
	terminal.attributes('-topmost', True)

	inp_cmd = Entry(terminal, width=25, selectbackground="green", font=["Courier new", 14])
	inp_cmd.delete(0, END)
	inp_cmd.pack(pady=10)
	inp_cmd.focus_set()

	btn_grp = Frame(terminal)
	btn_grp.pack(side=BOTTOM, pady=10)

	btn_run = Button(btn_grp, text="Run", command=run_click, width=75, height=50, **btnargs)
	btn_run.pack(side=LEFT, padx=5)
	btn_run = Button(btn_grp, text="Cancel", command=terminal.destroy, width=75, height=50, **btnargs)
	btn_run.pack(side=RIGHT, padx=5)

	inp_cmd.bind("<Return>", run_click)
	inp_cmd.bind("<Up>", scroll_thru)
	inp_cmd.bind("<Escape>", close_terminal)

	inp_cmd.bind("<Control-m>", lambda e:shortc(wrd=mvs))
	inp_cmd.bind("<Control-r>", lambda e:shortc(wrd="rpc"))

	terminal.mainloop()

#### app root

root = Tk()
root.iconbitmap(r"C:\Windows\System32\SndVol.exe")
root.attributes('-topmost', True)
root.config(bg="white")
root.geometry("340x100")


#### fixed vars

mvs = "mvs"
appdir = environ["appdata"] + "/VolumePanel/data"
ws = ["in","s2d","https"]
media_there = False
pixelVirtual = PhotoImage(width=1, height=1)
args={"bg":"green" ,"fg":"white", "activebackground":"lightgreen", "activeforeground":"black"}
btnargs={"bg":"green", "fg":"white", "activebackground":"darkgreen", "activeforeground":"lightgreen"
		, "disabledforeground":"white", "compound":"c", 'image':pixelVirtual}
firstword_list = ["Volume", "Sound", "Voice", "Noise", "ஒலி", "கூச்சல்", "குரல்", "आवाज़", "कोलाहल", "ध्वनि", "आयतन", "ஏடு"]
lastword_list = ["Panel", "Box", "Corner", "Control", "पैनल", "संदूक", "कोना", "नियंत्रण", "சேணவகை", "பெட்டி", "மூலை", "கட்டுப்பாடு"]

random_title()
# print(choice(firstword_list))
# print(choice(lastword_list))


#### menu

menubar = Menu(root)
volmenu = Menu(menubar, tearoff=0, **args)
volmenu.add_command(label="Increase", command=lambda :volume(None, side="up", times=1))
volmenu.add_command(label="Double Increase", command=lambda :volume(None, side="up", times=2))
volmenu.add_separator()
volmenu.add_command(label="Decrease", command=lambda :volume(None, side="down", times=1))
volmenu.add_command(label="Double Decrease", command=lambda :volume(None, side="down", times=2))
volmenu.add_separator()
volmenu.add_command(label="Mute", command=lambda: p.press("volumemute"))
volmenu.add_separator()
volmenu.add_command(label="Sound Vol", command=lambda: startfile("sndvol"))

funcmenu = Menu(menubar, tearoff=0, **args)
funcmenu.add_command(label="Shots Dir", command=lambda :startfile(r"C:\Users\PVER\OneDrive\Pictures\Screenshots"))
funcmenu.add_command(label="Save Shot Here", command=ss_here)
funcmenu.add_separator()
funcmenu.add_command(label="Skool", command=lambda :startfile(environ["skl"]))

funcmenu.add_separator()
ttl_changeMenu = Menu(funcmenu, tearoff=0, **args)
funcmenu.add_cascade(label="Dislike title", menu=ttl_changeMenu)
ttl_changeMenu.add_command(label="Change it", command=random_title)
ttl_changeMenu.add_separator()
ttl_changeMenu.add_command(label="Set fore-word", command=lambda: manual_title("foreword"))
ttl_changeMenu.add_command(label="Set hind-word", command=lambda: manual_title("hindword"))

funcmenu.add_command(label="Sticky", command=sticky)

menubar.add_cascade(label="Volume", menu=volmenu)
menubar.add_command(label="Quick Shot", command=lambda: p.press("prntscrn"))
menubar.add_cascade(label="More", menu=funcmenu)

root.config(menu=menubar)

#### app screen

b3 = Button(root, text="Prev track", command=lambda:scrn_move('e', side="left"), state=DISABLED, **btnargs, height=700)
b3.pack(side=LEFT)

b4 = Button(root, text="Next track", command=lambda:scrn_move('e', side="right"), state=DISABLED, **btnargs, height=700)
b4.pack(side=RIGHT)

b = Button(root, text="Volume up", command=lambda:p.press("volumeup"), **btnargs, width = 500, height=30)
b.pack()
b.focus_set()

b2 = Button(root, text="Volume down", command=lambda:p.press("volumedown"), **btnargs, width = 500, height=30)
b2.pack(side=BOTTOM)


# root.bind("<Button-2>", lambda e:b.focus_set())
root.bind("<Button-2>", media_pauseplay)
root.bind("<Button-3>", lambda e:able())
root.bind("<Control-Button-1>", lambda t:media_pauseplay(togl=False))

root.bind("<Alt-s>", sticky)
root.bind("<Alt-c>", key_command)
root.bind("<Alt-t>", random_title)

root.bind("<Home>", lambda e:AppView.current().pin())
root.bind("<End>", lambda e:AppView.current().unpin())

root.bind("<Configure>", adjust)
root.bind("<MouseWheel>", scrnmove_mousewhell)
root.bind("<Double-Delete>", malert)
# root.bind("<MouseWheel>", lambda e:p.hotkey('ctrl', 'win', "left"))

#### Default bindings

def bind_default():
	b.bind("<Up>", lambda e:volume(None, side="up", times=1)) #single up
	b.bind("<Down>", lambda e:volume(None, side="down", times=2)) # doubledown
	b.bind("<a>", lambda e:volume(None, side="up", times=1)) # single up
	b.bind("<z>", lambda e:volume(None, side="down", times=2)) # doubledown
	b.bind("<q>", lambda e:able()) # shutup

	b2.bind("<Down>", lambda e:volume(None, side="down", times=1)) # single down
	b2.bind("<Up>", lambda e:volume(None, side="up", times=2)) # doubleup
	b2.bind("<z>", lambda e:volume(None, side="down", times=1)) # single down
	b2.bind("<a>", lambda e:volume(None, side="up", times=2)) # doubleup
	b2.bind("<q>", lambda e:able()) # shutup
	# b2.bind(f"<`>", lambda e:p.hotkey('ctrl', 'win', f'right')) ######### Temply off
	b2.bind(f"<.>", lambda e:scrn_move('e', side="right"))
	b2.bind(f"<,>", lambda e:scrn_move('e', side="left"))
	# b2.bind(f"<Escape>", lambda e:scrn_move('e', side="left")) ######### Temply off

	b3.bind("<Key>", lambda e:scrn_move('e', side="left"))
	b4.bind("<Key>", lambda e:scrn_move('e', side="right"))

	b.bind("<Enter>", lambda e: b.config(background="lightgreen", foreground="black"))
	b.bind("<Leave>", lambda e: b.config(background="green", foreground="white"))
	b2.bind("<Enter>", lambda e: b2.config(background="lightgreen", foreground="black"))
	b2.bind("<Leave>", lambda e: b2.config(background="green", foreground="white"))
bind_default()

################################ BORE MODE SETTINGS

def bind_gm(event):
	global bore_lvl
	#toggle
	b.unbind("<Return>")
	b.bind("<Return>", lambda event:unbind_gm(None))
	root.iconbitmap("c:/windows/system32/control.exe")
	#gm1
	b.bind("<b>", gm_1)
	b.bind("<Control-b>", lambda e:gm_1(e, clr=True))
	b.bind("<Alt-b>", lambda e:gm_1(e, opp=-1))
	#gm2
	b2.bind("<Key>", gm_2)
	#gm3
	b.bind("<p>", lambda e:gm_3(None, dire="up"))
	b.bind("<l>", lambda e:gm_3(None, dire="lft"))
	b.bind("<;>", lambda e:gm_3(None, dire="dwn"))
	b.bind("<'>", lambda e:gm_3(None, dire="ryt"))
	b.bind("<Control-p>", lambda e:gm_3(None, dire="up", gear=5))
	b.bind("<Control-l>", lambda e:gm_3(None, dire="lft", gear=5))
	b.bind("<Control-;>", lambda e:gm_3(None, dire="dwn", gear=5))
	b.bind("<Control-'>", lambda e:gm_3(None, dire="ryt", gear=5))
	#gm3_moded
	b.bind("<f>", lambda e:gm_3(None, dire="ryt", gear=bore_lvl, from_="lft"))
	b.bind("<e>", lambda e:gm_3(None, dire="up", gear=bore_lvl, from_="lft"))
	b.bind("<d>", lambda e:gm_3(None, dire="dwn", gear=bore_lvl, from_="lft"))
	b.bind("<s>", lambda e:gm_3(None, dire="lft", gear=bore_lvl, from_="lft"))

def unbind_gm(event):
	#toggle
	b.unbind("<Return>")
	b.bind("<Return>", lambda event:bind_gm(None))
	root.iconbitmap("c:/windows/system32/sndvol.exe")
	#gm1
	b.unbind("<b>")
	b.unbind("<Control-b>")
	#gm2
	b2.unbind("<Key>")
	#gm3
	b.unbind("<p>")
	b.unbind("<l>")
	b.unbind("<;>")
	b.unbind("<'>")
	b.unbind("<Control-p>")
	b.unbind("<Control-l>")
	b.unbind("<Control-;>")
	b.unbind("<Control-'>")
	#gm3_moded
	b.unbind("<f>")
	b.unbind("<e>")
	b.unbind("<d>")
	b.unbind("<s>")

unbind_gm(None)
bore_lvl = 0

def gm_1(e, opp=1, clr=False):
	global bore_lvl
	# print(Wm.wm_title(root))
	# root.title(Wm.wm_title(root) + "2")
	if "_" in Wm.wm_title(root):
		ttl = f"{firstword}_{lastword}"
	else:
		ttl = f"{firstword} {lastword}"
	if not clr:
		bore_lvl = bore_lvl + opp
	else:
		bore_lvl = 0
	root.title(f"{ttl} {bore_lvl}")

def gm_2(e):
	print(e.keysym)
	if e.keysym == "F7":
		root.title("")
	elif e.keysym == "BackSpace":
		root.title(Wm.wm_title(root)[:-1])
	else:
		lst_char = e.char
		if e.keysym == "XF86AudioPrev":
			lst_char = "q"
		if e.keysym == "XF86AudioPlay":
			lst_char = "a"
		if e.keysym == "XF86AudioNext":
			lst_char = "z"
		if e.keysym == "Delete":
			lst_char = "."
		if e.keysym == "Insert":
			lst_char = ","
		root.title(Wm.wm_title(root) + lst_char)

def gm_3(e, dire, gear=1, from_="ryt"):
	x_axis, y_axis = root.geometry()[root.geometry().index("+"):].split("+")[-2], root.geometry()[root.geometry().index("+"):].split("+")[-1]
	if from_=="ryt":
		try:
			gear = int(Wm.wm_title(root)[-1])
		except:
			pass
	if dire=="up":
		y_axis = int(y_axis) - gear
	elif dire=="dwn":
		y_axis = int(y_axis) + gear
	elif dire=="ryt":
		x_axis = int(x_axis) + gear
	elif dire=="lft":
		x_axis = int(x_axis) - gear
	root.geometry(f"+{x_axis}+{y_axis}")

#################################### BORE MODE SETTINGS - up

root.mainloop()
