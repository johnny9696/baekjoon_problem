import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    h,m,s = map(int,input().split())
    """
    시간은 1시간에 360/12  = 30도
    1분에 1/2도
    1초에  1/120 도
    분은 1분에 6도
    1초에 1/10 도
    초는 1초에 6도 
    """
    h_rad = float(h*30) + 0.5*m + 1/120 * s
    m_rad = float(m*6) + 0.1 * s
    s_rad = float(s*6)
    a = 360 - abs(h_rad- m_rad) if abs(h_rad- m_rad) > 180 else abs(h_rad- m_rad)
    b = 360 - abs(h_rad- s_rad) if abs(h_rad- s_rad) > 180 else abs(h_rad- s_rad)
    c = 360 - abs(s_rad- m_rad) if abs(s_rad- m_rad) > 180 else abs(s_rad- m_rad)
    print(min(a,b,c))