import win32gui
import win32con
import win32api
import win32ui

class SimpleRenderer:
    def __init__(self, width, height, pixel_size=10):
        self.width = width
        self.height = height
        self.pixel_size = pixel_size
        self.pixels = [[0] * (width // pixel_size) for _ in range(height // pixel_size)]
        self.bitmap = None

    def draw_pixel(self, x, y, color):
        x //= self.pixel_size
        y //= self.pixel_size
        self.pixels[y][x] = color

    def render(self, hwnd):
        hdc = win32gui.GetDC(hwnd)

        # CreateDC 함수를 사용하여 메모리 DC 생성
        mem_dc = win32ui.CreateDC()

        # CreateCompatibleBitmap 함수를 사용하여 비트맵 생성
        self.bitmap = win32ui.CreateBitmap()
        self.bitmap.CreateCompatibleBitmap(mem_dc, self.width, self.height)
        mem_dc.SelectObject(self.bitmap)

        # 픽셀 그리기
        for y, row in enumerate(self.pixels):
            for x, color in enumerate(row):
                color = color if color else win32api.RGB(0, 0, 0)
                for i in range(self.pixel_size):
                    for j in range(self.pixel_size):
                        mem_dc.SetPixel(x * self.pixel_size + i, y * self.pixel_size + j, color)

        # 비트맵을 윈도우 DC로 전송
        mem_dc.BitBlt(hdc, 0, 0, self.width, self.height, mem_dc, 0, 0, win32con.SRCCOPY)

        win32gui.ReleaseDC(hwnd, hdc)

class App:
    def __init__(self):
        self.width = 400
        self.height = 400
        self.renderer = SimpleRenderer(self.width, self.height)

        class_name = 'PixelRendererClass'
        wc = win32gui.WNDCLASS()
        wc.lpfnWndProc = self.wnd_proc
        wc.lpszClassName = class_name
        wc.hInstance = win32api.GetModuleHandle(None)
        class_atom = win32gui.RegisterClass(wc)

        self.hwnd = win32gui.CreateWindow(
            class_atom,
            "Pixel Renderer",
            win32con.WS_OVERLAPPED | win32con.WS_CAPTION | win32con.WS_SYSMENU,
            win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,
            self.width, self.height,
            0, 0, 0, None
        )
        win32gui.ShowWindow(self.hwnd, win32con.SW_SHOWNORMAL)
        win32gui.UpdateWindow(self.hwnd)

    def run(self):
        while True:
            self.renderer.draw_pixel(50, 50, win32api.RGB(255, 0, 0))
            self.renderer.draw_pixel(100, 100, win32api.RGB(0, 255, 0))
            self.renderer.render(self.hwnd)
            win32gui.PumpWaitingMessages()

    def wnd_proc(self, hwnd, msg, wparam, lparam):
        if msg == win32con.WM_DESTROY:
            win32gui.PostQuitMessage(0)
            return 0
        else:
            return win32gui.DefWindowProc(hwnd, msg, wparam, lparam)

if __name__ == "__main__":
    app = App()
    app.run()
