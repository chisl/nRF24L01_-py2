#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""nRF24L01+: Single Chip 2.4GHz Transceiver"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["Nordic Semiconductor"]
__license__    = "TBD"
__version__    = "0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

class REG:
	CONFIG = 0
	EN_AA = 1
	EN_RXADDR = 2
	SETUP_AW = 3
	SETUP_RETR = 4
	RF_CH = 5
	RF_SETUP = 6
	STATUS = 7
	OBSERVE_TX = 8
	RPD = 9
	RX_ADDR_P0 = 10
	RX_ADDR_P1 = 11
	RX_ADDR_P2 = 12
	RX_ADDR_P3 = 13
	RX_ADDR_P4 = 14
	RX_ADDR_P5 = 15
	TX_ADDR = 16
	RX_PW_P0 = 17
	RX_PW_P1 = 18
	RX_PW_P2 = 19
	RX_PW_P3 = 20
	RX_PW_P4 = 21
	RX_PW_P5 = 22
	FIFO_STATUS = 23
	DYNPD = 28
	FEATURE = 29
