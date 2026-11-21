#include "Game/xfont/xfont.h"

class XFColor_s {
public:
    unsigned long Y;
    unsigned long Cb;
    unsigned long Cr;
};

XFColor_s XFcolor[] = {
    {0xb4, 0x80, 0x80},
    {0xa2, 0x2c, 0x8e},
    {0x83, 0x9c, 0x2c},
    {0x70, 0x48, 0x3a},
    {0x54, 0xb8, 0xc6},
    {0x41, 0x64, 0xd4},
    {0x23, 0xd4, 0x72},
    {0x10, 0x80, 0x80}
};

unsigned long m_fbSize;
void* m_xfb;

unsigned long XfbWidth;
short cc;
short cc2;

void XFONTInit(unsigned long fbWidth, unsigned long fbSize)
{
    XfbWidth = fbWidth;
    m_fbSize = fbSize;
}

void XFONTSetFrameBuffer(void* xfb)
{
    m_xfb = xfb;
}

void XFONTSetFgColor(unsigned long color)
{
    cc  = (unsigned short)((XFcolor[color].Y << 8) + XFcolor[color].Cb);
    cc2  = (unsigned short)((XFcolor[color].Y << 8) + XFcolor[color].Cr);
}
