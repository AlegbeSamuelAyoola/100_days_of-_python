bar1 = "\033[0;31m =\033[0m"
bar2 = "\033[1;37m =\033[0m"
bar3 = "\033[0;34m =\033[0m"

Header = (f"{bar1}{bar2}{bar3} Music App {bar3}{bar2}{bar1}")
print(f"{Header: ^130}")
print()
print(f"🔥▶️  \033[1;37m Radio Gaga\033[0m")
print(f"      Queen")
print()
print(f"\033[1;37m PREV\033[0m")
next_button = (f"\033[1;32m NEXT\033[0m")
print(f"{next_button: >22}")
pause_button = (f"\033[1;35m PAUSE\033[0m")
print(f"{pause_button: >29}")
print()
print()
print()
print()
welcome = "\033[1;37m WELCOME TO\033[0m"
armbook = "\033[1;34m--      ARMBOOK      --\033[0m"
print(f"{welcome: ^75}")
print(f"{armbook: ^75}")
print()
text1 = "Definitely not a rip off of"
text2 = "a certain other social"
text3 = "networking site."
print(f"{text1}".rjust(60))
print(f"{text2}".rjust(60))
print(f"{text3}".rjust(60))
print()
honest = "\033[0;31m Honest.\033[0m"
print(f"{honest: >46}")
print()
user = "\033[1;37m Username:\033[0m"
pword = "\033[1;37m Password:\033[0m"
print(f"{user: >47}")
print(f"{pword: >47}")