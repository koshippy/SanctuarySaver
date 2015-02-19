import itertools

hotkeys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{NUMPAD0}', '{NUMPAD1}', '{NUMPAD2}', '{NUMPAD3}', '{NUMPAD4}', '{NUMPAD5}', '{NUMPAD6}', '{NUMPAD7}', '{NUMPAD8}', '{NUMPAD9}', '{NUMPADMULT}', '{NUMPADADD}', '{NUMPADSUB}', '{NUMPADDIV}', '{NUMPADDOT}']

hotkey_template = '''
HotKeySet("HOTKEY_HERE", 'HOTKEY_FUNCTIONNAME')

Func HOTKEY_FUNCTIONNAME()
   If WinActive($rpgwindow) Then ControlSend($rpgwindow,"","","HOTKEY_HERE{ENTER}")
EndFunc

'''

tfile = '''Opt("WinTitleMatchMode",2)
Global $rpgwindow = WinGetHandle("SanctuaryRPG: Black Edition")

'''
names = itertools.permutations('abcdefghi')
for hotkey in hotkeys:
        tfile += hotkey_template.replace('HOTKEY_HERE',hotkey).replace('HOTKEY_FUNCTIONNAME',''.join(names.next()))

tfile += '''
HotKeySet("{F2}", '_exit')

Func _exit()
   Exit
EndFunc

While 1
   Sleep(1000)
WEnd'''