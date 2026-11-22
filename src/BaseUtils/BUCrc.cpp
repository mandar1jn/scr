#include "BUCrc.h"

unsigned int gpuiCrc32_table[0x100];
unsigned long long gpuiCrc64_table[0x100];

static unsigned int CRCReflect(unsigned int _uiRef, unsigned int _uiCh)
{
	return 0;
}

void BUCrcInitTable32()
{

}

unsigned int BUCRCGenerate(const char* _zString)
{
	unsigned int result = 0xFFFFFFFF;

	for(int i = 0 ; _zString[i]; i++)
	{
		int idx = (result ^ _zString[i]) & 0xFF;
		result = (result >> 8) ^ gpuiCrc32_table[idx];
	}

	return result ^ 0xffffffff;
}

unsigned int BUCRCGenerate(const char* _zString, unsigned int _uiLen)
{
	unsigned int result = 0xFFFFFFFF;

	while((int)*_zString)
	{
		if(!_uiLen--)
			break;

		int idx = (result & 0xFF) ^ *_zString;
		_zString = &_zString[1];
		result = result >> 8 ^ gpuiCrc32_table[idx];
	}

	return result ^ 0xffffffff;
}

unsigned int BUCRCGenerate(const unsigned char*, unsigned int _uiSize)
{
	return 0;
}

static unsigned long long CRCReflect64(unsigned long long _uiRef, unsigned int _uiCh)
{
	return 0;
}

void BUCrcInitTable64()
{
	
}

void BUCrcInitTable()
{
	BUCrcInitTable32();
	BUCrcInitTable64();
}
