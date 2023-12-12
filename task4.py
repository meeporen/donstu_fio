time = int(input())
if time >= 86400:
    d = time//86400
    h = (time//3600)%24
    m = (time//60)%60
    s = time%60
    print(f'Now: day {d}, hours {h}, minutes {m}, seconds {s}')
elif time >=3600:
    h = (time//3600)%24
    m = (time//60)%60
    s = time%60
    print(f'Now: hours {h}, minutes {m}, seconds {s}')
elif time>=60:
    m=(time//60)%60
    s = time%60
    print(f'Now: min{m},sec{s}')
else:
    print("Now: sec",time)
