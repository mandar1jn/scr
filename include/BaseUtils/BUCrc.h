#pragma once

void BUCrcInitTable32();
unsigned int BUCRCGenerate(const char* _zString);
unsigned int BUCRCGenerate(const char* _zString, unsigned int _uiLen);
unsigned int BUCRCGenerate(const unsigned char*, unsigned int _uiSize);
void BUCrcInitTable64();
void BUCrcInitTable();
