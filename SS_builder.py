import itertools

hotkeys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{NUMPAD0}', '{NUMPAD1}', '{NUMPAD2}', '{NUMPAD3}', '{NUMPAD4}', '{NUMPAD5}', '{NUMPAD6}', '{NUMPAD7}', '{NUMPAD8}', '{NUMPAD9}', '{NUMPADMULT}', '{NUMPADADD}', '{NUMPADSUB}', '{NUMPADDIV}', '{NUMPADDOT}']

hotkey_template = '''
HotKeySet("HOTKEY_HERE", 'HOTKEY_FUNCTIONNAME')

Func HOTKEY_FUNCTIONNAME()
   HotKeySet("HOTKEY_HERE")
   Send("HOTKEY_HERE")
   If Pause Then
      Sleep(20)
      Send("{ENTER}")
   EndIf
   HotKeySet("HOTKEY_HERE", 'HOTKEY_FUNCTIONNAME')
EndFunc

'''

tfile = '''Opt("WinTitleMatchMode",2)
Global $rpgwindow = WinGetHandle("SanctuaryRPG: Black Edition")
Global Pause = True

'''
names = itertools.permutations('abcdefghi')
for hotkey in hotkeys:
        tfile += hotkey_template.replace('HOTKEY_HERE',hotkey).replace('HOTKEY_FUNCTIONNAME',''.join(names.next()))

tfile += '''
HotKeySet("{F2}", '_exit')
HotKeySet("{F3}", '_pause')

Func _exit()
   Exit
EndFunc

Func _pause()
   Pause = NOT Pause
EndFunc

While 1
   Sleep(1000)
WEnd'''